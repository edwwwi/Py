for num in range(1,100 ):
    s = 0
    temp = num
    while temp > 0:
        s += temp % 10
        temp = temp // 10
    
    if s % 8 == 0:
        print(num)