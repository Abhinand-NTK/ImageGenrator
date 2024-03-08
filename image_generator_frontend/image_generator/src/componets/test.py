def  even(ls):
    count = 0
    for i in ls:
        if i.isnumeric():
            if int(i) % 2 == 0:
                count += 1
    return count


a = input() 
print(even(a))
print(a)