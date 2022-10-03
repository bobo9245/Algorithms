const fs = require('fs');
const [n,...input] = fs.readFileSync('/dev/stdin').toString().trim().split("\n");

input.sort((a,b)=>{
	let [x1,y1] = [parseInt(a.split(' ')[0]),parseInt(a.split(' ')[1])];
	let [x2,y2] = [parseInt(b.split(' ')[0]),parseInt(b.split(' ')[1])];
	return (x1-x2==0?y1-y2:x1-x2);
})

const answer = input.join('\n');
console.log(answer);