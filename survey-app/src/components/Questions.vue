<script setup lang="ts">
import { computed, ref } from "vue";
import Question from "./Question.vue";
import { useRouter } from "vue-router";

const currentQuestionIdx = ref(0);
const router = useRouter();

const questions = ref([
  {
    question: "ถ้าวันนี้เป็นวันหยุดคุณจะ",
    answer: 0,
    choices: [
      {
        choice: "นอนเล่น พักผ่อน",
        score: 10,
      },
      {
        choice: "ดูหนัง ดูซีรี่ส์ เล่นเกม",
        score: 20,
      },
      {
        choice: "เรียนรู้อะไรใหม่ ๆ",
        score: 30,
      },
    ],
  },
  {
    question: "คุณต้องการพัฒนาภาษาอังกฤษเพื่ออะไร",
    answer: 0,
    choices: [
      {
        choice: "การทำงาน",
        score: 10,
      },
      {
        choice: "เที่ยวต่างประเทศ",
        score: 20,
      },
      {
        choice: "ใช้ชีวิตประจำวัน",
        score: 30,
      },
    ],
  },
  {
    question: "คำถาม 3",
    answer: 0,
    choices: [
      {
        choice: "การทำงาน",
        score: 10,
      },
      {
        choice: "เที่ยวต่างประเทศ",
        score: 20,
      },
      {
        choice: "ใช้ชีวิตประจำวัน",
        score: 30,
      },
    ],
  },
  {
    question: "คำถาม 4",
    answer: 0,
    choices: [
      {
        choice: "การทำงาน",
        score: 10,
      },
      {
        choice: "เที่ยวต่างประเทศ",
        score: 20,
      },
      {
        choice: "ใช้ชีวิตประจำวัน",
        score: 30,
      },
    ],
  },
  {
    question: "คำถาม 5",
    answer: 0,
    choices: [
      {
        choice: "การทำงาน",
        score: 10,
      },
      {
        choice: "เที่ยวต่างประเทศ",
        score: 20,
      },
      {
        choice: "ใช้ชีวิตประจำวัน",
        score: 30,
      },
    ],
  },
  {
    question: "คำถาม 6",
    answer: 0,
    choices: [
      {
        choice: "การทำงาน",
        score: 10,
      },
      {
        choice: "เที่ยวต่างประเทศ",
        score: 20,
      },
      {
        choice: "ใช้ชีวิตประจำวัน",
        score: 30,
      },
    ],
  },
]);

const currentQuestion = computed(() => {
  return questions.value[currentQuestionIdx.value];
});

const currentQuestionNumber = computed(() => {
  return `Q${currentQuestionIdx.value + 1}`;
});

function getMaxQuestion() {
  return questions.value.length - 1;
}

function getQuestionIndex(currentIdx: number) {
  return Math.max(0, Math.min(getMaxQuestion(), currentIdx));
}

function nextQuestion() {
  currentQuestionIdx.value = getQuestionIndex(currentQuestionIdx.value + 1);
}

function previousQuestion() {
  currentQuestionIdx.value = getQuestionIndex(currentQuestionIdx.value - 1);
}

const isLast = computed(() => {
  return currentQuestionIdx.value === getMaxQuestion();
});

function handleChangeAnswer(idx: number) {
  return function (answer: number) {
    questions.value[idx].answer = answer;
  };
}

function handleSaveAnswer() {
  localStorage.setItem("answer", JSON.stringify(questions.value));
  router.push("result");
}
</script>

<template>
  {{ currentQuestionNumber }}
  <Question
    v-model="currentQuestion"
    :key="currentQuestion.question"
    @update:change-answer="(e) => handleChangeAnswer(currentQuestionIdx)(e)"
  />
  <button @click="previousQuestion">กลับ</button>

  <button v-if="isLast" @click="handleSaveAnswer">สรุปผล</button>
  <button v-else @click="nextQuestion">ต่อไป</button>
</template>
