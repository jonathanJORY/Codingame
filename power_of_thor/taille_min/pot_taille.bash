#!/bin/bash
read -r lx ly tx ty
while true; do
  read -r remaining_turns
  dx=$((lx>tx?1:(lx<tx?-1:0)))
  dy=$((ly>ty?1:(ly<ty?-1:0)))
  ((tx+=dx))
  ((ty+=dy))
  move=""
  [[ $dy -gt 0 ]]&&move+="S"
  [[ $dy -lt 0 ]]&&move+="N"
  [[ $dx -gt 0 ]]&&move+="E"
  [[ $dx -lt 0 ]]&&move+="W"
  echo "$move"
done
