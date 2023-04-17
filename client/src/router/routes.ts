import { RouteRecordRaw } from 'vue-router';

const routes: RouteRecordRaw[] = [
  {
    path: '/',
    component: () => import('layouts/MainLayout.vue'),
    children: [
      { path: '', component: () => import('pages/IndexPage.vue') },
      { path: 'signin', component: () => import('pages/SignInPage.vue') },
      { path: 'user', component: () => import('pages/user/UserIndexPage.vue') },
      { path: 'agent', component: () => import('pages/agent/AgentIndexPage.vue') },
      { path: 'chat/create', component: () => import('pages/chat/ChatCreatePage.vue') },
      { path: 'chat/:id', component: () => import('pages/chat/ChatPage.vue') },
    ],
  },

  // Always leave this as last one,
  // but you can also remove it
  {
    path: '/:catchAll(.*)*',
    component: () => import('pages/ErrorNotFound.vue'),
  },
];

export default routes;
