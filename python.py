# print("Hello World")
# name = input("Куда тебя послать? ")
# print("Иди ка ты", name)

# num_1 = int(input("Введите первое значение: "))
# num_2 = float(input("Введите второе значение: "))
# num_3 = num_1 + num_2
# print("Result is", num_3)
# del num_3

# Списки
# l = []
# a = [a + b for a in "list" if a != "s" for b in "soup" if b != "u"]
# print(a)

# l.append(2)
# l.append(4)
# print(l)

# b = [24, 67]
# l.extend(b)
# print(l)

# l.insert(2, 56)
# print(l)

# l.remove(56)
# print(l)

# l.pop(0)
# print(l)

# print(l.index(67))
# print(l.count(67))
# print(l)

# l.reverse()
# print(l)

# l.sort()
# print(l)

# l.clear()
# print(l)

# Индексы и срезы
# l = [34, "sd", 56, 34.34]
# # print(l[0])
# # print(l[-1])
# i = 0
# while i < 4:
# 	print(l[i])
# 	i += 1

# # item[START:STOP:STEP]
# print(l[:])
# print(l[1::])
# print(l[1:2:])
# print(l[::2])

# Кортежи (неизменяемые списки)
# a = (1, 2, 3, 4, 5, 6, 7, 8, 9)  # можно писать без запятой
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print(a.__sizeof__())
# print(b.__sizeof__())
# c = tuple("Hello World")
# print(c)

# Словари
# d = {
#     "test_1": 1,
#     "test_2": 2,
#     "test_3": 3,
#     "test_4": 4,
# }
# print(d["test_3"])

# d = dict(test_1=1, test_2=2, test_3=3, test_4=4)
# d["test_1"] = 0
# print(d["test_1"])

# d = dict([("test_1", 1), ("test_2", 2), ("test_3", 3), ("test_4", 4)])
# print(d["test_1"])

# d = dict.fromkeys(["test_1", "test_2"])
# print(d)

# d = dict.fromkeys(["test_1", "test_2"], 1)
# print(d)

# d = {a : a ** 2 for a in range(10)}
# print(d)

# Множества
m = set('HELLO')
print(m)
m.add(12)
print(m)
n = frozenset('WORLD') # неизменяемое множество
# n.add(12)
print(n)


m = {1, 2, 3, 4, 5}
print(m)

m = {a ** 2 for a in range(10)}
print(m)
print(len(m))
x = 36
print(x in m)
x = {64, 103, 36}
print(m)
print(x)
print(m.isdisjoint(x))  # TRUE не имеют общих элементов. Если хоть один совпадает, то FALSE

# m.update(x) # добавление значения в множество
# print(m)
# m.intersection_update(x) # останутся только смежные значения
# print(m)
# m.difference_update(x) # останутся только несмежные значения
# print(m)
# m.symmetric_difference_update(x) # 
# print(m)
m.add(23)
print(m)
m.remove(23)
m.discard(36)
print(m)
m.pop()
print(m)
m.clear()
print(m)


