fn main() {
    println!("Hello, world!");

    let x = 5;
    let mut y = 5;
    y = 20;

    println!("y is {y}");

    if x > 5 {
        println!("x is greater than 5");
    } else {
        println!("x is less than or equal 5");
    }

    loop {
        println!("infinite loop");
        break;
    }

    for i in 0..5 {
        println!("i = {} y = {}", i, y);
    }

    // ownership
    //
    let s1 = String::from("hello");
    let len = len(&s1);
    println!("The `{}` has {} length", s1, len);

    let mut s2 = s1;
    //println!("s1 = {}", s1); // Error: s1 is nolonger valid
    change_string(&mut s2);
    println!("s2 = {}", s2);

    s2 = String::from("world");
    println!("s2 = {}", s2);
}

fn len(s: &String) -> usize {
    return s.len();
}

fn change_string(s: &mut String) {
    s.push('!');
}
