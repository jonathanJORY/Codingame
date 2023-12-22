#include <stdio.h>
int main(){
 int lx, ly, tx, ty, t;
 scanf("%d %d %d %d",&lx,&ly,&tx,&ty);
 while(scanf("%d",&t)!=EOF){
  printf("%s%s\n",(ly>ty)-(ly<ty)>0?"S":(ly>ty)-(ly<ty)<0?"N":"",(lx>tx)-(lx<tx)>0?"E":(lx>tx)-(lx<tx)<0?"W":"");
  tx+=(lx>tx)-(lx<tx);
  ty+=(ly>ty)-(ly<ty);}
 return 0;
}
