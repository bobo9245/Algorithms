const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split("\n");

const n = Number(input[0]);
let arr = new Array(2);
for(let i = 0;i<arr.length;i++){
	arr[i] = input[i+1].trim().split(' ').map(e=>e*1);
}

console.log(n);
console.log(arr);