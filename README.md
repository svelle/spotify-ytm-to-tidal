# Transfer Music from Spotify and YouTube Music to Tidal

This program consists of three separate scripts: `spotify_artists.py`, `tidal_artists.py` and `ytm_artists.py` each script pulls the existing artists and stores them in a json file. The `tidal_artists.py` also compares existing artists, queries the Tidal library and prompts you if you want to add the found artist to your favorites.


## Setup

Each script basically uses whatever API Wrapper was simplest to use at the time of me writing this script and therefore relies on its own way of configuration.

The three libs used are:

- `tekore` for Spotify
- `tidalapi` for Tidal
- `ytmusicapi` for YouTube Music


### Setup tekore

To configure tekore you need to first create a new spotify application in the developer center: https://developer.spotify.com/dashboard/applications.
I have added a `tekore_default.cfg` which you can just copy and rename to `tekore.cfg` and fill out the missing fields. Note that the URL should stay the same otherwise the call won't work if you're deploying this locally.

### Setup ytmusicapi

This one is a bit more finnicky, basically you need to login to YTM in your browser and then copy the session headers and paste them into a file called `headers.json` for obvious security reasons I could not provide an example file. But really it's just following the steps here: https://ytmusicapi.readthedocs.io/en/latest/setup.html

### Setup tidalapi

The Tidal script *should* prompt you for authentication when you run it. However you'll need to replace the favorites id in the script with your own, which you'll need to pull from the Chrome dev console. Simply open up the Tidal Web Player and navigate to "Artists" (while keeping open the dev console) and look for the `artists` api call. In its Request Headers you should find a `:path:` header which looks something like `/v1/users/yourid/favorites/...` copy the `yourid` set of numbers and paste it into the `tidal_artists.py` where the comment tells you to replace the id.