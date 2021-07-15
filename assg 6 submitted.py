#Akarsh Jain
# 2020CS10318
#assignment 6

#problem 1 

class Quiz:
    def __init__(self,title,answer):
        self.title=title
        self._answer=answer #list of answers
        self._attempts={} # this is a dictionary which stores (entryNo:response)
    def _score(self,student):
        # student input is the entryNo
        self._sc=0
        for i in range(len(self._answer)):
            if self._answer[i]==self._attempts[student][i]:
                self._sc+=1
        return self._sc #represents number of correct answers

        
class Course:
    def __init__(self,courseCode,Q_list):
        self.courseCode=courseCode
        self._Q_list=Q_list # list of quizzes


class Student:
    def __init__(self,entryNo,C_list):
        self.entryNo=entryNo
        self._C_list=C_list #list of courses student is taking
    def attempt(self,courseCode,quizTitle,attemptedAnswers):
        for course in self._C_list:
            if course.courseCode==courseCode:
                for quiz in course._Q_list:
                    if quiz.title==quizTitle:
                        if not self.entryNo in quiz._attempts:  #checks whether already attempted 
                            quiz._attempts[self.entryNo]=attemptedAnswers #entry added to dictionary
        
    def getUnattemptedQuizzes(self):
        self._unattempt=[]
        for course in self._C_list:
            for quiz in course._Q_list:
                if not self.entryNo in quiz._attempts:
                    self._unattempt.append((course.courseCode,quiz.title))
        return self._unattempt
        
    def getAverageScore(self,courseCode):
        self._sum=0
        self._number=0
        for course in self._C_list:
            if course.courseCode==courseCode:
                for quiz in course._Q_list:
                    if self.entryNo in quiz._attempts:
                        self._sum+=quiz._score(self.entryNo)
                        self._number+=1
        #self._sum is the total of all attempted quizzes
        #self._number is the number of attempted quizzes
        return self._sum/self._number


#problem 2
class Matrix:
    def __init__(self,l):
        self.list=l # gives the matrix in list of list dense form
    def __str__(self):
        for row in self.list:
            for item in row:
                print('{} '.format(item),end='')
            print('\n')
        return ''
    def rows(self):
        return len(self.list) #number of rows
    def coloumns(self):
        return len(self.list[0]) #number of coloumns
    def __add__(self,a):
        n=self.rows()
        m=self.coloumns()
        x=[[(self.list[i][j]+a.list[i][j]) for j in range(m)] for i in range(n)]
        return Matrix(x)
    def __sub__(self,a):
        n=self.rows()
        m=self.coloumns()
        x=[[(self.list[i][j]-a.list[i][j]) for j in range(m)] for i in range(n)]
        return Matrix(x)
    def __mul__(self,x):
        a=self.rows()
        b=self.coloumns()
        assert len(x.list)==b
        c=len(x.list[0])
        aux=[[0 for i in range(c)]for j in range(a)]
        for i in range(c):
            for j in range(a):
                for k in range(b):
                    aux[j][i]+=(self.list[j][k]*x.list[k][i])
        return Matrix(aux)
    def toSparse(self):
        l=[]
        for i in range(self.rows()):
            s=[]
            for j in range(self.coloumns()):
                if self.list[i][j]!=0:
                    #if it was 0 then no need to be written in the sparse form
                    s.append((j,self.list[i][j]))
            l.append(s)
        return SparseMatrix(l,self.rows(),self.coloumns())
                    
