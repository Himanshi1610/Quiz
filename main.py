from info import admin_setup
from info import Login
from info import User

import color as cl
import emojizz as em

print(cl.white+cl.bold+'\n\n\nWelcome to Codo Sapien\n\n\n'+cl.reset+em.alien)

fp = open('files/Admin.txt','r')
x = fp.readlines()
fp.close
if x[0] == 'True':
	ob = admin_setup.setup()
else:
	ob = Login.Login()
	r = ob.options()
	if r == 'Learner':
		ob2 = User.User()
		ob2.user_info()