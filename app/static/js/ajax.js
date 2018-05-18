// AJAX request using build-in XMLHttpRequest object //

function ajaxGet(url, callback) {
	
	var req = new XMLHttpRequest();
	req.open("GET", url);
	req.addEventListener("load", function() {
		// if no errors occur
		if (req.status >= 200 && req.status < 400) {
			global_response = JSON.parse(req.responseText)
			response = global_response.response
			callback(response, global_response);
		} else {
			console.error(req.status + " " + req.statusText + " " + url);
		}
	});
	req.addEventListener("error", function() {
		console.error("Network error in URL: " + url);
	});
	req.send(null);
}