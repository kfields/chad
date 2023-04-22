import { ref, computed } from 'vue';

import { useMutation } from '@urql/vue';
import { defineStore } from 'pinia';
import jwtDecode from 'jwt-decode'

import { graphql } from '../gql';

export const useUserStore = defineStore('user', () => {
  //let user = $ref<User | null | undefined>();
  //const user = computed(() => supabase.auth.user());
  //let user = $ref<User | null | undefined>(supabase.auth.user());
  //const isSignedIn = computed(() => user != null);

  const authToken = ref('')
  const authStatus = ref('')
  const authPayload = ref({})

  const signInResult = useMutation(
    graphql(`
      mutation signIn($input: SignInInput!) {
        signIn(input: $input) {
          token
        }
      }
    `)
  );

  async function signIn(email: string, password: string) {
    console.log('signIn');
    const input = { email, password };
    const variables = { input };
    signInResult.executeMutation(variables).then((result) => {
      console.log(result);

      const token = result.data?.signIn.token as string
      authToken.value = token
      localStorage.setItem('authToken', token)
      console.log('authToken', authToken.value)

      const payload = jwtDecode(token) as object
      authPayload.value = payload
      //state.user = user
      //localStorage.setItem('user', user)
      console.log('authPayload', authPayload.value)

      //state.identity = Identity.create(user.role)

      authStatus.value = 'success'
    });
  }

  async function signOut() {
    console.log('signOut');
  }

  return {
    authToken,
    //user,
    //isSignedIn,
    signIn,
    signOut,
  };
});
