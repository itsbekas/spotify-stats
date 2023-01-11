<script lang="ts">
	import type { PageData } from "./$types";

    export let data: PageData

    $: ({ ranking } = data);
</script>

<section>
    <table>
        <tr>
            <th>Position</th>
            <th>Track</th>
        </tr>
        {#each ranking[0]["tracks-short_term"] as trackId, i}
            <tr>
                <td>{i+1}</td>
                <td>{trackId}</td>
            </tr>
        {/each}
    </table>
</section>