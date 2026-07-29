import main

# test add :
hash_map = main.HashMap()


letters = ['a', 4, 'c', 'd', 'e', 'fk', 'g', 7, 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z', 9.5]

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





