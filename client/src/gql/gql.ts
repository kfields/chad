/* eslint-disable */
import * as types from './graphql';
import type { TypedDocumentNode as DocumentNode } from '@graphql-typed-document-node/core';

/**
 * Map of all GraphQL operations in the project.
 *
 * This map has several performance disadvantages:
 * 1. It is not tree-shakeable, so it will include all operations in the project.
 * 2. It is not minifiable, so the string of a GraphQL query will be multiple times inside the bundle.
 * 3. It does not support dead code elimination, so it will add unused operations.
 *
 * Therefore it is highly recommended to use the babel or swc plugin for production.
 */
const documents = {
    "\n  fragment ChatItem on Chat {\n    id\n    name\n  }\n": types.ChatItemFragmentDoc,
    "\n    query myChats($first: Int!) {\n      myChats(first: $first) {\n        edges {\n          node {\n            ...ChatItem\n          }\n        }\n      }\n    }\n  ": types.MyChatsDocument,
    "\n    query chatMessages($chatId: ID!) {\n      chatMessages(chatId: $chatId) {\n        edges {\n          node {\n            ...MessageItem\n          }\n        }\n      }\n    }\n  ": types.ChatMessagesDocument,
    "\n  fragment MessageItem on Message {\n    id\n    content\n  }\n": types.MessageItemFragmentDoc,
    "\n  fragment UserItem on User {\n    id\n    username\n  }\n": types.UserItemFragmentDoc,
    "\n    query myBots($first: Int!) {\n      myBots(first: $first) {\n        edges {\n          node {\n            id\n            name\n          }\n        }\n      }\n    }\n  ": types.MyBotsDocument,
    "\n    mutation createChat($input: CreateChatInput!) {\n      createChat(input: $input) {\n        id\n      }\n    }\n  ": types.CreateChatDocument,
    "\n    query chat($id: ID!) {\n      chat(id: $id) {\n        id\n      }\n    }\n  ": types.ChatDocument,
    "\n    mutation sendChatMessage($input: SendChatMessageInput!) {\n      sendChatMessage(input: $input) {\n        id\n        content\n      }\n    }\n  ": types.SendChatMessageDocument,
    "\n    query chatQuery($id: ID!) {\n      chat(id: $id) {\n        id\n        name\n      }\n    }\n  ": types.ChatQueryDocument,
    "\n    query allUsers($first: Int!) {\n      allUsers(first: $first) {\n        edges {\n          node {\n            ...UserItem\n          }\n        }\n      }\n    }\n  ": types.AllUsersDocument,
    "\n      mutation signIn($input: SignInInput!) {\n        signIn(input: $input) {\n          token\n        }\n      }\n    ": types.SignInDocument,
};

/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 *
 *
 * @example
 * ```ts
 * const query = graphql(`query GetUser($id: ID!) { user(id: $id) { name } }`);
 * ```
 *
 * The query argument is unknown!
 * Please regenerate the types.
 */
export function graphql(source: string): unknown;

/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment ChatItem on Chat {\n    id\n    name\n  }\n"): (typeof documents)["\n  fragment ChatItem on Chat {\n    id\n    name\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    query myChats($first: Int!) {\n      myChats(first: $first) {\n        edges {\n          node {\n            ...ChatItem\n          }\n        }\n      }\n    }\n  "): (typeof documents)["\n    query myChats($first: Int!) {\n      myChats(first: $first) {\n        edges {\n          node {\n            ...ChatItem\n          }\n        }\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    query chatMessages($chatId: ID!) {\n      chatMessages(chatId: $chatId) {\n        edges {\n          node {\n            ...MessageItem\n          }\n        }\n      }\n    }\n  "): (typeof documents)["\n    query chatMessages($chatId: ID!) {\n      chatMessages(chatId: $chatId) {\n        edges {\n          node {\n            ...MessageItem\n          }\n        }\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment MessageItem on Message {\n    id\n    content\n  }\n"): (typeof documents)["\n  fragment MessageItem on Message {\n    id\n    content\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n  fragment UserItem on User {\n    id\n    username\n  }\n"): (typeof documents)["\n  fragment UserItem on User {\n    id\n    username\n  }\n"];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    query myBots($first: Int!) {\n      myBots(first: $first) {\n        edges {\n          node {\n            id\n            name\n          }\n        }\n      }\n    }\n  "): (typeof documents)["\n    query myBots($first: Int!) {\n      myBots(first: $first) {\n        edges {\n          node {\n            id\n            name\n          }\n        }\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    mutation createChat($input: CreateChatInput!) {\n      createChat(input: $input) {\n        id\n      }\n    }\n  "): (typeof documents)["\n    mutation createChat($input: CreateChatInput!) {\n      createChat(input: $input) {\n        id\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    query chat($id: ID!) {\n      chat(id: $id) {\n        id\n      }\n    }\n  "): (typeof documents)["\n    query chat($id: ID!) {\n      chat(id: $id) {\n        id\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    mutation sendChatMessage($input: SendChatMessageInput!) {\n      sendChatMessage(input: $input) {\n        id\n        content\n      }\n    }\n  "): (typeof documents)["\n    mutation sendChatMessage($input: SendChatMessageInput!) {\n      sendChatMessage(input: $input) {\n        id\n        content\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    query chatQuery($id: ID!) {\n      chat(id: $id) {\n        id\n        name\n      }\n    }\n  "): (typeof documents)["\n    query chatQuery($id: ID!) {\n      chat(id: $id) {\n        id\n        name\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n    query allUsers($first: Int!) {\n      allUsers(first: $first) {\n        edges {\n          node {\n            ...UserItem\n          }\n        }\n      }\n    }\n  "): (typeof documents)["\n    query allUsers($first: Int!) {\n      allUsers(first: $first) {\n        edges {\n          node {\n            ...UserItem\n          }\n        }\n      }\n    }\n  "];
/**
 * The graphql function is used to parse GraphQL queries into a document that can be used by GraphQL clients.
 */
export function graphql(source: "\n      mutation signIn($input: SignInInput!) {\n        signIn(input: $input) {\n          token\n        }\n      }\n    "): (typeof documents)["\n      mutation signIn($input: SignInInput!) {\n        signIn(input: $input) {\n          token\n        }\n      }\n    "];

export function graphql(source: string) {
  return (documents as any)[source] ?? {};
}

export type DocumentType<TDocumentNode extends DocumentNode<any, any>> = TDocumentNode extends DocumentNode<  infer TType,  any>  ? TType  : never;