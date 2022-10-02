//https://www.acmicpc.net/problem/1094

const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim();
const length = Number(input).toString(2);
const arr = length.split('');
let count = arr.filter(e => e==1).length;
console.log(count);