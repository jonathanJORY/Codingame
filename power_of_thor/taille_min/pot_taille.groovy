Scanner sc=new Scanner(System.in)
int lx=sc.nextInt(),ly=sc.nextInt(),tx=sc.nextInt(),ty=sc.nextInt()
while (true){
  sc.nextInt()
  int dx=lx<=>tx,dy=ly<=>ty
  tx+=dx
  ty+=dy
  println("${dy<0?'N':dy>0?'S':''}${dx>0?'E':dx<0?'W':''}")}
