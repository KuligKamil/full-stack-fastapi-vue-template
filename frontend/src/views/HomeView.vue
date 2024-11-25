
<script setup lang="ts">
import { ref } from 'vue';

const data = ref(null)
const error = ref(null)
const count = ref(null)


fetch('http://0.0.0.0:8000/items')
  .then((res) => res.json())
  .then((json) => {
    data.value = json[0]
    count.value = json[1]
  }).catch((err) => (error.value = err))

</script>
<template>
  <div>
    <h1>Home</h1>
    <p>Welcome to the Home page</p>
    <pre>{{ data }}</pre>
  </div>
</template>
 