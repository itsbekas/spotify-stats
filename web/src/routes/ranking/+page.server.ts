import { spotify_stats } from "$lib/server/spotify-stats"

import type { PageServerLoad } from "./$types"

export const load: PageServerLoad = async function() {
    const data = await spotify_stats["rankings"].find().sort({"id": -1}).limit(1).project({_id: 0}).toArray();
    return { ranking: data }
}