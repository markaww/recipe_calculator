# Recipe calculator

### At home, we use this program when we plan our weekly meals, before we go shopping. It helps us not only keep our choices original and interesting, but it also helps us save a lot of time when we plan our meals.

<img src="https://static01.nyt.com/images/2017/09/25/dining/bonebrothchickenstock/bonebrothchickenstock-articleLarge.jpg">


This tool produces a selection of recipes, classified into 7 categories (Beef, chicken, pork, pasta, seafood/fish, salads and healthy recipes). 

The program uses webscraping to get recipe URLs off the website allrecipes.com, and stores them into a dictionary as values, where the corresponding key is a recipe category. 

Then, for each category key, 3 recipe url values are randomly selected. The output is compiled into a list and sent via email. 

NOTE: for this program to run correctly, e-mail information is required. You will need to set up an environment variables file with the necessary e-mail information. 
Simply create a file in your root folder called '.bash_profile' and copy into it the 3 lines below using your own email information:
 
export EMAIL="youremail"

export PASSWORD="yourpassword"

export DESTINATION="yourdestinationemail" 

_An additional step you may want to consider is automation. In my case, I have setup a crontab job that makes this program run automatically on a weekly basis so I don't have to go and fetch new recipes, comfortably receiving them in my email directly._ 

Enjoy your cooking! 
