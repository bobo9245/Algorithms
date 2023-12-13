// https://www.acmicpc.net/problem/2475

const fs = require('fs');
var answer = 0;
const input = fs.readFileSync('/dev/stdin').toString().trim().split(" ").map(e=>answer+=Math.pow(Number(e),2));

answer%=10;

console.log(answer);