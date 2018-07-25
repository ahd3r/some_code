'''
Movie

Optimized
Do that user can go back if he push wrong button
More info about found movie
Safe data of movies in json-file
'''
# import json
 
movie=[]

with open('data.txt', 'w') as inside:
	json.dump(movie, inside)

def add_movie():
	print()
	name = input('Name of the movie: ')
	director = input('Director of the movie: ')
	year_of_created = int(input('Year of created the movie: '))
	status = 0

	movie.append({
		'name': {'name_2': name, 'status': status},
		'director': director,
		'year_of_created': year_of_created
		})

	print()
	print(f'Movie `{name}` was added in your lib and now you can watch it')
	print()
	print()

def watch_movie():
	print('\nWatching movie...\nI dont know how to do it yet or know...')

	if movie != []:
		print()
		print('Your movie: ')
		for show_all_movie in movie:
			print(f"Name: {show_all_movie['name']['name_2']}")
			print(f"Director: {show_all_movie['director']}")
			print(f"Release: {show_all_movie['year_of_created']}")
			print()
		print()

	else:
		print()
		print('You dont have any movie yet')
		print()
		print()

def finde_movie():
	print()
	if movie != []:
		print('Your movie:')
		for finde_a_movie in movie:
			print(f"Name: {finde_a_movie['name']['name_2']}")
			print(f"Director: {finde_a_movie['director']}")
			print(f"Release: {finde_a_movie['year_of_created']}")
			print()
		print()

		type_search = input(' by name `n`\n by creator `c`\n by year `y`\nYour choice: ')
		res = []
		resultat=[]
		status_res=[]
		print()
		if type_search == 'n':
			letter_search_n = []
			search = input('Type the name of movie: ')
			for s in search:
				letter_search_n.append(s)
			for finde_a_movie_2 in movie:
				if search == finde_a_movie_2['name']['name_2']:
					res.insert(0, finde_a_movie_2['name'])
				else:
					for letter_movie in finde_a_movie_2['name']['name_2']:
						for new_letter_seach_n in letter_search_n:
							if new_letter_seach_n==letter_movie:
								if finde_a_movie_2['name'] not in res:
									res.append(finde_a_movie_2['name'])
								else:
									finde_a_movie_2['name']['status'] += 1
		elif type_search == 'c':
			letter_search_c = []
			search_c = input('Type the creator of movie: ')
			for s in search_c:
				letter_search_c.append(s)
			for finde_a_movie_2 in movie:
				if search_c == finde_a_movie_2['director']:
					res.insert(0, finde_a_movie_2['name'])
				else:
					for letter_director in finde_a_movie_2['director']:
						for compare in letter_search_c:
							if compare == letter_director:
								if finde_a_movie_2['name'] in res:
									res.append(finde_a_movie_2['name'])
		elif type_search == 'y':
			search_y = int(input('Type a year of release the movie: '))
			for finde_a_movie_2 in movie:
				if search_y == finde_a_movie_2['year_of_created']:
					res.insert(0, finde_a_movie_2['name'])
		else:
			print('This simbol is not recognized')

		if res == [] and type_search == 'n':
			print(f'The {search} was not found')
			print()
			print()
		elif res == [] and type_search == 'c':
			print(f'The {search_c} was not found')
			print()
			print()
		elif res == [] and type_search == 'y':
			print(f'The {search_y} was not found')
			print()
			print()
		else:
			for finde_a_movie_3 in res:
				status_res.append(finde_a_movie_3['status'])
			status_res.sort(reverse=True)
			for finale in status_res:
				for one_more in res:
					if finale == one_more['status']:
						resultat.append(res['name_2'])
					else:
						print('Its never happened')
			for r in resultat:
				print(r)
			print()
			print()
	else:
		print('You have no a movie')
		print()
		print()

def menu():
	
	user_input = input(' if you want to add a movie press `a`;\n if you want to see a movie press `w`;\n if you want to finde a movie press `f`;\n if you want to quit press `q`;\n Your choice: ')

	while user_input != 'q':
		if user_input == 'a':
			add_movie()
		elif user_input == 'w':
			watch_movie()
		elif user_input == 'f':
			finde_movie()
		else:
			print()
			print('Unknow command — try again.')
			print()
			print()

		user_input = input(' if you want to add a movie press `a`;\n if you want to see a movie press `w`;\n if you want to finde a movie press `f`;\n if you want to quit press `q`;\n Your choice: ')

menu()
