#!/usr/bin/python

# initialize
my_dict = {}

# add item
my_dict['name'] = 'brian'
my_dict['state'] = 'florida'
my_dict['age'] = 37

print my_dict

# access item
print my_dict['name']

# change item
my_dict['name'] = 'engineer man'

# remove item by index
del my_dict['state']

# iterate
for k, v in my_dict.iteritems():
	print k, '=>', v