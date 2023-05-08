# STACK using lists
stack = []
def push():
	ele = int(input('Enter the element : '))
	stack.append(ele)
	print(stack)
def pop_ele():
	if not stack:
		print('the stack is empty')
	else:
		e = stack.pop()
		print('element is removed')
		print(stack)
while True:
	print('select the operation 1.push  2.pop  3.quit 4.showStack')
	choice = (int(input()))
	if choice == 1:
		push()
	elif choice == 2:
		pop_ele()
	elif choice == 3:
		break 
	elif choice == 4:
		if not stack :
			print('stack is empty')
		else:
			print(stack)
	else:
		print( ' select the correct operation ')