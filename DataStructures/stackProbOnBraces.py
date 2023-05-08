#Stack problem on balanced condition of braces
st = []
s = input()
bal = True
for char in s:
	if (char == '{' or char =='[' or char == '('):
		st.append(char)
	elif(char == '}' or char ==']' or char == ')'):
		if (len(st) == 0):
			bal = False
			break
	elif (char == '}'):
		if (len(st) and st.pop()!='{'):
			bal = False
			break
	elif (char == ']'):
		if (len(st) and st.pop()!='['):
			bal = False
			break
	elif (char == ')'):
		if (len(st) and st.pop()!='('):
			bal = False
			break
	else:
			bal = False
			break
if (bal == False or len(st)):
	print('Not balanced')
else:
	print('balanced')