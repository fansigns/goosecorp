document.getElementById('hidden').hidden = true;

var vid = document.getElementById('myVideo');

document.addEventListener('click', function () {
	document.getElementById('welcome').hidden = true;

	document.getElementById('hidden').hidden = false;

	vid.play();
});

vid.onended = function () {
	vid.play();
};
