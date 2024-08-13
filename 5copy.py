#copy ถ้าไม่ใช้จะทำให้ list 2  ตัว นี้มี memory  address เดียวกัน

lst_a = [1,2,3,4,5]

lst_b = lst_a.copy()

lst_b[0] = 5
print(lst_b)

print(lst_a)