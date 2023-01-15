import { getArtistFromId, spotify_stats } from "$lib/server/spotify-stats"
import type { Document } from "mongodb";
import type Track from "$lib/model/track";
import type Artist from "$lib/model/artist";

import type { PageServerLoad } from "./$types"

async function getTopTracks(): Promise<Track[]> {
    let tracks = (await spotify_stats["tracks"].find().sort({"count": -1}).limit(150).project({"_id": 0}).toArray()) as Document[];
    let tracksWithArtists = await Promise.all(tracks.map(async track => track.artists.map(async (artist: string): Promise<Artist> => await getArtistFromId(artist))));
}

export const load: PageServerLoad = async function() {
    return {
        tracks: await getTopTracks(),
    }
}