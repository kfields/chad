<template>
  <q-page padding>
    <h1>Create Chat</h1>
    <q-select
      filled
      bottom-slots
      v-model="model"
      :options="bots"
      option-label="name"
      option-value="id"
      label="Bot"
      counter
      maxlength="12"
    >
      <template v-slot:before>
        <q-avatar>
          <img src="https://cdn.quasar.dev/img/avatar5.jpg" />
        </q-avatar>
      </template>

      <template v-slot:after>
        <q-btn round dense flat icon="send" @click="createChat"/>
      </template>
    </q-select>
  </q-page>
</template>

<script setup lang="ts">
import { ref, computed, watch } from 'vue';
import { useRouter } from 'vue-router';
import { useQuery, useMutation } from '@urql/vue';
import { graphql } from '../../gql';

const router = useRouter();

const model = ref<Bot | null>(null);

const { data } = useQuery({
  query: graphql(`
    query myBots($first: Int!) {
      myBots(first: $first) {
        edges {
          node {
            id
            name
          }
        }
      }
    }
  `),
  // variables are typed!
  variables: { first: 10 },
});

const bots = computed(() => data.value?.myBots?.edges?.map((e) => e?.node));

watch(
  bots,
  (newResult) => {
    if (newResult && newResult.length > 0) {
      model.value = newResult[0];
    }
  },
  { immediate: true }
);

const createChatResult = useMutation(
  graphql(`
    mutation createChat($input: CreateChatInput!) {
      createChat(input: $input) {
        id
      }
    }
  `)
);

const createChat = async function () {
  console.log('create chat');
  const input = { to: model.value.id };
  const variables = { input };

  console.log(variables);
  createChatResult.executeMutation(variables).then((result) => {
    console.log(result);
    let id = result.data?.createChat.id
    router.replace(`/chat/${id}`)
  });
};

</script>
