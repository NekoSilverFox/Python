# 发布模块
from distutils.core import setup

# 多值字典参数
setup(name="message",  # 包名
      version="1.0",  # 版本
      description="nekosilverfox's 发送和接收消息模块",  # 描述信息
      long_description="完整的发送和接收消息模块",  # 完整描述信息
      author="silverfox",  # 作者
      author_email="666@666.com",  # 作者邮箱
      url="www.666.com",  # 主页
      py_modules=["message.send_message",
                  "message.receive_message"])