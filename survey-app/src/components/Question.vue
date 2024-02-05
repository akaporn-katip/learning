<script setup lang="ts">
import { ref } from "vue";

const question: any = defineModel({ required: true });
const emitter = defineEmits(["update:change-answer"]);
const answer = ref(question.value.answer);
</script>
<template>
  {{ question.question }}
  <label v-for="choice in question.choices" :key="choice.score">
    <input
      type="radio"
      v-model="answer"
      :value="choice.score"
      @change="$emit('update:change-answer', answer)"
    />
    {{ choice.choice }}
  </label>
</template>
