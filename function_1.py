#1
#def a():
#    return 5
#print(a())

#Prediction: 5


#2
#def a():
#    return 5
#print(a()+a())

#Prediction: 10


#3
#def a():
#    return 5
#    return 10
#print(a())

#Prediction: 5


#4
#def a():
#    return 5
#    print(10)
#print(a())

#Prediction: 5 


#5
#def a():
#    print(5)
#x = a()
#print(x)

#Prediction: null


#6
#def a(b,c):
#    print(b+c)
#print(a(1,2) + a(2,3))

#Prediction: undefined 


#7
#def a(b,c):
#    return str(b)+str(c)
#print(a(2,5))

#Prediction: "2 5"


#8
#def a():
#    b = 100
#    print(b)
#    if b < 10:
#        return 5
#    else:
#        return 10
#    return 7
#print(a())

#Prediction: 100 10 7 error


#9
#def a(b,c):
#    if b<c:
#        return 7
#    else:
#        return 14
#   return 3
#print(a(2,3))
#print(a(5,3))
#print(a(2,3) + a(5,3))

#Prediction: 7  14  7 


#10
#def a(b,c):
#    return b+c
#    return 10
#print(a(3,5))

#Prediction: 8


#11
#b = 500
#print(b)
#def a():
#    b = 300
#    print(b)
#print(b)
#a()
#print(b)

#Prediction: 500 300 error 


#12
#b = 500
#print(b)
#def a():
#    b = 300
#    print(b)
#    return b
#print(b)
#a()
#print(b)

#Prediction: 500 500 500


#13
#b = 500
#print(b)
#def a():
#    b = 300
#    print(b)
#    return b
#print(b)
#b=a()
#print(b)

#Prediction: 500 500 300


#14
#def a():
#    print(1)
#    b()
#    print(2)
#def b():
#    print(3)
#a()

#Prediction: 1 2 3 1 2 3 


#15
#def a():
#    print(1)
#    x = b()
#    print(x)
#    return 10
#def b():
#    print(3)
#    return 5
#y = a()
#print(y)

#Prediction: 1 10 3 5 1