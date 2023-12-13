const fs = require('fs');
const [n,...input] = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

input.sort((a,b)=>{
	ageA = parseInt(a.split(' ')[0]);
	ageB = parseInt(b.split(' ')[0]);
	if(ageA>ageB)
		return 1;
	else if(ageA==ageB)
		return 0;
	else
		return -1;
})

const answer = input.join('\n');
console.log(answer);