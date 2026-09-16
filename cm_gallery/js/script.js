// -*- coding: cp932 -*-
/**
 * スクロール連動アニメーション (js-scroll)
 */
document.addEventListener('DOMContentLoaded', function () {
	var scrollTargets = document.querySelectorAll('.js-scroll');
	if (!scrollTargets.length) return;

	if ('IntersectionObserver' in window) {
		var observer = new IntersectionObserver(function (entries) {
			entries.forEach(function (entry) {
				if (entry.isIntersecting) {
					entry.target.classList.add('is-active');
					observer.unobserve(entry.target);
				}
			});
		}, {
			rootMargin: '0px 0px -30px 0px',
			threshold: 0
		});

		scrollTargets.forEach(function (el) {
			observer.observe(el);
		});
	} else {
		function onScrollCheck() {
			var triggerBottom = window.innerHeight - 30;
			for (var i = 0; i < scrollTargets.length; i++) {
				var target = scrollTargets[i];
				if (!target.classList.contains('is-active')) {
					var rect = target.getBoundingClientRect();
					if (rect.top < triggerBottom) {
						target.classList.add('is-active');
					}
				}
			}
		}
		window.addEventListener('scroll', onScrollCheck, { passive: true });
		window.addEventListener('resize', onScrollCheck, { passive: true });
		onScrollCheck();
	}
});
