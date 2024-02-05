import { createApp } from "vue";
import { RouterOptions, createRouter, createWebHashHistory } from "vue-router";
import RootLayout from "./components/RootLayout.vue";
import MainPage from "./components/MainPage.vue";
import QuestionPage from "./components/QuestionPage.vue";
import ResultPage from "./components/ResultPage.vue";

const routes = [
  {
    path: "",
    component: RootLayout,
    children: [
      {
        path: "",
        component: MainPage,
      },
      {
        path: "questions",
        component: QuestionPage,
      },
      {
        path: "result",
        component: ResultPage,
      },
    ],
  },
];

const router = createRouter({
  history: createWebHashHistory(),
  routes,
} as RouterOptions);

createApp(RootLayout).use(router).mount("#app");
