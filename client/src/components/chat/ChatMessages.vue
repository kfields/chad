<script setup lang="ts">
import { useQuery } from '@urql/vue'
import { ref, computed } from 'vue'

import MessageCard from '../message/MessageCard.vue'
import { graphql } from '../../gql'
import { Chat } from '../../gql/graphql'

const props = defineProps<{
  chat: Chat
}>();

const chatId = ref(props.chat.id)

const { data } = await useQuery({
  query: graphql(`
    query chatMessages($chatId: ID!) {
      chatMessages(chatId: $chatId) {
        edges {
          node {
            ...MessageItem
          }
        }
      }
    }
  `),
  // variables are typed!
  variables: { chatId: chatId.value }
})

const chatMessages = computed(() => data.value?.chatMessages?.edges?.map(e => e?.node))
</script>

<template>
  <q-list v-for="message of chatMessages" :key="(message.id as string)"><MessageCard :message="message" /></q-list>
</template>
