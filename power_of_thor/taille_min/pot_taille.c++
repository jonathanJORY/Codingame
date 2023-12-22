#include<iostream>
int main(){
 int lx,ly,tx,ty;
 std::cin>>lx>>ly>>tx>>ty;
 while(1){
 int t;std::cin>>t;int dx=(lx>tx)-(lx<tx),dy=(ly>ty)-(ly<ty);
 tx+=dx;ty+=dy;
 std::cout<<(dy>0?"S":dy<0?"N":"")<<(dx>0?"E":dx<0?"W":"")<<'\n';}
}
