import { collections } from "$lib/server/services/database.service"

import type { PageServerLoad } from "./$types"

export const load: PageServerLoad = async function() {
    const data = await collections.artists?.find().sort({"count": -1}).limit(20).project({_id: 0}).toArray();
    return { artists: data }
}