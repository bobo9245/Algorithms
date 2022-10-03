// 원래 문제 링크 : https://school.programmers.co.kr/learn/courses/30/lessons/12925
// 블로그 풀이 : https://bobo9245.tistory.com/39
// 문자열을 정수로 바꾸기

var solution = (s) => {
    var strArr = s.split('');
    let isMinus = false;
    if(strArr[0]=='-'){
        strArr.shift();
        isMinus=true;
    }
    var string = strArr.join('');
    console.log(string);
    var answer=parseInt(string);
    return isMinus?-answer:answer;
            
}