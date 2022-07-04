import _locale

def func(a , b=[]):
    b.append(a)
    print(id(b))
    a = b[:]
    del b
    return a


a = func(1)
a = func(2)
print(a)

#python m function k andr declared variables ko same memory milti h chahe kitni baar bulaye unhe aur delete krne pr bhi vo value nhi jati
#mtlb variable ka reference toh delete ho gya but jo memory pr value h vo nhi hui aur hr baar jb function recall hoga toh vhi memory milegi