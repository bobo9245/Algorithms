const fs = require('fs');
const isPrimal = (num) => {
	i=2;
	if(num==2) 
		return true;
	else {
		while(Math.pow(i,2)<=num){
		if(num%i==0)
			return false;
		i++;
		}
		return true;
	}
}

const [m,n] = fs.readFileSync('input.txt').toString().trim().split(" ").map(Number);

for(let i = m;i<=n;i++){
	if(isPrimal(i)) console.log(i);
}