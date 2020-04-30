n, m = list(map(int, input().split()))
t=1
for i in range(1,n+1):
    if i%2 == 0:
        if t%2!=0:
            for j in range(1,m):
                print(".", end='')

            print("#",end='')
            t +=1
        else:
            print("#", end='')
            for j in range(1,m):
                print(".", end='')

            t +=1

    else:
        for j in range(1,m+1):
            print("#", end='')


    print()
            
