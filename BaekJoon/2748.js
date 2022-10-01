const fs = require('fs');
const file=process.platform==='linux'?'/dev/stdin':'./input.txt';
const input = fs.readFileSync(file).toString().trim()*1;//바로 숫자로.

console.log(fib(input));
var arr = new Array(90);
arr.fill(-1);
arr[0]=0;
arr[1]=1;
var fib = (n) => {
	if(n<=1)
		return arr[n];
	else{
		if(arr[n]!=-1)
			return arr[n];
		arr[n] = BigInt(fib(n-1))+BigInt(fib(n-2));
		return arr[n];
	}
}