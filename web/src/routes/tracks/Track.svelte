<!-- Track.svelte -->

<script lang="ts">
    import type Track from "$lib/model/track";
    export let track: Track;
</script>

<tr>
    <td>{track.name}</td>
    <td>{track.artists[0].name}</td>
    <td>{track.count}</td>
    <td>{track.lastListened}</td>
</tr>
