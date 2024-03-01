<script setup lang="ts">

import Button from "primevue/button";
import {type Ref, ref} from "vue";
import {useToast} from "primevue/usetoast";
import type {ValidationReport} from "@/types";
import ValidationResults from "@/components/ValidationResults.vue";

const uploadFile = ref()
const fileSelected = ref(false)
const fileInput: Ref<HTMLInputElement | null> = ref(null)
const isConverting = ref(false)
const toast = useToast()
const report = ref<ValidationReport | null>(null)

const handleFileInput = async (event: Event) => {
  const target = event.target as HTMLInputElement
  const files = target.files
  if (files && files.length > 0) {
    uploadFile.value = files[0]
    fileSelected.value = true
  } else {
    uploadFile.value = ''
    fileSelected.value = false
  }
}

const handleFileInputClearClick = () => {
  uploadFile.value = ''
  if (fileInput.value) {
    fileInput.value.value = ''
  }

  fileSelected.value = false
}

const handleConvertButtonClick = async () => {
  isConverting.value = true
  report.value = null

  try {
    const formData = new FormData();
    formData.append("file", uploadFile.value)
    const response = await fetch('/api/v1/convert', {
      method: 'POST',
      body: formData,
    })

    if (response.status == 200) {
      report.value = await response.json()
    } else {
      const data = await response.json()
      console.log(data.detail)
      throw new Error(
        `Request to the server failed with status ${response.status}. Message: ${data['detail']}`
      )
    }
  } catch (err) {
    toast.add({ severity: 'error', summary: 'Error', detail: err })
  }
  isConverting.value = false
}
</script>

<template>
  <h1 class="text-4xl">Data Submission</h1>

  <h2 class="text-2xl">Excel Data Submission</h2>
  <p>Geochemistry data submitted here must use the GeochemXL templates.</p>
  <p>The GeochemXL templates are available at <a href="https://github.com/Kurrawong/geochemxl/tree/main/templates" target="_blank">github.com/Kurrawong/geochemxl/templates</a>.</p>
  <input
      ref="fileInput"
      type="file"
      accept=".ttl,.xlsx,.json"
      @change="handleFileInput"
  />
  <button v-if="fileSelected" @click="handleFileInputClearClick">
    <i class="pi pi-times"></i>
  </button>

  <div class="pt-4">
    <Button
      type="button"
      :disabled="!uploadFile"
      :loading="isConverting"
      label="Convert"
      icon="pi pi-wrench"
      @click="handleConvertButtonClick"
      class="text-white bg-blue-700 hover:bg-blue-800 focus:ring-4 focus:ring-blue-300 font-medium rounded-lg text-sm px-5 py-2.5 mr-2 mb-2 dark:bg-blue-600 dark:hover:bg-blue-700 focus:outline-none dark:focus:ring-blue-800"
    >
    </Button>
  </div>

  <div v-if="report" class="pt-8">
    <hr />
    <ValidationResults v-if="report" title="Conversion Results" :report="report" />
  </div>
</template>

<style scoped>

</style>