length = float(input('length of the room in meter: ')) # 长
width = float(input('width of the room in meter: ')) # 宽
cost_per_chi = float(input('cost per square chi: ')) # 价格
area_meter = length * width # 计算面积
area_chi = area_meter * 9 # 单位是平方尺
total_cost = area_chi * cost_per_chi
print('The area is', area_meter, 'square meter.') # 面积200.0平方米。
print('Theat is ',area_chi, 'square chi.') # 即1800.0平方尺。
print('Which will cost', total_cost) # 这将花费 9000.0