#2020CS10318
#assignment 5
#Akarsh Jain

#problem 1
def gridPlay(grid):
    m=len(grid[0]) #number of rows
    n=len(grid) #number of coloumns
    a=[grid[j] for j in range(n)]
    for j in range(1,m):
        #invariant: the entries from a[0][0] to a[0][j-1] represent the penalty in reaching that position
        a[0][j]=grid[0][j]+a[0][j-1]
    for i in range(1,n):
        #invariant: the entries from a[0][0] to a[i-1][0] represent the penalty in reaching that position
        a[i][0]=grid[i][0]+ a[i-1][0]       
    for i in range(1,n):
        #invariant: the entries in a till a[i-1] (i-1 th row) represent the penalty in reaching that position
        for j in range(1,m):
            #invariant: the entries in a till a[i][j-1] represent the penalty in reaching that position
            a[i][j]=min(a[i-1][j],a[i-1][j-1],a[i][j-1])+grid[i][j]
            #assert: the entries in a till a[i][j] represent the penalty in reaching that position
        #asset:the entries in a till a[i] (i th row) represent the penalty in reaching that position
            
    #assert: the penalty faced is the value of entry a[n-1][m-1] by invariant
    return a[n-1][m-1]

#problem 2

# this function checks whether the input is vowel of consonant
def vowel(n):
    if n in ['a','e','i','o','u']:
        return True
    return False
    
def stringProblem(a,b):
    #assert: a,b are non-empty strings
    A=[[0 for i in range(len(b)+1)] for j in range(len(a)+1)]
    # character b[j-1] represents jth index coloumn (coloumn starting from 0)
    # character a[i-1] represents ith index row (row starting from 0) 
    for i in range(len(b)+1): # reason for doing this loop is written at last of this function **
        A[0][i]=i
    for j in range(len(a)+1):
        A[j][0]=j
    for i in range(1,len(a)+1):
        #invariant: A[x][y] represents the min. number of changes to convert string a[0:x] to b[0:y] for x<i
        for j in range(1,len(b)+1):
            #invariant: A[x][y] represents the min. number of changes to convert string a[0:x] to b[0:y] for x<i+1,y<j
            if a[i-1]==b[j-1]:
                # since the two characters are already equal min no. changes will be the changes required to change the remaining list
                A[i][j]=A[i-1][j-1]
            else:
                if vowel(a[i-1]):
                    if vowel(b[j-1]):
                        # min of three possibilities either replace a[i-1] by b[j-1] or delete a[i-1] or insert b[j-1]
                        A[i][j]=1+min(A[i-1][j],A[i][j-1],A[i-1][j-1])
                        # A[i-1][j] represent deletion of element from string a
                        # A[i][j-1] represents insertion of an element in string a and then since the elements will be equal min changes in the remaining part of the string have to be found out
                        # A[i-1][j-1] represents replacement of a[i-1] by b[j-1]
                    else:
                        # min of two possibilities either delete a[i-1] or insert b[j-1]
                        # replacement is not possible in this case
                        A[i][j]=1+min(A[i-1][j],A[i][j-1])
                else:
                    # min of three possibilities either replace a[i-1] by b[j-1] or delete a[i-1] or insert b[j-1]
                    A[i][j]=1+min(A[i-1][j],A[i][j-1],A[i-1][j-1])
            #assert: A[x][y] represents the min. number of changes to convert string a[0:x] to b[0:y] for x<i,y<j+1
        #assert: A[x][y] represents the min. number of changes to convert string a[0:x] to b[0:y] for x<i+1
    return A[len(a)][len(b)]
# ** Reason for doing the middle loop: the first row and first coloumn of the matrix are there for the case in which deletion of element occurs and one of the string gets empty and then min changes will be the number of elements in the other string.
# explained with greater detail in .pdf file



#problem 3

# this checks whether n is a leap year or not
def isleap(n):
    if n%4 != 0:
        return False
    if n%400==0:
        return True
    if n%100==0:
        return False
    return True

