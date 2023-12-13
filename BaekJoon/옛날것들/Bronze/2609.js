const fs = require('fs');
const file=process.platform==='linux'?'/dev/stdin':'./input.txt';
const [a,b] = fs.readFileSync('./dev/stdin').toString().trim().split(" ").map(e=>e*1);

let i = a;
let j = b;

while (i % j !== 0) {
    let n = i % j;
    if (n !== 0) {
        i = j;
        j = n;
    }
}
console.log(j)
console.log(a*b/j)