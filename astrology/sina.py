import os, re, random
xingzuo = ('Aries', 'Taurus', 'Gemini', 'Cancer', 'leo', 'Virgo', 'Libra', 'Scorpio', 'Sagittarius', 'Capricorn', 'Aquarius', 'Pisces')
f = open('raw_result.txt', 'a')
f.write('"新浪星座":{')
for xz in xingzuo:
    os.system('curl http://astro.sina.com.cn/fate_day_%s/ > %s_sina.html'%(xz, xz))
    text = open('%s_sina.html'%xz, 'r').read()
    
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
    comment_pattern = '((?<=今日提醒：).*?(?=</p>)).*(去做：.*?(?=</p>)).*(别做：.*?(?=</p>)).*?((?<=　　).*?(?=</p>))'
    comment_obj = re.search(comment_pattern, text, re.DOTALL)
    comment = ''
    for i in range(1, 5):
        comment = comment +  comment_obj.group(i) + '\\n'
    
    
    os.system('rm %s_sina.html'%xz)
    def convert(val):
        if val == 'Qing':
            return str(80+random.randint(-20, 20)) + '%'
        if val == 'Yin':
            return str(40+random.randint(-20, 20)) + '%'
        if val == 'DuoYun':
            return str(60+random.randint(-20, 20)) + '%'
        if val == 'ZhenYu':
            return '阵雨'
        if val == 'XiaoYu':
            return '小雨'
        if val == 'ZhongYu':
            return '中雨'
        if val == 'DaYu':
            return '大雨'
        if val == 'BaoYu':
            return '暴雨'
        if val == 'LeiDian':
            return '雷电'
        if val == 'LeiZhenYu':
            return '雷阵雨'
        if val == 'XiaoXue':
            return '小雪'
        if val == 'ZhongXue':
            return '中雪'
        if val == 'DaXue':
            return '大雪'
        if val == 'YuJiaXue':
            return '雨夹雪'
        if val == 'Feng':
            return '风'
        if val == 'Mai':
            return '霾'
    zonghe = convert(zonghe)
    work = convert(work)
    love = convert(love)
    fortune = convert(fortune)
    f.write('"%s":{'%xz.upper())
    f.write('"综合运势":"%s",' %zonghe)
    f.write('"工作运势":"%s",' %work)
    f.write('"爱情运势":"%s",' %love)
    f.write('"财运运势":"%s",' %fortune)
    f.write('"健康运势":"%s",' %health)
    f.write('"幸运颜色":"%s",' %color)
    f.write('"幸运数字":"%s",' %number)
    f.write('"贵人星座":"%s",' %person)
    f.write('"开运水晶":"%s",' %crystal)
    f.write('"今日提醒":"%s"' %comment)
    if xz != 'Pisces':
        f.write('},')
    else:
        f.write('}}')
f.write(',')
f.close()
