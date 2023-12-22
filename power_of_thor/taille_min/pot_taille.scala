import scala.io.StdIn._
object Player extends App{
  val Array(e,f,a,b)=readLine.split(" ").map(_.toInt)
  var(x,y)=(a,b)
  while(true){
    readLine
    print((if(f>y)"S"else if(f<y)"N"else"")+{y+=math.signum(f-y);""}+(if(e>x)"E"else if(e<x)"W"else"")+{x+=math.signum(e-x);"\n"})
  }
}
