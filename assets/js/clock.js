update_clock();

function update_clock() {
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

	var clock_element = document.getElementById('clock');

	clock_element.innerHTML = hours + ':' + minutes + ':' + seconds;
}
setInterval(update_clock, 1000);
