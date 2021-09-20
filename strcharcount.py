def strcharuniq (string):
	for i in range(len(string)-1):
		if(string[i] in string[i+1:]):
			return False
	return True

def strcharuniq2 (string):
	for i in range(len(string)):
		if (string.count(string[i]) > 1):
			return False
	return True

def strcharcount (string):
	string_d = dict.fromkeys(list(string))
	for key in list(string_d):
		string_d[key] = string.count(key)
	return string_d

str1 = 'abcdefghija'
str2 = 'abcd'
str3 = 'abcc'
str4 = 'aa'
str5 = ''
str6 = 'aaaaabbbbbbb'

string_tests = [str1, str2, str3, str4, str5, str6]
for string in string_tests:
	print(string)
	print(strcharuniq(string))
	print(strcharuniq2(string))
	print(strcharcount(string))
	print()