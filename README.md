# sentimentbot
Discord bot that evaluates user messages for positivity and tracks  calculated behavior scores for each user using [TextBlob](https://textblob.readthedocs.io) and [discord.py](https://discordpy.readthedocs.io/en/latest/)

![alt text](https://raw.githubusercontent.com/novelqq/sentimentbot/master/sentiment_example.JPG)
## Installation
```
pip install textblob
python -m textblob.download_corpora
pip install discord
```

## Usage
1. Place discord bot token in `auth/token.txt`
2. run `$ python main.py`
3. In Discord, type "!score @user" to display @user current behavior score.

User data is stored in `/userdata.json`
