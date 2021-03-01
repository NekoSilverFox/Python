
# 通过import语句导入一个包
# 注意：包名和变量命名一样，不应为数字开头
# import 模块1_猫


# 使用 `import 模块名1 as 模块别名` 为一个模块起别名
import 模块2_狗 as Dog  # 模块别名使用大驼峰
Dog.say_hello()


# 使用 `from 模块名1 import 工具名` 部分工具
from 模块1_猫 import say_hello
say_hello()


# 如果多个模块，存在同名的函数，那么后导入模块的函数会覆盖掉先导入的函数
# 所以可以再配合 as 起别名
from 模块1_猫 import tital as tital_cat
print(tital_cat)


# 使用 __file__ 可以查看文件目录
print(Dog.__file__)

# （了解） 使用 `from 模块名 import *` 可以一次性全部导入
from 模块1_猫 import *
print(tital)