"""
a=input()	#str
b=int("z")-int("Z")	#str
if "a" <= a <= "z" :
    print("%s(ASCII: %d) => %s(ASCII: %d)" (a, ord(a), chr(int(a)-b), ord(chr(int(a)-b))))
elif "A" <= a <="Z" :
	print("%s(ASCII: %d) => %s(ASCII: %d)" (a, ord(a), chr(int(a)+b), ord(chr(int(a)-b))))
"""
a=input()
if "a" <= a <= "z" :
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(a,ord(a),a.upper(),ord(a.upper())))
elif "A" <= a <= "Z" :
    print("{0}(ASCII: {1}) => {2}(ASCII: {3})".format(a,ord(a),a.lower(),ord(a.lower())))