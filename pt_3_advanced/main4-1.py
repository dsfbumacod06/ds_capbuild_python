'''
Argument Parsing Kineso
'''

def myfunction(*args,**kwargs):
    print(args[0])
    print(args[1])
    print(args[2])
    print(args[3])
    print(kwargs['KEYONE']) # kwargs are dictionarys
    print(kwargs['KEYTWO'])

myfunction('hey', True, 19, 'w0W', KEYONE="TEST", KEYTWO=7)
    