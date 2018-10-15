global p;
p=15;

global g;
g=3;

pr1 = randi([2 1000],1,1)
pr2 = randi([2 1000],1,1)

a=powermod(g,pr1,p)
b=powermod(g,pr2,p)


ss1 = powermod(b,pr1,p)
ss2 = powermod(a,pr2,p)
