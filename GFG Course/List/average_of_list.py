def average_of_list(l):
    return sum(l)/len(l)
def average_of_list_2(l):
    sum = 0
    num = 1
    for i in l:
        sum +=i
        num +=1
    return sum/num

print(average_of_list_2([1,2,3,5,7,8,235,25]))

        
