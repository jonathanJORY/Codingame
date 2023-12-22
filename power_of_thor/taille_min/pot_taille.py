l,m,t,u=map(int,input().split())
while input():
 d,e=(l>t)-(l<t),(m>u)-(m<u);t+=d;u+=e;print('S'*(e>0)+'N'*(e<0)+'E'*(d>0)+'W'*(d<0))
