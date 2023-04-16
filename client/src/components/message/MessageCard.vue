<template>
  <q-item clickable v-ripple>
    <q-item-section>
      {{ content }}
    </q-item-section>
  </q-item>
</template>

<script setup lang="ts">
import { graphql, FragmentType, useFragment } from '../../gql'

const MessageItemFragment = graphql(`
  fragment MessageItem on Message {
    id
    content
  }
`)

const props = defineProps<{
    message: FragmentType<typeof MessageItemFragment>
}>();

const message = useFragment(MessageItemFragment, props.message)
const content = message.content;
</script>
