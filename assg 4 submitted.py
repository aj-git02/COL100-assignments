#problem 1

#the function isint(x) checks whether the string x is made of integer or has decimal
def isint(x):
    for i in range(0,10):
        #assert: x is a string with a single element
        #invariant: the string does not contain intgers from 0 to i-1
        #note here instead of str function indiviual cases of '1','2''etc. could also have been made
        if x==str(i):
            #assert: string has an integer
            return True
    #assert:string does not have a integer
    if x=='.':
        #assert: string has a decimal
        return True
    #assert:string does not have a integer or a decimal
    return False

#readNumber is the function asked in problem statement
def readNumber(s,i):
    #assert:s[i] is a integer
    j=i+1
    a=len(s)
    while (j!=a and isint(s[j])):
        #invariant: s[i:j] contains a integer or a float and j is not equal to a
        j+=1
    return (s[i:j],j)

#signeval takes two floats x,y identifies the sign in string a and performs the required computation
def signeval(x,y,a):
        if a=='+':
            return x+y
        if a=='-':
            return x-y
        if a=='*':
            return x*y
        if a=='/':
            return x/y

#evalParen is the function asked in problem statement
def evalParen(s,i):
    #assert: the input inside brackets may be of four forms
    #'sign may be other than +'
    #case1 : ()+x     
    #case2 : ()+()
    #case3 : x+y
    #case4 : x+()
    # only (x) does not make sense 
    if s[i+1]=='(':
        #assert: case 1 or case 2 have to be tackled
        (a,b)=evalParen(s,i+1)
        #assert: s[b] contains the operator according to which operation has to be done
        if s[b+1]=='(':
            #assert: case 2 has to be tackled
            (c,d)=evalParen(s,b+1)
            return (signeval(float(a),float(c),s[b]),d+1)
        #assert: case 1 has to be tackled
        (c,d)=readNumber(s,b+1)
        return (signeval(float(a),float(c),s[b]),d+1)
    #assert: either case 3 or case 4
    (a,b)=readNumber(s,i+1)
    if isint(s[b+1])==True:
        #assert: case 3 has to be tackled
        (c,d)=readNumber(s,b+1)
        return (signeval(float(a),float(c),s[b]),d+1)
    #assert: case 4 has to be tackled
    (e,f)=evalParen(s,b+1)
    return (signeval(float(a),float(e),s[b]),f+1)

#evaluate is the function asked in problem statement
def evaluate(s):
    #assert: there are two cases for the input
    #case1: single number
    #case2: combination like x+y or x+() or ()+x
    if isint(s[0]):
        (a,b)=readNumber(s,0)
        if len(s)==b:
            #assert: this is case1
            return a
    #assert:case2 is the only case left
    #in this brackets can be added to the string and evalParen can be used
    s='('+s+')'
    (b,c)=evalParen(s,0)
    return b


#problem 2

# sumcheck checks whther x can be represented as a sum of two distinct numbers from l in a unique way
def sumcheck(x,l):
    count=0
    for i in range(len(l)):
        #invariant 1: count represents the number of ways in which the number x can be represented as a sum of two distinct numbers from l, one of the numbers having index between 0,i-1
        for j in range(i+1,len(l)):
            #invariant 2: count represents the number of ways in which the number x can be represented as a sum of two distinct numbers from l, (one being from 0,i-1) or (one being i and other between i+1,j-1)
            if x==l[i]+l[j] :
                count+=1
                if count>=2 :
                    # assert: x can be represented as sum of two distinct numbers from l in more than one way
                    return False
            #assert: count represents the number of ways in which the number x can be represented as a sum of two distinct numbers from l, one of the numbers having index between 0,i
        #assert: count represents the number of ways in which the number x can be represented as a sum of two distinct numbers from l
    if count==0:
        #assert: x cannot be represented as sum of two distinct numbers from l in any way
        return False
    #assert count==1 and x can be represented as a sum of two distinct numbers from l in a unique way
    return True


#  next term provides the next term of the given sequence
def nextterm(l):
    x=l[-1]+1
    while (not sumcheck(x,l)):
        #invariant: all numbers between l[-1] and x including x cannot be part of the sequence
        x+=1
    #assert: x satisfies sumcheck(x,l) and all numbers between l[-1] and x do not satisfy hence x is next term of the sequence
    return x
    
