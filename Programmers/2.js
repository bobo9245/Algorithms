//원래 문제 : https://school.programmers.co.kr/learn/courses/30/lessons/12909
//블로그 코딩 풀이 : https://bobo9245.tistory.com/37
//이 문제와 유사 : https://www.acmicpc.net/problem/9012 
//올바른 괄호

function solution(s){
    var strArr = s.split('');
    var count=0;
    for(let i=0;i<strArr.length;i++){
        if(strArr[i]=='(')
            count++;
        else if(strArr[i]==')')
            count--;
        if(count<0)
            break;
    }
    return(count==0)
}