# twitter-sentiment-analysis-app
## Testing APIs
The testAPIs.ipynb file was created in order to be able to test the APIs 
freely, as is possible in a Jupyter notebook.<br><br>

## Front End Attempt
The twitter-sentiment-app folder has a react app that when run using ```npm start``` creates a local website in which you can login through a google account or a local account that you create. The information for accounts (other than passwords) is stored in a server that is accessible by us through google cloud. We assume the user's computer has the required dependencies (React, nodeJS) downloaded. The initial relevant code is in the folder src.zip. <br><br>

## Console App
Next, the console app that can be started by running getLastTweet.py (we coded it in Python 3.10.7, likely works with other python 3 versions) through the terminal: ```python getLastTweet.py [USERNAME TO SEARCH]``` where ```[USERNAME TO SEARCH]``` should be replaced with the twitter handle you wish to check (no @), or a list of user handles only separated by a comma (no spaces). If the file is run with no username, the program will default to @BU_tweets. Once run, the program will print out the most recent tweet by the user and automatically terminate the program. If any of the usernames given is not a real twitter username, the program will exit and just print "Username not found", this was done to avoid an excess use of the program by bots that are just guessing usernames.
