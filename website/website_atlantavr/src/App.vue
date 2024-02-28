<script setup>
import HelloWorld from './components/HelloWorld.vue'
import TheWelcome from './components/TheWelcome.vue'
</script>

<template>
  <header>
    <div class="barre_top">
      <TheWelcome></TheWelcome>
    </div>
  </header>
  <div>
    <hello-world></hello-world>
  </div>
</template>

<style>
.barre_top {
  z-index: -1;
  position: fixed;
  margin-top: -30px;
  height: 120px;
  width: 110%;
  margin-left: -10px;
  background-color: #304444;
}
</style>
