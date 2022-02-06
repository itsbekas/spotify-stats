from config import firebase_project, spotify_scopes
from dotenv import load_dotenv
from util import *

from google.cloud import firestore

import spotipy
from spotipy.oauth2 import SpotifyOAuth

def run():
    log("Starting update")
    update_all_top_tracks()
    update_all_top_artists()
    log("Update finished")
    pass

def add_to_firebase(collection, document, data):~

    # Base document
    doc = db.collection(collection).document(document)
    # Save latest timestamp
    a = doc.set({
        'latest-timestamp': firestore.SERVER_TIMESTAMP
    }, merge=True)
    # Get saved timestamp
    timestamp = doc.get().to_dict()['latest-timestamp']
    # Select history collection from base document
    doc_history = doc.collection('history').document()
    # Set timestamp for current history document
    doc_history.set({
        'timestamp':timestamp,
    })

    for item in data:
        doc_history.collection('tracks').document().set(item)
        

    log("Added " + document.replace('_', ' ') + " " + collection.replace('-', ' ') + " to database.")

def get_top_tracks(time_range):
    log("Getting top tracks for", time_range.replace('_', ' '))
    response = sp.current_user_top_tracks(limit=50, offset=0, time_range=time_range)
    top_tracks = []
    for idx, item in enumerate(response['items']):
        track = {
            'position':idx+1,
            'id':item['id'],
            'name':item['name'],
            'artist':item['artists'][0]['name']
        }
        top_tracks.append(track)
    log("Got top tracks for", time_range.replace('_', ' '))
    return top_tracks

def update_all_top_tracks():
    log("Updating all top tracks")
    for time_range in time_ranges:
        top_tracks = get_top_tracks(time_range)
        add_to_firebase('top-tracks', time_range, top_tracks)
    log("Updated all top tracks")

def get_top_artists(time_range):
    log("Getting top artists for", time_range.replace('_', ' '))
    response = sp.current_user_top_artists(limit=50, offset=0, time_range=time_range)
    top_artists = []
    for idx, item in enumerate(response['items']):
        artist = {
            'position':idx+1,
            'id':item['id'],
            'name':item['name']
        }
        top_artists.append(artist)
    log("Got top artists for", time_range.replace('_', ' '))
    return top_artists

def update_all_top_artists():
    log("Updating all top artists")
    for time_range in time_ranges:
        top_artists = get_top_artists(time_range)
        add_to_firebase('top-artists', time_range, top_artists)
    log("Updated all top artists")

if __name__ == '__main__':

    global db, sp

    # Todo: Elapsed time

    print("------", currentDate(), "------")
    log("Initializing")
    
    # Load environment variables stored in .env
    load_dotenv()
    log("Credentials loaded")

    # Connect to Firestore
    log("Connecting to Firestore")
    db = firestore.Client(project=firebase_project)
    log("Connected to Firestore")

    # Connect to Spotify
    log("Connecting to Spotify")
    sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=spotify_scopes))
    log("Connected to Spotify")

    run()