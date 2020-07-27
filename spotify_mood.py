from __future__ import print_function
import sys
import spotipy
import spotipy.util as util
import csv


class Track:
    def __init__(self, title, artist, track_id):
        self.title = title;
        self.artist = artist;
        self.track_id = track_id;
        self.danceability = 0
        self.energy = 0
        self.loudness = 0 
        self.speechiness = 0
        self.acousticness = 0
        self.instrumentalness = 0
        self.liveness = 0 
        self.valence = 0



def get_audio_features(sp, track_id, track_title):

    track_info = []
    track_info.append(track_title)
    track_info.append(sp.audio_features(track_id)[0]['danceability'])
    track_info.append(sp.audio_features(track_id)[0]['energy'])
    track_info.append(sp.audio_features(track_id)[0]['loudness'])
    track_info.append(sp.audio_features(track_id)[0]['speechiness'])
    track_info.append(sp.audio_features(track_id)[0]['acousticness'])
    track_info.append(sp.audio_features(track_id)[0]['liveness'])
    track_info.append(sp.audio_features(track_id)[0]['valence'])
    return track_info


def create_csv(tracks):
    fields = ['title','danceability', 'energy', 'loudness', 'speechiness', 'acousticness',
              'liveness', 'valence']
    
    filename = "tracks.csv"
    with open(filename, 'w') as csvfile:
        csvwriter = csv.writer(csvfile)
        csvwriter.writerow(fields)
        csvwriter.writerows(tracks)





def extract_data():
    
    # scope = "user-top-read"
    scope = "user-read-recently-played"
    username = '12121709026'
    token = util.prompt_for_user_token(username, scope)
    tracks = [] 

    if token:
        sp = spotipy.Spotify(auth=token)

        #getting user's recently played songs (top 50)

        results = sp.current_user_recently_played(limit=30)
        
        for item in results['items']:
            track = item['track']
            track_title = track['name']
            track_artist = track['artists'][0]['name']
            track_id = track['id']
            print(track_title)
            
            track_info = get_audio_features(sp, track_id, track_title)
            #print(track)
            tracks.append(track_info)
           # print('\n')

        '''
        #getting user's recent top tracks 
     #   results = sp.current_user_top_tracks(limit=5, time_range='short_term')

        print(results)
        for item in results['items']:
            song_title = item['name']
            song_artist = item['artists'][0]['name']

     
        '''
        print(tracks)
    else:
        print("error")

    return tracks


if __name__ == '__main__':
    tracks = extract_data()
    create_csv(tracks)
