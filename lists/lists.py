test_list = ["Trufel", "Zhura", "Nekit", "Gavrila"]
print(test_list[0])
print(test_list[1])
print(test_list[2])
print(test_list[3])

test_list[0] = "Sonya"

print(f"Hello, {test_list[0]}")

test_list.append("Trufel")
test_list.insert(0, "Bash")
print(test_list)

del test_list[2]
print(test_list)

bash = test_list.pop(0)
print(bash)
print(test_list)

test_list.remove("Gavrila")
print(test_list)

test_list.sort()
print(sorted(test_list))
print(test_list)
test_list.sort(reverse=True)
print(test_list)
test_list.reverse()
print(test_list)
print(len(test_list))
