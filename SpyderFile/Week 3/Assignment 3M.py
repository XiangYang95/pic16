import time

Num = int or float or long or complex

#first function to divide lists of numbers
def my_divide1(a,b):
    return [float(i)/j for i,j in zip(a,b)]


#second function to divide lists of number
def my_divide2(a,b):
    for i,j in zip(a,b):
        if j == 0 or not isinstance(i,Num) or not isinstance(j,Num):
            print "Something's wrong with my input to my_divide2"
            return []
        
    return [float(i)/j for i,j in zip(a,b)]

#third function to divide lists of number
def my_divide3(a,b):
    try:
        return [float(i)/j for i,j in zip(a,b)]
    
    except:
        print "Something's wrong with my input to my_divide3"
        return []
    
timeList = []

def checkTime(f, a, b):
    for i in range(10):
        begin = time.clock()
        f(a,b)
        end = time.clock()
        timeList.append(end - begin)
    timeTaken = reduce(lambda x,y: (x+y)/2.0, timeList)
    print "The average time taken to complete the division for {} is {}".format(f.__name__, timeTaken)
    
a = range(0,1000000); b = range(1,1000001)


checkTime(my_divide2, a, b)

checkTime(my_divide3, a, b)

a = range(0,1000000); b = range(1,1000000)+ [0]

checkTime(my_divide2, a, b)

checkTime(my_divide3, a, b)

a = range(0,1000000); b = range(1,1000000)+ ['a']

checkTime(my_divide2, a, b)

checkTime(my_divide3, a, b)

#fourth function to divide lists of number
def my_divide4(a,b):
    try:
        return [float(i)/j for i,j in zip(a,b)]
    except TypeError:
        print "Non-numeric data detected"
        return []
    except ZeroDivisionError:
        print "There is a zero in b"
        return []
    except:
        print "Something's wrong with my input to my_divide4"
        return []   
    
print my_divide4([1,2,3], [1,[1,2],0])

print my_divide4([1,2,4], [1,2,0])
