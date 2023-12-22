use std::io::{self, Write};
fn main() {
    let mut input = String::new();
    io::stdin().read_line(&mut input).unwrap();
    let mut coords: Vec<i32> = input.split_whitespace().map(|num| num.parse().unwrap()).collect();
    let (mut c, mut d) = (coords[2], coords[3]);
    loop {
        io::stdin().read_line(&mut input).unwrap();
        let (x, y) = (coords[0], coords[1]);
        let mut move_dir = String::new();
        if d<y {move_dir.push('S'); d+=1; }
        if d>y {move_dir.push('N'); d-=1; }
        if c<x {move_dir.push('E'); c+=1; }
        if c>x {move_dir.push('W'); c-=1; }
        println!("{}", move_dir);
        io::stdout().flush().unwrap();
    }
}
