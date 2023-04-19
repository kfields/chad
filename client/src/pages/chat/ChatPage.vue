<template>
  <div class="chat-container q-pa-md">
    <ChatMessages v-if="chat" :chat="chat" />
    <div style="height: 128px;" />
    <div class="input-container">
      <q-input
        bottom-slots
        v-model="text"
        label="Send a message ..."
        @keydown.enter.prevent="sendMessage"
      >
        <template v-slot:before>
          <q-avatar>
            <img src="https://cdn.quasar.dev/img/avatar5.jpg" />
          </q-avatar>
        </template>

        <template v-slot:after>
          <q-btn round dense flat icon="send" @click="sendMessage" />
        </template>
      </q-input>
    </div>
  </div>
</template>

<style scoped>
.chat-container {
  height: 100%;
  display: flex;
  flex-direction: column;
}

.input-container {
  position: fixed;
  bottom: 0;
  width: 70%;
  padding: 10px;
  background-color: black;
}
</style>

<script setup lang="ts">
import { ref, computed, watch } from 'vue';
import { useRoute } from 'vue-router';
//import { useRouter } from 'vue-router';
import { useQuery, useMutation } from '@urql/vue';
import { graphql } from '../../gql';

import ChatMessages from 'components/chat/ChatMessages.vue'

const route = useRoute();

const id = route.params.id as string;
console.log('id: ', id)
const { data } = await useQuery({
  query: graphql(/* GraphQL */ `
    query chatQuery($id: ID!) {
      chat(id: $id) {
        id
        name
      }
    }
  `),
  // variables are typed!
  variables: { id },
});

const chat = ref(data.value?.chat)
const chat_id = data.value?.chat.id;
const text = ref('');

/*const sendMessage = function () {
  console.log('send message');
};*/

const sendChatMessageResult = useMutation(
  graphql(`
    mutation sendChatMessage($input: SendChatMessageInput!) {
      sendChatMessage(input: $input) {
        id
        content
      }
    }
  `)
);

const sendMessage = async function () {
  console.log('send chat message');
  const input = { id: chat_id as string, content: text.value };
  const variables = { input };

  console.log(variables);
  sendChatMessageResult.executeMutation(variables).then((result) => {
    console.log(result);
    //let message = result.data?.sendChatMessage.message
    let message = result.data?.sendChatMessage
    console.log(message);
    text.value = '';
  });
};

</script>
