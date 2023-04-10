<script setup lang="ts">
import { useQuery } from '@urql/vue'
import { computed } from 'vue'

import UserItem from 'components/user/UserItem.vue'
import { graphql } from '../../gql'

const { data } = useQuery({
  query: graphql(/* GraphQL */ `
    query allUsers($first: Int!) {
      allUsers(first: $first) {
        edges {
          node {
            ...UserItem
          }
        }
      }
    }
  `),
  // variables are typed!
  variables: { first: 10 }
})

const users = computed(() => data.value?.allUsers?.edges?.map(e => e?.node))
</script>

<template>
  <ul>
    <q-list v-for="user of users" :key="(user.id as string)"><UserItem :user="user" /></q-list>
  </ul>
</template>
