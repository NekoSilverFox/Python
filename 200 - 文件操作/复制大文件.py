# 1. 打开文件
file_read = open("input", encoding="UTF-8")
file_write = open("output", "w", encoding="UTF-8")

# 2. 读、写
""" 
# 使用 while 读写
while True:
    # 读取一行内容
    text = file_read.readline()
    if not text:
        break
    file_write.write(text)
"""

# 使用 for 读写
for line in file_read.read():
    file_write.write(line)


# 3. 关闭文件
file_read.close()
file_write.close()