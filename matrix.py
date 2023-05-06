li = [[10, 5, 9], [6, 2, 3],[15, 14, 17]]
mli = [[ ],[ ],[ ]]
print('upper diagonals')
for i in range(len(li)):
	for j in range(len(li[i])):
		if (i < j):
			print(li[i][j], end = ' ')
			mli[i].append(li[i][j])
		else:
			print(' ', end=' ')
			mli[i].append(' ')
	print()
print('diagonals')
for i in range(len(li)):
	for j in range(len(li[i])):
		if(i == j):
			print(li[i][j], end=' ')
			mli[i].append(li[i][j])
		else:
			print(' ', end=' ')
			mli.append(' ')
	print()
print('lower diagonals')
for i in range(len(li)):
	for j in range(len(li[i])):
		if(i > j):
			print(li[i][j], end=' ')
			mli[i].append(li[i][j])
		else:
			print(' ', end =' ')
			mli[i].append(' ')
	print()