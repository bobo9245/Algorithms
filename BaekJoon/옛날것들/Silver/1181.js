const fs = require('fs');
const file=process.platform==='linux'?'/dev/stdin':'./input.txt';
const [n, ...arr] = fs.readFileSync('/dev/stdin').toString().trim().split("\n");


var set=new Set(arr);
var newArr = [...set];
newArr.sort((str1, str2) => {
	return str1.length-str2.length || str1.localeCompare(str2);
});
for(let i=0;i<newArr.length;i++)
	console.log(newArr[i]);