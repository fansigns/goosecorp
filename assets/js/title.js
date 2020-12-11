javascript: (function () {
	var start = new Date();
	var pad = function (i) {
		var s = '0' + Math.floor(i);
		return s.substr(s.length - 2);
	};
	var newTimerStr = function () {
		var currentTime = new Date(),
			hours = currentTime.getHours(),
			minutes = currentTime.getMinutes();
		seconds = currentTime.getSeconds();
		if (minutes < 10) {
			minutes = '0' + minutes;
		}
		if (seconds < 10) {
			seconds = '0' + seconds;
		}
		return `[${hours} : ${minutes} : ${seconds}]`;
	};
	setInterval(function () {
		document.title = newTimerStr();
	}, 1000);
})();
