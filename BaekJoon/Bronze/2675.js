const fs = require('fs');
const [n, ...arr] = fs.readFileSync('input.txt').toString().trim().split(/\s/);

console.log(arr);