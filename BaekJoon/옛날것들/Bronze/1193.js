const fs = require('fs');
let X = fs.readFileSync('input.txt').toString().trim();
let [first,second]=[0,0];

if(X==1) console.log('1/1');
else 
	for(let i = 1;i<Math.floor(Math.sqrt(3200));i++)
		if((Math.pow(i,2)+i)/2<X && X <= (Math.pow(i,2)+3*i+2)/2){
			const num = (Math.pow(i,2)+3*i+2)/2;
			first = i+X-num;
			second = num-X+1;
			console.log(`${first}/${second}`);
			break;
		}

