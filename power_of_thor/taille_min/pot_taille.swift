import Foundation
let i=readLine()!.split(separator: " ").map{Int($0)!}
let a=i[0]
let b=i[1]
var c=i[2]
var d=i[3]
while true {
    let _=readLine()!
    let dx=(a>c) ? 1:(a<c) ? -1:0
    let dy=(b>d) ? 1:(b<d) ? -1:0
    c+=dx
    d+=dy
    let moveY=dy>0 ? "S":dy<0 ? "N":""
    let moveX=dx>0 ? "E":dx<0 ? "W":""
    print(moveY + moveX)
}
