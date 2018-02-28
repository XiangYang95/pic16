import time

#first methoud: function method

def f(x): 
    return x**2

N = 1000000000

k = range(1001)
x = range(N)

y = []

# =============================================================================
# begin = time.clock()
# 
# for i in x:
#     y.append(f(i))
# 
# end = time.clock()
# 
# =============================================================================
timelist = []

for j in k:
    begin= time.clock()
    for i in x:
        y.append(f(i))
    end = time.clock()
    timetaken = end - begin
    timelist.append(timetaken)

TimeTaken1 = reduce(lambda x, y: (x+y)/2.0, timelist)

print TimeTaken1

#second method: lambda method

# =============================================================================
# begin = time.clock()
# 
# for i in x:
#     y.append(lambda i: i**2)
#     
# end = time.clock()
# =============================================================================

timelist = []
for j in k:
    begin= time.clock()
    for i in x:
        y.append(lambda x: x**2)
    end = time.clock()
    timetaken = end - begin
    timelist.append(timetaken)

TimeTaken2 = reduce(lambda x,y: (x+y)/2.0, timelist)

#third method: without function method

# =============================================================================
# begin = time.clock()
# 
# for i in x:
#     y.append(i**2)
#     
# end = time.clock()
# 
# =============================================================================
timelist = []

for j in k:
    begin= time.clock()
    for i in x:
        y.append(i**2)
    end = time.clock()
    timetaken = end - begin
    timelist.append(timetaken)

TimeTaken3 = reduce(lambda x,y: (x+y)/2.0, timelist)

print TimeTaken1, TimeTaken2, TimeTaken3

#fourth method: reuse list

y = range(N)

begin = time.clock()

for i in y:
    i = i**2

end = time.clock()

TimeTaken4 = end - begin

#fifth method: list comprehension

begin = time.clock()

y = [k**2 for k in range(N)]

end = time.clock()

TimeTaken5 = end - begin

#sixth method: map method

begin = time.clock()

y = list(map(lambda x: x**2, range(N)))

end = time.clock()

TimeTaken6 = end - begin

print TimeTaken4,TimeTaken5,TimeTaken6