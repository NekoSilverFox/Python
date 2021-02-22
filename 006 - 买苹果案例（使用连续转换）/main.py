# 006 - 买苹果案例（使用连续转换）

price = float(input("请输入苹果的价格："))

weight = float(input("请输入苹果的重量："))

money = price * weight

print("苹果单价 `%.3f` 元／斤，购买了 `%f` 斤，需要支付 `%f` 元" % (price, weight, money))