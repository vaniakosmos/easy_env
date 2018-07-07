easy_env
========

.. image:: https://travis-ci.org/vaniakosmos/easy_env.svg?master
		:target: https://travis-ci.org/vaniakosmos/easy_env

Implement common operations over env vars such as reading booleans and integers.

Installation
------------

.. code-block:: bash

	pip install easy_env


Usage
-----

.. code-block:: python

	import os
	import easy_env


	# setup env vars
	setup_vars = [
		('int', '42'),
		('float', '42.9'),
		('bool', 'yes'),
		('str', 'foo bar'),
		('bytes', 'Zm9v'),  # base64 encoded b'foo'
		('list', '1,2,3'),
		('list2', '4 5 6'),
	]
	for var, value in setup_vars:
		os.environ[var] = value


	# get var
	assert easy_env.get_int('int') == 42
	assert easy_env.get_float('float') == 42.9
	assert easy_env.get_bool('bool') is True
	assert easy_env.get_str('str') == 'foo bar'
	assert easy_env.get_bytes('bytes') == b'foo'
	assert easy_env.get_list('list') == ['1', '2', '3']

	# get w/ default
	assert easy_env.get_int('NEW_VAR', 5) == 5

	# get w/o default
	assert easy_env.get_int('NEW_VAR') is None

	# get w/o default and raise exception
	try:
		easy_env.get_int('NEW_VAR', raise_error=True)
		assert False
	except KeyError:
		assert True

	# get list of integers
	assert easy_env.get_list('list', item_factory=int) == [1, 2, 3]
	# get list w/ another separator
	assert easy_env.get_list('list2', separator=' ') == ['4', '5', '6']

	# detect type based on type of default
	assert easy_env.get('int', 1) == 42
	assert easy_env.get('int') == '42'
	assert easy_env.get('float', 1.0) == 42.9
	assert easy_env.get('bool', False) is True
	assert easy_env.get('bytes', b'') == b'foo'
	assert easy_env.get('list2', default=[], separator=' ') == ['4', '5', '6']


	# set int
	easy_env.set_int('int_var', 42)
	assert os.getenv('int_var') == '42'

	# set float
	easy_env.set_float('float_var', 42.0)
	assert os.getenv('float_var') == '42.0'

	# set bool
	easy_env.set_bool('bool_var', True)
	assert os.getenv('bool_var') == '1'
	easy_env.set_bool('bool_var', False)
	assert os.getenv('bool_var') == '0'

	# set string
	easy_env.set_str('str_var', 'foo bar')
	assert os.getenv('str_var') == 'foo bar'

	# set bytes
	easy_env.set_bytes('bytes_var', b'foo')
	assert os.getenv('bytes_var') == 'Zm9v'

	# set list
	easy_env.set_list('list_var', [1, 2, 3])
	assert os.getenv('list_var') == '1,2,3'
	easy_env.set_list('list_var', [1, 2, 3], separator=' ')
	assert os.getenv('list_var') == '1 2 3'
	easy_env.set_list('list_var', [1, 2, 3], serializer=lambda x: str(x - 1))
	assert os.getenv('list_var') == '0,1,2'
