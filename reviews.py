data=[]
count = 0
with open('reviews.txt', 'r') as f:
	for line in f:
		data.append(line)
		count==1  # count =count + 1
		if count % 2 == 0:
			print(len(data))
print(len(data))
print(data[0])

sum_len = 0
for d in data:  #把清单中的每一个都依次拿出来
	sum_len = sum_len + len(d) #把每一个长度加起来

print('average len', sum_len/len(data))