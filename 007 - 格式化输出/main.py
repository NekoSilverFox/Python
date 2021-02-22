# 007 - 格式化输出

name = "Fox"
age = 17
print("My name is %s, now %d years old" % (name, age))

print("=" * 100)

student_num = 1
print("My student numbers is %06d" % student_num)  # 000001

print("=" * 100)

print("男女同学各占比 %.2f%%" % 50 * 10)  # 【重点】
print("---")
print("男女同学各占比 %.2f%%" % (50 * 10))  # 【重点】
