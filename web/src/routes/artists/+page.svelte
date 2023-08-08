<script>
  import { onMount } from 'svelte';
  import { getArtists } from '../api';

  let artists = [];

  onMount(async () => {
    artists = await getArtists(50);
  });
</script>

<ul>
  {#each artists as artist (artist.id)}
    <li>{artist.name}</li>
  {/each}
</ul>
