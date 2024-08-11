# Here given a list [1,2,1] having sum=2 find the subsequenc {[1,1],[2]} 
print("Hello World")
def print_s(ind, ds, count, sum, arr, n):
    if ind == n:
        if count == sum:
            print(*ds)
        return
    ds.append(arr[ind])
    count += arr[ind]
    print_s(ind + 1, ds, count, sum, arr, n)
    count -= arr[ind]
    ds.pop()
    print_s(ind + 1, ds, count, sum, arr, n)

if __name__ == "__main__":
    arr = [1, 2, 1]
    n = 3
    sum = 2
    ds = []
    print_s(0, ds, 0, sum, arr, n)