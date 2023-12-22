import std.stdio,std.conv,std.string;
void main(){
  auto inputs=strip(readln()).split();
  int lX=to!int(inputs[0]);
  int lY=to!int(inputs[1]);
  int tX=to!int(inputs[2]);
  int tY=to!int(inputs[3]);
  while (true){
    readln();
    string r="";
    if (tY>lY){r~="N";tY--;}
    else if (tY<lY){r~="S";tY++;}
    if (tX>lX){r~="W";tX--;}
    else if (tX<lX){r~="E";tX++;}
    writeln(r);}
}
