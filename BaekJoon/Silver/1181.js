const fs = require('fs');
const file=process.platform==='linux'?'/dev/stdin':'./input.txt';
const [n, ...arr] = fs.readFileSync(file).toString().trim().split("\n");

var set=new Set(arr);
var newArr = [...set];
newArr.sort(compareFunc);
for(let i=0;i<newArr.length;i++)
	console.log(newArr[i]+"\n");

var compareFunc = (str1, str2) => {
	str1.length-str2.length || a.localeCompare(b);
}

// var compareFunc = (str1, str2) => {
// 	if(str1.length<str2.length)
// 		return 1;
// 	else if(str1.length==str2.length){
// 		if(str1<str2)
// 			return 1;
// 		else if(str1==str2)
// 			return 0;
// 		else
// 			return -1;
// 	}
// 	else
// 		return -1;
// }