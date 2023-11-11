<template>
  <v-container>
    <v-row align="center" justify="center">
      <v-col cols="8">
        <v-form @submit.prevent="onSubmit">
          <v-card-title>Crossposter app</v-card-title>
          <v-textarea v-model="text" label="Text" required></v-textarea>
          <span>Character count: {{ charactersCount }}</span>
          <v-file-input v-model="files" label="File input" multiple></v-file-input>
          <v-row>
            <v-col v-for="(url, index) in fileURLs" :key="index">
              <v-img :src="url" height="200px"></v-img>
            </v-col>
          </v-row>
          <v-checkbox v-model="hashtagCheckbox" label="Add hashtags?"></v-checkbox>
          <v-text-field v-model="hashtags" label="Hashtags"></v-text-field>
          <div v-for="(checkbox, index) in checkboxes">
            <v-checkbox :label="checkbox.label" :key="index" v-model="checkbox.model"></v-checkbox>
          </div>
          <v-checkbox v-model="scheduleTimeCheckbox" label="Schedule time?"></v-checkbox>
          <div v-if="scheduleTimeCheckbox">
            <input type="datetime-local" label="Select Datetime" v-model="scheduleTime"><br>
            <br>
          </div>
          <v-btn type="submit">Submit</v-btn>
        </v-form>
      </v-col>
    </v-row>
  </v-container>
</template>


<script setup lang="ts">
import { ref, computed } from 'vue'
import axios from 'axios';


const text = ref('')
const files = ref([])
const hashtagCheckbox = ref(true)
const hashtags = ref('')

const scheduleTimeCheckbox = ref(true)
const tomorrow = new Date()
tomorrow.setDate(tomorrow.getDate() + 1)
const scheduleTime = ref(tomorrow)


const checkboxes = ref([
  { model: ref(false), label: 'Bluesky' },
  { model: ref(false), label: 'Mastodon' },
  { model: ref(false), label: 'Posthaven' },
  { model: ref(false), label: 'Instagram' },
  { model: ref(false), label: 'Twitter' },
  { model: ref(false), label: 'Facebook' },
])

const fileURLs = computed(() => files.value.map(file => URL.createObjectURL(file)))
const charactersCount = computed(() => text.value.length + (hashtagCheckbox.value ? hashtags.value.length : 0))

const onSubmit = async () => {
  const formData = new FormData();
  formData.append('text', text.value);
  formData.append('hashtagCheckbox', hashtagCheckbox.value.toString());
  formData.append('hashtags', hashtags.value);
  checkboxes.value.forEach((checkbox, index) => {
    formData.append(`checkbox_${index}`, checkbox.model.toString());
  });
  files.value.forEach((file, index) => {
    formData.append(`file_${index}`, file);
  });
  formData.append('scheduleTime', scheduleTime?.value.toString());

  try {
    const response = await axios.post('http://localhost:5000/submit', formData);
    console.log(response.data);
  } catch (error) {
    console.error(error);
  }
}

</script>
