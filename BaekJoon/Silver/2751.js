const fs = require('fs');
const [n, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split("\n").map(e=>parseInt(e,10));

arr.sort((a,b)=>{
	if(a>b)
		return 1;
	else if(a==b)
		return 0;
	else
		return -1;
})
		 
console.log(arr.join('\n'));
//생각보다 console.log가 느리다!