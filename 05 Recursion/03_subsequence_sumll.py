# print any 1 subsequence whose sum is sum
print("Hello World")
def print_subset(ind, ds, s, sum, arr, n):
    if ind == n:


        '''if base condition satisfied:
             return true
        else: base condition not satisfied
            return false'''
        

        if s == sum:
            print(*ds)
            return True
        # condition not satisfied return False
        else:
            return False
    
    ds.append(arr[ind])
    s += arr[ind]


    '''if(f()==true):
        return True
    else:
        return False'''
    

    if print_subset(ind + 1, ds, s, sum, arr, n)==True:
        return True
    s -= arr[ind]
    ds.pop()
    # not picked
    if print_subset(ind + 1, ds, s, sum, arr, n)==True:
        return True
    else:
        return False
if __name__ == "__main__":

    arr = [1, 2, 1]
    n = 3
    sum = 2
    ds = []
    print_subset(0, ds, 0, sum, arr, n)

