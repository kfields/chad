<script setup lang="ts">
import { useQuery, useSubscription } from '@urql/vue';
import { ref, computed, watch } from 'vue';

import MessageCard from '../message/MessageCard.vue';
import { graphql } from '../../gql';
import { Chat, Message, MessageItemFragment, ChatMessageEvent, ChatEventSubscription } from '../../gql/graphql';

const props = defineProps<{
  chat: Chat;
}>();

const chatId = ref(props.chat.id);

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
  variables: { chatId: chatId.value },
});

const chatMessages = ref<MessageItemFragment[]>([]);

const messages = computed(() =>
  data.value?.chatMessages?.edges?.map((e) => e?.node) as MessageItemFragment[]
);

watch(
  messages,
  (newResult: MessageItemFragment[]) => {
    chatMessages.value = newResult;
  },
  { immediate: true }
);

const handleSubscription = (messages = [], response: ChatEventSubscription) => {
  console.log(messages)
  console.log(response)
  const event = response.chat
  switch (event?.__typename) {
    case 'ChatMessageEvent':
      console.log('ChatMessageEvent')
      const message = (event as ChatMessageEvent).message
      console.log(message)
      chatMessages.value.push(message)
  }
  return [response, ...messages];
};

const result = useSubscription(
  {
    query: graphql(`
      subscription chatEvent($id: ID!) {
        chat(id: $id) {
          __typename
          id
          timestamp
          ... on ChatMessageEvent {
            message {
              ...MessageItem
            }
          }
        }
      }
    `),
    variables: { id: chatId.value },
  },
  handleSubscription
);
</script>

<template>
  <div class="card-column">
    <MessageCard
      v-for="message of chatMessages"
      :key="(message.id as string)"
      :message="message"
    />
  </div>
</template>
