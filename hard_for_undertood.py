def call(calling, data):
	return calling(data)

def call_call(my_username):
	return my_username['name']

user={'name': 'Ander', 'last_name': 'Stacen'}

print(call(call_call, user))

def call_lambda(fun_for_lamb, some_data):
	return fun_for_lamb(some_data)

print(call_lambda(lambda me: me['last_name'], user))
