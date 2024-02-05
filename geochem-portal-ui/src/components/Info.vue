<script setup lang="ts">
import Button from 'primevue/button'
import Dialog from 'primevue/dialog'

import { ref } from 'vue';

const standardQVisible = ref(false);
const profileQVisible = ref(false);
const vocabQVisible = ref(false);

const props = defineProps<{ large: boolean }>()
</script>

<template>
  <aside class="lg:col-span-1" :class="{ 'lg:block hidden': props.large }">
    <article class="bg-[#f8f8fa] p-5">
      <h2 class="text-xl">Quick Links</h2>

      <article>
        <h3 class="text-base">Geochemistry Standard</h3>
        <a
            @click="standardQVisible = true"
            class="italic cursor-pointer"
        >
          What is this Standard for?
        </a>
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
          <li>
            <a href="http://linked.data.gov.au/def/geochem#_core_profile" target="_blank">Core Profile <i class="pi pi-external-link"></i></a>
            <ul>
              <li><a href="https://raw.githubusercontent.com/Kurrawong/gsq-geochem/main/profiles/core/validator.ttl" target="_blank">Core Validator <i class="pi pi-external-link"></i></a></li>
              <li><a href="https://raw.githubusercontent.com/Kurrawong/gsq-geochem/main/profiles/core/validator-combined.ttl" target="_blank">Core Validator - with data expansion <i class="pi pi-external-link"></i></a></li>
            </ul>
          </li>
          <li>
            <a href="http://linked.data.gov.au/def/geochem#_gsq_profile" target="_blank">GSQ Profile <i class="pi pi-external-link"></i></a>
            <ul>
              <li><a href="https://github.com/Kurrawong/gsq-geochem/raw/main/profiles/gsq/templates/GeochemXL-v3.0.xlsx" target="_blank">GeochemXL Template v3.0 <i class="pi pi-external-link"></i></a></li>
              <li><a href="https://raw.githubusercontent.com/Kurrawong/gsq-geochem/main/profiles/gsq/validator.ttl" target="_blank">GSQ Validator <i class="pi pi-external-link"></i></a></li>
              <li><a href="https://raw.githubusercontent.com/Kurrawong/gsq-geochem/main/profiles/gsq/validator-compounded.ttl" target="_blank">GSQ Validator - with data expansion <i class="pi pi-external-link"></i></a></li>
            </ul>
          </li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Vocabularies</h3>
        <a
            @click="vocabQVisible = true"
            class="italic cursor-pointer"
        >
          What is a Vocabulary?
        </a>
        <ul class="list-disc pl-[2rem]">
          <li><RouterLink to="/vocabs">GSQ Profile Vocabularies</RouterLink></li>
        </ul>
      </article>

      <article>
        <h3 class="text-base">Validation</h3>
        <p>Validate input text or files to the left</p>
      </article>

      <article>
        <h3 class="text-base">This System</h3>
        <ul class="list-disc pl-[2rem]">
          <li><RouterLink to="/system">More about this Portal system</RouterLink></li>
        </ul>
      </article>

    </article>

  </aside>

  <Dialog
      v-model:visible="standardQVisible"
      modal
      header="This Standard"
      :style="{ width: '50rem' }"
      :breakpoints="{ '1199px': '75vw', '575px': '90vw' }"
    >
      <p>
        This Standard is for geochemistry data exchange. It has been created to assist industry submitting data to multiple governments in Australia and to assist government with receiving data from multiple companies.
      </p>
      <p>
        It can, of course, be used to exchange data between companies or governments also.
      </p>
      <p>
        This standard aligns with international geochemistry data initiatives, such as <a href="https://onegeochemistry.github.io/">OneGeochemistry</a>, so it can be used in that context too.
      </p>
    </Dialog>

  <Dialog
      v-model:visible="profileQVisible"
      modal
      header="Profiles"
      :style="{ width: '50rem' }"
      :breakpoints="{ '1199px': '75vw', '575px': '90vw' }"
    >
      <p>
        Profiles of a Standard are constraints on its use. Profiles of this Geochemistry Standard are designed to guarantee certain forms of use.
      </p>
      <p>
        The <strong>Core</strong> Profile mandates certain properties for objects, such as a title for a Datasets and results for Observation events.
      </p>
      <p>
        The <strong>GSQ</strong> Profile mandates the use of particular vocabularies for certain values, such as which procedures are used for an Observation.
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
        This model expects vocabulary terms to be used at many placed in the Standard, such as for the procedure used for an Observation.
      </p>
      <p>
        Specific vocabularies are required for use by Profiles of this Model. For examples, see the <strong>GSQ Profile's</strong> list of vocabulary use requirements:
      </p>
      <ul>
        <li><a href="https://linked.data.gov.au/def/geochem#_vocabulary_restrictions">GSQ Profile Vocabulary Restrictions</a></li>
      </ul>
    </Dialog>
</template>
