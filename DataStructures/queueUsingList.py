# Queues using lists
queue = []
def enqueue():
	ele = int(input('Enter the element : '))
	queue.append(ele)
	print(queue)
def dequeue():
	if not queue:
		print('the Q is empty')
	else:
		e = queue.pop(0)
		print('element is removed', e)
def display():
		print(queue)
while True:
	print('select the operation 1.push  2.pop  3.quit 4.showQueue<')
	choice = (int(input()))
	if choice == 1:
		enqueue()
	elif choice == 2:
		dequeue()
	elif choice == 3:
		break 
	elif choice == 4:
		if not queue :
			print('queue is empty')
		else:
			print(queue)
	else:
		print( ' select the correct operation ')