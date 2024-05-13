# 嵌套循环
print("\tDog \tBun \tKetCHUP \tMustard \tOnions")
count = 1
for dog in [0,1]:  # dog loop
    for bun in [0,1]:  # bun loop
        for ketchup in [0,1]:  # ketchup loop
            for mustard in [0,1]:  # mustard loop
                for onion in [0,1]:
                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion)  # onion loop
                    count = count + 1

# Dog 	Bun 	KetCHUP 	Mustard 	Onions
# 1 	0 	 0 	 0 	0 	 0
# 2 	0 	 0 	 0 	0 	 1
# 3 	0 	 0 	 0 	1 	 0
# 4 	0 	 0 	 0 	1 	 1
# 5 	0 	 0 	 1 	0 	 0
# 6 	0 	 0 	 1 	0 	 1
# 7 	0 	 0 	 1 	1 	 0
# 8 	0 	 0 	 1 	1 	 1
# 9 	0 	 1 	 0 	0 	 0
# 10 	0 	 1 	 0 	0 	 1
# 11 	0 	 1 	 0 	1 	 0
# 12 	0 	 1 	 0 	1 	 1
# 13 	0 	 1 	 1 	0 	 0
# 14 	0 	 1 	 1 	0 	 1
# 15 	0 	 1 	 1 	1 	 0
# 16 	0 	 1 	 1 	1 	 1
# 17 	1 	 0 	 0 	0 	 0
# 18 	1 	 0 	 0 	0 	 1
# 19 	1 	 0 	 0 	1 	 0
# 20 	1 	 0 	 0 	1 	 1
# 21 	1 	 0 	 1 	0 	 0
# 22 	1 	 0 	 1 	0 	 1
# 23 	1 	 0 	 1 	1 	 0
# 24 	1 	 0 	 1 	1 	 1
# 25 	1 	 1 	 0 	0 	 0
# 26 	1 	 1 	 0 	0 	 1
# 27 	1 	 1 	 0 	1 	 0
# 28 	1 	 1 	 0 	1 	 1
# 29 	1 	 1 	 1 	0 	 0
# 30 	1 	 1 	 1 	0 	 1
# 31 	1 	 1 	 1 	1 	 0
# 32 	1 	 1 	 1 	1 	 1