import java.util.*
fun main() {
  val i = Scanner(System.`in`)
  val lx = i.nextInt()
  val ly = i.nextInt()
  var tx = i.nextInt()
  var ty = i.nextInt()
  while (true){
    i.nextInt()
    print((if(ty<ly)"S" else if(ty>ly)"N" else "").also{ty+=ly.compareTo(ty)}+(if(tx<lx)"E" else if(tx>lx)"W" else "").also{tx+=lx.compareTo(tx)}+"\n")}
}
