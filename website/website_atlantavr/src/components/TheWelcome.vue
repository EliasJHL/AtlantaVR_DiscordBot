<script setup>
import WelcomeItem from './WelcomeItem.vue'
import DocumentationIcon from './icons/IconDocumentation.vue'
import ToolingIcon from './icons/IconTooling.vue'
import EcosystemIcon from './icons/IconEcosystem.vue'
import CommunityIcon from './icons/IconCommunity.vue'
import SupportIcon from './icons/IconSupport.vue'
</script>

<template>
  <div id="form_text_barre">
    <div class="name">
      <h1>AtlantaVR_Bot</h1>
      <div class="connecte">
        <button></button>
      </div>
    </div>
    <div class="action">
      <h2>Liste</h2>
      <h3>Ajouter</h3>
      <h4>Supprimer</h4>
    </div>
  </div>
</template>

<style>
#form_text_barre {
  margin-top: 27px;
  position: fixed;
  width: 100%;
  height: 100px;
}

.name {
  margin-left: 30px;
}

.name h1 {
  color: white;
  font-family: Ubuntu, serif;
  font-weight: bold;
  font-size: 36px;
}

.action {
  margin-left: 78%;
  margin-top: -72px;
}

.action h2 {
  color: white;
  font-family: Ubuntu, serif;
  font-weight: bold;
  font-size: 36px;
}

.action h3 {
  color: white;
  font-family: Ubuntu, serif;
  font-weight: bold;
  font-size: 36px;
  margin-left: 140px;
  margin-top: -70px;
}

.action h4 {
  color: white;
  font-family: Ubuntu, serif;
  font-weight: bold;
  font-size: 36px;
  margin-left: 320px;
  margin-top: -75px;
}

.connecte {
  z-index: 2;
  border-radius: 10px;
  margin-left: 12%;
  margin-top: -60px ;
  height: 36px;
  width: 36px;
  background-color: #9b9b9b;
}

.connecte button {
  background-color: green;
  height: 15px;
  width: 15px;
  margin: 28%;
  border-radius: 10px;
  border-color: transparent;
}
</style>