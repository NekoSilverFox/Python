# 1. 打开文件
file_read = open("input", encoding="UTF-8")
file_write = open("output", "w", encoding="UTF-8")

# 2. 读、写
text = file_read.read()
file_write.write(text)

# 3. 关闭文件
file_read.close()
file_write.close()
