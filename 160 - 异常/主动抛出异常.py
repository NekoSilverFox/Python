"""
### 4.2 抛出异常

* `Python` 中提供了一个 `Exception` **异常类**
* 在开发时，如果满足 **特定业务需求时**，希望 **抛出异常**，可以：
  1. **创建** 一个 `Exception` 的 **对象**
  2. 使用 `raise` 关键字抛出 **异常对象**
"""

def input_passwd():
    # 1. 提示用户输入密码
    pwd = input("请输入密码：")

    # 2. 如果密码长度 >=8 ，返回用户输入的密码
    if len(pwd) >= 8:
        return pwd

    # 如果 <8 抛出异常
    exc = Exception("密码长度不够")  # 创建异常变量
    raise exc  # 主动抛出异常

try:
    print(input_passwd())
except Exception as result:
    print("捕获了异常：%s" % result)