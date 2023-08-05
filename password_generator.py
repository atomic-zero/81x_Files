
# Code by 7wp@81x
# Des: Simple name based automatic wordlist generator

import itertools
import random

data_dict = {}

def password_generator(password_data, user):
	minimum_length = 6
	null_pass = 'baby'
	tmp_dict1,tmp_dict,tmp_list,data,tmp,log,middle,count = {}, {}, [], {}, [], [], "", 0
	wordlist = ['gwapoako','gwapoako123','qwerty123','love123','love143','iloveyou']
	extend = ['123','12345','1234','143','self']
	password_list = password_data.split(" ")
	try:
		if len(password_list) == 3:
			middle += password_list[1]
			password_list.pop(1)
		elif len(password_list) >= 4:
			tmp.append(password_list[-0])
			tmp.append(password_list[-1])
		elif len(password_list) == 1:
			tmp.append(password_list[-0])
			tmp.append(null_pass)
		if len(tmp) != 0:
			password_list = tmp
		for da, add in itertools.product(password_list, extend):
			count += 1
			if add == '143':
				if middle != "":
					if middle+'123' in log:
						data.update({count:middle.lower()+'12345'})
					else:
						data.update({count:middle.lower()+'123'})
						log.append(middle.lower()+'123')
				else:
					data.update({count:da.lower()+add})
			elif add == "self":
				if len([*da]) >= minimum_length:
					data.update({count:da.lower()})
				else:
					ran = random.choice(wordlist).lower()
					data.update({count:ran})
					wordlist.remove(ran)
			else:
				data.update({count:da.lower()+add})
		count = 5
		for x in range(1,minimum_length):
			count +=1
			tmp_list.append(x)
			tmp_list.append(count)
		for c in tmp_list: tmp_dict.update({c:data.get(c)})

		count = 0
		for x in tmp_dict.keys():
			count +=1
			tmp_dict1.update({count:tmp_dict.get(x)})

		data = tmp_dict1
		data.update({'Name':password_data.strip()})
		data_dict.update({user:data})
		print(f'\r \033[0m[\033[0;31m*\033[0m] List generated: \033[0;31m{str(len(data_dict.values()))}\033[0m',end='')
	except AttributeError:
		return 'drop'
	except ValueError:
		return 'drop'

"""
data_list = ['Jhon Niel|Username1','Jonny James smith|Username0']
for x in data_list:
	data = x.split('|')
	username = data[-1]
	name = data[-0]
	password_generator(name,username)
print(data_dict)
# Output:
	{'Username1': {1: 'jhon123', 2: 'niel123', 3: 'jhon12345', 4: 'niel12345', 5: 'jhon1234', 6: 'niel1234', 7: 'jhon143', 8: 'niel143', 9: 'love123', 10: 'love143', 'Name': 'Jhon Niel'}, 'Username0': {1: 'jonny123', 2: 'smith123', 3: 'jonny12345', 4: 'smith12345', 5: 'jonny1234', 6: 'smith1234', 7: 'james123', 8: 'james123', 9: 'qwerty123', 10: 'love143', 'Name': 'Jonny James smith'}}
for x in data_dict:
	password1 = data_dict.get(x).get(1)
	name = data_dict.get(x).get('Name')
"""
