<script>
   import { currentPage } from "../stores/currentPage";

   currentPage.set("Index");

</script>

<div class="contianer mx-auto items-center flex flex-col flex-auto text-center ">
    <div class="bg-django-900 w-full py-36">
        <h1 class="text-6xl my-4 font-bold text-django-100">django.social</h1>
        <br />
        <p class="text-sm text-django-100 font-bold">Inclusive social events for the django community</p>
    </div>
    <div class="w-3/4 py-8">
        <h1 class="text-3xl font-bold text-black mb-4">About</h1>
        <p class="text-sm text-black">
            Welcome to django social.<br>
            This is the home of easy to run events for the django community worldwide.<br>
            Our mission is simple, bring the community together and socialise.<br>
            Django social events are oppurtunities to meet with local django enthusiasts in your area. An event can be as simple as a walk in the park, playing board games or something fancier (if you have a willing sponser).<br>
            With the world opening up again after the pandemic a lot of people find themselves without social interactions that they once had through working in an office. People have also re-located, moving to new cities. Finding a local Django Social event should be easy.<br>
            The idea for django social started with Jon Gould, running the inaugural events in London in 2022, <a class="text-blue-400" href="https://www.Linkedin.com/in/jongould">Jon</a> runs <a class="text-blue-400" href="https://www.foxleytalent.com">Foxley Talent</a>, the go-to recruitment company within the Python and Django communities.<br>
            If you want to find out more about our groups, get in <a class="text-blue-400" href="/contact/">contact</a> or find out about running your own django social event please explore the site for more information.

        </p>
    </div>
    <div class="w-3/4 py-8">
        <h1 class="text-3xl font-bold text-black mb-4">Gallery</h1>
        <div class="flex gap-4 justify-center content-center justify-items-center flex-wrap">
            <img src="/images/image1.jpeg" alt="image1"/>
            <img src="/images/image2.jpeg" alt="iamge2"/>
            <img src="/images/image3.jpeg" alt="image3"/>
            <img src="/images/image4.jpeg" alt="image4"/>
            <img src="/images/image5.jpeg" alt="image5"/>
        </div>
    </div>
</div>
