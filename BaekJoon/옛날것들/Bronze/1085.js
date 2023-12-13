const fs = require('fs');

const file=process.platform==='linux'?'/dev/stdin' : './input.txt';
const input=fs.readFileSync(file).toString().trim().split(' ');

var x,y,w,h;
x=input[0];
y=input[1];
w=input[2];
h=input[3];

console.log(Math.min(x,y,h-y,w-x));