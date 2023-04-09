import { ref } from 'vue';
import { defineStore } from 'pinia';

export const useUiStore = defineStore('ui', () => {
  const light = ref(false);
  const navDrawerOpen = ref(true);

  function toggleNavDrawer() {
    navDrawerOpen.value = !navDrawerOpen.value;
  }

  return {
    light,
    navDrawerOpen,
    toggleNavDrawer,
  };
});
