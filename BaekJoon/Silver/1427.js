const fs = require('fs');
const number = fs.readFileSync('input.txt').toString().trim();
let arr = [];

for(let i = 0;i<number.length;i++)
	arr.push(Number(number[i]));

const answer = arr.sort(function(a,b){return (b-a)}).join('');

console.log(answer);