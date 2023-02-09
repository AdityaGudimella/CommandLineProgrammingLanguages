# Echo

## Introduction

In this chapter, we're going to build an echo clone. The `echo` command on linux just
prints it's arguments to STDOUT. You can read about the `echo` command here:

- [man pages](https://man7.org/linux/man-pages/man1/echo.1p.html)
- [tldr](https://tldr.ostera.io/echo)

You can also run `man echo` in your shell to see the documentation for `echo`.

### Examples of echo

Here are some example usages:

1. Print a string to STDOUT

    ```bash
    echo Hello
    ```

2. Printing multiple strings to STDOUT

    ```bash
    echo Hello World
    ```

    This outputs `Hello World` to STDOUT.

3. Treatment of spaces between strings

    ```bash
    echo Hello    World  # (1)!
    ```

    1. There are 4 spaces between `Hello` and `World`

    This still outputs `Hello World` to STDOUT. This is because `echo` treats `Hello`
    and `World` as separate arguments. (This is true at least for the `bash` and `zsh`
    shells)

4. Getting spaces between parts to show

    ```bash
    echo "Hello    World"  # (1)!
    ```

    1. Note the quotes surrounding the words.

    This will output `Hello    World` as we intended it to.

5. The `-n` argument

    ```bash
    echo -n Hello World
    ```

    This will output `Hello World` without a trailing newline. This is useful if you
    want to print something to STDOUT and then prompt the user for input on the same
    line.


## Building the echo clone

We will create an `echo` clone named `echo_` that supports the `-n` optional argument.
Note the `_` at the end of our project. We do this to not mask the builtin `echo`
program.

### Creating the project

Let's create a new project for this.

=== "C#"

    TODO: WIP
=== "Python"

    TODO: WIP
=== "Rust"

    ```bash title="From parent dir of project"
    cargo new echo_  # (1)!
    ```

    1. I haven't specified the `--bin` argument. It is the default project type.


#### Directory structure

The directory structure looks like follows:

```bash title="From parent dir of project"
tree echo_
```

=== "C#"
    TODO: WIP
=== "Python"
    TODO: WIP
=== "Rust"

    ```bash title="Output"
    echo_
    ├── Cargo.toml
    └── src
        └── main.rs
    ```

There's nothing interesting to see here, so let's move on to the code.

### The code

Our clone must output whatever is passed as its arguments. This means that we need to be
able to access the command-line arguments from within our program.

=== "C#"
    TODO: WIP
=== "Python"
    TODO: WIP
=== "Rust"

    We can interact with the environment in rust using the `std::env` crate. It provides
    an [args](https://doc.rust-lang.org/std/env/fn.args.html) function that returns the
    arguments that the program was started with. It returns an struct of type
    [Args](https://doc.rust-lang.org/std/env/struct.Args.html). So we can basically
    get the command-line arguments to our program by calling `std::env::args()`.

    We can use the [println!](https://doc.rust-lang.org/std/macro.println.html) macro to
    print text to the console, but trying to print the arguments directly as
    `println!(std::env::args());` will not work. This is becasue the `println!` macro
    expects a string literal, but we're passing it an `Args` struct.

    If you try to run the following program, the program will fail to compile:

    ```rust title="src/main.rs"
    fn main() {
        println!(std::env::args());
    }
    ```

    It will give you the following error:

    ```bash title="Repo root"
    cargo run
    ```

    ```bash title="Output"
    error: format argument must be a string literal
    --> src/main.rs:2:14
    |
    2 |     println!(std::env::args());
    |              ^^^^^^^^^^^^^^^^
    |
    help: you might be missing a string literal to format with
    |
    2 |     println!("{}", std::env::args());
    |              +++++

    error: could not compile `echo_` due to previous error
    ```

    The compiler is pointing us in the right direction here. Let's try it's suggestion:

    ```rust title="src/main.rs"
    fn main() {
        println!("{}", std::env::args());
    }
    ```

    Running this will give us another error:

    ```bash title="Error Output"
    error[E0277]: `Args` doesn't implement `std::fmt::Display`
    --> src/main.rs:2:20
    |
    2 |     println!("{}", std::env::args());
    |                    ^^^^^^^^^^^^^^^^ `Args` cannot be formatted with the default formatter
    |
    = help: the trait `std::fmt::Display` is not implemented for `Args`
    = note: in format strings you may be able to use `{:?}` (or {:#?} for pretty-print) instead
    = note: this error originates in the macro `$crate::format_args_nl` which comes from the expansion of the macro `println` (in Nightly builds, run with -Z macro-backtrace for more info)

    For more information about this error, try `rustc --explain E0277`.
    error: could not compile `echo_` due to previous error
    ```

    The compiler is telling us that for a struct to be formatted as a string, it needs
    to implement the `std::fmt::Display`
