# Here we have given a list=[3,1,2] and we have to find the subsequence {[3,1,2],[3,1],[3,2],[1,2],[3],[1],[2],[]}
print("Hello Woeld")
def ss(ind,res,arr,n):
    if ind ==n:
        if len(res) == 0:
            print("[]")
        else:
            print(" ".join(str(x) for x in res))
        return 
    
    res.append(arr[ind])
    ss(ind+1,res,arr,n)
    res.pop()
    ss(ind+1,res,arr,n)
print("Hello World")
arr=[3,1,2]
n=3
res=[]
ss(0,res,arr,n)