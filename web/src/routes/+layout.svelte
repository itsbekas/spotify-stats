<script>
    import "../app.css";
    import Navbar from "./Navbar.svelte";
</script>

<div class="bg-neutral-900 mx-auto w-full min-h-screen h-full">
    <Navbar/>
    <div class="text-zinc-200 flex justify-center">
        <slot/>
    </div>
</div>

