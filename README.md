<<<<<<< HEAD
# PokemonGo-Bot
[PokemonGo-Bot](https://github.com/PokemonGoF/PokemonGo-Bot) is a project created by the [PokemonGoF](https://github.com/PokemonGoF) team.

## Table of Contents
- [Installation](https://github.com/PokemonGoF/PokemonGo-Bot/blob/dev/docs/installation.md)
- [Documentation](https://github.com/PokemonGoF/PokemonGo-Bot/blob/dev/docs/)
- [Support](#support)
 - [Help](#configuration-issueshelp)
 - [Bugs](#bugs--issues)
 - [Feature Requests](#feature-requests)
 - [Pull Requests](#pull-requests)
- [Features](#features)
- [Credits](#credits)

The project is currently setup in two main branches:
- `dev` also known as `beta` - This is where the latest features are, but you may also experience some issues with stability/crashes.
- `master` also known as `stable` - The bot 'should' be stable on this branch, and is generally well tested.

## Support
### Development Channel
[![Join the chat at https://gitter.im/pikabot-org/Lobby](https://badges.gitter.im/pikabot-org/db.svg)](https://gitter.im/pikabot-org/Lobby?utm_source=badge&utm_medium=badge&utm_campaign=pr-badge&utm_content=badge)

### Configuration issues/help
If you need any help please don't create an issue as we have a great community on Slack. You can count on the community in [#help](https://pokemongo-bot.slack.com/messages/help/) channel.
 - [Click here to signup (first time only)](https://pokemongo-bot.herokuapp.com)
 - [Join here if you're already a member](https://pokemongo-bot.slack.com/messages/general/)

###[Bugs / Issues](https://github.com/PokemonGoF/PokemonGo-Bot/issues?q=is%3Aissue+sort%3Aupdated-desc)
If you discover a bug in the bot, please [search our issue tracker](https://github.com/PokemonGoF/PokemonGo-Bot/issues?q=is%3Aissue+sort%3Aupdated-desc) first. If it hasn't been reported, please [create a new issue](https://github.com/PokemonGoF/PokemonGo-Bot/issues/new) and ensure you follow the template guide so that our team can assist you as quickly as possible.

###[Feature Requests](https://github.com/PokemonGoF/PokemonGo-Bot/labels/Feature%20Request)
If you have a great idea to improve the bot, please [search our feature tracker](https://github.com/PokemonGoF/PokemonGo-Bot/labels/Feature%20Request) first to ensure someone else hasn't already come up with the same great idea.  If it hasn't been requested, please [create a new request](https://github.com/PokemonGoF/PokemonGo-Bot/issues/new) and ensure you follow the template guide so that it doesnt get lost with the bug reports.
While you're there vote on other feature requests to let the devs know what is most important to you.

###[Pull Requests](https://github.com/PokemonGoF/PokemonGo-Bot/pulls)
If you'd like to make your own changes, make sure you follow the pull request template, and ensure your PR is made against the 'dev' branch.

If this is your first time making a PR or aren't sure of the standard practice of making a PR, here are some articles to get you started.
 - [GitHub Pull Request Tutorial](https://www.thinkful.com/learn/github-pull-request-tutorial/)
 - [How to write the perfect pull request](https://github.com/blog/1943-how-to-write-the-perfect-pull-request)
 - [A great example from one of our own contributors](https://github.com/PokemonGoF/PokemonGo-Bot/pull/3912)

## Features
- [x] GPS Location configuration
- [x] Search Pokestops
- [x] Catch Pokemon
- [x] Determine which pokeball to use (uses Razz Berry if the catch percentage is low!)
- [x] Exchange Pokemon as per configuration
- [x] Evolve Pokemon as per configuration
- [x] Auto switch mode (Inventory Checks - switches between catch/farming items)
=======
# PokemonGo-Bot - a pokemon script that can catch pokemons and spin the pokestops.

## Project chat

[![Slack Status](https://pokemongo-bot.herokuapp.com/badge.svg)](https://pokemongo-bot.herokuapp.com)

We use [Slack](https://slack.com) as a web chat. [Click here to join the chat!](https://pokemongo-bot.herokuapp.com)

## Features:
 * Search Fort(Spin Pokestop)
 * Catch Pokemon
 * Release low cp pokemon
 * Walking as you
 * Use the ball you have to catch, don't if you don't have

# To-Do:
- [ ] Google Map API key setup
>>>>>>> ab604452c2a0a72e13fa6d940fa55902d3b01466
- [x] Limit the step to farm specific area for pokestops
- [x] Rudimentary IV Functionality filter
- [x] Ignore certain pokemon filter
- [x] Adjust delay between Pokemon capture & Transfer as per configuration
- [x] Hatch eggs
- [x] Incubate eggs
- [x] Crowd Sourced Map Prototype
- [ ] [Standalone Desktop Application] (https://github.com/PokemonGoF/PokemonGo-Bot-Desktop)
- [ ] Use candy
<<<<<<< HEAD
=======
- [x] Code refactor

## Installation

### Python Installation
    [Install Python 2.7](https://wiki.python.org/moin/BeginnersGuide/Download)
    [Install PIP](https://pip.pypa.io/en/stable/installing/)
### Google Protobuf Installation
    MAC:  brew update && brew install --devel protobuf
### Install Pokemon_Go_Bot

    Download or clone the repository.
    Using a terminal navigate into the clone repository.
    Install all requirements for the project using `pip install -r ./requirements.txt`
### Google Maps API (Code is not done yet)


Google Maps API: a brief guide to your own key

This project uses Google Maps. There's one map coupled with the project, but as it gets more popular we'll definitely hit the rate-limit making the map unusable. That said, here's how you can get your own and replace ours:

1. Navigate to this [page](https://console.developers.google.com/flows/enableapi?apiid=maps_backend,geocoding_backend,directions_backend,distance_matrix_backend,elevation_backend,places_backend&keyType=CLIENT_SIDE&reusekey=true)
2. Select 'Create a project' in the dropdown menu.
3. Wait an eternity.
4. Click 'Create' on the next page (optionally, fill out the info)
5. Copy the API key that appears.
6. After the code done, will update here how to replace.

## Usage
    usage: pokecli.py [-h] -a AUTH_SERVICE -u USERNAME -p PASSWORD -l LOCATION [-w]  [-d] [-t] [-s] [-c]

    optional arguments:
      -h, --help                                    show this help message and exit
      -a AUTH_SERVICE, --auth_service AUTH_SERVICE  Auth Service ('ptc' or 'google')
      -u USERNAME, --username USERNAME              Username
      -p PASSWORD, --password PASSWORD              Password
      -l LOCATION, --location LOCATION              Location (Address or 'xx.yyyy,zz.ttttt')
      -w SPEED,  --walk SPEED                       Walk instead of teleport with given speed (meters per second max 4.16 because of walking end on 15km/h)
      -s SPINSTOP, --spinstop                       Enable Spinning of PokeStops
      --maxstep MAX_STEP                            Set the steps around your initial location(DEFAULT 5 mean 25 cells around your location)
      -c CP, --cp                                   Set the CP to transfer or lower (eg. 100 will transfer CP0-99) OR use 'smart' to Releases same types of pokemon with lower CP on every catch and keeping single copy of pokemon with highest CP. (Note: this will also release your existing pokemon. Use with caution)
      -d, --debug                                   Debug Mode
      -t, --test                                    Only parse the specified location
      -tl, --transfer_list                          Transfer These Pokemons regardless their CP


### Command Line Example
    Pokemon Trainer Club (PTC) account:
    $ python2 pokecli.py -a ptc -u tejado -p 1234 --location "New York, Washington Square"
    Google Account:
    $ python2 pokecli.py -a google -u tejado -p 1234 --location "New York, Washington Square"

## FAQ

### Losing Starter Pokemon and others
    You can use -c 1 to protect your first stage low CP pokemon.
### Does it run automatally?
    Not yet, still need a trainer to train the script param. But we are very close to.
### Set GEO Location
    It works, use -l "xx.yyyy,zz.ttttt" to set lat long for location. -- diordache
### FLEE
   The status code "3" corresponds to "Flee" - meaning your Pokemon has ran away.
   {"responses": { "CATCH_POKEMON": { "status": 3 } }
### My pokemon are not showing up in my Pokedex?
   Finish the tutorial on a smartphone. This will then allow everything to be visible.
### How can I maximise my XP per hour?
Quick Tip: When using this script, use a Lucky egg to double the XP for 30 mins. You will level up much faster. A Lucky egg is obtained on level 9 and further on whilst leveling up. (from VipsForever via /r/pokemongodev)



## Requirements
 * Python 2
 * requests
 * protobuf
 * gpsoauth
 * geopy
 * s2sphere
 * googlemaps


## Contributors (Don't forget add yours here when you create PR:)
eggins -- The first pull request :)  
crack00r  
ethervoid
Bashin
tstumm
TheGoldenXY
Tienkhoi
>>>>>>> ab604452c2a0a72e13fa6d940fa55902d3b01466

## Gym Battles
[PokemonGo-Bot](https://github.com/PokemonGoF/PokemonGo-Bot) takes a strong stance against automating gym battles. Botting gyms will have a negative effect on most players and thus the game as a whole. We will thus never accept contributions or changes containing code specific for gym battles.

## Analytics
[PokemonGo-Bot](https://github.com/PokemonGoF/PokemonGo-Bot) is very popular and has a vibrant community. Because of that, it has become very difficult for us to know how the bot is used and what errors people hit. By capturing small amounts of data, we can prioritize our work better such as fixing errors that happen to a large percentage of our user base, not just a vocal minority.

Our goal is to help inform our decisions by capturing data that helps us get aggregate usage and error reports, not personal information. To view the code that handles analytics in our master branch, you can use this [search link](https://github.com/PokemonGoF/PokemonGo-Bot/search?utf8=%E2%9C%93&q=BotEvent).

If there are any concerns with this policy or you believe we are tracking something we shouldn't, please open a ticket in the tracker. The contributors always intend to do the right thing for our users, and we want to make sure we are held to that path.

If you do not want any data to be gathered, you can turn off this feature by setting `health_record` to `false` in your `config.json`.

## Credits
- [tejado](https://github.com/tejado) many thanks for the API
- [U6 Group](http://pgoapi.com) for the U6
- [Mila432](https://github.com/Mila432/Pokemon_Go_API) for the login secrets
- [elliottcarlson](https://github.com/elliottcarlson) for the Google Auth PR
- [AeonLucid](https://github.com/AeonLucid/POGOProtos) for improved protos
- [AHAAAAAAA](https://github.com/AHAAAAAAA/PokemonGo-Map) for parts of the s2sphere stuff
- [Breeze ro](https://github.com/BreezeRo) for some of the MQTT/Map stuff

## Contributors
 * eggins [first pull request]
 * crack00r
 * ethervoid
 * Bashin
 * tstumm
 * TheGoldenXY
 * Reaver01
 * rarshonsky
 * earthchie
 * haykuro
 * 05-032
 * sinistance
 * CapCap
 * mzupan
 * gnekic(GeXx)
 * Shoh
 * luizperes
 * brantje
 * VirtualSatai
 * dmateusp
 * jtdroste
 * msoedov
 * Grace
 * Calcyfer
 * asaf400
 * guyz
 * DavidK1m
 * budi-khoirudin
 * riberod07
 * th3w4y
 * Leaklessgfy
 * steffwiz
 * pulgalipe
 * BartKoppelmans
 * phil9l
 * VictorChen
 * AlvaroGzP
 * fierysolid
 * surfaace
 * surceis
 * SpaceWhale
 * klingan
 * reddivision
 * DayBr3ak
 * kbinani
 * mhdasding
 * MFizz
 * NamPNQ
 * z4ppy.bbc
 * matheussampaio
 * Abraxas000
 * lucasfevi
 * pokepal
 * Moonlight-Angel
 * mjmadsen
 * nikofil
 * bigkraig
 * nikhil-pandey
 * thebigjc
 * JaapMoolenaar
 * eevee-github
 * g0vanish
 * cmezh
 * Nivong
 * kestel
 * simonsmh
 * joaodragao
 * extink
 * Quantra
 * pmquan
 * net8q
 * SyncX
 * umbreon222
 * DeXtroTip
 * rawgni
 * Breeze Ro
 * bruno-kenji

## Disclaimer
©2016 Niantic, Inc. ©2016 Pokémon. ©1995–2016 Nintendo / Creatures Inc. / GAME FREAK inc. © 2016 Pokémon/Nintendo Pokémon and Pokémon character names are trademarks of Nintendo. The Google Maps Pin is a trademark of Google Inc. and the trade dress in the product design is a trademark of Google Inc. under license to The Pokémon Company. Other trademarks are the property of their respective owners.
[Privacy Policy](http://www.pokemon.com/us/privacy-policy/)

[PokemonGo-Bot](https://github.com/PokemonGoF/PokemonGo-Bot) is intended for academic purposes and should not be used to play the game *PokemonGo* as it violates the TOS and is unfair to the community. Use the bot **at your own risk**.

[PokemonGoF](https://github.com/PokemonGoF) does not support the use of 3rd party apps or apps that violate the TOS.


[![Analytics](https://ga-beacon.appspot.com/UA-81468120-1/welcome-page-master)](https://github.com/igrigorik/ga-beacon)
