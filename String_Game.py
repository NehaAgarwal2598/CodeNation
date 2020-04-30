#Alice BOb remove elements from string canno remove if both extremes are same print who won

def solve(self, A):
    res = []
    player = ['Alice', 'Bob']
    n = len(A)
    for i in range(n):
        ele = list(A[i])
        n0 = ele[0]
        nn = ele[len(ele)-1]
        index = (len(ele)-2)%2
        
        if n0 == nn and  index !=0:
            res.append(player[index])
            
        elif n0 == nn and index ==0:
            res.append(player[index])
            
        elif n0 != nn and index !=0:
            res.append(player[index-1])
            
        elif n0 != nn and index ==0:
            res.append(player[index+1])
            
    return res
