const fs = require('fs');
const input = fs.readFileSync('./dev/stdin').toString().trim().split("\n").map(e=>e.toString());
input.pop();
input.forEach(str=>{
	let answer = true;
	for(let i = 0;i<str.length;i++)
		if(str.charCodeAt(i)!=str.charCodeAt(str.length-1-i))
			answer=false;
	console.log(answer?'yes':'no');
})