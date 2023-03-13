from __future__ import annotations

from typing import TYPE_CHECKING

import spotifystats.models.album as alb

def get_album(spotify_id: str) -> alb.Album:
    return alb.Album.objects(spotify_id=spotify_id).first()    
