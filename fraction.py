def co(m,n):
           while m%n!=0:
               oldm=m
               oldn=n
               m=oldn
               n=oldm%oldn
           return n


class Fraction:
        def __init__(self,top,bottom):
            
            self.num=int(top)
            self.den=int(bottom)
        def __str__(self):
            common=co(self.num,self.den)
            #print 'com',common,'selfnum',self.num,'selfden',self.den
            self.num=self.num//common
            self.den=self.den//common
            return str(self.num)+"/"+str(self.den)
        def __add__(self,other):
            newnum=(self.num*other.den)+(self.den*other.num)
            newden=(self.den)*(other.den)
            return Fraction(newnum,newden)
        def __sub__(self,other):
            newnum=(self.num*other.den)-(self.den*other.num)
            newden=(self.num*self.den)
            return Fraction(newnum,newden)
        def __mul__(self,other):
            newnum=(self.num*other.num)
            print newnum
            newden=(self.den*other.den)
            return Fraction(newnum,newden)
        
        def __truediv__(self,other):
            newnum=self.num*other.den
            newden=self.den*other.num
            return Fraction(newnum,newden)
        ''' Comparative studies'''
        def __gt__(self,other):
            result=self.num/self.den>other.num/other.den
            return result
        def __ge__(self,other):
            result=self.num/self.den>=other.num/other.den
            return result
        def __lt__(self,other):
            result=self.num/self.den<other.num/other.den
            return result
        def __lte__(self,other):
            result=self.num/self.den<=other.num/other.den
            return result
        def __ne__(self,other):
            result=self.num/self.den!=other.num/other.den
            return result
        
        def getNum(self):
            return self.num
        def getden(self):
            return self.den
try:
    v1=int(input("Enter value1"))
    v2=int(input("Enter Value 2"))
    myf=Fraction(v1,v2)
except:
    print ("can only be int")
print myf    
myf2=Fraction(5,13)
myf3=Fraction(3,10)
#print (myf+myf2+myf3)
#num=myf.getNum()
#print num
#print myf.__str__()
#print myf-myf2
#print "mul",myf3*myf2,"end:"
#print "div",(myf).__truediv__(myf2)
#print "gt",myf>myf2
#print "gte",myf>=myf3
#print "lt",myf<myf2
#print "lte",myf<=myf2
#print "ne",myf!=myf3

