<script setup lang="ts">
defineProps<{
  text: string
}>()
</script>
<template>
  <div class="border-solid border-2 border-black py-1/2 px-1 rounded-full text-xs font-bold text-cente">
    {{ text }}
  </div>
</template>