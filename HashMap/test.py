import main

# test add :
hash_map = main.HashMap()


letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x','y', 'z']

num = 0
for i in letters:
    num += 1
    hash_map.add(i, num)

num = 0
for i in letters:
    num += 1
    v = hash_map.get(i)
    print(f"is {i} = {num} :", v == num)

print(hash_map.array)




