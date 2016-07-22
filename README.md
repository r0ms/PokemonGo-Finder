# Pokemon Go Notification System

This is a fork of [the popular PokemonGo-Map repository](https://github.com/AHAAAAAAA/PokemonGo-Map) with the purpose of allowing users to search for specific Pokemon without having to constantly monitor the map of nearby Pokemon. It's team minded, because this allow you and your team to efficiently track Pokémon that spawn near your work location and go hunting during lunch break ;) . All API and map functionality was left untouched.


## Config File
Instead of from the command-line, all arguments are read from a `config.json` file. In addition to all of the options laid out [here](https://github.com/AHAAAAAAA/PokemonGo-Map/wiki/Usage), I've introduced three required fields: `slackWebhook` to obviously join a channel on Slack and latitude and longitude to calculate the distance between you and the Pokémon.
Here's a sample `config.json`:

```
{
  "auth_service": "google",
  "username": "myemailuser",
  "password": "pikachu123",
  "step_limit": 5,
  "location": "30, rue de la Victoire, Paris",
  "latitude" : 48.875418,
  "longitude": 2.338118,
  "notify": "dratini,magnemite,electabuzz,hitmonchan,hitmonlee,chansey,lapras,snorlax,porygon,mew,mewtwo,moltres,zapdos,articuno,ditto,seel,gyarados,cubone",
  "slackWebhook" : "https://hooks.slack.com/services/youslackwebhook"
}
```

## Install

Install the necessary dependencies (including the Pushbullet client) by running `pip install --upgrade -r requirements.txt`. Create a config file and then run the main script using `python main.py`.

*Using this software is against the ToS and can get you banned. Use at your own risk.*

## Notifications
You'll have to set up notifications where you'd like to receive them. I installed the [Pushbullet Chrome Extension](https://chrome.google.com/webstore/detail/pushbullet/chlffgpmiacpedhhbkiomidkjlcfhogd?hl=en) and then decided that I found more utility by installing the Pushbullet iPhone app and receiving the notifications on my phone.
