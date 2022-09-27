<script>
    import { currentPage } from "../stores/currentPage";
    import useAxios from "../lib/useAxios"

    currentPage.set("Contact");

    let fullName;
    let email;
    let number;
    let message;

    const send = async () => {
        const api = useAxios();
        const response = await api.post("/send/", {
            fullName,
            email,
            number,
            message
        });
        groups = JSON.parse(response.data);
    };

</script>

<div class="flex flex-col flex-auto items-center">
    <div class="bg-django-900 w-full m-0 p-4 text-center">
        <h1 class="text-django-100 text-xl font-bold">contact us</h1>
    </div>
    <form class="my-10" on:submit|preventDefault={send}>
        <div class="flex flex-col my-4">
            <label class="text-django-600 text-xl" for="fullname">Full Name</label>
            <input class="border-b border-gray-300 border-solid w-full" type="text" name="fullname" bind:value={fullName} />
        </div>
        
        <div class="flex flex-col my-4">
            <label class="text-django-600 text-xl" for="email">Email</label>
            <input class="border-b border-gray-300 border-solid w-full" type="email" name="email" bind:value={email} />
        </div>

        <div class="flex flex-col my-4">
            <label class="text-django-600 text-xl" for="number">Phone Number</label>
            <input class="border-b border-gray-300 border-solid w-full" type="tel" name="number" bind:value={number} />
        </div>

        <div class="flex flex-col my-4">
            <label class="text-django-600 text-xl" for="message">Message</label>
            <textarea class="border border-gray-300 border-solid w-full my-2 py-4" bind:value={message} />
        </div>
        <button class="bg-django-600 text-django-100 rounded-lg p-2 w-64 m-4" type="submit">Send</button>
    </form>
</div>