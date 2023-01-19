import { collections } from "$lib/server/services/database.service"

import type { PageServerLoad } from "./$types"

export const load: PageServerLoad = async function() {
    const data = await collections.rankings?.find().sort({"id": -1}).limit(1).project({_id: 0}).toArray();
    return { ranking: data }
}