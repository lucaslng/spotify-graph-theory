# Spotify Graph Theory

A Spotify webscraper to create a graph of users and the users they follow.

## Disclaimer

This is 100% against Spotify TOS, use at your own risk

## How to use

- clone
- make a .env using example.env
  - TOKEN is the value of the sp_dc cookie when you open spotify.com which can be obtained by logging into spotify on a browser -> going to any website ending with spotify.com -> inspect menu -> applications tab -> cookies -> copy the very long string value of the sp_dc cookie
  - TARGETID is the Spotify userid of the origin of the graph that you want to create. The userid can be obtained by going to the user on a browser and looking at the url which should be <https://open.spotify.com/user/><user id\>
- run main.py
