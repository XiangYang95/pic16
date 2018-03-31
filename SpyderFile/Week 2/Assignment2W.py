str1 = """
Lorem ipsum dolor sit amet, consectetur adipiscing elit,
 sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
 Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris 
 nisi ut aliquip ex ea commodo consequat. Duis aute irure dolor in 
 reprehenderit in voluptate velit esse cillum dolore eu fugiat nulla pariatur. 
 Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia 
 deserunt mollit anim id est laborum.
"""
x = str1.split()

print x

y = {j:x.count(j) for j in x}

print y

print len(y)

dictx = {}
setx = set(x)
for k in setx:
    counter = 0
    for l in x:
        if k == l:
            counter += 1
    dictx[k] = counter

print dictx

f = open("The Mysterious Affair at Styles.txt", "r")

fileOfF = f.read()

import time

begin1 = time.clock()

f1 = {j:fileOfF.count(j) for j in fileOfF}

end1 = time.clock()

totalTime1 = end1 - begin1

begin2 = time.clock()

dictf = {}
setf = set(fileOfF)
for k in setf:
    counter = 0
    for l in fileOfF:
        if k == l:
            counter += 1
    dictf[k] = counter
    
end2 = time.clock()

totalTime2 = end2 - begin2

print totalTime1, totalTime2








