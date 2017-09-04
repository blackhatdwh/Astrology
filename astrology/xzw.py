import os, re
os.system('rm astro_xzw.html')
os.system('curl http://www.xzw.com/fortune/aries/ > astro_xzw.html')
text = open('astro_xzw.html', 'r').read()

zonghe_pattern = '(?<=综合运势：</label><span class="star_m star_blue"><em style=" width:).*?(?=px)'
zonghe = re.search(zonghe_pattern, text).group(0)
love_pattern = '(?<=爱情运势：</label><span class="star_m star_blue"><em style=" width:).*?(?=px)'
love = re.search(love_pattern, text).group(0)
work_pattern = '(?<=事业学业：</label><span class="star_m star_blue"><em style=" width:).*?(?=px)'
work = re.search(work_pattern, text).group(0)
fortune_pattern = '(?<=财富运势：</label><span class="star_m star_blue"><em style=" width:).*?(?=px)'
fortune = re.search(fortune_pattern, text).group(0)
health_pattern = '(?<=健康指数：</label>).*?(?=</li>)'
health = re.search(health_pattern, text).group(0)
color_pattern = '(?<=幸运颜色：</label>).*?(?=</li>)'
color = re.search(color_pattern, text).group(0)
number_pattern = '(?<=幸运数字：</label>).*?(?=</li>)'
number = re.search(number_pattern, text).group(0)
person_pattern = '(?<=速配星座：</label>).*?(?=</li>)'
person = re.search(person_pattern, text).group(0)
