import color as cl
import emojizz as em


def setup():
	print(cl.gold+'\n\n\nCodo Sapien seems empty, starting setup. . . \n\n\n'+em.load)
	print(cl.blue+'\n\nEnter your name:')
	name = input()
	print('Enter Super User email:')
	ename = input()
	print('Enter Super User password:')
	password  = input()
	fp = open('files/Admin.txt','w')
	fp.write(ename+';'+password)
	fp.close()
	fp = open('files/User.txt','w')
	fp.write(name+';'+ename+';'+'0'+';'+'0'+';'+'\n')
	fp.close()
	print('\n\nSubjects available: \n1. Python\n2. JAVA\n3. JavaScript\n4. C/C++\n\n'+cl.reset)
	while(True):
		try:
			print(cl.blue+'\n\n\nEnter Number of questions you want to add in Python:'+cl.reset)
			qs = int(input())
			if qs>10 or qs<5:
				print(cl.red+'Enter a atleast 5 questions and atmost 10 questions in this section'+cl.reset)
			else:
				for i in range(qs):
					while(True):
						print(cl.blue+'Enter difficulty level: Easy(1), Medium(2), Hard(3)'+cl.reset)
						try:
							diff = int(input())
							if diff<=3 and diff>=1:
								break
							else:
								print(cl.red+'Wrong input.'+cl.reset+em.w_i)
						except ValueError:
							print(cl.red+'try again..'+cl.reset+em.w_i)
					while(True):
						print('\n\n\nEnter Qs',i+1)
						qs = input()
						print('\nEnter option','a.')
						a = input()
						print('\nEnter option','b.')
						b = input()
						print('\nEnter option','c.')
						c = input()
						print('\nEnter option','d.')
						d = input()
						print('\nEnter Correct Option:')
						ans = input()
						if ans not in 'abcd':
							print(cl.red+'wrong Format. Try again.'+cl.reset+em.w_i)
							continue
						if qs == '' or a == '' or b == '' or c == '' or d == '' or ans == '':
							print(cl.red+'Input cannot be empty'+cl.reset+em.w_i)
							continue
						elif ans in 'abcd':
							fp = open('files/Python.txt','a')
							fp.write(str(diff)+';'+qs+';'+a+';'+b+';'+c+';'+d+';'+ans+';'+'\n')
							fp.close()
							break
				break
		except ValueError:
			print(cl.red+'Try Again'+cl.reset+em.w_i)

	while(True):
		try:
			print(cl.blue+'\n\n\nEnter Number of questions you want to add in JAVA:'+cl.reset)
			qs = int(input())
			if qs>10 or qs<5:
				print(cl.red+'Enter a atleast 5 questions and atmost 10 questions in this section'+cl.reset+em.w_i)
			else:
				for i in range(qs):
					while(True):
						print(cl.blue+'Enter difficulty level: Easy(1), Medium(2), Hard(3)'+cl.reset)
						try:
							diff = int(input())
							if diff<=3 and diff>=1:
								break
							else:
								print(cl.red+'Wrong input.'+cl.reset+em.w_i)
						except ValueError:
							print(cl.red+'try again..'+cl.reset+em.w_i)
					while(True):
						print(cl.blue+'Enter Qs',i+1)
						qs = input()
						print('Enter option','a.')
						a = input()
						print('Enter option','b.')
						b = input()
						print('Enter option','c.')
						c = input()
						print('Enter option','d.')
						d = input()
						print('Enter Correct Option:'+cl.reset)
						ans = input()
						if ans not in 'abcd':
							print(cl.red+'wrong Format. Try again.'+cl.reset+em.w_i)
							continue
						if qs == '' or a == '' or b == '' or c == '' or d == '' or ans == '':
							continue
						elif ans in 'abcd':
							fp = open('files/JAVA.txt','a')
							fp.write(str(diff)+';'+qs+';'+a+';'+b+';'+c+';'+d+';'+ans+';'+'\n')
							fp.close()
							break
				break
		except ValueError:
			print(cl.red+'Try Again'+cl.reset+em.w_i)
	while(True):
		try:
			print(cl.blue+'\n\n\nEnter Number of questions you want to add in JavaScript:'+cl.reset)
			qs = int(input())
			if qs>10 or qs<5:
				print(cl.red+'Enter a atleast 5 questions and atmost 10 questions in this section'+cl.reset+em.w_i)
			else:
				for i in range(qs):
					while(True):
						print(cl.blue+'Enter difficulty level: Easy(1), Medium(2), Hard(3)'+cl.reset)
						try:
							diff = int(input())
							if diff<=3 and diff>=1:
								break
							else:
								print(cl.red+'Wrong input.'+cl.reset+em.w_i)
						except ValueError:
							print(cl.red+'try again..'+cl.reset+em.w_i)
					while(True):
						print(cl.blue+'Enter Qs',i+1)
						qs = input()
						print('Enter option','a.')
						a = input()
						print('Enter option','b.')
						b = input()
						print('Enter option','c.')
						c = input()
						print('Enter option','d.')
						d = input()
						print('Enter Correct Option:'+cl.reset)
						ans = input()
						if ans not in 'abcd':
							print(cl.red+'wrong Format. Try again.')
							continue
						if qs == '' or a == '' or b == '' or c == '' or d == '' or ans == '':
							continue
						elif ans in 'abcd':
							fp = open('files/JavaScript.txt','a')
							fp.write(str(diff)+';'+qs+';'+a+';'+b+';'+c+';'+d+';'+ans+';'+'\n')
							fp.close()
							break
				break
		except ValueError:
			print(cl.red+'Try Again'+cl.reset+em.w_i)
	while(True):
		try:
			print(cl.blue+'\n\n\nEnter Number of questions you want to add in C/C++:'+cl.reset)
			qs = int(input())
			if qs>10 or qs<5:
				print(cl.red+'Enter a atleast 5 questions and atmost 10 questions in this section'+cl.reset+em.w_i)
			else:
				for i in range(qs):
					while(True):
						print(cl.blue+'Enter difficulty level: Easy(1), Medium(2), Hard(3)'+cl.reset)
						try:
							diff = int(input())
							if diff<=3 and diff>=1:
								break
							else:
								print(cl.red+'Wrong input.'+cl.reset+em.w_i)
						except ValueError:
							print(cl.red+'try again..'+cl.reset+em.w_i)
					while(True):
						print(cl.blue+'Enter Qs',i+1)
						qs = input()
						print('Enter option','a.')
						a = input()
						print('Enter option','b.')
						b = input()
						print('Enter option','c.')
						c = input()
						print('Enter option','d.')
						d = input()
						print('Enter Correct Option:'+cl.reset)
						ans = input()
						if ans not in 'abcd':
							print(cl.red+'wrong Format. Try again.'+cl.reset+em.w_i)
							continue
						if qs == '' or a == '' or b == '' or c == '' or d == '' or ans == '':
							continue
						elif ans in 'abcd':
							fp = open('files/C.txt','a')
							fp.write(str(diff)+';'+qs+';'+a+';'+b+';'+c+';'+d+';'+ans+';'+'\n')
							fp.close()
							break
				break
		except ValueError:
			print(cl.red+'Try Again'+cl.reset+em.w_i)
	print(cl.gold+'\n\nSetup Successfull!!\n\n'+em.reset)