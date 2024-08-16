def ps(ind, s, sum, arr, n):
    if ind == n:
        # Condition satisfied return 1
        if s == sum:
            return 1
        # Condition not satisfied return 0
        else:
            return 0
    s += arr[ind]


'''l=f()
    r=f()
    return l+r'''

''' for more then 2 elements to add
    s=0
    for (i=1->n)
    s+=f()
    return s'''


    l = ps(ind + 1, s, sum, arr, n)
    s -= arr[ind]
    r = ps(ind + 1, s, sum, arr, n)
    return l + r

if __name__ == "__main__":
    print("Hello world!")
    arr = [1, 2, 1]
    n = 3
    sum = 2
    print(ps(0, 0, sum, arr, n))