#this calculates the day of 1st january for a input year n (1 is monday,2 tuesday....)
def jan(n):
    # initially count is 1 represents 1st jan 1753 was monday
    count=1
    a=n-1
    while a>=1753:
        if isleap(a):
            count+=2
            #since 366%7=2 hence count must be altered by 2
        else:
            count+=1
            #since 365%7=1 hence count must be altered by 1
        a-=1
    if count%7==0:
        #this is introduced since days staring from 1
        return 7
    return count%7


mlist={1:'January',2:'February',3:'March',4:'April',5:'May',6:'June',7:'july',8:'August',9:'September',10:'October',11:'November',12:'December'}

# monuber gives the number of days in a month
def monumber(n,x):
    # n is the month number from mlist
    # x is the year 
    if n==1 or n==3 or n==5 or n==7 or n==8 or n==10 or n==12 :
        return 31
    if n==2:
        if isleap(x):
            return 29
        else:
            return 28
    return 30

#mostart gives the day on which the month will start
def mostart(a,b):
    #a= month number from mlist
    #b= year
    i=1
    s=jan(b)
    while i<a:
        if (s+monumber(i,b))%7==0:
            #this case had to be made since days have been considered numbered from 1 to 7. so 0 must represent 7
            s=7
        else:
            s=(s+monumber(i,b))%7
        i+=1
    return s

#nextweek gives the date from which next week of a month is to be started
def nextweek(a,b):
    #a is the start date of previous week ( in case of firat week it is 1 )
    #b is the start day of the previous week
    return 8+a-b


# month writes to the file f a set of three months side by side i.e. with month numbers a,a+1,a+2 
def month(a,b,f):
    #a=month set to be printed is a,a+1.a+2
    #b=year
    #f=file in which calendar is made
    # x1,x2 | y1,y2 | z1,z2 represent the staring day and starting date for each of the side by side months
    x1=mostart(a,b) 
    x2=1 
    y1=mostart(a+1,b)
    y2=1
    z1=mostart(a+2,b)
    z2=1
    f.write('{:^21}{:^25}{:^21}'.format(mlist[a],mlist[a+1],mlist[a+2])+'\n') 
    f.write('{:<21}{:^25}{:>21}'.format('  M  T  W  T  F  S  S','  M  T  W  T  F  S  S','  M  T  W  T  F  S  S')+'\n')
    for i in range(1,7):
        #i represents the week number 
        for k in range(x1-1):
            #this leaves spaces when the week does not start from monday (e.g jan 1 comes on thursday)
            f.write('   ')
        for j in range(x2,8-x1+x2):
            #this prints the dates of a week
            if j<=monumber(a,b):
                f.write(' {0:0=2d}'.format(j))
            else:
                # this means that all dates coming in a month have been written. just for proper formatting spaces are introduced
                f.write('   ')
        f.write('  ')
        # same for month a+1
        for k in range(y1-1):
            f.write('   ')
        for j in range(y2,8-y1+y2):
            if j<=monumber(a+1,b):    
                f.write(' {0:0=2d}'.format(j))
            else:
                f.write('   ')
        f.write('  ')
        #same for month a+2
        for k in range(z1-1):
            f.write('   ')
        for j in range(z2,8-z1+z2):
            if j<=monumber(a+2,b):
                f.write(' {0:0=2d}'.format(j))
            else:
                f.write('   ')
        f.write('\n')
        # x2,y2,z2 representing dates are assigned new values using nextweek function
        x2=nextweek(x2,x1)
        y2=nextweek(y2,y1)
        z2=nextweek(z2,z1)
        # x1,x2,x3 will be 1 because start day of further weeks will be monday 
        x1=1
        y1=1
        z1=1

def printCalendar(n):
    with open('calendar.txt','x') as f:
        f.write('{:^67}'.format(n)+'\n') #writes the year on top of calendar
        for i in [1,4,7,10]:
            month(i,n,f)
            #by definition of month function it prints 3 months side by side. so eventually all 12 months will be printed
        f.close()













