<script setup lang="ts">
import { useQuery } from '@urql/vue'
import { computed } from 'vue'

import ChatCard from './ChatCard.vue'
import { graphql } from '../../gql'

const { data } = useQuery({
  query: graphql(/* GraphQL */ `
    query myChats($first: Int!) {
      myChats(first: $first) {
        edges {
          node {
            ...ChatItem
          }
        }
      }
    }
  `),
  // variables are typed!
  variables: { first: 10 }
})

const chats = computed(() => data.value?.myChats?.edges?.map(e => e?.node))
</script>

<template>
  <ul>
    <q-list v-for="chat of chats" :key="(chat.id as string)"><ChatCard :chat="chat" /></q-list>
  </ul>
  <q-page-sticky position="bottom-right" :offset="[18, 18]">
    <q-btn fab color="primary" icon="add" to="/chat/create" />
  </q-page-sticky>

</template>
