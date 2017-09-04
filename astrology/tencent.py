import os, re
os.system('rm pre_astro_tencent.html')
os.system('curl http://astro.fashion.qq.com/ | iconv -f gbk > pre_astro_tencent.html')
text = open('pre_astro_tencent.html', 'r').read()
target_pattern = '(<h3>白羊座.*?href=")(.*?)(?=")'
target = re.search(target_pattern, text, re.DOTALL).group(2)
os.system('curl %s | iconv -f gbk > astro_tencent.html' %target)
text = open('astro_tencent.html', 'r').read()

person_pattern = '(?<=贵人星座：).*(?=<)'
person = re.search(person_pattern, text).group(0)
color_pattern = '(?<=幸运颜色：).*(?=<)'
color = re.search(color_pattern, text).group(0)
number_pattern = '(?<=幸运数字：).*(?=<)'
number = re.search(number_pattern, text).group(0)
health_pattern = '(?<=健康运势：).*(?=<)'
health = re.search(health_pattern, text).group(0)

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

print(zonghe)
print(love)
print(work)
print(fortune)
