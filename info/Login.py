
import color as cl
import emojizz as em



class Login:
	user = {}
	admin = []
	
	def __init__(self):
		self.sub = 0

	def options(self):
		while(True):
			print(cl.cyan+'\n\n\nPlease choose the login type:\n\n'+cl.reset)
			print(cl.cyan+'\n1. Super-User\n2. Learner\n3. Top Scores\n4. Exit'+cl.reset)
			self.user = self.num_input()
			if self.user == 1:
				print(cl.cyan+'Enter your email:')
				self.email = input()
				print('Enter your password:')
				self.password = input()
				fp = open('files/Admin.txt','r')
				info = fp.readlines()
				for i in range(len(info)):
					info[i] = info[i].split(';')
					if self.email == info[i][0]:
						if self.password == info[i][1]:
							print('\n\nWelcome Back!\n\n'+cl.reset)
							self.Admin_options(self.sub)
							continue
						else:
							print(cl.red+'Wrong password!! Try Again.'+em.w_i+cl.reset)
							continue
				else:
					print(cl.red+'Admin email does not exists.'+em.w_i+cl.reset)
			elif self.user == 2:
				return 'Learner'
				break
			elif self.user == 3:
				fp = open('files/User.txt','r')
				x = fp.readlines()
				fp.close()
				print(x)
				x = [x[i].split(';') for i in range(len(x))]
				x.sort(key = lambda x:x[3])
				print(x)
				if len(x)>10:
					n = 10
				else:
					n = len(x)
				for i in range(n):
					print(n-i,x[i][0],'Marks:',x[i][3])
			elif self.user == 4:
				print('Bye')
				break
			else:
				print(cl.red+'Wrong Input try again.'+em.w_i+cl.reset)


	def Admin_options(self,sub):
		while(True):
			try:
				print(cl.cyan+'\n\n\nSelect an Option:')
				print('1. Edit Quiz\n2. Set up new Quiz\n3. View Feedbacks\n4. Exit')
				select = self.num_input()
				if select == 1 or select == 2:
					print('Select Subject:\n1. Python\n2. JAVA\n3. JavaScript\n4. C/C++\n\n'+cl.reset)
					self.sub = self.num_input()
					if self.sub not in [1,2,3,4]:
						print(cl.red+'Wrong Selection\nTry Again'+em.w_i+cl.reset)
						continue
					if select == 1:
						print(cl.cyan+'\n\nQuiz Editing:\n1. Add Questions\n2. Change correct options\n3. Delete Questions'+cl.reset)
						edit = self.num_input()
						if edit == 1:
							r = self.add_questions(self.sub)
						elif edit == 2:
							r = self.change_answer(self.sub)
						elif edit ==3:
							r = self.del_qs(self.sub)
						else:
							print(cl.red+'Wrong Selection!'+em.w_i+cl.reset)
							continue
						if r == 'No':
							continue
					elif select == 2:
						self.new_quiz(self.sub)
				elif select == 3:
					fp = open('files/Feedback.txt','r')
					x =  fp.readlines()
					for i in range(len(x)):
						print(i+1,x[i])
				elif select == 4:
					break
				else:
					print(cl.red+'Wrong input try again.'+em.w_i+cl.reset)
			except ValueError:
				print(cl.red+'Enter right option number'+em.w_i+cl.reset)



	def add_question(self,sub):
		while(True):
			op = []
			print(cl.cyan+'\n\n\nCategory of question:\nHard (Choose H/h)\n2. Medium (Choose M/m)\n3. Easy (Choose E/e)'+cl.reset)
			cat = input()
			if cat in 'Hh':
				diff = 3
			elif cat in 'Mm':
				diff = 2
			elif cat in 'Ee':
				diff = 1
			else:
				print('Please enter H/h or M/m or E/e')
				continue
			qs = input(cl.cyan+'Enter the question: ')
			for i in range(4):
				print('Enter option ',chr(97+i),':',end = ' ')
				op[i] = input()
				ans = input('Enter correct option: '+cl.reset)
			if self.sub == 1:
				fp = open('files/Python.txt','a')
			elif self.sub == 2:
				fp = open('files/JAVA.txt','a')
			elif self.sub == 3:
				fp = open('files/JavaScript.txt','a')
			elif self.sub == 4:
				fp = open('files/C.txt','a')
			else:
				print(cl.red+'Try Again!!'+em.w_i+cl.reset)
				return 'No'
			if qs == '' or op[0] == '' or op[1] == '' or op[2] == '' or op[3] == '' or ans not in 'abcd':
				print(cl.red+'You cannot store blank input'+em.w_i+cl.reset)
				fp.close()
				continue
			else:
				fp.write(str(diff)+';'+qs+';'+op[0]+';'+op[1]+';'+op[2]+';'+op[3]+';'+ans+';','\n')
				fp.close()
				print(cl.cyan+'\n\nQuestion added Successfully!!\n\n'+cl.reset)
				break

	def change_answer(self,sub):
		while(True):
			if self.sub == 1:
				fp = open('files/Python.txt','r')
			elif self.sub == 2:
				fp = open('files/JAVA.txt','r')
			elif self.sub == 3:
				fp = open('files/JavaScript.txt','r')
			elif self.sub == 4:
				fp = open('files/C.txt','r')
			else:
				print(cl.red+'Try Again!!'+em.w_i+cl.reset)
				return 'No'
			x = fp.readlines()
			fp.close()
			x = [x[i].split(';') for i in range(len(x))]
			for i in range(len(x)):
				print(cl.cyan+'\n\nDifficulty Level:',x[i][0],'\n','Qs',i+1,x[i][1],'\n',chr(97),x[i][2],'\n',chr(98),x[i][3],'\n',chr(99),x[i][4],'\n',chr(100),x[i][5])
			print('\n\nEnter question number whose answer needs to be changed: '+cl.reset)
			qs = self.num_input()
			ans = input(cl.cyan+'Enter new correct option: '+cl.reset)
			if ans == '':
				print(cl.red+'Answer cannot be empty'+em.w_i+cl.reset)
				continue
			elif ans in 'abcd':
				if self.sub == 1:
					fp = open('files/Python.txt','w')
				elif self.sub == 2:
					fp = open('files/JAVA.txt','w')
				elif self.sub == 3:
					fp = open('files/JavaScript.txt','w')
				elif self.sub == 4:
					fp = open('files/C.txt','w')
				for i in range(len(x)):
					if i+1 == qs:
						x[i][6] = ans
				fp.write(str(x[i][0])+';'+x[i][1]+';'+x[i][2]+';'+x[i][3]+';'+x[i][4]+';'+x[i][5]+';'+x[i][6]+';'+'\n')
			print(cl.gold+'\n\n\nAnswer Successfully Changed!\n\n'+cl.reset)
			fp.close()
			break

	def del_qs(self,sub):
		if self.sub == 1:
			fp = open('files/Python.txt','r')
		elif self.sub == 2:
			fp = open('files/JAVA.txt','r')
		elif self.sub == 3:
			fp = open('files/JavaScript.txt','r')
		elif self.sub == 4:
			fp = open('files/C.txt','r')
		else:
			print(cl.red+'Try Again!!'+em.w_i+cl.reset)
			return 'No'
		x = fp.readlines()
		fp.close()
		x = [x[i].split(';') for i in range(len(x))]
		for i in range(len(x)):
			print(cl.cyan+'\n\nDifficulty Level:',x[i][0],'\n','Qs',i+1,x[i][1],'\n',chr(97),x[i][2],'\n',chr(98),x[i][3],'\n',chr(99),x[i][4],'\n',chr(100),x[i][5])
		print('Enter question number you want to delete: '+cl.reset)
		qs = self.num_input()
		if qs <= len(x):
			if self.sub == 1:
				fp = open('files/Python.txt','w')
			elif self.sub == 2:
				fp = open('files/JAVA.txt','w')
			elif self.sub == 3:
				fp = open('files/JavaScript.txt','w')
			elif self.sub == 4:
				fp = open('files/C.txt','w')
			else:
				print(cl.red+'Try Again!!'+em.w_i+cl.reset)
			for i in range(1,len(x)):
				if i == qs:
					x.pop(i)
				if len(x) == 0:
					fp.write('')
					print(cl.red+'\n\nQuiz now empty.\n\n'+em.w_i+cl.reset)
					break
				else:
					fp.write(str(x[i-1][0])+';'+x[i-1][1]+';'+x[i-1][2]+';'+x[i-1][3]+';'+x[i-1][4]+';'+x[i-1][5]+';'+x[i-1][6]+';'+'\n')
			fp.close()
			print(cl.gold+'\n\n\nQuestion Successfully Deleted!!\n\n'+cl.reset)

				

	def new_quiz(self,sub):
		while(True):
			print(cl.cyan+'\n\n\nEnter number of questions you want to add:'+cl.reset)
			qs_n = self.num_input()
			if qs_n >= 5 and qs_n<=10:
				if self.sub == 1:
					fp = open('files/Python.txt','w')
				elif self.sub == 2:
					fp = open('files/JAVA.txt','w')
				elif self.sub == 3:
					fp = open('files/JavaScript.txt','w')
				elif self.sub == 4:
					fp = open('files/C.txt','w')
				else:
					print(cl.red+'Try Again!!'+em.w_i+cl.reset)
					return 'No'
				for i in range(qs_n):
					while(True):
						print(cl.cyan+'\n\nEnter Difficulty Level Hard(3), Medium(2) or Easy(1)',':'+cl.reset)
						diff = int(input())
						if diff not in [1,2,3]:
							print(cl.red+'This level of difficulty not available'+em.w_i+cl.reset)
							continue
						print(cl.cyan+'\n\n\nEnter question number ',i+1)
						qs = input()
						print('Enter answer option',chr(97),':')
						a = input()
						print('Enter answer option',chr(98),':')
						b = input()
						print('Enter answer option',chr(99),':')
						c = input()
						print('Enter answer option',chr(100),':')
						d = input()
						print('Enter correct answer option',':'+cl.reset)
						ans = input()
						if qs == '' or op[0] == '' or op[1] == '' or op[2] == '' or op[3] == '' or ans not in 'abcd':
							print(cl.red+'You cannot store blank or wrong input'+em.w_i+cl.reset)
							continue 
						else:
							fp.write(str(diff)+';'+qs+';'+a+';'+b+';'+c+';'+d+';'+ans+';'+'\n')
							print(cl.cyan+'\n\n\nQuestion successfully added.\n\n'+cl.reset)
							break
				fp.close()
				print(cl.gold+'\n\n\nNew Quiz was successfully added.\n\n'+cl.reset)
				break
			else:
				print(cl.red+'You can not add this number of questions!'+em.w_i+cl.reset)


	@staticmethod
	def num_input():
	    while(True):
	        try:
	            num = int(input())
	            if num>0:
	            	return num
	            else:
	            	print(cl.red+'\nEnter a Natural Number'+em.w_i+cl.reset)
	            	continue
	        except ValueError:
	            print(cl.red+'\nEnter a digit Value. Try Again.'+em.w_i+cl.reset)