
<script>

    export let group;
    export let border;

</script>


<div class="{border ? 'border-t-2' : ''} border-b-2 border-rounded-lg border-gray-300 border-solid w-full">
    <a href={`/${group.node.urlname}`} class="flex flex-col items-center">
        <div class="flex flex-col justify-between p-4 leading-normal items-center">
            <h5 class="mb-4 text-2xl font-bold text-django-600">{group.node.name}</h5>
            <h6 class="mb-1 text-xs text-black pb-3">{group.node.description.slice(0, 400) + group.node.description.length > 400 ? '...' : ''}</h6>
            <button class="bg-django-600 text-django-100 p-2 rounded-lg hover:bg-django-700 w-64">View</button>
        </div>
    </a>
</div>