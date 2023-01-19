import { getArtistById, collections } from "$lib/server/services/database.service"
import type { Document } from "mongodb";
import type Track from "$lib/model/track";
import type Artist from "$lib/model/artist";

import type { PageServerLoad } from "./$types"

async function getTopTracks(): Promise<Track[]> {
    let tracks: Track[] = (await collections.tracks?.aggregate([
        {
            $sort: { count: -1 }
        },
        {
            $limit: 50
        },
        {
            $lookup: {
                from: 'artists',
                localField: 'artists',
                foreignField: 'id',
                as: 'artists'
            }
        },{
            $project: {
                _id: 0,
                name: 1,
                count: 1,
                lastListened: "$last_listened",
                artists: {
                    $map: {
                        input: '$artists',
                        as: 'artist',
                        in: {
                            $mergeObjects: [
                                '$$artist',
                                {
                                    _id: 0
                                }
                            ]
                        }
                    }
                }
            }
        }
    ]).toArray()) as Track[];
    return tracks;
}

export const load: PageServerLoad = async function() {
    return {
        tracks: await getTopTracks(),
    }
}