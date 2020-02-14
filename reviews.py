data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count +=1  # count =count + 1
		if count % 100000 == 0:
			print(len(data))
print('档案数总共有', len(data), '笔资料')
print(data[0])

sum_len = 0
for d in data:  #把清单中的每一个都依次拿出来
	sum_len = sum_len + len(d) #把每一个长度加起来

print('average len', sum_len/len(data))

new = []  #建立新清单
for d in data:    #先写for loop去读取资料，行程字串
	if len(d)<100:
		new.append(d)
print('in total there are', len(new), 'reviews which lenth is less than 100')
print(new[0])


good = []
for d in data:
	if 'good' in d:
		good.append(d)
print('一共有', len(good),'提及到good' )
print(good[0])


#文字计数
wc = {}    # word_count
for d in data:
	words = d.split() # split里面设置空格符号则是以空格划分，若什么都没有，则连续空格就不会计入
	for word in words:
		if word in wc:   #不在可以用 not in
			wc[word] += 1  #当已经定义为word：1后，第二次遇见改为word：2
		else:
			wc[word] = 1  #新增新的key进字典，并定义为word:1



for word in wc:     #这里的word是字典里的key
	if wc[word] > 1000000:
		print(word, wc[word])   #wc[word]是word的值，word是关键字

print(len(wc))

while True:
	word = input('请问你想查询那个字？')
	if word == 'q':
		break
	if word in wc:
		print(word, '出现了', wc[word], '次')
	else:
		print('这个字没有哦')

print('感谢使用')



