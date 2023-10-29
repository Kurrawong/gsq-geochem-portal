<script setup lang="ts">
import { ref } from 'vue'

import Sidebar from 'primevue/sidebar'

import Validator from '@/components/Validator.vue'
import Info from '@/components/Info.vue'

const visibleRight = ref(false)
</script>

<template>
  <main>
    <div class="flex">
      <h1 class="text-4xl pb-4">GSQ Geochemistry Data Portal</h1>
      <div class="grow"></div>
      <div class="block lg:hidden place-self-center">
        <button
          icon="pi pi-info-circle"
          @click="visibleRight = true"
          class="border-0 text-white bg-[#225578] hover:bg-[#1c4764] cursor-pointer focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-4 py-3 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
        >
          <i class="pi pi-info-circle align-middle"></i>
        </button>
      </div>
    </div>

    <div class="lg:grid lg:grid-cols-3">
      <article class="lg:col-span-2">
        <section>
          <div class="pt-4 pr-4">
            <div style="display:grid;">
              <div style="grid-column:1; padding:5px;">
                <h3>About</h3>
                <h4>This System</h4>
                <p>This is a one-stop-shop for the <a href="https://linked.data.gov.au/def/abis">(proposed) Geochemistry Data Exchange standard</a> built for the <a href="https://www.business.qld.gov.au/industries/mining-energy-water/resources/geoscience-information/gsq">Geological Survey of Queensland</a>. For more information, contact them!</p>
                <h4>Geochem Standard</h4>
                <p>The Standard is a proposed data exchange standard geochemistry results. It aligns with the <a href="#">OneChecemistry</a> initiative and <a href="">AuScope</a>. More info is linked to on the right.</p>
              </div>
              <div style="grid-column:2; padding:5px;">
                <h3>Validation</h3>
                <p>Validate data according to <em>Profiles</em> of the Standard, using one of the several validators loaded below.</p>
                <h3>Profiles</h3>
                <p><em>Profiles</em> are constrained versions of the Standard and there are several See <em>Documentation</em> to the right.</p>
                <h3>Vocabularies</h3>
                <p>All vocabularies for use with this Standard are linked to on the right.</p>
              </div>
            </div>
          </div>
        </section>
        <section>
          <div class="pt-4 pr-4">
            <Validator />
          </div>
        </section>
      </article>

      <Sidebar v-model:visible="visibleRight" position="right">
        <Info :large="false" />
      </Sidebar>
      <Info large />
    </div>
  </main>
</template>

<style>
.p-sidebar .p-sidebar-header,
.p-sidebar-content {
  @apply bg-[#f8f8fa];
}

.p-sidebar .p-sidebar-content {
  @apply px-0;
}
</style>
