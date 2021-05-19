list= [23,33,52,13,44]
for i in range(len(list)-1):
    for j in range(1,len(list)):
        if list[j-1]>list[j]:
            list[j-1],list[j] = list[j],list[j-1]
