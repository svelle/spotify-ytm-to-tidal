from ytmusicapi import YTMusic
import json

ytmusic = YTMusic('headers.json')
upload_artists = ytmusic.get_library_upload_artists(limit=2000)
artists = []
for artist in upload_artists:
    artists.append(artist["artist"])
library_artists = ytmusic.get_library_artists(limit=2000)
for artist in library_artists:
    artists.append(artist["artist"])

artists.sort()

artists = list(dict.fromkeys(artists))

f = open("ytm_artists.json", "w")
f.write(json.dumps(artists))
f.close()