```python
####################
# 国家
####################

# ctry: 国家名称
# -> force ctry所属势力
def force_of(ctry):
    pass

# ctry: 国家名称
# force: 势力
# diff: 修正值
# () ctry的force的影响力增加diff
def update_inf(ctry, force, diff):
    pass

# ctry: 国家名称
# force: 势力
# value: 值
# () ctry的force的影响力设置为value
def set_inf(ctry, force, value):
    pass

# ctry: 国家名称
# force: 势力
# -> int ctry的force的影响力
def get_inf(ctry, force):
    pass

# ctry: 国家名称
# -> bool force是否为战场国
def is_battle(ctry):
    pass

# ctry: 国家名称
# -> [region] ctry所在的区域
def region_of(ctry):
    pass

# ctry: 国家名称
# -> [ctry] ctry的邻国
def neighbour(ctry):
    pass

# ctry: 国家名称
# force: 势力
# -> bool ctry是否临近force的超级大国
def neighbour_of_force(ctry, force):
    pass

####################
# 区域
####################

# reg: 区域名称
# -> [region] reg的子区域
def sub_region(reg):
    pass

# reg: 区域名称
# -> [ctry] reg里的国家（包括子区域）
def sub_ctry(reg):
    pass

# reg: 区域名称
# force: 势力
# -> bool force在reg是否存在
def exist(reg, force):
    pass

# reg: 区域名称
# force: 势力
# -> bool force在reg是否支配
def dominate(reg, force):
    pass

# reg: 区域名称
# force: 势力
# -> bool force在reg是否控制
def control(reg, force):
    pass

# force: 势力
# diff: 修正值
# () force获得diff的分数
def update_vp(force, diff):
    pass

# -> int 骰子1~6的点数
def roll():
    pass
####################
# 核危机、军事行动指数
####################

# -> int 核危机指数
def get_nuclear():
    pass

# diff: 修正值
# () 核危机指数增加diff
def update_nuclear(diff):
    pass

# force: 势力
# -> int force的军事行动指数
def get_military(force):
    pass

# force: 势力
# diff: 修正值
# () force的军事行动指数增加diff
def update_military(force, diff):
    pass

# force: 势力
# () 重置force的军事行动指数
def reset_military(force):
    pass

####################
# 太空竞赛
####################

# force: 势力
# -> int force的太空竞赛进度
def get_space(force):
    pass

# force: 势力
# () force的太空竞赛进度前进1
def inc_space(force):
    pass

####################
# 回合、行动轮
####################

# -> int 回合数
def get_round():
    pass

# () 回合数加1
def inc_round():
	pass

# -> (int, force) 当前行动轮（不包含头条）和势力
def get_turn():
    pass

# () 前移一个行动轮与势力的组合
def inc_turn():
    pass

# round: 回合数
# -> int 行动轮的数量（不包含头条）
def num_turns(round):
    pass
```

