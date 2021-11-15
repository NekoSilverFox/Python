train_dir = 'G:\\tensorflow_project\\cat_and_dog\\data\\train'

logs_train_dir = 'G:\\tensorflow_project\\cat_and_dog\\logs'

# 1. 打开文件
file = open(train_dir, "r+", encoding="UTF-8")  # 区分大小写

# 2. 读取文件内容
text = file.read()
print(text)

# 写入文件
file.write("123")

# 3. 关闭文件
file.close()


print("-" * 50)


# 1. 打开文件
file = open("input", "r+", encoding="UTF-8")  # 区分大小写

while True:
    # 2. 读取一行内容
    text = file.readline()
    # 判断是否读取到内容
    if not text:
        break
    print(text)
    
# 3. 关闭文件
file.close()
