
import color as cl
import emojizz as em


class User:
	record = {}
	id1 = ''
	mail = ''

	def user_info(self):
		while(True):
			f_name = input('Enter Your User Name: ').split(' ')
			name = f_name[0]
			email = input('Enter your email: ')
			if name == '' or email == '':
				continue
			fp = open('files/User.txt','r')
			x = fp.readlines()
			fp.close()
			x = [x[i].split(';') for i in range(len(x))]
			flag = 0
			attempted = 0
			marks = 0
			for i in range(len(x)):
				if x[i][0] == name and x[i][1] == email:
					attempted = int(x[i][2])
					marks = int(x[i][3])
					print(cl.cyan+'Welcome Back!'+cl.reset)
				else:
					flag +=1
				self.record[(x[i][0],x[i][1])] = [x[i][2],x[i][3]]
			if flag == len(x):
				x.append([name,email,attempted,marks,'\n'])
				self.record[(name,email)] = [0,0]
				fp = open('files/User.txt','w')
				for i in range(len(x)):
					fp.write(x[i][0]+';'+x[i][1]+';'+str(x[i][2])+';'+str(x[i][3])+';'+'\n')
			fp.close()
			self.id1 = name
			self.mail = email
			self.options()
			break

	def options(self):
		while True:
			print(cl.cyan+'Select one of the options:\n1. Take a quiz\n2. View Overall results\n3. Give Feedback\n4. Exit\n'+cl.reset)
			option = self.num_input()
			if option == 1:
				self.quiz()
			elif option == 2:
				self.result()
			elif option == 3:
				self.feedback()
			elif option == 4:
				print('BYE')
				break
			else:
				print(cl.red+'Wrong input try again'+em.w_i+cl.reset)
				continue

	def quiz(self):
		while(True):	
			print(cl.cyan+'Choose a subject:\n1. Python\n2. JAVA\n3. JavaScript\n4. C/C++'+cl.reset)
			sub = self.num_input()
			if sub == 1:
				fp = open('files/Python.txt','r')
				x = fp.readlines()
				if not x:
					print(cl.red+'Sorry Python Quiz is not available right now'+em.w_i+cl.reset)
					continue
			elif sub == 2:
				fp = open('files/JAVA.txt','r')
				x = fp.readlines()
				if not x:
					print(cl.red+'Sorry JAVA Quiz is not available right now'+em.w_i+cl.reset)
					continue
			elif sub == 3:
				fp = open('files/JavaScript.txt','r')
				x = fp.readlines()
				if not x:
					print(cl.red+'Sorry JavaScript Quiz is not available right now'+em.w_i+cl.reset)
					continue
			elif sub == 4:
				fp = open('files/C.txt','r')
				x = fp.readlines()
				if not x:
					print(cl.red+'Sorry C/C++ Quiz is not available right now'+em.w_i+cl.reset)
					continue
			else:
				print(cl.red+'Try Again!!'+em.w_i+cl.reset)
				continue
			fp.close()
			print(cl.cyan+'Choose difficulty level:\n Beginner(1), Roorkie(2), Pro(3)'+cl.reset)
			diff = self.num_input()
			if diff>3 or diff<1:
				print(cl.red+'This Level not yet added, try again.'+em.w_i+cl.reset)
				continue
			x = [x[i].split(';') for i in range(len(x))]
			attempt = 0
			m=0
			l=[]
			for i in range(len(x)):
				if diff == int(x[i][0]):
					while(True):
						print('Qs',attempt+1,x[i][1],'\na.',x[i][2],'\nb.',x[i][3],'\nc.',x[i][4],'\nd.',x[i][5])
						ans = input()
						if ans == x[i][6]:
							m+=10
							attempt+=1
							break
						elif ans not in 'abcd':
							print(cl.red+'Wrong Input. Try again.'+em.w_i+cl.reset)
							continue
						else:
							attempt+=1
							break
					l.append(i)
			if attempt == 0:
				print(cl.red+'Sorry Quiz not available. Try different quiz'+em.w_i+cl.reset)
			else:
				for i in l:
					print('Qs',attempt+1,x[i][1],'\na.',x[i][2],'\nb.',x[i][3],'\nc.',x[i][4],'\nd.',x[i][5],'\nCorrect option:',x[i][6])
				fp = open('files/User.txt','r')
				x = fp.readlines()
				fp.close()
				x = [x[i].split(';') for i in range(len(x))]
				fp = open('files/User.txt','w')
				for i in range(len(x)):
					x[i][2] = int(x[i][2])
					x[i][3] = int(x[i][3])
					if x[i][0] == self.id1 and x[i][1] == self.mail:
						x[i][2]= x[i][2]+attempt
						x[i][3]=x[i][3]+m
					fp.write(x[i][0]+';'+x[i][1]+';'+str(x[i][2])+';'+str(x[i][3])+';'+'\n')
				fp.close()
				info = self.record[(self.id1,self.mail)]
				self.record[(self.id1,self.mail)] = [int(info[0])+attempt,int(info[1])+m]
				print(self.id1,'your Result is','\nQuestions answered',attempt,'\nCorrect answers:',m/10,'\nMarks Obtained:',m,'\nTotal Marks',attempt*10)
				break

	def result(self):
		info = self.record[(self.id1,self.mail)]
		print(self.id1,'Scored Total:',info[0],'\nAttempted total quizzes:',info[1])


	def feedback(self):
		fp = open('files/Feedback.txt','a+')
		print(cl.cyan+'Enter your feedback/Comment:'+cl.reset)
		fd = input()
		fp.write(fd+'\n')
		fp.close()


	@staticmethod
	def num_input():
	    while(True):
	        try:
	            num = int(input())
	            if num>0:
	            	return num
	            else:
	            	print(cl.red+'Enter a Natural Number'+em.w_i+cl.reset)
	            	continue
	        except ValueError:
	            print(cl.red+'Enter a digit Value. Try Again.'+em.w_i+cl.reset)
