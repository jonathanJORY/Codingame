using System;
class Player {
  static void Main(string[] args) {
    string[] inputs=Console.ReadLine().Split(' ');
    int lX=int.Parse(inputs[0]);
    int lY=int.Parse(inputs[1]);
    int tX=int.Parse(inputs[2]);
    int tY=int.Parse(inputs[3]);
      while (true) {
        int remainingTurns=int.Parse(Console.ReadLine());
        int dx=Math.Sign(lX-tX);
        int dy=Math.Sign(lY-tY);
        tX+=dx;
        tY+=dy;
        Console.WriteLine((dy>0?"S":(dy<0?"N":""))+(dx>0?"E":(dx<0?"W":"")));}
    }
}
