lis = [0, 2, 0, 3, 4, 0, 5, 6, 0]
for i in range(len(lis)):
	for j in range(i, len(lis)):
		if (lis[i] == 0):
			pass;
		else:
			if lis[j] == 0:
				lis[i], lis[j]= lis[j], lis[i]
print(lis)