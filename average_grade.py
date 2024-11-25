grades = [[3,4,5,5,3], [5,4,5,5],[3,3,5,5,2,5],[4,4,5,5,],[2,2,2]]
student = {'Max', 'Boby', 'Irene','Den','Aaron'}
a = list(student)
b = sorted(a)                                                             # list fixed
x = []
for d in grades:
    x.append(sum(d)/len(d))                                               # average grades calculating
list_final = [[b[0], x[0]], [b[1], x[1]], [b[2], x[2]], [b[3], x[3]],[b[4], x[4]]]
dict_= dict(list_final)                                                    # dictionary compiled
print(dict_)