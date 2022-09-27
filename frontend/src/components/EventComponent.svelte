<script>
    import dayjs from "dayjs";

    export let event;
    export let border;

</script>


<div class="{border ? 'border-t-2' : ''} border-b-2 border-rounded-lg border-gray-300 border-solid w-full">
    <a href={event.node.eventUrl} class="flex flex-col items-center">
        <div class="flex flex-col justify-between p-4 leading-normal items-center">
            <h5 class="mb-2 text-2xl font-bold text-django-600">{event.node.title}</h5>
            <p class="mb-3 font-normal text-gray-700">{event.node.dateTime ? dayjs(event.node.dateTime).format("dddd, MMMM, D YYYY").toString() : ''}</p>
            <h6 class="mb-1 text-xs text-black pb-3">{event.node.description.slice(0, 400) + event.node.description.length > 400 ? '...' : ''}</h6>
            <button class="bg-django-600 text-django-100 p-2 rounded-lg hover:bg-django-700 w-64">Meetup</button>
        </div>
    </a>
</div>