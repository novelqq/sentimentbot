# sentimentbot
Discord bot that tracks users behavior scores using TextBlob and discord.py

## Installation
```
pip install textblob
python -m textblob.download_corpora
pip install discord
```

## Usage
1. Place discord bot token in `auth/token.txt`
2. `$ python main.py`
3. In Discord, type "!score @user" to display @user current behavior score.
4. User data is stored in `/userdata.json`
