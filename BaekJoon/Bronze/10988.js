const fs = require('fs');
const file=process.platform==='linux'?'./dev/stdin':'./input.txt';
const input = fs.readFileSync(file).toString().trim();

console.log(isPalin(input)?1:0);

var isPalin = (str) => {
	let answer = true;
	let start = 0;
	let end = str.lenght-1;
	
	while(start<end){
		if(str[start]==str[end]){
			start++;
			end--;
		}
		else{
			answer=false;
			break;
		}
	}
	return answer;
}

//const fs = require('fs');
// const input = fs.readFileSync("./dev/stdin").toString().trim();
// let answer = 1;
// let start = 0;
// let end = input.length - 1;

// while (start < end) {
//   if (input[start] == input[end]) {
//     start++;
//     end--;
//   } else {
//     answer = 0;
//     break;
//   }
// }

// console.log(answer)