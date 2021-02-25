# 024 - 缺省参数 - 指定函数缺省参数的默认值
"""
在参数后使用赋值语句，可以指定参数的缺省值
注意：
    必须保证带有默认值的缺省参数在【参数列表末尾】！！！
    错误 --> def demo(val1, val2=1, val3)
"""


def print_info(name, gender=True):
    gender_text = "Boy"
    if not gender:
        gender_text = "Girl"
    print("%s is %s" % (name, gender_text))


print_info("Fox")
print_info("Silverfox", False)

"""
注意：对于含有多个缺省参数的函数，需要指定参数名！！
"""


def many_default_argu(age, sex="M", marry=False):
    print("I am %d years old, sex is %s, marry is %s" % (age, sex, marry))


many_default_argu(17, marry=True)  # 具有多个缺省参数时，需要指定参数

num_list = [6, 4, 5]
num_list.sort(reverse=False)  # 具有多个缺省参数时，需要指定参数
print(num_list)  # [4, 5, 6]
