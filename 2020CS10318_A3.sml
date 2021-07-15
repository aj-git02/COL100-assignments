(*problem 1*)
fun IntToLgint(n)=if n div 10 =0 then [n] else (n mod 10)::IntToLgint(n div 10);
fun len(x)= if x=[] then 0 else 1+len(tl(x));
fun LgintToInt(n)=if len(n)>10 then 1000000000 else if n=[] then 0 else hd(n)+LgintToInt(tl(n));

fun addLgint([],y)=y
  | addLgint(x,[])=x
  | addLgint([],[])=[]
  | addLgint(x,y)=
let val c=hd(x)+hd(y) in
  if c>9 then if tl(x)=[] then [c-10]@addLgint([1],tl(y)) else
  [c-10]@addLgint((1+hd(tl(x)))::tl(x),tl(y)) 
    else [c]@addLgint(tl(x),tl(y))
end;

fun last(l)= if tl(l)=[] then hd(l) else last(tl(l)); 

fun Lglesseq(x,y)=if len(x)>len(y) then false else if len(x)<len(y) then true else
if last(x)>last(y) then false else if last(x)<last(y) then true else
if tl(x)=[] then true else Lglesseq(tl(x),tl(y));

(* problem 2*)
fun per(a:int,b)= (real(a)-b)*100.0/b;

fun increament(a,b,c,d)=
let fun inc(x)=if x<0.0 then 0 else 1+inc(x-10.0)
in inc(a-10.0)+inc(b-10.0)+inc(c-10.0)+inc(d-10.0) end;

fun add(x:real,y)=x+y;

per(60,100.0/3.0);

fun qPerformance(l)=
let val A= (foldl add 0.0 (map (fn (a,b,c,d,e) => real(a)) l)) / real(len(l))
  val B= (foldl add 0.0 (map (fn (a,b,c,d,e) =>real(b)) l)) / real(len(l))
  val C= (foldl add 0.0 (map (fn (a,b,c,d,e) =>real(c)) l)) / real(len(l))
  val D= (foldl add 0.0 (map (fn (a,b,c,d,e) =>real(d)) l)) / real(len(l));
in 
 map (fn (a,b,c,d,e) => real(e)*((100.0+real(increament(per(a,A),per(b,B),per(c,C),per(d,D))))/100.0)) l end;

qPerformance([(10, 20, 30, 40, 100000), (30, 30, 20, 50, 150000), (60, 10, 10, 50,
200000)]);
(*last salary has 7% hike instead of 8% because SML not changing 79.99999 to 80*)

fun budgetRaise(l)=let 
val a=foldl add 0.0 (qPerformance(l))
val  b=map (fn (a,b,c,d,e) =>real(e)) l
 val c= foldl add 0.0 b
in (a-c)*100.0/c end;

(*problem 3*)

fun consmap(x,y)=if y=[] then [] else (x::hd(y))::consmap(x,tl(y));

fun ielem(x,y,l)=if x=y then hd(l) else ielem(x,y+1,tl(l));

fun irem(x,y,l)= if x=y then tl(l) else hd(l)::irem(x,y+1,tl(l));

fun specialmap(f,g,l,i)=if i=len(l) then [] else 
f(ielem(i,0,l),g(irem(i,0,l)))@specialmap(f,g,l,i+1);

fun lexicographicPerm(n)=if tl(n)=[] then [n] else
consmap(hd(n),lexicographicPerm(tl(n)))@specialmap(consmap,lexicographicPerm,n,1);


lexicographicPerm ["a","b","c"];









 





