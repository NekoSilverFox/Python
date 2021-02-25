poem = ["沁园春 · 雪",
        "-- 毛",
        "       北国风光",
        "千里冰封",
        "万里      雪飘",
        "望长城内\t外",
        "惟\n余莽莽"]

for str_poem in poem:
    # 先使用 `strip` 方法去除空白字符
    # 再使用 `center` 方法显示文本
    # 【重点】trip()只能删除头或尾的空字符，中间的不行
    print("|%s|" % str_poem.strip().center(10, "　"))  # strip("指定字符") strip 中也可以指定字符
