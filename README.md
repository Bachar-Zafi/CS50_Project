# CS50_Project

# Zafi's personal project - Querying asset climate risk results – converting Json data into a sqlite3 database to be queried through a user-friendly web browser interface

#### Video Demo:  <URL HERE>
#### Description:

In this project I built a Flask-based web application to enable a user to gain insights into their asset’s modelled climate risks results (originally stored in JSON format) by submitting a few basic queries through a (drop down box-based) browser interface. 

The answer to each query (submitted by a user by clicking a ‘submit’ button) is displayed at the bottom of the webpage (e.g. “The asset's VAR in your chosen year of 2090 is: 0.00022”). 

To enable this browser-based querying process I had to complete the following key steps:

-	Using Flask, set up a server connection through which to display information in a web browser

-	Using python dictionaries, pull out the relevant data from the JSON file and use it to populate two sqlite3 database tables.

-	Set up a HTML file to enable the browser display of the following three basic query types, using drop down boxes (note VAR, TIP and FP are three commonly used climate risk metrics):

o	What is the asset’s value at risk (VAR) / technical insurance premium (TIP) / failure probability (FP) in a given year (user chooses a year from a drop-down box)?
o	What is the hazard with the highest VAR / FP in a given year (user chooses a year from a drop-down box)?
o	In what year was this asset's maximum (user chooses a metric – VAR / TIP / FP) reached?

Following is a description of all files used in the project and the functions they each perform:

File name	File type	Key functions performed
temp.json	JSON	-	Holding the original dataset of modelled asset risk results in a lightweight format
Queries.py	Python	-	Enabling the querying (through the use of cursor.execute commands) of the sqlite3 database so as to respond to any of the three types of questions the user can submit in the browser
App.py	Python	-	Calling the appropriate function for each application route, to handle both the GET and POST cases 
-	Rendering the html templates to be displayed in the browser
Create_changing_table.py	Python	-	Generates the schema of the full SQL table user to answer user queries
Json_to_SQL_Code.py	Python	-	Converting all metric data read from the JSON file into Python dictionaries (e.g. Haz_FP_by_Year and Hazard_VAR_by_Year)
-	Creating the sqlite3 database holding all the relevant asset risk information the user will be able to query through the browser interface
Project_webpage.html	HTML	-	Setting up the querying text the drop down boxes and the ‘submit’ buttons to be displayed in the browser 
MyDataBase.db	sqlite3 database	This sqlite3 database contains the following 2 tables, which between them hold all the information originally held in the JSON file:
-	full_table – containing all modelled risk information to be used in answering the user’s climate risk queries, i.e. all modelled FP and VAR results for each year between 1990 and 2100, for 8 climate hazards and for the asset as a whole, as well as TIP results for the asset as a whole
-	non_changing – containing general reference information about the asset, such as its geo- location (in latitude and longitude) and its heat threshold 



