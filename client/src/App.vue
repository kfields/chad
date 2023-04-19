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
  subscriptionExchange,
} from '@urql/vue';
import { cacheExchange } from '@urql/exchange-graphcache';
import { authExchange } from '@urql/exchange-auth';
import { SubscriptionClient } from 'subscriptions-transport-ws';

async function initializeAuthState() {
  const token = localStorage.getItem('authToken');
  const refreshToken = localStorage.getItem('refreshToken');
  return { token, refreshToken };
}

const subscriptionClient = new SubscriptionClient('ws://localhost:8000/graphql/', {
  reconnect: true,
});

const client = createClient({
  url: process.env.GRAPHQL_ENDPOINT ? process.env.GRAPHQL_ENDPOINT : '',
  exchanges: [
    //TODO: This is messing with subscriptions.  Fix it later ...
    /*cacheExchange({
    }),*/
    authExchange(async (utils) => {
      let { token, refreshToken } = await initializeAuthState();
      return {
        addAuthToOperation(operation) {
          if (!token) return operation;
          //console.log('authToken', token)
          return utils.appendHeaders(operation, {
            Authorization: `Bearer ${token}`,
          });
        },
        didAuthError(error, _operation) {
          return error.graphQLErrors.some(
            (e) => e.extensions?.code === 'FORBIDDEN'
          );
        },
        async refreshAuth() {
          //logout();
          console.log('refreshAuth');
        },
      };
    }),
    fetchExchange,
    subscriptionExchange({
      forwardSubscription: (request) => subscriptionClient.request(request),
    }),
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
