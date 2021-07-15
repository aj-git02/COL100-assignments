(* problem 1________________*)

fun f(n)=
if n=1 then 1 else if n=2 then 2 else f(n-1)+f(n-2);
f(4);

(*problem 2______________________*)

fun modifiedDigitSum(n)=if n<>0 then 2*modifiedDigitSum(n div 10)+n mod 10 else 0;
modifiedDigitSum(132);

(*problem 3_______________*)

fun issquare(a,b)=if a<b then false else if a=b*b then true else issquare(a,b+1);

fun canitself(x,y)=if y>x then false else if issquare(x-y*y,0)
 then true else canitself(x,y+1);

fun squaredCount(n)= if n=1 then 1 else 
if canitself(n,0)
then squaredCount(n-1)+1 else squaredCount(n-1);
squaredCount(20);
squaredCount(50);


(*problem 4_________________*)

fun abs(x :real)=if x<0.0 then ~x else x;

fun sum(f,a,b):real=if a>b then 0.0 else f(a)+sum(f,a+1,b);

fun nterm(n)=if n mod 2 =1 then 4.0/(2.0*real(n)*(2.0*real(n)+1.0)*(2.0*real(n)+2.0)) else ~4.0/(2.0*real(n)*(2.0*real(n)+1.0)*(2.0*real(n)+2.0));

fun nilakanthaSum(t)=if t>3.0 then 3.0 else 
let 
  fun greatest(t,x)= if abs(nterm(x)) < t then x else greatest(t,x+1);
in 3.0+ sum(nterm,1,greatest(t,1))
end;
nilakanthaSum(0.000001);
nilakanthaSum(5.0);


  
