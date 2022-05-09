function second(c)
{
    var pattern_num = /[0-9]/;   
    var pattern_eng = /[a-zA-Z]/;   
    var pattern_spc = /[_.-]/;
    if (pattern_num.test(c)|| pattern_eng.test(c)||pattern_spc.test(c))
        return c
    else 
        return ''
}
function solution(new_id) {
    var answer = '';
    new_id = new_id.toLowerCase()
    console.log(new_id)
    for(let i = 0 ; i < new_id.length;i++)
    {
        answer += second(new_id[i])
    }
    console.log(answer)
    answer = answer.replace("..",".")
    console.log(answer)
    return answer;
}
solution("...!@BaT#*..y.abcdefghijklm")
