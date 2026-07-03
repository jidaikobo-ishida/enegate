FROM php:8.1-apache

# Set locale
ENV LANG C.UTF-8
ENV LC_ALL C.UTF-8

# Enable Apache modules
RUN a2enmod rewrite

# Install dependencies
RUN apt-get update && apt-get install -y \
    libpng-dev \
    libjpeg-dev \
    libfreetype6-dev \
    && docker-php-ext-configure gd --with-freetype --with-jpeg \
    && docker-php-ext-install gd

# Set PHP configuration for Shift_JIS
RUN echo "default_charset = \"Shift_JIS\"" > /usr/local/etc/php/conf.d/charset.ini
RUN echo "mbstring.internal_encoding = \"UTF-8\"" >> /usr/local/etc/php/conf.d/charset.ini
RUN echo "mbstring.http_output = \"Pass\"" >> /usr/local/etc/php/conf.d/charset.ini

# Add Directory block to allow access and process .html as PHP
RUN echo '<Directory "/var/www/html">' >> /etc/apache2/apache2.conf
RUN echo '    Options Indexes FollowSymLinks' >> /etc/apache2/apache2.conf
RUN echo '    AllowOverride All' >> /etc/apache2/apache2.conf
RUN echo '    Require all granted' >> /etc/apache2/apache2.conf
RUN echo '    AddType application/x-httpd-php .html' >> /etc/apache2/apache2.conf
RUN echo '    DirectoryIndex index.html index.php' >> /etc/apache2/apache2.conf
RUN echo '</Directory>' >> /etc/apache2/apache2.conf

WORKDIR /var/www/html
