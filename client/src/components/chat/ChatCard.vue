<template>
  <q-item clickable v-ripple>
    <q-item-section>
      <router-link class="text-h6" :to="`/chat/${chat?.id}`">{{
        title
      }}</router-link>
    </q-item-section>
  </q-item>
</template>

<script setup lang="ts">
import { graphql, FragmentType, useFragment } from '../../gql'

const ChatItemFragment = graphql(/* GraphQL */ `
  fragment ChatItem on Chat {
    id
    title
  }
`)

const props = defineProps<{
    chat: FragmentType<typeof ChatItemFragment>
}>();

const chat = useFragment(ChatItemFragment, props.chat)
const title = chat.title;
</script>
