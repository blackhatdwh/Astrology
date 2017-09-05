import os, re
xingzuo = (('Aries','白羊座'), ('Taurus','金牛座'), ('Gemini','双子座'), ('Cancer','巨蟹座'), ('Leo','狮子座'), ('Virgo','处女座'), ('Libra','天秤座'), ('Scorpio','天蝎座'), ('Sagittarius','射手座'), ('Capricorn','摩羯座'), ('Aquarius','水瓶座'), ('Pisces','双鱼座'))
f = open('raw_result.txt', 'a')
f.write('---start---\n')
f.write('腾讯星座\n')
os.system('curl http://astro.fashion.qq.com/ | iconv -f gbk > pre_astro_tencent.html')
pre_text = open('pre_astro_tencent.html', 'r').read()
os.system('rm pre_astro_tencent.html')
for xz in xingzuo:
    target_pattern = '(<h3>%s.*?href=")(.*?)(?=")'%xz[1]
    target = re.search(target_pattern, pre_text, re.DOTALL).group(2)
    os.system('curl %s | iconv -f gbk > %s_tencent.html' %(target, xz[0]))
    text = open('%s_tencent.html'%xz[0], 'r').read()
    
    person_pattern = '(?<=贵人星座：).*(?=<)'
    person = re.search(person_pattern, text).group(0)
    color_pattern = '(?<=幸运颜色：).*(?=<)'
    color = re.search(color_pattern, text).group(0)
    number_pattern = '(?<=幸运数字：).*(?=<)'
    number = re.search(number_pattern, text).group(0)
    health_pattern = '(?<=健康运势：).*(?=<)'
    health = re.search(health_pattern, text).group(0)
    comment_pattern = '(?<=maintext">).*(?=</p>)'
    comment = re.search(comment_pattern, text).group(0)
    
    zonghe_pattern = '(综合运势：.*?)<img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" />'
    zonghe = ''
    search_obj = re.search(zonghe_pattern, text, re.DOTALL)
    for i in range(2, 7):
        zonghe += search_obj.group(i)
    
    love_pattern = '(爱情运势：.*?)<img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" />'
    love = ''
    search_obj = re.search(love_pattern, text, re.DOTALL)
    for i in range(2, 7):
        love += search_obj.group(i)
    
    work_pattern = '(综合运势：.*?)<img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" />'
    work = ''
    search_obj = re.search(work_pattern, text, re.DOTALL)
    for i in range(2, 7):
        work += search_obj.group(i)
    
    fortune_pattern = '(财运运势：.*?)<img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" /><img src="http://mat1.gtimg.com/astro/2014zlk/jrys/xing(\d).jpg" />'
    fortune = ''
    search_obj = re.search(fortune_pattern, text, re.DOTALL)
    for i in range(2, 7):
        fortune += search_obj.group(i)
    
    def convert(val):
        if val == '12222':
            return '20%'
        if val == '11222':
            return '40%'
        if val == '11122':
            return '60%'
        if val == '11112':
            return '80%'
        if val == '11111':
            return '100%'
    os.system('rm %s_tencent.html'%xz[0])
    
    zonghe = convert(zonghe)
    work = convert(work)
    love = convert(love)
    fortune = convert(fortune)
    
    f.write('%s\n'%xz[0].upper())
    f.write('综合运势：%s\n' %zonghe)
    f.write('工作运势：%s\n' %work)
    f.write('爱情运势：%s\n' %love)
    f.write('财运运势：%s\n' %fortune)
    f.write('健康运势：%s\n' %health)
    f.write('幸运颜色：%s\n' %color)
    f.write('幸运数字：%s\n' %number)
    f.write('贵人星座：%s\n' %person)
    f.write('今日提醒：%s\n' %comment)
f.write('---end---\n')
f.close()
