row = 1

while row <= 9:

    col = 1

    while col <= row:

        # print('*', end="")
        print("%d*%d=%d" % (col, row, row * col), end="\t")

        col += 1

    # print('%d' % row)
    print("")

    row += 1
