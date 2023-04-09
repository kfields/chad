<template>
  <router-view />
</template>

<script setup lang="ts">
import { onMounted, watch } from 'vue';
import { useQuasar } from 'quasar';
import { storeToRefs } from 'pinia';
import { useUiStore } from 'stores/ui';

import {
  createClient,
  provideClient,
  fetchExchange,
} from '@urql/vue';

import { cacheExchange } from '@urql/exchange-graphcache';

const client = createClient({
  url: process.env.GRAPHQL_ENDPOINT ? process.env.GRAPHQL_ENDPOINT : '',
  exchanges: [
    cacheExchange({
      keys: {
        LaunchLinks: () => null,
      },
    }),
    fetchExchange,
  ],
  requestPolicy: 'cache-and-network',
});

provideClient(client);

const $q = useQuasar();

const { light } = storeToRefs(useUiStore());
watch(light, (value) => {
  $q.dark.set(!value);
});

onMounted(() => {
  $q.dark.set(true);
});
</script>
