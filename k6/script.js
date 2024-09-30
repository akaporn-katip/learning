import http from "k6/http";
import { sleep } from "k6";
import { URL } from 'https://jslib.k6.io/url/1.0.0/index.js';

export const options = {
  //stages: [
  //  { duration: '10s', target: 10 }
  //]
  vus: 40,
  duration: "60s",
  insecureSkipTLSVerify: true,
  setupTimeout: '120s',
};

export default function () {
  const query = {
    transaction: true,
    successRate: true,
    channelUsages: true,
    trendType: "hourly",
    startTime: "2024-06-01T05:33:19.376Z",
    endTime: "2024-07-20T05:33:19.376Z",
  };

  const url = new URL("https://192.168.1.100:9443/api/dashboard/summaryDashboard");

  Object.keys(query).forEach((key) => {
    url.searchParams.append(key, query[key])
  })

  const bearer =
    "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJrZXkiOiJwNEs2MDNFSGRtZFV1ZG5YUWczWkJvIiwicHVibGljSWQiOiJlbnRyb0NBQSIsInJvbGUiOiJDQUEiLCJleHAiOjE3MjE0NTE0MTAsInN5c0VtYWlsIjoiYWthcG9ybi5rQGVudHJvbmljYS5jby50aCIsImlhdCI6MTcyMTM2NTAxMH0.UnZg8DHbkJ9AHrihABhpc_qofr9kSGtyx2qFvgr7vqc";

  const res = http.get(url.toString(), {
    headers: {
      "x-authorization": bearer,
      "x-transaction": `${new Date().getTime()}`,
    },
    query: {
      transaction: true,
    },
  });
  sleep(1);
}
