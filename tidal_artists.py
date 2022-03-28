from traceback import print_tb
import tidalapi
import json

sp = open("spotify_artists.json")
sp_dict = json.load(sp)
yt = open("ytm_artists.json")
yt_dict = json.load(yt)

artists = []
for artist in sp_dict:
    artists.append(artist.lower())
for artist in yt_dict:
    artists.append(artist.lower())
artists.sort()
artists = list(dict.fromkeys(artists))

f = open("tidal_session.json")
data = json.load(f)
f.close

session = tidalapi.Session()
session.load_oauth_session(data['session_id'], data['token_type'], data['access_token'], data['refresh_token'])
favorites = tidalapi.Favorites(session, '') # REPLACE THIS WITH YOUR OWN USER ID

# session.login_oauth_simple()

# session_dict = {
#     "session_id":session.session_id,
#     "refresh_token":session.refresh_token,
#     "access_token":session.access_token,
#     "token_type":session.token_type
#     }

# f = open("tidal_session.json","w")
# f.write(json.dumps(session_dict))
# f.close()

# f = open("tidal_artists.json", "w")
# f.write(json.dumps(artist_names))
# f.close

tidal_artists = favorites.artists()
existing_artists =  []
for artist in tidal_artists:
    existing_artists.append(artist.name.lower())
    print(artist.name.lower())



print("-----")
print(artists[:10])
print("-----")

i = 0

rejected_artists = []

for artist in artists:
    if artist.lower() in existing_artists:
        continue
    i += 1
    sr = session.search('artist',artist)
    print(f'Searching for "{artist}". ({i}/{len(artists)})')
    if len(sr.artists) != 0:
        name = sr.artists[0].name
        if name.lower() in existing_artists:
            print("Top Search result already in Library, skipping.")
            print("=====================")
            continue
        print(f'Found "{name}".')
        add = input("Add Artist to library? (Y/n/a)")
        if add.lower() == 'y' or add.lower() == '':
            print(f'Adding {name} to library.')
            # print(sr.artists[0].id)
            favorites.add_artist(sr.artists[0].id)
            print("Done.")
        elif add.lower() == 'a':
            print("Aborting.")
            break
        else:
            print(f'Skipping {name}.')
            rejected_artists.append(name)
    else:
        print(f'Nothing found for {artist} skipping.')    
    print("=====================")

f = open("rejected.json", "w")
f.write(json.dumps(rejected_artists))
f.closen