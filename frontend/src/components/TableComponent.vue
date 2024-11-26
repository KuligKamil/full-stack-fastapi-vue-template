<script setup lang="ts">
import { ref, defineProps } from 'vue';


defineProps({
  headers: {
    type: Array,
    required: true,
  },
  items: {
    type: Array,
    required: true,
  },
  fields: {
    type: Array,
    required: true,
  },
});
// const props = defineProps<{
//   // type: [],
//   required: true
// }>();

</script>

<template>
  <div class="">
    <table class="min-w-full bg-white">
      <thead>
        <tr>
          <th class="py-2 px-4 border-b" v-for="(header, index) in headers" :key="index">{{ header }}</th>

        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index">
          <td class="py-2 px-4 border-b" v-for="(field, index2) in fields" :key="index">{{ item[field] }}</td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

