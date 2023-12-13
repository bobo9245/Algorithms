const fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim().split('\n');

let answer = '';

const [n,m] = input[0].split(' ').map(e=>e*1);

input.shift();
input.shift();

const problems = input.slice(n-1,input.length);
for(let i = 0;i<m;i++)
	input.pop();

problems.forEach((problem) => {
	if(Number.isNaN(Number(problem)))
		// answer.push(input.findIndex(e=>e==problem)+2);
		answer+=`${input.findIndex(e=>e==problem)+2}\n`
	else{
		// answer.push(input[parseInt(problem,10)-2]);
		answer+=`${input[parseInt(problem,10)-2]}\n`
	}
		
})

console.log(answer);