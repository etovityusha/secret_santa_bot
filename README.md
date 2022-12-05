# Secret Santa Bot

#### What is Secret Santa?

Secret Santa is a simple way to exchange gifts among a group of people. This bot is designed to help you run a Secret Santa exchange.

#### How does it work?

The bot will randomly assign people to give presents to each other.
It will then send a message to each person with the name of the person they are giving a gift to.
Who will have to give the gift to you, you will find out only when you all meet.

#### How do I run it on my computer?

1) Get your token from BotFather
2) Create file ".env" in the root directory of the project
3) Paste your token into the file like this `TOKEN=bot_token OWNER=your_telegram_username`
4) [Create a virtual environment](https://docs.python.org/3/tutorial/venv.html#creating-virtual-environments)
5) Install dependencies with `pip install -r requirements.txt`
6) Run the bot with `python3 main.py`
7) Invite your friends to the bot
8) Run `/roll` command owner of the bot

All users will receive their Secret Santa assignments! 🎁

#### How do I run it on a server?

You can use [Heroku](https://www.heroku.com/) to run the bot on a server. You can find a tutorial [here](https://devcenter.heroku.com/articles/getting-started-with-python).

##### Other

In MVP version bot supports only russian language.
This project shows transition from a quickly written minimal version to a more stable and reliable. The project is under active development.

##### TODO:

[x] Make MVP version with memory storage and Russian language
[ ] Split logic into layers (handlers, services, repositories)
[ ] Support more storage types (local file, MongoDB, PostgreSQL)
[ ] Test all layers
[ ] Support more languages (English, Spanish)
[ ] Dockerize
