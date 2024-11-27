<script setup lang="ts">
import { ref, defineProps } from 'vue';
import TypeBadge from './TypeBadge.vue'

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
})


</script>

<template>
  <div class="">
    <table class="min-w-full bg-white">
      <thead>
        <tr>
          <th class="py-2 px-4 border-b text-left" v-for="(header, index) in headers" :key="index">{{ header.label }}
          </th>
        </tr>
      </thead>
      <tbody>
        <tr v-for="(item, index) in items" :key="index" class="hover:bg-gray-100 cursor-pointer">
          <td class="py-2 px-4 border-b" v-for="(field, index2) in fields" :key="index2">
            <template v-if="field == 'tags'" v-for="(tag) of item[field]">
              <TypeBadge :text="tag" class="m-2" />
            </template>
            <template v-else>
              {{ item[field] }}
            </template>


          </td>
        </tr>
      </tbody>
    </table>
  </div>
</template>

