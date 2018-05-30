# Project-7_GrandPy-Bot
### A bot that tells geography to users !

GrandPy Bot is the result of an open source project that integrates a back-end part based on Python and front-end part developed with HTML, CSS and JavaScript. It has been developed in an agile methodology following the TDD process, in a virtual environment and uses Flask framework, Bootstrap library and Google Maps and MediaWiki APIs.

Enter your geographic question in the search bar, you will see your requested place on a Google Map and some information about it in the dialogue area.
The interactions between GrandPy and the users are asynchronous (AJAX), so it is not necessary to reload the entire page to have a response.
*Note that for now this app is made for french users, because it returns the results in this language.*

### External resources
* [Trello board](https://trello.com/b/dFZZYaTC/oc-project-7-grandpy-bot) with the user stories to organize the project.

### To fork the Project
* *You must have*:
1. **Python 3.x** and **pip** package manager;
2. the use of a **virtual environment** is recommended;
3. **Flask** framework.

* *Requirements*:
1. tap `pip install requirements.txt` on your terminal.

* *Configuration*:
1. API keys
    * Google Map *Geocoding* API key,
    * Google Map *JavaScript* API key.
2. Flask secret key
3. Your local URL

* *Run the server*:
1. tap `python run.py` on your terminal.

### Note
GrandPy Bot app has been deployed and is hosted by Heroku.
