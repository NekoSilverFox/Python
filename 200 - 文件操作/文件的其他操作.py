# 针对文件的其他操作，需要导入 os 模块
# 具体替他函数，请见笔记
import os

# 重命名文件
# os.rename("output - 副本", "output2")

# 删除文件
# os.remove("output2")

# 查看当前目录内容
print(os.listdir("."))

# 判断是否为目录
print(os.path.isdir("output"))
print(os.path.isdir(".idea"))

# 生成目录
# os.mkdir("test")

# 删除目录
os.rmdir("test")
