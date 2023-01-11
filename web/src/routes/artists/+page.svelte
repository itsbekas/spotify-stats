<script lang="ts">
    import { timestampToDate } from "$lib/util";
	import type { PageData } from "./$types";

    export let data: PageData

    $: ({ artists } = data);
</script>

<section>
    <table class="table-auto">
        <tr>
            <th>Name</th>
            <th>Listen Count</th>
            <th>Last Listened</th>
        </tr>
        {#each artists as artist}
            <tr>
                <td>{artist.name}</td>
                <td>{artist.count}</td>
                <td>{timestampToDate(artist.last_listened)}</td>
            </tr>
        {/each}
    </table>
</section>