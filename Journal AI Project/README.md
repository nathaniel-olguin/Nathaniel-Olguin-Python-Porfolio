# Flow of the Program:



 	1.	User writes a journal entry.

 	2.	Program saves the entry to the entries folder.

 	3.	Program sends the text to analysis.

 	4.	Analysis returns:

 		▪	word frequency

 		▪	simple sentiment (positive or negative)

 		▪	length

 	5.	Program stores results in the reports folder.





# py file responsibilities:

#####  	◯  journal.py

######  		◉  Handles:

 				▪	getting the text from the user

 				▪	saving it into data/entries



#####  	◯  analysis.py

######  		◉  IMPORTANT INFO:

 				•	Depends on internal module: [My Py Modules/njro.py](https://github.com/nathaniel-olguin/Nathaniel-Olguin-Python-Porfolio/tree/main/My%20Py%20Modules)

######  		◉  Handles:

 				•	reading the text

 				•	analyzing it

 				•	returning results

 				•	saving a report into reports





# File name system:

#####  	◯  journal entries will be saved like:

 		 	▪	2025▪11▪29.txt

 		 	▪	2025▪11▪30.txt



#####  	◯  reports will be saved similarly:

 		 	▪	report\\\_2025▪11▪29.json

 		 	▪	report\\\_2025▪11▪30.json



#####  	◯  The program will need to:

 		 	▪	get today’s date

 		 	▪	use it for file names





# Project Goals:

#####  	◯  Minimum goals:

 			✔ Save text to a file

 			✔ Analyze word frequency

 			✔ Count number of words

 			✔ Print the results



#####  	◯  Stretch goals:

 			⬜ Simple sentiment scoring

 			⬜ Create a JSON report

 			⬜ Build a tiny web interface later

 			⬜ Add charts or graphs