class SparseMatrix:
    def __init__(self,sparse_matrix,n_rows,n_cols):
        self.list=sparse_matrix
        self.row=n_rows
        self.col=n_cols
    def __str__(self):
        for i in range(self.row):
            #prev represents the index after which the last non-zero element ended
            prev=0
            for j in range(len(self.list[i])):
                (a,b)=self.list[i][j]
                for k in range(prev,a):
                    print ('0 ',end='')
                print ('{} '.format(b),end='')
                prev=a+1
            for k in range(prev,self.col):
                print('0 ',end='')
            print('\n')
        return '' 

    def __add__(self,other):
        l=[[] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                #inp1 represents what value does self has at ith row and jth coloumn 
                #inp2 represents what value does other has at ith row and jth coloumn
                inp1=0 
                inp2=0
                for k in range(len(self.list[i])):
                    (a,b)=self.list[i][k]
                    if j==a:
                        #assert:self has non-zero value ith row jth column
                        inp1=b
                        break
                for k in range(len(other.list[i])):
                    (a,b)=other.list[i][k]
                    if j==a:
                        #assert:other has non-zero value ith row jth column
                        inp2=b
                        break
                if inp1!=0:
                    if inp2!=0:
                        #assert: both of them are non-zero hence sum is appended
                        l[i].append((j,inp1+inp2))
                    else:
                        #assert: only inp1 is non-zero hence appended
                        l[i].append((j,inp1))
                else:
                    if inp2!=0:
                        #assert: only inp2 is non-zero hence appended
                        l[i].append((j,inp2))
                #assert: if both inp1 and inp2 are 0 then no need to append      
        return SparseMatrix(l,self.row,self.col)
    def __sub__(self,other):
        l=[[] for j in range(self.row)]
        for i in range(self.row):
            for j in range(self.col):
                #inp1 represents what value does self has at ith row and jth coloumn 
                #inp2 represents what value does other has at ith row and jth coloumn
                inp1=0
                inp2=0
                for k in range(len(self.list[i])):
                    (a,b)=self.list[i][k]
                    if j==a:
                        #assert:self has non-zero value ith row jth column
                        inp1=b
                        break
                for k in range(len(other.list[i])):
                    (a,b)=other.list[i][k]
                    if j==a:
                        #assert:other has non-zero value ith row jth column
                        inp2=b
                        break
                if inp1!=0:
                    if inp2!=0:
                        #assert: both of them are non-zero hence difference is appended
                        l[i].append((j,inp1-inp2))
                    else:
                        #assert: only inp1 is non-zero hence appended
                        l[i].append((j,inp1))
                else:
                    if inp2!=0:
                        #assert: only inp2 is non-zero hence 0-inp2 appended
                        l[i].append((j,-inp2))
                #assert: if both inp1 and inp2 are 0 then no need to append
        return SparseMatrix(l,self.row,self.col)
    def __mul__(self,other):
        a=self.row
        b=self.col
        assert other.row==b
        c=other.col
        X=[[] for i in range(a)]
        for i in range(a):
            for j in range(c):
                #iteration is performed for all ith rows and jth coloumns
                val=0 #this is the sum of products of elements in ith row and jth coloumn
                for k in range(b):
                    #inp1 represents what value does self has at ith row and kth coloumn 
                    #inp2 represents what value does other has at kth row and jth coloumn
                    inp1=0 
                    inp2=0
                    for x in range(len(self.list[i])):
                        (p,q)=self.list[i][x]
                        if k==p:
                            #ith row and kth coloumn entry is non-negative
                            inp1=q
                            break
                    for x in range(len(other.list[k])):
                        (p,q)=other.list[k][x]
                        if j==p:
                            #kth row and jth coloumn entry is non-negative
                            inp2=q
                            break
                    if inp1!=0:
                        if inp2!=0:
                            #assert: both of them are non-zero hence product is added to val
                            val+=inp1*inp2         
                if val!=0:
                    #if val was zero then there was no need to append
                    X[i].append((j,val))
        return SparseMatrix(X,a,c)
    #nth_row function is only used in dense matrix conversion
    #nth_row gives the nth row with the zero elements (in dense form)
    def nth_row(self,n):
        #this gives the nth row of the matrix with zero elements also
        A=[0 for i in range(self.col)]
        for item in self.list[n]:
            (a,b)=item
            A[a]=b
        return A
    def toDense(self):
        D=[self.nth_row(j) for j in range(self.row)]
        return Matrix(D)


#problem 3

#move function appends the newposition to the list and marks previous position as 'X'(to avoid circular motion)
def move(arr,lis,di):
    (a,b)=lis[-1]
    if di==0: #right movement
        lis.append((a,b+1))
        arr[a][b]='X'
    if di==1:  #down movement
        lis.append((a+1,b))
        arr[a][b]='X'
    if di==2:  #left movement
        lis.append((a,b-1))
        arr[a][b]='X'
    if di==3:  #up movement
        lis.append((a-1,b))
        arr[a][b]='X'

#goodformat makes the list look good by replacing movements by 'U','D','R','L'
def goodFormat(s):
    for i in range(1,len(s)):
        #invariant: elements before index i-1 are converted to 'good' form
        (a,b)=s[i-1]
        (c,d)=s[i]
        if a==c:
            #assert: movement from a[i-1] to a[i] was either right or left
            if b==d+1:
                #assert: movement from a[i-1] to a[i] was left
                s[i-1]='L'
            else:
                #assert: movement from a[i-1] to a[i] was right
                s[i-1]='R'
        if a==c+1:
            #assert: movement from a[i-1] to a[i] was up
            s[i-1]='U'
        if a+1==c:
            #assert: movement from a[i-1] to a[i] was down
            s[i-1]='D'
    s.pop() # last element is poped since it is the location of 'E' and no further movements are to be made

def traverseMaze(file):
    #assert:maze is solvable
    with open(file) as f:
        temp=f.readlines() #temp is a temperorary list to store the strings
        f.close()
        l=[]
        for item in temp:
            a=item.split(' ')
            if a[-1]=='X\n': #this condition is made since the the last element of each row has unwanted \n (used for moving to next line) 
                a[-1]='X'
            if a[-1]=='E\n':
                a[-1]='E'
            if a[-1]=='S\n':
                a[-1]='S'
            if a[-1]=='_\n':
                a[-1]='_'
            l.append(a)
        # the list of lists l now contains the maze
        a=len(l[0])
        b=len(l)
        for i in range(b): # to find start and end position
            for j in range(a):
                if l[i][j]=='S':
                    pos=(i,j) #this is staring position
                if l[i][j]=='E':
                    lt=(i,j) #this is the end point
        s=[pos]  #this is a list to store positions visited. last element is the current position
        arr=[[l[j][i] for i in range(a)] for j in range(b)] #duplicate maze
        (i,j)=pos
        while s[-1]!=lt:
            #invariant: all elements in list s do not represent position having 'E'
            if i>=1 and (arr[i-1][j]=='_' or arr[i-1][j]=='E'):
                move(arr,s,3)
                # moves up in the array
                i-=1
                continue
            if j>=1 and (arr[i][j-1]=='_' or arr[i][j-1]=='E'):
                move(arr,s,2)
                # moves left in the array
                j-=1
                continue
            if i<b-1 and (arr[i+1][j]=='_' or arr[i+1][j]=='E'):
                move(arr,s,1)
                # moves down in the array
                i+=1
                continue
            if j<a-1 and (arr[i][j+1]=='_' or arr[i][j+1]=='E'):
                move(arr,s,0)
                # moves right in the array
                j+=1
                continue
            #asssert: the current position has walls on all sides. Hence we must go back to previous position and choose some other path to go.
            (c,d)=s[-1]
            s.pop()
            arr[c][d]='X' #current position is marked as 'X' so to not repeat visits
            (i,j)=s[-1] #setting up i and j for next iteration of the loop
        #assert: the last element in s represents position with 'E'
        goodFormat(s)
        return s
        
