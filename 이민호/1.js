function solution(id_list, report, k) 
{
    var set = new Set(report)
    const Report = [...set]
    var diction = {}
    const answer = []

    for (let i = 0; i < id_list.length; i++)
    {
        diction[id_list[i]] = 0;
    }
    for (let i = 0; i < Report.length; i++)
    {
        diction[Report[i].split(' ')[1]]++
    }
    for (let i = 0; i < id_list.length; i++)
    {
        num = 0
        for (let j = 0; j < Report.length; j++)
        {
            if (id_list[i] === Report[j].split(' ')[0])
            {
                if (diction[Report[j].split(' ')[1]] >= k)
                {
                    num++
                }
            }
        }
        answer.push(num)
    }

    return answer;
}
a = solution(["muzi", "frodo", "apeach", "neo"],["neo frodo","muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"],   2)
console.log(a)
