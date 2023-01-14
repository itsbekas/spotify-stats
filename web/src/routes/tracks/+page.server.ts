import { spotify_stats } from "$lib/spotify-stats"

import type { PageServerLoad } from "./$types"

export const load: PageServerLoad = async function() {
    const tracks = await spotify_stats["tracks"].find().sort({"count": -1}).limit(150).project({_id: 0}).toArray();
    return {
        tracks: data,

    }
}