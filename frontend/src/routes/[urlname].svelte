<script>
    import { page } from "$app/stores";
    import { onMount } from "svelte";
    import dayjs from "dayjs";
    import useAxios from "$lib/useAxios";
    import EventComponent from "../components/EventComponent.svelte"

    let group = {};
    let events = {};
    let pastEvents = [];
    let mounted = false;

    if ($page.params.urlname == "djangosocial-london") {
        pastEvents = [
            {
                node : {
                    eventUrl : 'https://www.meetup.com/djangosocial-london/events/286878309/',
                    title : 'Django Developer Picnic',
                    dateTime : null,
                    description : "It would be great to have one more Social before the height of the summer holidays. The weather is nice at the moment so we'll be getting the rugs out and having a picnic tea after work."
                }
            },
            {
                node : {
                    eventUrl : 'https://www.meetup.com/djangosocial-london/events/285592811/',
                    title : 'A walk in the park...',
                    dateTime : null,
                    description : "What better way to start the new era of Django social events than a simple walk in the park. Come along, for a meander through Regents park with fellow Django developers/enthusiasts/hobbyists after work on Thursday 26th May.Meet at Regents Park at 18:30 at the English Gardens. The walk will start at 7pm and last around an hour. There's no obligation to hang around afterwards but if enough people are interested there is the option of a drink at the nearby pub."
                }
            }
        ]
    }

    onMount(async () => {
        const api = useAxios();
        let urlname = $page.params.urlname;
        const response = await api.get(`/groups/${urlname}/`);
        group = JSON.parse(response.data).data.groupByUrlname;
        events = group.unifiedEvents.edges;
        mounted = true;
    })

</script>

{#if mounted}
    <div class="">
        <div class="bg-django-900 w-full m-0 p-4 text-center">
            <h1 class="text-django-100 text-xl font-bold">{group.name.toLowerCase()}</h1>
        </div>
        <div class="flex-col flex flex-auto text-black items-center text-center mx-auto md:w-1/3 sm:w-full">
            <div>
                <h1 class="my-3 text-2xl font-bold">What we're about</h1>
                <p class="mb-6 text-sm">{group.description}</p>
            </div>
            <div class="w-4/5">
                <h1 class="my-2 text-2xl font-bold">Upcoming Events</h1>
                {#if events.length < 1}
                <p>No events scheduled</p>
                {:else}
                    {#each events as e}
                        {#if e.node.timeStatus == "UPCOMING"}
                            {#if events.indexOf(e) > 0}
                                <EventComponent event={e} border={false}/>
                            {:else}
                                <EventComponent event={e} border={true} />
                            {/if}
                        {/if}
                    {/each}
                {/if}
            </div>
            <div class="w-4/5 my-8">
                <h1 class="my-2 text-2xl font-bold">Past Events</h1>
                {#if events.length < 1}
                <p>No past events</p>
                {:else}
                    {#each pastEvents as e}
                        {#if events.indexOf(e) > 0}
                            <EventComponent event={e} border={false}/>
                        {:else}
                            <EventComponent event={e} border={true} />
                        {/if}
                    {/each}
                {/if}
            </div>
        </div>
    </div>
{/if}