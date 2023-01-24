import type Ranking from "$lib/model/ranking";
import { collections } from "$lib/server/services/database.service"

import type { PageServerLoad } from "./$types"

async function getCurrentRanking(): Promise<Ranking> {
    let ranking = await collections.rankings?.aggregate([
        {
            $sort: { id: -1 }
        },
        {
            $limit: 1
        },
        {
            $lookup: {
                from: "tracks",
                localField: "tracks_short_term",
                foreignField: "_id",
                as: "tracks_short_term"
            }
        },
        {
            $unwind: "$tracks_short_term"
        },
        {
            $project: {
                _id: 0,
                timestamp: "$id",
                tracks: "$tracks_short_term"
            }
        }
    ]).next();
    return ranking;
}

export const load: PageServerLoad = async function() {
    return {
        ranking: await getCurrentRanking(),
    }
}