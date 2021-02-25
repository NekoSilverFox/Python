# 024 - 缺省参数 - 指定函数缺省参数的默认值

# 在参数后使用赋值语句，可以指定参数的缺省值
def print_info(name, gender=True):
    gender_text = "Boy"
    if not gender:
        gender_text = "Girl"
    print("%s is %s" % (name, gender_text))


print_info("Fox")
print_info("Silverfox", False)
