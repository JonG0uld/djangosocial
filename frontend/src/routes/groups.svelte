<script>

    import { onMount } from "svelte";
    import useAxios from "../lib/useAxios"
    import GroupComponent from "../components/GroupComponent.svelte"
    import { currentPage } from "../stores/currentPage"

    let groups = [];

    currentPage.set("Groups");

    onMount(async () => {
        const api = useAxios();
        const response = await api.get("/groups/");
        groups = JSON.parse(response.data).data.proNetworkByUrlname.groupsSearch.edges;
    })

</script>

<div>
    <div class="bg-django-900 w-full m-0 p-4 text-center">
        <h1 class="text-django-100 text-xl font-bold">django social groups</h1>
    </div>
    <div class="container mx-auto items-center flex flex-col flex-auto text-center my-10 md:w-1/3 sm:w-full">
        {#each groups as g}
            {#if groups.indexOf(g) > 0}
                <GroupComponent group={g} border={false}/>
            {:else}
                <GroupComponent group={g} border={true} />
            {/if}
        {/each}
    </div>
</div>