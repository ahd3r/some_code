file=open('text.txt', 'r')
print('You can find: ', end='')
line=file.readlines()
mas=[]
mas_finally=[]
for x in line[1:]:
	mas.append(x.strip())
for y in mas:
	mas_finally.append(y.split(','))
q=len(mas_finally)
sort_mas=[]
for m in range(q):
	sort_mas.append(mas_finally[m][0])
sort_mas.sort()
for n in range(q):
	print(sort_mas[n], end='. ')
file.close()
print()
user_type = input('Write a name, what you want to know(`q` for quite): ')
new_open=open('text.txt', 'r')
you_can_watch=new_open.readlines()
first_mas_in_search=[]
mas_for_call=[]
for xx in you_can_watch[1:]:
	first_mas_in_search.append(xx.strip().split(','))
qq=len(first_mas_in_search)
for num in range(qq):
	mas_for_call.append({
		'Name': first_mas_in_search[num][0],
		'Age': first_mas_in_search[num][1],
		'University': first_mas_in_search[num][2],
		'Job': first_mas_in_search[num][3]
	})
while user_type != 'q':
	print()
	user_type = input('Write a name, what you want to know(`q` for quite): ')
	for call in range(qq):
		if user_type == mas_for_call[call]['Name']:
			print('Name: '+ mas_for_call[call]['Name'])
			print('Age: '+ mas_for_call[call]['Age'])
			print('University: '+ mas_for_call[call]['University'])
			print('Job: '+ mas_for_call[call]['Job'])
new_open.close()

''' IN TEXT.TXT
Name,Age,Univer,Job
Vel,18,Custom,lower
Alex,17,Metal,coder
Ander,17,Custom,programing
Vlad,19,KNU,marcketing
'''