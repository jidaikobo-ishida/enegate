import os
import re

def process_file(filepath):
    # Skip partials
    if '/block/' in filepath or '/blocks/' in filepath:
        return

    try:
        with open(filepath, 'rb') as f:
            raw_content = f.read()
    except Exception as e:
        print(f"Error reading {filepath}: {e}")
        return

    # Try decoding
    content = None
    encoding = None
    for enc in ['utf-8', 'shift_jis', 'cp932']:
        try:
            content = raw_content.decode(enc)
            encoding = enc
            break
        except UnicodeDecodeError:
            continue

    if content is None:
        print(f"Could not decode {filepath}")
        return

    # Check if it's a full page (has <head>)
    if '<head' not in content.lower():
        return

    viewport_tag = '<meta name="viewport" content="width=device-width, initial-scale=1.0">'
    
    # Check for existing viewport tag
    # More flexible regex to catch spaces around '='
    if '<meta name="viewport"' in content.lower() or 'name="viewport"' in content.lower():
        # Match name="viewport" first
        new_content = re.sub(
            r'<meta\s+name\s*=\s*["\']viewport["\']\s+content\s*=\s*["\'][^"\']*["\']\s*/?>',
            viewport_tag,
            content,
            flags=re.IGNORECASE
        )
        if new_content == content:
            # Match content first
            new_content = re.sub(
                r'<meta\s+content\s*=\s*["\'][^"\']*["\']\s+name\s*=\s*["\']viewport["\']\s*/?>',
                viewport_tag,
                content,
                flags=re.IGNORECASE
            )
    else:
        # Insert new viewport tag
        # Try inserting after charset
        charset_match = re.search(r'<meta\s+charset\s*=\s*["\'][^"\']*["\']\s*/?>', content, re.IGNORECASE)
        if charset_match:
            pos = charset_match.end()
            new_content = content[:pos] + '\n' + viewport_tag + content[pos:]
        else:
            # Insert after <head>
            head_match = re.search(r'<head[^>]*>', content, re.IGNORECASE)
            if head_match:
                pos = head_match.end()
                new_content = content[:pos] + '\n' + viewport_tag + content[pos:]
            else:
                return # Should not happen if <head> was found

    if new_content != content:
        print(f"Updating {filepath}")
        with open(filepath, 'w', encoding=encoding) as f:
            f.write(new_content)

def main():
    for root, dirs, files in os.walk('.'):
        if 'node_modules' in dirs:
            dirs.remove('node_modules')
        if 'ai' in dirs:
            dirs.remove('ai')
            
        for file in files:
            if file.endswith('.html') or file.endswith('.php'):
                filepath = os.path.join(root, file)
                process_file(filepath)

if __name__ == "__main__":
    main()
