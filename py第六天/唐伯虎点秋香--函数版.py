# 定义一个列表，表示有哪些人
import random
person_list = [{"name":"张三","ph":10},{"name":"李四","ph":10}]

# 先让两个人掉血
drop_blood = random.randint(1,3)
person_list[0]["ph"] -= drop_blood
person_list[1]["ph"] -= drop_blood
print(person_list[0]["ph"])



