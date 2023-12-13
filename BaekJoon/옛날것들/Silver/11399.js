const fs = require('fs');
const [n, ...arr] = fs.readFileSync('dev/stdin').toString().trim().split(/\s/);

arr1 = arr.map((e)=>+e);
arr1.sort((a,b)=>a-b);
let answer = 0;
for(let i = 0;i<arr1.length;i++)
	for(let j = 0;j<=i;j++)
		answer+=arr1[j];

console.log(answer);