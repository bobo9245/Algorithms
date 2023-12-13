const fs = require('fs');
const [n, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split(/\s/).map(e=>parseInt(e));

let count=0;

arr.forEach(x=>{
	let c =0;
	for(let i=2;i<x;i++){
		if(x%i==0)
			c++;
	}
	if(c==0){
		if(x>1)
			count++;
	}
})

console.log(count);