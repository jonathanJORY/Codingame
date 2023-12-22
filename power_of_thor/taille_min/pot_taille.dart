import 'dart:io';
void main(){
  var inputs=stdin.readLineSync()!.split(' ');
  int lx=int.parse(inputs[0]),ly=int.parse(inputs[1]),tx=int.parse(inputs[2]),ty=int.parse(inputs[3]);
  while (true){
    stdin.readLineSync();
    print('${(ty<ly?'S':ty>ly?'N':'')}${(tx<lx?'E':tx>lx?'W':'')}');
    tx+=(lx-tx).sign;
    ty+=(ly-ty).sign;}
}