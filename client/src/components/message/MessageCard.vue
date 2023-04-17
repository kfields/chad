<template>
  <q-card>
    <q-card-section>
    {{ from_name }}
    </q-card-section>
    <q-card-section>
      {{ content }}
    </q-card-section>
  </q-card>
</template>

<script setup lang="ts">
import { graphql, FragmentType, useFragment } from '../../gql'

const MessageItemFragment = graphql(`
  fragment MessageItem on Message {
    id
    from { id name }
    content
  }
`)

const props = defineProps<{
    message: FragmentType<typeof MessageItemFragment>
}>();

const message = useFragment(MessageItemFragment, props.message)
const content = message.content;
const from_name = message.from.name;
</script>
