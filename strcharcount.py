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
