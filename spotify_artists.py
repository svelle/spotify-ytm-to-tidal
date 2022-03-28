import json
import tekore as tk

conf = tk.config_from_file('tekore.cfg', return_refresh=True)
user_token = tk.refresh_user_token(*conf[:2], conf[3])

spotify = tk.Spotify(user_token)

artists_out = []
last_old = "foo"
last = ""
while last_old != last:
    last_old = last
    if last != "":
        artists = spotify.followed_artists(limit=50,after=last)
    else:
        artists = spotify.followed_artists(limit=50)
    for artist in artists.items:
        artists_out.append(artist.name)
        last = artist.id

f = open("spotify_artists.json", "w")
f.write(json.dumps(artists_out))
f.close()