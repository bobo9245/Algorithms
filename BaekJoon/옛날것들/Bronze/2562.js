const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim().split("\n");
// const input = fs.readFileSync('input.txt').toString().trim().split("\n").map(e=>parseInt(e));

const max = Math.max(...input);

console.log(max);
console.log(input.indexOf(max)+1);