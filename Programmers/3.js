//원래 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12909
//블로그 풀이 : https://bobo9245.tistory.com/38
//폰켓몬

function solution(nums){
    var ponketmons=[];
    nums.forEach((x)=>{
        if(ponketmons.find(n=>n==x)==undefined)
            ponketmons.push(x);
    });
    return (ponketmons.length<nums.length/2?ponketmons.length:nums.length/2);
}