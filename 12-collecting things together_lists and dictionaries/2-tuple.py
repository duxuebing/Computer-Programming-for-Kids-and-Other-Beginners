mu_tuple = ("red", "green", "blue")

joeMarks = [55, 63, 77, 81]
tomMarks = [65, 61, 67,72]
bethMarks = [97,95,92,88]


classMarks = [joeMarks, tomMarks, bethMarks]
print(classMarks)  # [[55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88]]

classMarks = [[55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88]]
print(classMarks)  # [[55, 63, 77, 81], [65, 61, 67, 72], [97, 95, 92, 88]]

for studentMarks in classMarks:
    print(studentMarks)
# [55, 63, 77, 81]
# [65, 61, 67, 72]
# [97, 95, 92, 88]

print(classMarks[0])  # [55, 63, 77, 81]
print(classMarks[0][2])  # 77
