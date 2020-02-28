# 生成战力分布图

示例代码
```python
from tool import generate_ability_map

abilities = ['智力', '力量', '速度', '耐力', '能量', '技能']
super_heros = {
    '美国队长': [5, 4, 3, 4, 3, 7],
    '钢铁侠': [6, 3, 5, 5, 3, 3],
    '绿巨人': [6, 7, 3, 7, 1, 5],
    '蜘蛛侠': [5, 4, 5, 4, 2, 5],
    '灭霸': [7, 7, 7, 7, 7, 7],
    '雷神': [2, 5, 6, 7, 6, 6],
    '绯红女巫': [3, 3, 3, 3, 7, 3],
    '黑寡妇': [5, 3, 2, 3, 3, 7],
    '鹰眼': [5, 3, 3, 2, 2, 7],
}
generate_ability_map(abilities, super_heros)
```
运行结果
![](.readme/super_heros)