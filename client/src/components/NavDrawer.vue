<template>
  <q-drawer v-model="navDrawerOpen" class="drawer" side="left">
    <q-list
      style="float: left; border-right: 1px solid rgb(46, 46, 46); height: 100%"
    >
      <q-item to="/" :exact="true" v-ripple>
        <q-item-section>
          <q-icon name="o_home" size="xs" />
        </q-item-section>
      </q-item>

      <q-item to="/agent" v-ripple>
        <q-item-section>
          <q-icon name="o_smart_toy" size="xs" />
        </q-item-section>
      </q-item>

      <q-item to="/cores" v-ripple>
        <q-item-section>
          <q-icon name="o_hub" size="xs" />
        </q-item-section>
      </q-item>

    </q-list>

    <div class="navbox" id="layout-navbox"></div>
  </q-drawer>
</template>

<script setup lang="ts">
import { storeToRefs } from 'pinia';
import { useUiStore } from '../stores/ui';

const { navDrawerOpen } = storeToRefs(useUiStore());
</script>

<style lang="scss">
.navbox {
  white-space: nowrap;
  overflow: hidden;
  height: 100%;
  //background-color: #222222;
  font-size: 0.8125rem;
  font-weight: 600;
}
</style>
