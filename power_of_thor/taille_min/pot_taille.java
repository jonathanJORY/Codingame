package taille_min;
import java.util.*;
class Player{public static void main(String a[]){
Scanner s=new Scanner(System.in);
int lx=s.nextInt(),ly=s.nextInt(),tx=s.nextInt(),ty=s.nextInt();
while(s.hasNext()){s.next();int dx=Integer.compare(lx,tx),dy=Integer.compare(ly,ty);
tx+=dx;ty+=dy;System.out.println((dy>0?"S":dy<0?"N":"")+(dx>0?"E":dx<0?"W":""));}
s.close();}}
