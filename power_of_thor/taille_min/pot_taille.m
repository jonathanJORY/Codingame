#import <Foundation/Foundation.h>
int main(){
  int lx,ly,tx,ty;
  scanf("%d%d%d%d",&lx,&ly,&tx,&ty);
  while (1){
    printf("%s%s\n",(ty<ly?"S":ty>ly?"N":""),(tx<lx?"E":tx>lx?"W":""));
    tx+=(tx<lx)-(tx>lx);
    ty+=(ty<ly)-(ty>ly);
    scanf("%*d");}
}
