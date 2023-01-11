<script lang="ts">
    import { timestampToDate } from "$lib/util";
	import type { PageData } from "./$types";

    import Track from './Track.svelte'

    export let data: PageData

    $: ({ tracks } = data);
</script>

<section>
    <table>
        <!-- <tr>
            <th>Name</th>
            <th>Artist</th>
            <th>Listen Count</th>
            <th>Last Listened</th>
        </tr> -->
        {#each [tracks[0]] as track}
            <Track track={track}/>
        {/each}
    </table>
</section>