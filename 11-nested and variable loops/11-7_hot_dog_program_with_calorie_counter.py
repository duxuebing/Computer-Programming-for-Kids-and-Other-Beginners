dog_cal = 140 # <---- (本行及以下4行) 列出热狗各成分的热量
bun_cal = 120
ket_cal = 80
mus_cal = 20
onion_cal = 40
print("\tDog \tBun \tKetchup\tMustard\tOnions\tCalories") # <---- 打印表头
count = 1
for dog in [0, 1]: # <---- 热狗循环是外循环
    for bun in [0, 1]:  # (本行及以下11行) 嵌套循环
        for ketchup in [0, 1]:
            for mustard in [0, 1]:
                for onion in [0, 1]:
                    total_cal = (bun * bun_cal)+(dog * dog_cal) + (ketchup * ket_cal)+(mustard * mus_cal) + (onion * onion_cal) #(本行及以下2行) 在内循环中计算热量

                    print("#", count, "\t", end='')
                    print(dog, "\t", bun, "\t", ketchup, "\t", end='')
                    print(mustard, "\t", onion, end='')
                    print("\t", total_cal)
                    count = count + 1

# Dog 	Bun 	Ketchup	Mustard	Onions	Calories
# 1 	0 	 0 	 0 	0 	 0	 0
# 2 	0 	 0 	 0 	0 	 1	 40
# 3 	0 	 0 	 0 	1 	 0	 20
# 4 	0 	 0 	 0 	1 	 1	 60
# 5 	0 	 0 	 1 	0 	 0	 80
# 6 	0 	 0 	 1 	0 	 1	 120
# 7 	0 	 0 	 1 	1 	 0	 100
# 8 	0 	 0 	 1 	1 	 1	 140
# 9 	0 	 1 	 0 	0 	 0	 120
# 10 	0 	 1 	 0 	0 	 1	 160
# 11 	0 	 1 	 0 	1 	 0	 140
# 12 	0 	 1 	 0 	1 	 1	 180
# 13 	0 	 1 	 1 	0 	 0	 200
# 14 	0 	 1 	 1 	0 	 1	 240
# 15 	0 	 1 	 1 	1 	 0	 220
# 16 	0 	 1 	 1 	1 	 1	 260
# 17 	1 	 0 	 0 	0 	 0	 140
# 18 	1 	 0 	 0 	0 	 1	 180
# 19 	1 	 0 	 0 	1 	 0	 160
# 20 	1 	 0 	 0 	1 	 1	 200
# 21 	1 	 0 	 1 	0 	 0	 220
# 22 	1 	 0 	 1 	0 	 1	 260
# 23 	1 	 0 	 1 	1 	 0	 240
# 24 	1 	 0 	 1 	1 	 1	 280
# 25 	1 	 1 	 0 	0 	 0	 260
# 26 	1 	 1 	 0 	0 	 1	 300
# 27 	1 	 1 	 0 	1 	 0	 280
# 28 	1 	 1 	 0 	1 	 1	 320
# 29 	1 	 1 	 1 	0 	 0	 340
# 30 	1 	 1 	 1 	0 	 1	 380
# 31 	1 	 1 	 1 	1 	 0	 360
# 32 	1 	 1 	 1 	1 	 1	 400