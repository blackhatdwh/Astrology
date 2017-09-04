import os, re
os.system('rm astro_sina.html')
os.system('curl http://astro.sina.com.cn/fate_day_Aries/ > astro_sina.html')
text = open('astro_sina.html', 'r').read()

zonghe_pattern = '(?<=综合运势</td>\n\t{7}<td><i class=").*(?=")'
zonghe = re.search(zonghe_pattern, text).group(0)
love_pattern = '(?<=爱情运</td>\n\t{7}<td><i class=").*(?=")'
love = re.search(love_pattern, text).group(0)
work_pattern = '(?<=工作运</td>\n\t{7}<td><i class=").*(?=")'
work = re.search(work_pattern, text).group(0)
fortune_pattern = '(?<=财运</td>\n\t{7}<td><i class=").*(?=")'
fortune = re.search(fortune_pattern, text).group(0)
health_pattern = '(?<=健康指数</td>\n\t{7}<td>).*(?=</td>)'
health = re.search(health_pattern, text).group(0)
crystal_pattern = '(?<=开运水晶</td>\n\t{7}<td>).*(?=</td>)'
crystal = re.search(crystal_pattern, text).group(0)
color_pattern = '(?<=幸运颜色</td>\n\t{7}<td>).*(?=</td>)'
color = re.search(color_pattern, text).group(0)
number_pattern = '(?<=幸运数字</td>\n\t{7}<td>).*(?=</td>)'
number = re.search(number_pattern, text).group(0)
person_pattern = '(?<=贵人星座</td>\n\t{7}<td>).*(?=</td>)'
person = re.search(person_pattern, text).group(0)
