const fs = require('fs');
const input = fs.readFileSync('input.txt').toString().trim().split("\n");
let answer = 0;
for(let i = 0;i<input.length;i++)
	input[i] = input[i].split('');

for(let j = 0;j<8;j++)
	for(let k = 0;k<8;k++){
		if((j+k)%2==0 && input[j][k]=='F')
			answer++;
		else
			continue;
	}

console.log(answer);