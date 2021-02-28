# 类方法

"""
* 类方法需要用 **修饰器** `@classmethod` 来标识，**告诉解释器这是一个类方法**
* 类方法的 **第一个参数** 应该是 `cls`
  * 由 **哪一个类** 调用的方法，方法内的 `cls` 就是 **哪一个类的引用**
  * 这个参数和 **实例方法** 的第一个参数是 `self` 类似
  * **提示** 使用其他名称也可以，不过习惯使用 `cls`

3. 通过 **类名.** 调用 **类方法**，**调用方法时**，不需要传递 `cls` 参数
4. **在方法内部**
   * 可以通过 `cls.` **访问类的属性**
   * 也可以通过 `cls.` **调用其他的类方法**
"""

class Tool(object):

    count = 0

    def __init__(self, name):
        self.name = name
        Tool.count += 1

# 要使用 classmethod 修饰器
    @classmethod
    def show_tool_count(cls):
        print("目前有 %d 个工具" % cls.count)  # 注意要使用 cls.name 或 cls.count，而不是 self.name


tool1 = Tool("AXE")
Tool.show_tool_count()
