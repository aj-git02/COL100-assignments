(*problem 1________*)
fun isprime(n)=if n<=1 then false else
let 
  fun  prime_iter(x,y)=if y*y>x then true else if x mod y=0 then false else                prime_iter(x,y+1)   
in prime_iter(n,2) end;

fun nextprime(n)=if n=2 then 3 else if isprime(n+2) then n+2 else nextprime(n+2);

fun findPrimes(n)=let 
  fun pr(a,x,y)=if isprime(a-x-y)  then (x,y,a-x-y) else 
                  if x > a div 2 +1 then (0,0,0) else
                  if 0>a-x-y then pr(a,nextprime(x),nextprime(x)) else
                  pr(a,x,nextprime(y))
in pr(n,2,2) end;
findPrimes(1039);

(*problem 2___________________________*)

fun v(1)=500
  | v(2)=700
  | v(3)=300
  | v(4)=200
  | v(5)=300
  | v(n)=0 ;

fun w(1)=40
  | w(2)=80
  | w(3)=30
  | w(4)=50
  | w(5)=20
  | w(n)=11111110;

fun max(a,b)=if a>=b then a else b;

fun maximumValue(n:int,v,w,W:int) = 
  if W<0 then 0-v(n+1) else if n=0 then 0 else
max(maximumValue(n-1,v,w,W),maximumValue(n-1,v,w,W-w(n))+v(n));
maximumValue(5,v,w,100);

(*The following is a iterative algorithm for the same problem
fun mavalue(n:int,v,w,W:int,s:int) = 
  if W<0 then s-v(n+1) else if n<0 then s else
max(mavalue(n-1,v,w,W,s),mavalue(n-1,v,w,W-w(n),s+v(n)));
mavalue(4,v,w,100,0);*)

(*problem 3 ______________*)

fun f(0)="0"
  | f(1)="1"
  | f(2)="2"
  | f(3)="3"
  | f(4)="4"
  | f(5)="5"
  | f(6)="6"
  | f(7)="7"
  | f(8)="8"
  | f(9)="9";

fun toString(n)=if n=0 then "0" else 
let
  fun s_iter(x,y)=if x=0 then y else s_iter(x div 10,f(x mod 10)^y)
in s_iter(n,"") end;

fun name(0)="seconds"
  |name(1)="minutes"
  |name(2)="hours"
  |name(3)="days"
  |name(4)="years"
  |name(5)="millenia"
  |name(n)="";
fun factor(0)=60
  |factor(1)=60
  |factor(2)=24
  |factor(3)=365
  |factor(4)=1000
  |factor(n)=1000000;


fun convertUnitsIter(n,name,factor)=let fun c_iter(a,b,c,x)=if b=0 then a else 
  c_iter(toString(b mod factor(c))^" "^name(x)^" "^a,b div factor(c),c+1,x+1)
in c_iter("",n,0,0) end ;
convertUnitsIter(70000000,name,factor);

fun convertUnitsRec(n,name,factor)=let fun c_rec(x,y,z)=if x=0 then "" else 
  c_rec(x div factor(y),y+1,z+1)^" "^toString(x mod factor(y))^" "^name(z)
in c_rec(n,0,0) end;
convertUnitsRec(70000000,name,factor);

(*problem 4___________________________*)

fun g(n)= let fun g_iter(n,x)=if n div x>=1 andalso 4> n div x then x else g_iter(n,4*x)
in g_iter(n,1) end ;

fun intsqrt(n)= let fun int_iter(x,y,z)=if z=1 then x else 
   if (2*x+1)*(2*x+1) <= y div (z div 4) then  int_iter(2*x+1,y,z div 4) else            int_iter(2*x,y,z div 4)
in
  int_iter(1,n,g(n)) end;

intsqrt(400000000);





