"""
元组和字典的拆包（知道）

* 在调用带有多值参数的函数时，如果希望：
  * 将一个 【元组变量】，直接传递给 `args`
  * 将一个 【字典变量】，直接传递给 `kwargs`
* 就可以使用 【拆包】，简化参数的传递，【拆包】 的方式是：
  * 在 【元组变量前】，增加 【一个】 `*`
  * 在 【字典变量前】，增加 【两个】 `*`
"""


def demo(*args, **kwargs):
    print(args)
    print(kwargs)


# 需要将一个元组变量/字典变量传递给函数对应的参数
gl_nums = (1, 2, 3)
gl_xiaoming = {"name": "小明", "age": 18}

# demo(gl_nums, gl_xiaoming)  # 不是我们想要的结果 【会把 num_tuple 和 xiaoming 作为元组传递个 args】 ((1, 2, 3), {'name': '小明', 'age': 18})
demo(*gl_nums, **gl_xiaoming)
# demo(**gl_xiaoming, *gl_nums) 不能调换顺序！！