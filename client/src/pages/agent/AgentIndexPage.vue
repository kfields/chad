<script setup lang="ts">
import { useQuery } from '@urql/vue'
import { computed } from 'vue'

import AgentItem from 'components/agent/AgentItem.vue'
import { graphql } from '../../gql'

const { data } = useQuery({
  query: graphql(/* GraphQL */ `
    query allAgents($first: Int!) {
      allAgents(first: $first) {
        edges {
          node {
            ...AgentItem
          }
        }
      }
    }
  `),
  // variables are typed!
  variables: { first: 10 }
})

const agents = computed(() => data.value?.allAgents?.edges?.map(e => e?.node))
</script>

<template>
  <ul>
    <q-list v-for="agent of agents" :key="(agent.id as string)"><AgentItem :agent="agent" /></q-list>
  </ul>
</template>
