ques = [['what is capital of india? a)New delhi  b)Hyderabad',['a']], ['where is charminar located? a)Hyderabad  b)Mumbai', ['a']]]
a = input('Hi enter your name : ')
print(f'Hi {a} welcome to quiz')
qno = 0
score = 0
rnge = len(ques)
while (qno < rnge):
	print(ques[qno][0])
	ans = input('enter your answer ')
	if (ans == ques[qno][1][0]):
		print('correct answer')
		qno += 1
		score += 1
		if(score>=0):
			print('your current score ',score)
		else:
			print('your current score', score)
	else:
		print('wrong answer')
		if(score==0):
			print('your current score', score)
		else:
		    score -= 1
		    print('your current score ',score)
		retry = input('do you want to retry? y/n')
		if (retry == 'n'):
			break
		elif(retry == 'y'):
			rnge += 1
else:
	print('you cleared all questions')
	print('your total score ', score)