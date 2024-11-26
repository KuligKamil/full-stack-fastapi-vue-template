
<script setup lang="ts">
import { ref } from 'vue';
import TableComponent from '../components/TableComponent.vue';
const headers = ref(['Header 1', 'Header 2', 'Header 3'])
const data = ref([
  { field1: 'Value 1', field2: 'Value 2', field3: 'Value 3' },
  { field1: 'Value 4', field2: 'Value 5', field3: 'Value 6' },
  { field1: 'Value 7', field2: 'Value 8', field3: 'Value 9' },
])


// how to do filters
const fields = ref(['field1', 'field2', 'field3'])
const error = ref(null)
const count = ref(null)

// fetch('http://0.0.0.0:8000/items')
//   .then((res) => res.json())
//   .then((json) => {
//     data.value = json[0]
//     count.value = json[1]
//   }).catch((err) => (error.value = err))

</script>
<template>
  <div>
    <TableComponent :headers="headers" :items="data" :fields="fields" />
    <h1>Home</h1>
    <p>Welcome to the Home page</p>
    <pre>{{ data }}</pre>

  </div>
</template>
 