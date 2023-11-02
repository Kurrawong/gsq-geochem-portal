<script setup lang="ts">
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'

import { ref } from 'vue';

const profileQVisible = ref(false);
const vocabQVisible = ref(false);

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
        <a
            @click="profileQVisible = true"
            class="italic cursor-pointer"
        >
          What is a Profile?
        </a>
        <ul class="list-disc pl-[2rem]">
          <li><a href="http://linked.data.gov.au/def/geochem#_core_profile" target="_blank">Core <i class="pi pi-external-link"></i></a></li>
          <li><a href="http://linked.data.gov.au/def/geochem#_gsq_profile" target="_blank">GSQ <i class="pi pi-external-link"></i></a></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Vocabularies</h3>
        <h3 class="text-base">Profiles</h3>
        <a
            @click="vocabQVisible = true"
            class="italic cursor-pointer"
        >
          What is a Vocabulary?
        </a>
        <ul class="list-disc pl-[2rem]">
          <RouterLink to="/vocabs">Vocabularies Page</RouterLink>
        </ul>
      </article>

    </article>

  </aside>

  <Dialog
      v-model:visible="profileQVisible"
      modal
      header="Profiles"
      :style="{ width: '50rem' }"
      :breakpoints="{ '1199px': '75vw', '575px': '90vw' }"
    >
      <p>
        Profiles of a Specification are constraints on its use. Profiles of this Geochemistry Data Model are designed to guarantee certain forms of use
      </p>
      <p>
        The <strong>Core</strong> Profile mandates certain properties for objects, such as titles for datasets and results for observations.
      </p>
      <p>
        The <strong>GSQ</strong> Profile mandates the use of particular vocabularies for predicates, such as which procedures where used for an Observation.
      </p>
      <p>
        Users of this model can choose to conform to one, more, or no profiles. Use within Queensland must conform to the GSQ Profile.
      </p>
    </Dialog>

  <Dialog
      v-model:visible="vocabQVisible"
      modal
      header="Vocabularies"
      :style="{ width: '50rem' }"
      :breakpoints="{ '1199px': '75vw', '575px': '90vw' }"
    >
      <p>
        Vocabularies are just controlled lists of terms.
      </p>
      <p>
        This model expects multiple vocabularies to be used to supply values for many predicates, such as the procedure used for an Observation.
      </p>
      <p>
        Specific vocabularies are required for use by Profiles of this Model. For example, see the <strong>GSQ Profile's</strong> list of vocabulary use requirements:
      </p>
      <ul>
        <li><a href="https://linked.data.gov.au/def/geochem#_vocabulary_restrictions">GSQ Profile Vocabulary Restrictions</a></li>
      </ul>
    </Dialog>
</template>
