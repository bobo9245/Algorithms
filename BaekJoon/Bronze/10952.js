const fs = require('fs');
const input = fs.readFileSync('/dev/stdin').toString().trim().split("\n");
input.pop();

for(let i = 0;i<input.length;i++){
	let A = parseInt(input[i].split(' ')[0]);
	let B = parseInt(input[i].split(' ')[1]);
	let result = A+B;
	
	console.log(result);
}
	