<script setup lang="ts">
import { ref } from "vue";

const answers = ref(loadAnswer());

function loadAnswer() {
  return JSON.parse(localStorage.getItem("answer") ?? "");
}

function getAnswer() {
  return answers.value.map((ans: any) => ans.answer);
}

function sum(): number {
  return getAnswer().reduce((a: number, b: number) => a + b, 0);
}

function getResult(n: number) {
  if (n >= 131 && n <= 180) {
    return "The Gradual Learner";
  } else if (n >= 91 && n <= 130) {
    return "The Enthusiastic";
  } else if (n >= 60 && n <= 90) {
    return "The Hobbyist";
  } else {
    return "Number is out of the specified ranges";
  }
}
</script>

<template>Result :{{ getResult(sum()) }}</template>
