import os
os.system('rm raw_result.txt')
f = open('raw_result.txt', 'a')
f.write('{')
f.close()

os.system('python3 dyxz.py;')
os.system('python3 sina.py;')
os.system('python3 tencent.py;')
os.system('python3 xzw.py')

f = open('raw_result.txt', 'a')
f.write('}')
f.close()
