//원래 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12910
//블로그 풀이 : https://bobo9245.tistory.com/36
//나누어 떨어지는 숫자 배열

function solution(arr, divisor) {
    var answer = [];
    arr.forEach(x=>{
        if(x%divisor==0)
            answer.push(x);
    });
    if(answer.length==0)
        answer.push(-1);
    answer.sort(function(a, b)  {
        if(a > b) return 1;
        if(a === b) return 0;
        if(a < b) return -1;
    });
    return answer;
}