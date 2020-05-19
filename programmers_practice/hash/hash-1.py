def solution(participant, completion):
    arr = [[]]*26 // A to Z 
    
    for x in participant:
        arr[ord(x[0])].append(x)
    
    for y in completion:
        a = arr[ord(y[0])]
        idx = 0
        for z in a:
            if z == y:
                a.pop(idx)
                break
            idx += 1
    
    for x in arr:
        if x != []:
            answer = x
            break
    
    return answer