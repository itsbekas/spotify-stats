import { spotify_stats } from "$lib/server/spotify-stats"

import type { PageServerLoad } from "./$types"

export const load: PageServerLoad = async function() {
    const data = await spotify_stats["artists"].find().sort({"count": -1}).limit(20).project({_id: 0}).toArray();
    return { artists: data }
}