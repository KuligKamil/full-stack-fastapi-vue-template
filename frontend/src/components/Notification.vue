<script setup lang="ts">
import { useNotification } from '../composables/useNotification'
const { title, subtitle, type, isActiveNotification } = useNotification()
</script>
<template>
  <Transition name="bounce">
    <div id="notification" v-if="isActiveNotification" class="fixed right-0 left-0 bottom-4 m-auto px-4 py-3 bg-lime-200 text-black 
      rounded-lg shadow-lg w-full max-w-xs text-center z-50">
      <p class="font-bold text-xl">{{ title }}</p>
      <p class="font-medium">{{ subtitle }}</p>
      <button @click="isActiveNotification = false"
        class="absolute top-0 right-0 mt-1 mr-4 text-black text-2xl hover:text-gray-200">&times;</button>
    </div>
  </Transition>
</template>
<style>
.bounce-enter-active {
  animation: bounce-in 0.5s;
}

.bounce-leave-active {
  animation: bounce-in 0.5s reverse;
}

@keyframes bounce-in {
  0% {
    transform: scale(0);
  }

  50% {
    transform: scale(1.25);
  }

  100% {
    transform: scale(1);
  }
}
</style>