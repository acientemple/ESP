s1 = input('输入去年成绩：')
s2 = input('输入今年成绩')
s3 = (int(s2) - int(s1)) / int(s2)
s4 = s3 * 100
print('{0}，去年成绩是{1}，今年成绩是{2}'.format('小明', int(s1), int(s2)))
if int(s1) >= int(s2):
    print('小明得加油啊，没什么进步！')
else:
    print('%s成绩提升的百分比是：%.2f%%' % ('小明', s4))

