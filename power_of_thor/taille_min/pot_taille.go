package main
import "fmt"
func main(){
  var lx,ly,tx,ty int
  fmt.Scan(&lx,&ly,&tx,&ty)
  for{
	fmt.Scan(&struct{}{})
	move:=""
	if ly>ty{move+="S";ty++}else if ly<ty{move+="N"; ty--}
	if lx>tx{move+="E";tx++}else if lx<tx{move+="W"; tx--}
	fmt.Println(move)}
}
