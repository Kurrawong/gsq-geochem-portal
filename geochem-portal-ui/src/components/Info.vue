<script setup lang="ts">
const props = defineProps<{ large: boolean }>()
</script>

<template>
  <aside class="lg:col-span-1" :class="{ 'lg:block hidden': props.large }">
    <article class="bg-[#f8f8fa] p-5">
      <h2 class="text-xl">Documentation</h2>

      <article>
        <h3 class="text-base">Geochemistry Standard</h3>
        <ul class="list-disc pl-[2rem]">
          <li><a href="http://linked.data.gov.au/def/geochem/overview" target="_blank">Overview <i class="pi pi-external-link"></i></a></li>
          <li><a href="http://linked.data.gov.au/def/geochem" target="_blank">The Specification <i class="pi pi-external-link"></i></a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Profiles</h3>
        <p><em><a href="">What is a Profile?</a></em></p>
        <ul class="list-disc pl-[2rem]">
          <li><a href="https://kurrawong.github.io/gsq-geochem/spec.html#_core_profile" target="_blank">Core <i class="pi pi-external-link"></i></a></li>
          <li><a href="https://kurrawong.github.io/gsq-geochem/spec.html#_gsq_profile" target="_blank">GSQ <i class="pi pi-external-link"></i></a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Vocabularies</h3>
        <p><em><RouterLink to="/vocabs">What is a Vocabulary?</RouterLink></em></p>
        <ul class="list-disc pl-[2rem]">
          <RouterLink to="/vocabs">Vocabularies Page</RouterLink>
        </ul>
      </article>

    </article>
  </aside>
</template>
