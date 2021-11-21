'''6'''
# d=[{'name': 'affirm', 'confidence': 0.9448149204254}, {'name': 'affirm', 'confidence': 0.944814920425415}, {'name': 'inform', 'confidence': 0.9842240810394287}, {'name': 'inform', 'confidence': 0.9842240810394287}]
# res=[]
# st=[]
# for i in d:
# 	t=i['name']+str(i['confidence'])
# 	if t not in st:
# 		st.append(t)
# 		res.append(i)
# print(res)
# print(len(d),len(res))

'''7'''
# import re
# password=input()
# reg = "^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[@$!%*#?&])[A-Za-z\d@$!#%*?&]{6,16}$"
# re.compile(reg)
# if re.search(reg,password)  :
#     	print('Valid Password')
# else:print("Invalid Password")

"""8"""
# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d2:
# 	if d1.get(i)!=None:
# 			d1[i]=d2[i]+d1[i]
# 	else:
# 		d1[i]=d2[i]
# print(d1)~