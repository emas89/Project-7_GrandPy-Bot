// Function to display the answer from GrandPy

function display(response, global_response) {
	
	// create DOM objects

	var global_gp_answer = document.createElement("div");
	global_gp_answer.id = "global_gp_answer";
	var figure_Gp = document.createElement("figure");
	var Gp_answer_gmap = document.createElement("p");
	var answer_gmap = document.createElement("p");
	var Gp_answer_wiki = document.createElement("p");
	var answer_wiki = document.createElement("p");
	var text_answer = document.createElement("div");
	text_answer.id = "text_answer";

	var Gp_icon = document.createElement("img");

	Gp_icon.src = "/static/img/gp_1200.png";
	Gp_icon.alt = "GrandPy:";
	Gp_icon.title = "GrandPy";
	global_gp_answer.appendChild(figure_Gp);
	figure_Gp.appendChild(Gp_icon);
	global_gp_answer.appendChild(text_answer);
	dialogue.appendChild(global_gp_answer);

	// If Mediawiki and Gmap returned values
	if (response.wiki !== "ZERO_RESULT") {
	Gp_answer_gmap.textContent = response.Gp_answer_gmap+" "+response.gmap;
	Gp_answer_wiki.textContent = response.Gp_answer_wiki;

	source_url = document.createElement("a");
	source_url.href = "https://fr.wikipedia.org/?curid="+response.wiki_id
	source_url.textContent = " [Plus de détails]";
	answer_wiki.textContent = response.wiki+" ";
	answer_wiki.appendChild(source_url);

	text_answer.appendChild(Gp_answer_gmap);
	text_answer.appendChild(Gp_answer_wiki);
	text_answer.appendChild(answer_wiki);

	actualise_map(response.latitude, response.longitude, response.gmap);
	papy_loading("off")
	query_text.disabled = false;
	}
	// if gmap returns nothing
	else {
		if (response.gmap === "ZERO_RESULT"){
			var Gp_answer = document.createElement("p");
			Gp_answer.textContent = response.Gp_answer;
			text_answer.appendChild(Gp_answer);
			papy_loading("off")
			query_text.disabled = false;
			}

		// if only wikimedia returns nothing
		else {
			Gp_answer_gmap.textContent = response.Gp_answer_gmap+" "+response.gmap;;
			Gp_answer_wiki.textContent = response.Gp_answer_wiki;
			text_answer.appendChild(Gp_answer_gmap);
			text_answer.appendChild(Gp_answer_wiki);
			papy_loading("off")
			query_text.disabled = false;
			}
	}
}


// GrandPy thinking animation
function papy_loading(state) {
	var papy_loading_pict = document.getElementById("papy_face");
	
	if (state === "on") {
		var papy_gif = document.createElement("img");
		papy_gif.src = "/static/img/gp_thinking.gif";
		papy_gif.alt = "gif_papy"
		papy_gif.title = "Je cherche..."
		papy_gif.id = "gif_papy"
		papy_loading_pict.replaceChild(papy_gif, document.getElementById("papy_face_pict"))

	} else {
		var papy_face_pict = document.createElement("img")
		papy_face_pict.src = "/static/img/gp_query.png";
		papy_face_pict.alt = "Papy_face";
		papy_face_pict.id = "papy_face_pict";
		papy_face_pict.addEventListener("click", user_request_analyse);
		papy_loading_pict.replaceChild(papy_face_pict, document.getElementById("gif_papy"))
	}
}


// if the query has more than 2 characters
function user_request_analyse()
{
	if (form.elements.query.value.length > 2) {
			button_papy_link();
					}
	else 	{
			not_enough_words();
					}
}

// Main function called when the client ask a question to GrandPy
function button_papy_link() {
	papy_loading("on");
	query_text.disabled = true;
	var request = form.elements.query.value;
	form.elements.query.value="";
	var global_user_request = document.createElement("div");
	global_user_request.id = "global_user_request";
	var figure_user = document.createElement("figure");
	var user_icon = document.createElement("img");
	user_icon.src = "/static/img/user_1200.png";
	user_icon.alt = "User:";
	user_icon.title = "User";
	figure_user.appendChild(user_icon);
	var user_request = document.createElement("p");
	user_request.textContent = request;
	user_request.id = "user_request-text";
	global_user_request.appendChild(figure_user);
	global_user_request.appendChild(user_request);
	dialogue.appendChild(global_user_request);
	var url = encodeURI("http://127.0.0.1:5000/results/?query="+request);
	ajaxGet(url, display);
	
}

// If the question less than 2 characters
function not_enough_words()
{
	var text_answer = document.createElement("div");
	text_answer.id = "text_answer";

	var global_gp_answer = document.createElement("div");
	global_gp_answer.id = "global_gp_answer";

	var figure_Gp = document.createElement("figure");
	var Gp_icon = document.createElement("img");
	Gp_icon.src = "/static/img/gp_1200.png";
	Gp_icon.alt = "GrandPy:";
	Gp_icon.title = "GrandPy";

	var Gp_answer = document.createElement("p");
	Gp_answer.textContent = "Les jeunes d'aujourd'hui n'utilisent pas assez de mots...";

	text_answer.appendChild(Gp_answer);
	figure_Gp.appendChild(Gp_icon);
	global_gp_answer.appendChild(figure_Gp);
	global_gp_answer.appendChild(text_answer);
	dialogue.appendChild(global_gp_answer);
}