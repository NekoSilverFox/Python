"""
    包是包含多个模块的特殊目录
    目录下有一个特殊的文件 __init__.py
    包名的命名方式和变量名一样，使用小写字母 + `_`
    要在外界使用 **包** 中的模块，需要在 `__init__.py` 中指定 **对外界提供的模块列表**

    使用 `import 包名` 可以一次性导入包中的所有模块

"""
import message

message.send_msg.seng_msg("XXXXXXXXXX")
message.receive_msg.receive_msg()