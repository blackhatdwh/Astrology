import os, re
xingzuo = ('Aries', 'Taurus', 'Gemini', 'Cancer', 'Leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces')
f = open('raw_result.txt', 'a')
f.write('"星座屋":{')
for xz in xingzuo:
    os.system('curl http://www.xzw.com/fortune/%s/ > %s_xzw.html'%(xz, xz))
    text = open('%s_xzw.html'%xz, 'r').read()
    
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
    comment_pattern_1 = '(?<=短评：</label>).*?(?=</li>)'
    comment_1 = re.search(comment_pattern_1, text).group(0)
    comment_pattern_2 = '(?<=综合运势</strong><span>).*?(?=</span>)'
    comment_2 = re.search(comment_pattern_2, text).group(0)
    comment_pattern_3 = '(?<=爱情运势</strong><span>).*?(?=</span>)'
    comment_3 = re.search(comment_pattern_3, text).group(0)
    comment_pattern_4 = '(?<=事业学业</strong><span>).*?(?=</span>)'
    comment_4 = re.search(comment_pattern_4, text).group(0)
    comment_pattern_5 = '(?<=财富运势</strong><span>).*?(?=</span>)'
    comment_5 = re.search(comment_pattern_5, text).group(0)
    comment_pattern_6 = '(?<=健康运势</strong><span>).*?(?=</span>)'
    comment_6 = re.search(comment_pattern_6, text).group(0)
    comment = '短评：%s\\n综合运势：%s\\n爱情运势：%s\\n事业学业：%s\\n财富运势：%s\\n健康运势：%s\\n' % (comment_1, comment_2, comment_3, comment_4, comment_5, comment_6)
    
    def convert(val):
        return str(int(int(val)/16*20)) + '%'
    zonghe = convert(zonghe)
    work = convert(work)
    love = convert(love)
    fortune = convert(fortune)
    
    os.system('rm %s_xzw.html'%xz)
    
    f.write('"%s":{'%xz.upper())
    f.write('"综合运势":"%s",' %zonghe)
    f.write('"工作运势":"%s",' %work)
    f.write('"爱情运势":"%s",' %love)
    f.write('"财运运势":"%s",' %fortune)
    f.write('"健康运势":"%s",' %health)
    f.write('"幸运颜色":"%s",' %color)
    f.write('"幸运数字":"%s",' %number)
    f.write('"贵人星座":"%s",' %person)
    f.write('"每日提醒":"%s"' %comment)
    if xz != 'Pisces':
        f.write('},')
    else:
        f.write('}}')

f.close()
