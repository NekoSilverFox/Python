# while 循环

i = 1
while i <= 5:
    print("第%d次循环，Hello Python" % i)
    i = i + 1
print("循环结束 i = %d" % i)

print("=" * 50)

result = 0
i = 0
while i <= 100:
    if i % 2 == 0:
        print(i)
        result = result + i
    i += 1
print("循环结束，100内整数的和 结果为：%d" % result)
