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
    <div class="left_side initial">
      <div class="name">
        <h1>AtlantaVR_Bot</h1>
      </div>
      <div class="connecte">
        <button></button>
      </div>
    </div>
    <div class="action initial">
      <button class="liste">Liste</button>
      <button class="Ajouter">Ajouter</button>
      <button class="Supprimer">Supprimer</button>
    </div>
  </div>
</template>

<style>
#form_text_barre {
  margin-top: 27px;
  position: fixed;
  width: 100%;
  height: 100px;
  display: flex;
  resize: horizontal;
}

.left_side {
  width: 66%;
  flex: auto;
  background-color: rgba(208, 11, 11, 0.47);
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
  right: 10px;
  margin-top: 22px;
  width: 600px;
  flex: initial;
  background-color: rgba(217, 196, 196, 0.47);
}

.liste {
  background-color: transparent;
  border-color: transparent;
  color: white;
  font-family: Ubuntu, serif;
  font-weight: bold;
  font-size: 36px;
}

.Ajouter {
  background-color: transparent;
  border-color: transparent;
  color: white;
  font-family: Ubuntu, serif;
  font-weight: bold;
  font-size: 36px;
  margin-left: 25px;
}

.Supprimer {
  background-color: transparent;
  border-color: transparent;
  color: white;
  font-family: Ubuntu, serif;
  font-weight: bold;
  font-size: 36px;
  margin-left: 25px;
}

.connecte {
  z-index: 2;
  border-radius: 10px;
  margin-left: 300px;
  margin-top: -60px;
  height: 36px;
  width: 36px;
  background-color: #9b9b9b;
}

.connecte button {
  background-color: green;
  margin: 28%;
  height: 15px;
  width: 15px;
  border-radius: 10px;
  border-color: transparent;
}

@media (max-width: 1200px) {
  .left_side {
    width: 55%;
  }

  .liste {
    font-size: 32px;
  }

  .Ajouter {
    font-size: 32px;
  }

  .Supprimer {
    font-size: 32px;
  }

  .connecte {
    margin-top: -55px;
    margin-left: 260px;
  }

  .name h1 {
    font-size: 32px;
  }
}
</style>