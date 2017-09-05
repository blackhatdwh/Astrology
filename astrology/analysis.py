import json
text = open('raw_result.txt', 'r').read()
data = json.loads(text)

xingzuo = ('ARIES', 'TAURUS', 'GEMINI', 'CANCER', 'LEO', 'VIRGO', 'LIBRA', 'SCORPIO', 'SAGITTARIUS', 'CAPRICORN', 'AQUARIUS', 'PISCES')
source = ('第一星座', '新浪星座', '腾讯星座', '星座屋')
aspects = ('综合运势', '爱情运势', '工作运势', '财运运势', '健康运势')

def Predict(xz):
    predict = '%s\n'%xz
    # 综合，爱情，工作，财运，健康
    for a in aspects:
        max = 0
        max_source = ''
        for s in source:
            if int(data[s][xz][a][:-1]) > max:
                max = int(data[s][xz][a][:-1])
                max_source = s
        predict += '%s：%s%%（%s）\n'%(a, max, max_source)
    # 数字
    predict += '幸运数字：'
    for s in source:
        predict += '%s（%s） '%(data[s][xz]['幸运数字'], s)
    predict += '\n'
    # 颜色
    predict += '幸运颜色：'
    for s in source:
        predict += '%s（%s） '%(data[s][xz]['幸运颜色'], s)
    predict += '\n'
    # 贵人
    predict += '贵人星座：'
    for s in source:
        predict += '%s（%s） '%(data[s][xz]['贵人星座'], s)
    predict += '\n'
    # 开运水晶
    predict += '开运水晶：%s（新浪星座）\n'%data['新浪星座'][xz]['开运水晶']
    # 今日提醒
    predict += '今日提醒：\n'
    for s in source:
        predict += '（%s）%s\n'%(s, data[s][xz]['今日提醒'])

    print(predict)


for xz in xingzuo:
    Predict(xz)
