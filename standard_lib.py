from collections import OrderedDict

favorite_languages = OrderedDict()

favorite_languages['illia'] = 'java'
favorite_languages['nadia'] = 'python'
favorite_languages['ilya']  = 'javascript'

for name, language in favorite_languages.items():
	print(name.title() + "'s favorite lang is " + language.title())