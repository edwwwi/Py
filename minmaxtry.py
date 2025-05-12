def minmax(num):
    small = min(num)
    larg= max(num)
    return small,larg
no = [1,2,3,66,7,87,97,56,86,7,67]
no.sort()
print(no)

min_val,max_val = minmax(no)
print(min_val)
print(max_val)