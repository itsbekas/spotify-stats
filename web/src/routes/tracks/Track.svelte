<!-- Track.svelte -->

<script lang="ts">
    import { getArtistFromId } from "$lib/spotify-stats";
    export let track: Document;
</script>

<div>
    <tl>{track.name}</tl>
    <tl>{getArtistFromId(track.artist[0]).name}</tl>
    <tl>{track.count}</tl>
    <tl>{track.last_listened}</tl>
</div>