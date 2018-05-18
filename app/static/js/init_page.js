// Script called when page has been loaded

// Display GrandPy icon and start the dialogue

var dialogue = document.getElementById("dialogue");
var form = document.querySelector("form");
var query_text = form.query;
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
Gp_answer.textContent = "Mon expérience est proportionnelle à mon savoir, mets-moi à l'épreuve !";

text_answer.appendChild(Gp_answer);
figure_Gp.appendChild(Gp_icon);
global_gp_answer.appendChild(figure_Gp);
global_gp_answer.appendChild(text_answer);
dialogue.appendChild(global_gp_answer);

// Add event on form
form.addEventListener("submit", function(e){
	e.preventDefault();
	
	if (form.elements.query.value.length > 2){
		button_papy_link();
	}
	else {
		not_enough_words();
	}
	
});