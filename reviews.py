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