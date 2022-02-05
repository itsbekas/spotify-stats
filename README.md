## spotify-stats

Spotify-stats is a python script meant to be ran on a server. It connects to the Spotify API and gets the user's data about top tracks and artists every 30 minutes, and stores them on a firestore database, to track changes and evolution.

### How to use
You'll need to create 2 files:

`.env`:
```
SPOTIPY_CLIENT_ID=spotipy-client-id
SPOTIPY_CLIENT_SECRET=spotipy-client-secret
SPOTIPY_REDIRECT_URI=redirect-uri
```

`config.py`:
```
firebase-project:your-project-id
spotify-scopes:'user-top-read'
```
