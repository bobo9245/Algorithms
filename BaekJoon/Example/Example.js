const fs = require('fs');
const file=process.platform==='linux'?'/dev/stdin' : './input.txt';
let input = fs.readFileSync(file).toString().split('\n');

input = input[0];
//input = input.split(' ').map((item)=>Number(item));

solution(input[0],input[1]);

var solution = (a,b) => {
	console.log(a+b);
}