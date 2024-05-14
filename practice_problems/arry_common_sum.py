# input=[1,2,3,4,5],[3,4,5,8]=arr1,arr2
# output=12


def common_arry_sum(arr1,arr2):
    sum=0
    for num in arr1:
        if num in arr2:
            sum+=num
    return sum

print(common_arry_sum([1,2,3,4,5],[3,4,5,8]))


