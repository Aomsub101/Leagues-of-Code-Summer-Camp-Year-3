#dict key-value
s = "bird"

d = {"dog":"สุนัข", "banana":"กล้วย", s:"nok"}

# print(d["banana"]) #ไม่แนะนำ
print(d.get("bird")) #ดีกว่า เพราะถ้าพิมพ์ผิด จะ return ค่า none ออกมา