import os, re
xingzuo = ('Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces')
f = open('raw_result.txt', 'a')
f.write('"第一星座":{')
for xz in xingzuo:
    os.system('curl http://www.d1xz.net/yunshi/today/%s/ > %s_dyxz.html'%(xz, xz))
    text = open('%s_dyxz.html'%xz, 'r').read()
    
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
    
    
    os.system('rm %s_dyxz.html'%xz)
    f.write('"%s":{'%xz.upper())
    f.write('"综合运势":"%s",' %zonghe)
    f.write('"工作运势":"%s",' %work)
    f.write('"爱情运势":"%s",' %love)
    f.write('"财运运势":"%s",' %fortune)
    f.write('"健康运势":"%s",' %health)
    f.write('"幸运颜色":"%s",' %color)
    f.write('"幸运数字":"%s",' %number)
    f.write('"贵人星座":"%s",' %person)
    f.write('"今日提醒":"%s"' %comment)
    if xz != 'Pisces':
        f.write('},')
    else:
        f.write('}}')
f.write(',')
f.close()
