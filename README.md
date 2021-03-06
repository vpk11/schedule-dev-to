# SCHEDULE DEV.TO ARTICLES
> Stay updated with latest posts from dev.to community on your Telegram.

---

## Technologies🚀

### Python version
- **3.8**

---

## Installation🚀

### Clone
-  Clone this repo to your local machine

### Setup
- Install `pip`

- Get into the project root folder

- Install requirements
```shell
pip install -r requirements.txt
```

- Create `.env` file in the project root folder
```shell
touch .env
```

- Add the following as environtment variables in the `.env` file just created
```shell
TELEGRAM_CHAT_ID=REPLACE-YOUR-TELEGRAM-CHAT-ID-HERE
BOT_URL=REPLACE-YOUR-BOT-URL-HERE
```

- Don't know how to create a bot and get chat id? No problem... [Click here](#telegram-bot)

- Finally! Run the script!
```shell
python3 main.py
```

- You should see messages from your bot in the group on telegram

---

## Telegram Bot🚀

### Creating a bot
- Use telegrams `BotFather` for creating Telegram Bots. Search `@BotFather`

- Start a new chat with BotFather. Send `/newbot`

- BotFather will take you further to create a bot.

- After successfull creation, you will get a `token` to access HTTP API.

- Copy that and pase it in your `bot_url` in constants.py

### How to get telegram_chat_id
- Add the Telegram BOT to the group.

- Get the list of updates for your BOT:
```shell
https://api.telegram.org/bot<YourBOTToken>/getUpdates
```

- Note: The api call returns empty if there are no chat history in the group.

- If updates are present there will be a `chat` key with `id` present in its value.

- This is your telegram_chat_id. - Copy that and pase it in your `telegram_chat_id` in constants.py

---

## Team🚀
> Our Contributors

<!-- prettier-ignore -->
| [<img src="https://avatars0.githubusercontent.com/u/16625110?s=200&u=5c59d8d73ba6850e98333d0149dc84a6fc196b14&v=3" width="75px;"/><br /><sub><b>👨‍💻vpk11👨‍💻</b></sub>](https://wwww.github.com/vpk11)<br /> |
| :---: |

---

## References🚀
 - DEV API: https://developers.forem.com/api/
