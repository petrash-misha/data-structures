import main

# test add :
hash_map = main.HashMap()


letters = ['a', 4.7, 'c', 'd','fk', 'g', 7, 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'h', 'r', 's', 't', 'u', 'v', 'w', 'x','hj', False, [1, 3.6, 4, "gh"], 8, 3 + 4j, ("apple", "banana", "cherry"), range(5), 9.7]

print(hash_map._count)


num = 0
for i in letters:
    num += 1
    print("PRIME is: ", hash_map._prime)
    hash_map.add(i, num)

print(hash_map._array)
print(len(hash_map._array))
print(hash_map._count)

num = 0
for i in letters:
    num += 1
    v = hash_map.get(i)
    print(f"is {i} = {num} :", v == num)

print(hash_map._array)
print(len(hash_map._array))
print(hash_map._count)


print("----------------------------------------------")
num = -26
for i in letters:
    v = hash_map.update(i, num)
    print(f"is {i} = {num} :", v)
    num += 1

print(len(hash_map._array))
print(hash_map._array)
print(hash_map._count)

print("----------------------------------------------")


num = -26
for i in letters:
    v = hash_map.delete(i)
    print(f"is {i} deleted :", v == num)
    num += 1


print(len(hash_map._array))
print(hash_map._array)
print(hash_map._count)


print("----------------------------------------------")
num = 0
for i in letters:
    num += 1
    hash_map.add(i, num)

num = 0
for i in letters:
    num += 1
    v = hash_map.get(i)
    print(f"is {i} = {num} :", v == num)

print(len(hash_map._array))
print(hash_map._array)
print(hash_map._count)

print("----------------------------------------------")

hash_map.clear()
print(len(hash_map._array))
print(hash_map._array)
print(hash_map._count)





