<template>
  <q-item clickable v-ripple>
    <q-item-section>
      <router-link class="text-h6" :to="`/agents/${agent?.id}`">{{
        name
      }}</router-link>
    </q-item-section>
  </q-item>
</template>

<script setup lang="ts">
import { graphql, FragmentType, useFragment } from '../../gql'

const AgentItemFragment = graphql(/* GraphQL */ `
  fragment AgentItem on Agent {
    id
    name
  }
`)

const props = defineProps<{
    agent: FragmentType<typeof AgentItemFragment>
}>();

const agent = useFragment(AgentItemFragment, props.agent)
const name = agent.name;
</script>
