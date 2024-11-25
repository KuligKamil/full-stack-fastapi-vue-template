import { ref } from 'vue'

interface Notification {
  title: string
  subtitle: string
  type: 'success' | 'error'
}
const title = ref('Congratulations!')
const subtitle = ref('')
const isActiveNotification = ref(false)
const type = ref<Notification['type']>('success')
const timer = ref<number | null>(null)

export function useNotification() {
  const showNotification = ((notification: Notification) => {
    title.value = notification.title
    subtitle.value = notification.subtitle
    type.value = notification.type
    isActiveNotification.value = true
    if (timer.value) {
      clearTimeout(timer.value)
    }
    timer.value = setTimeout(() => {
      isActiveNotification.value = false
    }, 5000)
  })

  return { title, subtitle, type, isActiveNotification, showNotification }
}