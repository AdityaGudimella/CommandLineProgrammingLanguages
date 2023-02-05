use std::process::Command;  // 1

#[test]
fn hello() {
    let mut cmd = Command::new("./target/debug/hello_world");  // 2
    let result = cmd.output().unwrap();  // 3
    assert_eq!(String::from_utf8(result.stdout).unwrap(), "Hello, world!\n"); // 4
}
