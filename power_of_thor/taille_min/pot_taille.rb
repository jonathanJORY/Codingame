STDOUT.sync=true
a,b,c,d=gets.split.map(&:to_i)
loop do
  gets
  x=c< a ?(c+=1;"E"):c>a ?(c-=1;"W"):""
  y=d< b ?(d+=1;"S"):d>b ?(d-=1;"N"):""
  puts y+x
end
