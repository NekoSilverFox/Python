# 005 - 买苹果案例

price_str = input("请输入苹果的价格：")

weight_str = input("请输入苹果的重量：")

# 注意：两个字符串之间是不能直接使用乘法的
# money = price_str * weight_str

print("请支付：")
print(float(price_str) * float(weight_str))