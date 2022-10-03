//https://gurtn.tistory.com/55 이 페이지를 참고하였음.

const fs = require('fs');
let input = fs.readFileSync('input.txt').toString().trim()*1;
let count = 0;
while(true){
	if(input%5==0){
		console.log(count+input/5);
		break;
	}
	
	if(input < 0){
		console.log(-1);
		break;
	}
	
	count++;
	input-=3;
}
