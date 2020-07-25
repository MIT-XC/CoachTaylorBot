# CoachTaylorBot

## Setup
To download the bot, run `git clone https://github.com/MIT-XC/CoachTaylorBot.git` in your terminal
Switch to the CoachTaylorBot folder by running `cd CoachTaylorBot`
Run `sh setup.sh` to install necessary packages (html5lib, bs4, markovify)

## Running the Bot
Run the bot by typing `python3 hwtaylor_bot.py` in the terminal from this directory

The following prompts will appear to customize the bot:
1. What years to train the bot on (default is 2016-2020)
2. What seasons to train the bot on (default is xc, indoor, and outdoor)
3. Only print sentences that contain a certain word (if this word is not present in the corpus, it will never appear in any sentences and the bot will keep running)
4. Whether to [Gizoogle](http://www.gizoogle.net/) the outputted sentences
