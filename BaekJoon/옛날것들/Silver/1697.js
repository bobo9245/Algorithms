const fs = require('fs');
const [n,k] = fs.readFileSync('input.txt').toString().trim().split(" ").map(e=>e*1);

let visited = new Array(100001).fill(false);
let queue = [];
let isCompleted=false;
queue.push([n,0]);
while(queue.length!=0){
	const [A,length] = queue.shift();
	const dr = [A,-1,1];
	for(let i=0;i<3;i++){
		const num = A+dr[i];
		if(num==k){
			console.log(length+1);
			isCompleted=true;
			break;
		} 
		else if(num<0||num>100000||visited[num]) continue;
		visited[num]=true;
		queue.push([num,length+1]);
	}
	if(isCompleted) break;
}