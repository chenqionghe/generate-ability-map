import numpy as np
import matplotlib.pyplot as plt
import math
import matplotlib.colors as mcolors

# 导入中文
import matplotlib.font_manager as font_manager

font_dirs = ['./font']
font_files = font_manager.findSystemFonts(fontpaths=font_dirs)
font_list = font_manager.createFontList(font_files)
font_manager.fontManager.ttflist.extend(font_list)
plt.rcParams['font.family'] = 'SimHei'

# 启用主题
plt.style.use('ggplot')


# 获取极径范围
def get_range(data_list):
    max = min = 0
    for _, data in data_list.items():
        for v in data:
            if v < min:
                min = v
            if v > max:
                max = v
    return [min, max + 0.1]


# 生成能力分布图
def generate_ability_map(abilities, data_list, rows=3):
    min, max = get_range(data_list)

    # 根据能力项等分圆
    angles = np.linspace(0, 2 * np.pi, len(abilities), endpoint=False)
    angles = np.append(angles, angles[0])
    # 生成n个子图
    fg, axes = plt.subplots(math.ceil(len(data_list) / rows), rows, subplot_kw=dict(polar=True))
    # 打散为一维数组
    axes = axes.ravel()
    # 获取所有支持的颜色
    colors = list(mcolors.TABLEAU_COLORS)
    # 循环绘制
    i = 0
    for name, data in data_list.items():
        data = np.append(np.array(data), data[0])
        ax = axes[i]
        # 绘制线条
        ax.plot(angles, data, color=colors[i])
        # 填充颜色
        ax.fill(angles, data, alpha=0.7, color=colors[i])
        # 设置角度
        ax.set_xticks(angles)
        # 设置坐标轴名称
        ax.set_xticklabels(abilities)
        # 设置名称
        ax.set_title(name, size=10, color='black', position=(0.5, 0.4))
        # 设置极径范围
        ax.set_rmin(min)
        ax.set_rmax(max)
        i = i + 1
    plt.show()