# sumSequence provides the required list
def sumSequence(n):
    a=[1,2]
    while len(a)!=n:
        #len(a)!=n hence more terms have to be appended to list a 
        a.append(nextterm(a))
    # assert len(a)==n and a contains the numbers of the asked sequence
    return a  


#problem 3

def sumlist(l):
    sum=l[0]
    for i in range(len(l)-1):
        # invariant: sum = sum of all elements till index i of the list at start of loop
        sum+=l[i+1]
    #assert sum = sum of all elements in the list
    return sum

def min(a,b):
    if a<=b: return a
    else : return b
    #assert min returns minimum of a and b

def minLength(a,n):
    ans=len(a)+2
    # at start ans is unrealistic so that (*does not exist case*) may be detected
    for i in range(len(a)):
        # invariant 1: ans is the least length of a contigous list whose sum>n and starts from index 0..i-1 if such list exists
        for j in range(i,len(a)):
            # invariant 2: ans is the least length of a contigous list whose sum>n and starts from index 0..i-1 or starts at index i and is contained in a[i:j] if such list exists
            if sumlist(a[i:j+1])>n :
                ans=min(ans,len(a[i:j+1]))
        #assert: ans is the least length of a contigous list whose sum>n and starts from index 0...i if such list exists
    # assert: ans is the least length of a contigous list whose sum>n if such list existsif not exist then ans=len(a)+2
    if ans == len(a) +2 :
        #assert no such contigous list exist
        return -1
    else :
        #assert the minimum length of the contigous list is ans
        return ans


# problem 4


# Merges two subarrays of arr[] write the output to b[l:r]
# First subarray is arr[l:m] # Second subarray is arr[m:r]
def mergeAB(arr,b, l, m, r):
    i = l # Initial index of first subarray
    j = m # Initial index of second subarray
    k = l # Initial index of merged subarray
    while i < m and j < r :
        #invariant: list b from index l to k-1 is sorted
        if arr[i] <= arr[j]:
            b[k] = arr[i]
            i += 1
        else:
            b[k] = arr[j]
            j += 1
        k += 1
    while i < m:
        # Copy the remaining elements of arr[i:m], if there are any
         b[k] = arr[i]
         i += 1
         k += 1
    while j < r:
        # Copy the remaining elements of arr[j:r], if there are any
         b[k] = arr[j]
         j += 1
         k += 1


def mergeit(A,B,n,l):
    # A of size n consists of n/l sorted lists of size l each [last list may be shorter]
    # merge them in pairs writing the result to B [there may be one unpaired if not even]
    if n%l == 0:
         count=n//l
    else:
         count=n//l + 1
    for i in range( count//2 ):
        # invariant: all the elements upto upto 2*i*l have been copied into b as i sorted lists of length 2l each
         left=i*l*2
         right=min(left+2*l,n) # since last list could be shorter
         mergeAB(A,B,left,left+l,right)
    # Copy the last list if there is any (may happen if count is odd)
    for i in range(right,n):
        #assert: count was odd hence one list could not be paired with others
         B[i]=A[i]

def mergeSort(A):
    n=len(A)
    l=1
    B=[0 for x in range(n)]
    dir=0
    while l < n:
        #invariant: A or B according to value of dir contain n/l sorted lists of size l each [last list may be shorter]
        if dir == 0:
            #we have to copy result from A to B
            mergeit(A,B,n,l)
            dir=1
        else:
            #we have to copy result from B to A
            mergeit(B,A,n,l)
            dir=0
        l*=2
    #if result is in B copy result to A
    if dir==1:
        for i in range(n):
            A[i]=B[i]

def mergeContacts(l):
    mergeSort(l)
    #assert: list is sorted hence same names will occur consecutively
    #assert: list is not empty
    (a,b)=l[0]
    l[0]=(a,[b])
    ans=[l[0]]
    for i in range(1,len(l)):
        #invariant: emails have been merged for all people having entries till index i-1 and appended to ans
        (w,x)=l[i-1]
        (y,z)=l[i]
        if w==y:
            #assert: l[i] and l[i-1] have the same names hence emails to be merged
            (g,h)=ans[-1]
            h.append(z)
            ans[-1]=(g,h)
        else:
            l[i]=(y,[z])
            ans.append(l[i])
    #assert: ans contains merged result obtained from merging all entries with same names in l
    return ans

