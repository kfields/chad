<template>
  <q-item clickable v-ripple>
    <q-item-section>
      <router-link class="text-h6" :to="`/users/${user?.id}`">{{
        name
      }}</router-link>
    </q-item-section>
  </q-item>
</template>

<script setup lang="ts">
import { graphql, FragmentType, useFragment } from '../../gql'

const UserItemFragment = graphql(/* GraphQL */ `
  fragment UserItem on User {
    id
    username
  }
`)

const props = defineProps<{
    user: FragmentType<typeof UserItemFragment>
}>();

const user = useFragment(UserItemFragment, props.user)
const name = user.username;
</script>
