import json

# 打开 JSON 文件并加载数据1
with open('price.json', 'r') as json_file:
    data = json.load(json_file)

# 初始化总和变量
total_count = 0

# 遍历列表中的对象并计算 count 总和
for item in data:
    if 'count' in item:  # 检查对象中是否有 count 字段
        total_count += item['count']

# 打印 count 总和
print(f'Total Count: {total_count}')