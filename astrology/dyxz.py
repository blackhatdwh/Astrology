import os, re
os.system('curl http://www.d1xz.net/yunshi/today/Aries/ > astro_dyxz.html')
text = open('astro_dyxz.html', 'r').read()

love_pattern = '(?<=爱情).*?(?=")'
love = re.search(love_pattern, text).group(0)
fortune_pattern = '(?<=财运).*?(?=")'
fortune = re.search(fortune_pattern, text).group(0)
health_pattern = '(?<=健康).*?(?=")'
health = re.search(health_pattern, text).group(0)
work_pattern = '(?<=工作).*?(?=")'
work = re.search(work_pattern, text).group(0)
zonghe_pattern = '(?<=综合).*?(?=")'
zonghe = re.search(zonghe_pattern, text).group(0)
color_pattern = '(?<="quan_yuan"><li><div class="words_t">).*?(?=</div>)'
color = re.search(color_pattern, text).group(0)
number_pattern = '(?<=幸运颜色</div></li><li><div class="words_t">).*?(?=</div>)'
number = re.search(number_pattern, text).group(0)
person_pattern = '(?<=幸运数字</div></li><li><div class="words_t">).*?(?=</div>)'
person = re.search(person_pattern, text).group(0)
comment_pattern = '(?<=速配星座</div></li></ul><div class="txt"><p>).*?(?=</p>)'
comment = re.search(comment_pattern, text).group(0)


os.system('rm astro_dyxz.html')
f = open('result.txt', 'a')
f.write('\n第一星座：\n')
f.write('综合运势：%s\n' %zonghe)
f.write('工作运势：%s\n' %work)
f.write('爱情运势：%s\n' %love)
f.write('财运运势：%s\n' %fortune)
f.write('健康运势：%s\n' %health)
f.write('幸运颜色：%s\n' %color)
f.write('幸运数字：%s\n' %number)
f.write('贵人星座：%s\n' %person)
f.write('今日提醒：%s\n' %comment)
f.close()
