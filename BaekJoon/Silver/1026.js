const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().split("\n");
const n = Number(input[0]);
let answer = 0;
let arr = new Array(2);
for(let i = 0;i<arr.length;i++){
	arr[i] = input[i+1].trim().split(' ').map(e=>e*1);
}

let arr1 = [...arr[0]];
let arr2 = [...arr[1]];

arr1.sort((a,b)=>a-b);//오름차순 정렬
arr2.sort((a,b)=>b-a);//내림차순 정렬

console.log(arr1);
console.log(arr2);


for(let i = 0;i<n;i++)
	answer+=arr1[i]*arr2[i];

console.log(answer);