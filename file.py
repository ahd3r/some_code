# create a text_friends.txt and text_nearly_friends.txt in folder, where is our project before run the program
type_by_user = input('Write all friends, which you have, separated by comma(no spaces): ').split(',')
file_fill=open('text_friends.txt', 'w')
for all_friend in type_by_user:
	file_fill.write(all_friend+'\n')
file_fill.close()
friend=input('Write three name of your friend, separated by comma, which live near you(no spaces): ').split(',')
file=open('text_friends.txt', 'r')
friend_for_put = []
list_of_friends_in_file=file.read().split('\n')
for x in friend:
	if x in list_of_friends_in_file:
		friend_for_put.append(x)
	else:
		print(f'{x} not found')
file.close()
next_file = open('text_nearly_friends.txt', 'w')
for f in friend_for_put:
	next_file.write(f+'\n')
	print(f'{f} was added!')
print('Successful.')
next_file.close()