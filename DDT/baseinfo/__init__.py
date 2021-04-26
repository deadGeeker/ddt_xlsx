from xlrd import open_workbook


# exlce基本操作方法如下
# # 打开exlce表格，参数是文件路径
# data = xlrd.open_workbook('test.xlsx')
# # table = data.sheets()[0]           #  通过索引顺序获取
# # table = data.sheet_by_index(0)     #  通过索引顺序获取
# table = data.sheet_by_name(u'Sheet1')  # 通过名称获取
# nrows = table.nrows  # 获取总行数
# ncols = table.ncols  # 获取总列数
# #　获取一行或一列的值，参数是第几行
# print table.row_values(0)  # 获取第一行值
# print table.col_values(0)  # 获取第一列值

def read_xlsx(filename):
    x_data = []
    y_data = []
    wb = open_workbook(str(filename))
    for s in wb.sheets():
        for row in range(s.nrows):
            values = []
            for col in range(s.ncols):
                values.append(s.cell(row, col).value)
            x_data.append(values[0])
            y_data.append(values[1])
    return x_data, y_data


x, y = read_xlsx("baseinfo/test.xlsx")
# print(x, y)
data = []
temp = {"username": None, "passwd": None}
for i in range(1, len(x)):
    temp["username"] = x[i]
    temp["passwd"] = y[i]
    data.append(temp)

# data = [{"username": "Ray", "pwd": "123456"},
#         {"username": "Stephen", "pwd": "abcdefg"},
#         {"username": "Kobe", "pwd": "abc123"}]
# # print(data)
