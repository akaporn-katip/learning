<script setup lang="ts">
import { useRouter } from "vue-router";

const router = useRouter();
</script>
<template>
  main page
  <button @click="router.push('questions')">เริ่มเลย</button>
</template>
