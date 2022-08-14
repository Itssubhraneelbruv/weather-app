# weather-app
DESIGN GOALS

	Our program displays the weather in any city present in the world. It shows the visibility, Min-Max temperature, feels like, etc. This program uses a weather API to get the information and displays that information in the console

How does the program work?

Creating widgets:

           We use the modules tkinter, requests and PIL. The tkinter module helps to create the console and the elements present in the console. In this code we use the pack() function to place the widgets in the console. We Connected the butoon to the entry function using a lambda function.

 Connecting the API to the program:

              API stands for Application Programming Interface. An API enables companies to open up their applications' data and functionality to external third-party developers, business partners, and internal departments. Some examples of API-based interactions include a cloud application communicating with a server, servers pinging each other, or applications interacting with an operating system. To connect to the API we go to weatherapi.org. After signing up we copy the key which is provided by the website.



Making a GET request

                 In the user and the unit in which the temperature is shown. Then we use requests.get to get the information using requests module and then use json to convert the information sent by the website into a python dictionary. Json() helps in ending some data from the server to the client, so it can be displayed on a web the get function we enter the url of the website, the key, the city name which is given by page.

Getting information from the dictionary

               To get information from the dictionary we slice the dictionary and create w=different functions which contains different pieces of the dictionary. For ex: def visibility(responses) where responses contains the requests.get() function as mentioned above.

 


Using try except

            The try and except statements allows you to define a block of code to be tested for errors while it is being executed. The catch statement allows you to define a block of code to be executed, if an error occurs in the try block.

Linking the functions to the widgets

            After creating the user defined functions we link then to the function which contains the API key. In the API function each widget is linked to each function. The widgetss then take the returned value and display them in the console.



Changing the background:

           To change background we first download images related to temperatures available in the database. We then download the images in png form and save it in the name of given description i.e. broken clouds, sunny,etc. Then we create a function that uses PIL module to call the image in the program the image is called in the following syntax:
ImageTk.PhotoImage(Image.open(‘path’+description+’.png’)

How to use the program

To use the program we first run the program. After running the program a console appears with an entry widget and a search button beside it. Enter a city name in the entry and click the search button. The program gives back the weather and changes the background based on the condition of the city

Parts of the program

The program contains of 183 lines, it has 10 user defined functions and 14 widgets the console is of size 799x7000. It contains 20 png files.

Modules needed for this project

•	Tkinter
•	Requests
•	PIL
App features
•	provides accurate weather information based on location.
•	The forecasts are accentuated by images for clear comprehension
•	World-wide weather information
