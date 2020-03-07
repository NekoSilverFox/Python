print('---------------欢迎使用SilverFox名片创建系统---------------')
name = input('请输入您的名字：')
age = float(input('请输入您的年龄：'))
place = input('请输入您所在的地区：')
tel = input('请输入您的电话：')

print('请确认信息：')
print('姓名：%s' % name)
print('年龄；%.0f' % age)
print('所在地；%s' % place)
print('电话：%s' % tel)

put = str(input('如果信息正确，请输入‘y’创建名片'))

if put == 'y':
    print('--------------------已为您创建名片--------------------')
    print('姓名：%s' % name)
    print('年龄；%.0f' % age)
    print('所在地；%s' % place)
    print('电话：%s' % tel)
    print('----------------------------------------------------')
else:
    error = input('请输入错误信息')


