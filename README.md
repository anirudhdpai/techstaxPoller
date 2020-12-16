# techstaxPoller
getting data from The Cocktail DB and RandomUser APIs and displaying them on a UI

Question:

Step 1: Build a Poll System to collect data 
Build an API Poller system than will asynchronously poll data from the 2 APIs below every 5 seconds Use GET method. No keys or tokens required these are open APIs. 
1. https://www.thecocktaildb.com/api/json/v1/1/random.php 
2. https://randomuser.me/api/ 
If you use Python you can use TornadoWeb(https://www.tornadoweb.org/en/stable/), else in other languages try to search for similar framework  which will make your work easier. 
Please make sure you are using Async, because the CPU cores should not wait for the process to get  over. We will verify your system usage when you submit the task.

Step 2: Save the data onto a DB 
Save the result to preferably a MongoDB (or any database of your choice). The data will be used to  populate the UI.

Step 3: Show new data on UI 
Make an UI that will show the below details and auto refreshers every 15 seconds with the recent data  from the DB. On UI only show the new data that was fetched in the last run, don’t show the older ones. 
You can take the html code from here. https://codepen.io/Brejkish/pen/xZPmXb 
Your page should look like the below image. However, feel free to experiment with your own design. We  are more interested in seeing how good you can connect UI to backend and not so much of design to  start with.
