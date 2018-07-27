import sqlite3

def all():
	word = input('Type some letter (a (add), l (list), k (know), d (delete), q (quite)): ')

	create_bd()
	while word!='q':
		if word == 'a':
			name=input('Type a word: ')
			name_2=input('Type a explanation: ')
			add(name, name_2)
		elif word == 'l':
			listit()
		elif word == 'k':
			already_know=input('Write a word which you already know: ')
			know(already_know)
		elif word == 'd':
			want_delete=input('Write a word, which you want to delete: ')
			delete(want_delete)
		else:
			print('Try again')
		word = input('Type some letter (a (add), l (list), k (know), d (delete), q (quite)): ')

def create_bd():
	connect=sqlite3.connect('data.bd')
	cursor=connect.cursor()
	cursor.execute('CREATE TABLE IF NOT EXISTS dictionary (word text primary key, explanation text, know integer)') #maybe add a know (True or False)
	connect.commit()
	connect.close()

def add(name, name_2):
	connect=sqlite3.connect('data.bd')
	cursor=connect.cursor()
	cursor.execute('INSERT INTO dictionary VALUES(?, ?, 0)', (name, name_2))
	connect.commit()
	connect.close()

def listit():
	connect=sqlite3.connect('data.bd')
	cursor=connect.cursor()
	cursor.execute('SELECT * FROM dictionary')
	know=[{'name': row[0], 'explanation': row[1], 'know': row[2]} for row in cursor.fetchall()]
	connect.close()

	for x in know:
		print(f"({x['know']}) {x['name']} - {x['explanation']}")

def know(already):
	connect=sqlite3.connect('data.db')
	cursor=connect.cursor()
	cursor.execute('UPDATE dictionary SET know=1 WHERE word=?',(already,))	
	connect.commit()
	connect.close()

def delete(d):
	connect=sqlite3.connect('data.db')
	cursor=connect.cursor()
	cursor.execute('DELETE FROM dictionary WHERE word=?', (d,))
	connect.commit()
	connect.close()

all()