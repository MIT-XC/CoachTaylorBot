"""
Run the bot by typing "python3 hwtaylor_bot.py" in the terminal
from the directory containing this Python script

Run "sh setup.sh" to install necessary packages (html5lib, bs4, markovify)

Modify the capitalized variables at the top of this file to change
some parameters of the bot.
"""

import bs4
import markovify
import os
import re
import requests

DIR = os.path.dirname(os.path.abspath(__file__))
ARTICLES_DIRECTORY_PATH = os.path.join(DIR, "articles")
DEFAULT_START_YR = 2016
DEFAULT_END_YR = 2020
DEFAULT_SEASONS = ["xc", "itf", "otf"]
NUM_SENTENCES = 5

#Get user input about years, season, and optional keyword
default_years = [str(year) for year in range(DEFAULT_START_YR, DEFAULT_END_YR)]
user_input_year = input("Please enter the years you would like the model trained on separated by a dash, default is " + str(DEFAULT_START_YR) + "-" + str(DEFAULT_END_YR) + ": ")
if user_input_year:
    try:
        start_year, end_year = [int(year) for year in user_input_year.split("-")]
    except:
        print("Could not parse \"", user_input_year, "\"")
    target_years = [str(year) for year in range(start_year, end_year + 1)]
else:
    target_years = default_years
print("Years:", target_years)
print()

user_input_seasons = input("Please enter the seasons you would like the model trained on (e.g. \"xc, itf, otf\"), default is " + str(DEFAULT_SEASONS) + ": ")
if user_input_seasons:
    target_seasons = user_input_seasons.replace(" ", "").split(",")
else:
    target_seasons = DEFAULT_SEASONS
print("Seasons:", target_seasons)
print()

user_input_keyword = input("If you would like to only print sentences containing a certain word, enter that here (otherwise press Enter): ")
if user_input_keyword:
    print("Keyword:", user_input_keyword)
else:
    print("No keyword specified")
print()

do_gizoogle = (input("Gizoogle? [y/n] ") == 'y')
if do_gizoogle:
    print("Gizooglin output, phat chizzle!")
else:
    print("No gizoogle fo' you")
print()


#Combine all relevant articles
combined_text = ""
for s in target_seasons:
    for y in target_years:
        all_txt = os.path.join(ARTICLES_DIRECTORY_PATH, s, y, "all.txt")
        if os.path.exists(all_txt):
            with open(all_txt) as f:
                text = f.read()
                combined_text += text + "\n"

# Build the model.
text_model = markovify.Text(combined_text, state_size=3)

# Print five randomly-generated sentences
i = 0
while True:
    sentence = text_model.make_sentence()

    if do_gizoogle:
        params = {"translatetext": sentence}
        target_url = "http://www.gizoogle.net/textilizer.php"
        resp = requests.post(target_url, data=params)
        soup = bs4.BeautifulSoup(resp.text, "html5lib")
        sentence = soup.find("textarea").text

    if sentence:
        if user_input_keyword:
            if user_input_keyword in sentence:
                i += 1
                print(sentence)
        else:
            i += 1
            print(sentence)
    if i == NUM_SENTENCES:
        break
