# Hello World

## Introduction

In this chapter, we learn how to organize, run and test a program. The book uses a Unix
platform to demonstrate the concepts, and so will I. I'm using Ubuntu 22.04. I do expect
some familiarity with Unix for you to be able to follow along with this "book".

You will learn how to do the following:

- Create an executable / command line script
- Initialize a new project
- Include external libraries / projects as dependencies
- Interpret the exit status of the program
- Use common system commands and options
- Write `<insert programming language>` versions of `true` and `false` programs
- Organize, write and run tests


## Writing and running the code

The first program we will write is the classic "Hello, World!" program. This program
prints "Hello, World!" to the screen. To do that, we will create a new project.

### Creating the project

We can create a new project manually, but it's easier to use a tool to do it for us.
Most languages have a package manager and build tool that can create a new project for
us. We'll use the package manager and build tool for each language to create a new
project.

=== "C#"
    We could use the `dotnet new` command to create our project, but the directory
    structure it creates does not follow the best practices suggested by the .Net
    community. We can still use the `dotnet` command to help us though.

    ```bash title="From parent dir of repo"
    mkdir -p HelloWorld/src
    cd HelloWorld
    dotnet new sln
    dotnet new Console -o src/HelloWorldApp
    dotnet sln add src/HelloWorldApp/HelloWorldApp.csproj
    ```
=== "Python"
    To create a new Python project, we use the `poetry` command. Poetry is _a_ Python
    package manager and build tool. I say it is "a" python package manager instead of
    "the" because python has more than one package managers. Poetry is my favorite
    and I'd highly recommend it.

    ```bash title="From parent dir of repo"
    poetry new hello
    ```

=== "Rust"
    To create a new Rust project, we use the `cargo` command. Cargo is the Rust package
    manager and build tool.

    ```bash title="From parent dir of repo"
    cargo new --bin hello
    ```

#### What just happened?

When we create a new project, we are telling the package manager and build tool to
create a new project with the name `hello`. The package manager and build tool will
create a new directory with the name `hello` and create a new project in that
directory.

### Directory structure

Let's take a look at the directory structure of the project.

We can use the [tree](https://linux.die.net/man/1/tree) command to see the directory
structure of the project.

<!-- trunk-ignore(markdownlint/MD046) -->
```bash title="From parent dir of repo"
tree hello
```

=== "C#"

    ```bash title="Output"
    HelloWorld
    ├── HelloWorld.sln
    └── src
        └── HelloWorldApp
            ├── Program.cs
            ├── HelloWorldApp.csproj
            └── obj
                ├── HelloWorldApp.csproj.nuget.dgspec.json
                ├── HelloWorldApp.csproj.nuget.g.props
                ├── HelloWorldApp.csproj.nuget.g.targets
                ├── project.assets.json
                └── project.nuget.cache

    3 directories, 8 file
    ```

    The directory structure created by the `dotnet new` command does not follow the
    best practices followed by the `dotnet` community. See Scott Hanselman's
    [blog post](http://www.hanselman.com/blog/how-do-you-organize-your-code) on defining
    the directory structure for your projects.

=== "Python"

    ```bash title="Output"
    hello
    ├── README.md
    ├── hello
    │   └── __init__.py
    ├── pyproject.toml
    └── tests
        └── __init__.py

    2 directories, 4 files
    ```
=== "Rust"

    ```bash title="Output"
    hello
    ├── Cargo.toml
    └── src
        └── main.rs

    1 directory, 2 files
    ```

While each language has a different directory structure, there are a few similarities
between them.

- Each project has a main file where the code goes.
- Each project has a configuration file that contains the project information and
  dependencies.

### The configuration file

The configuration file typically contains information like project metadata, package
dependencies, tool directives etc. Let's take a look at the configuration file created.

=== "C#"

    ```xml title="src/HelloWorldApp/HelloWorldApp.csproj"
    <Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <OutputType>Exe</OutputType>  <!-- (1)! -->
        <TargetFramework>net6.0</TargetFramework>  <!-- (2)! -->
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>
    </PropertyGroup>
    ```

    1. This tells the build tool that the project is an executable.
    2. The dotnet version shown here will depend on the dotnet version installed on your
       system.
=== "Python"

    ```toml title="pyproject.toml"
    [tool.poetry]
    name = "hello"
    version = "0.1.0"
    description = ""
    authors = ["Aditya Gudimella <aditya.gudimella@gmail.com>"]
    readme = "README.md"

    [tool.poetry.dependencies]  # (1)!
    python = "^3.10"  # (2)!


    [build-system]
    requires = ["poetry-core"]
    build-backend = "poetry.core.masonry.api"
    ```

    1. This is where you list the libraries that your application depends on.
    2. This specifies the python versions on which this application will be supported.
       The version on your system may be different based on the python version present
       on your system.

    The `^3.10` notation means that our application will support python versions "3.10"
    and above.
=== "Rust"

    ```toml title="Cargo.toml"
    [package]
    name = "hello"
    version = "0.1.0"
    edition = "2021"

    # See more keys and their definitions at https://doc.rust-lang.org/cargo/reference/manifest.html

    [dependencies]  # (1)!
    ```

    1. This is where you list the libraries that your application depends on.

### The code

=== "C#"
    The entry point to a C# program is the `Main` method of a `Program` class. The
    `Main` method is the first method that is executed when the program is run. The
    `Program` class is the first class that is loaded when the program is run. Any
    application must contain at most one `Main` method. `dotnet` will raise an error
    if you try to create a project with more than one `Main` method.


    ```csharp title="src/HelloWorldApp/Program.cs"
    namespace HelloWorldApp;
    using System;

    public class Program
    {
        public static void Main()
        {
            Console.WriteLine("Hello, World!");  // (1)!
        }
    }
    ```

    1. The `;` at the end of the line is used to terminate a statement in C#.

    `Console.WriteLine` is a method that is used to print a line to the console. This is
    part of the `System` namespace. The `using` statement is used to import namespaces
    into the program.

    In C# 9.0 and greater, you can take advantage of Top-Level Statements. This means
    you can omit the `Program` class and the `Main` method. You can read more about
    Top-Level Statements [here](https://docs.microsoft.com/en-us/dotnet/csharp/fundamentals/program-structure/top-level-statements).
=== "Python"
    The entry point to a Python program is the file that is executed. Python doesn't
    require a `main` method or a `Program` class. Python will execute any code that is
    in the file. If you're making a command line script, you can define entry points to
    your application by defining it in the `pyproject.toml` file. We'll see that in
    action once we get to actually executing the programs.

    ```python title="hello/__init__.py"
    print("Hello, World!")  # (1)!
    ```

    1. Notice the lack of an ending `;` in Python. Python uses indentation and new lines
       to determine the scope of a block of code.

    The `print` function in python is used to print text to STDOUT. It adds a new line
    character at the end of the line, but this can be overriden.
=== "Rust"
    The entry point to a Rust program is the `main` function. Rust doesn't require a
    `Program` class. The `main` function is the first function that is executed when the
    program is run.


    ```rust title="src/main.rs"
    fn main() {
        println!("Hello, World!");  // (1)!
    }
    ```

    1. The `;` at the end of the line is used to terminate a statement in Rust.

    `println!` is a macro. It prints text to STDOUT. It adds a new line character at
    the end of the line.

### Running the program

Now that we have a program, let's run it. The commands are run from the root of the
repository.

=== "C#"

    ```bash title="From repo root"
    dotnet run --project src/HelloWorldApp/HelloWorldApp.csproj
    ```

    This will build the project and run the executable. The output will be similar to
    this:

    ```bash title="Output"
    Hello, World!
    ```
=== "Python"

    ```bash title="From repo root"
    poetry run python hello/__init__.py
    ```

    This will run the program. The output will be similar to this:

    ```bash title="Output"
    Hello, World!
    ```
=== "Rust"

    ```bash title="From repo root"
    cargo run
    ```

    This will build the project and run the executable. The output will be similar to
    this:

    ```bash title="Output"
    Hello, World!
    ```

### The executable

When you run the program, if the language is a compiled language, the program will be
compiled into an executable or byte code.

<!-- trunk-ignore(markdownlint/MD046) -->
```bash title="From parent dir of repo"
tree hello
```

=== "C#"

    C# is a compiled and managed language. The compiled code is run by a runtime called
    CLR.

    ```bash title="Output"
    hello
    ├── HelloWorld.sln
    └── src
        └── HelloWorldApp
            ├── bin
            │   └── Debug
            │       └── net6.0
            │           ├── HelloWorldApp
            │           ├── HelloWorldApp.deps.json
            │           ├── HelloWorldApp.dll
            │           ├── HelloWorldApp.pdb
            │           └── HelloWorldApp.runtimeconfig.json
            └── ...
    ```
=== "Python"

    Python is an compiled and interpreted language. The code is compiled to bytecode,
    and the resulting bytecode is interpreted by the python interpreter. For larger
    applications, you will typically see `*.pyc` files generated after the first time
    the program is run. For our program, there is no change to the directory structure.
=== "Rust"

    Rust is a compiled and unmanaged language. The code is compiled to a binary that is
    directly executed by the OS. Unlike C#, rust has no runtime.

    ```bash title="Output"
    hello
    ├── Cargo.lock
    ├── Cargo.toml
    ├── src
    │   └── main.rs
    └── target
        ├── ...
        └── debug
            ├── ...
            ├── hello
            └── ...
    ```

## Writing and running tests

Let's create some directories to hold our tests. Our directory structure now looks like
this.

<!-- trunk-ignore(markdownlint/MD046) -->
```bash title="From parent dir of repo"
tree hello
```

=== "C#"

    We will create a `tests` directory where we will put our tests.

    ```bash title="From repo root"
    mkdir tests
    dotnet new xunit -o tests/HelloWorldTests
    dotnet sln add tests/HelloWorldTests/HelloWorldTests.csproj
    ```

    This adds a new project named hello in the `tests` folder.

    ```bash title="tree"
    hello
    ├── ...
    ├── obj
    │   └── ...
    ├── src
    │   └── ...
    └── tests
        └── HelloWorldTests
            ├── UnitTest1.cs
            ├── Usings.cs
            ├── HelloWorldTests.csproj
            └── obj
                └── ...
    ```

    Specifying the project type as `xunit` when running `dotnet new xunit ...` results
    in a slightly different project configuration file.

    ```xml title="hello/tests/tests.csproj"
    <Project Sdk="Microsoft.NET.Sdk">

    <PropertyGroup>
        <TargetFramework>net6.0</TargetFramework>
        <ImplicitUsings>enable</ImplicitUsings>
        <Nullable>enable</Nullable>

        <IsPackable>false</IsPackable>
    </PropertyGroup>

    <ItemGroup>
        <PackageReference Include="Microsoft.NET.Test.Sdk" Version="17.1.0" />
        <PackageReference Include="xunit" Version="2.4.1" />  <!-- (1)! -->
        <PackageReference Include="xunit.runner.visualstudio" Version="2.4.3">
        <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        <PrivateAssets>all</PrivateAssets>
        </PackageReference>
        <PackageReference Include="coverlet.collector" Version="3.1.2">
        <IncludeAssets>runtime; build; native; contentfiles; analyzers; buildtransitive</IncludeAssets>
        <PrivateAssets>all</PrivateAssets>
        </PackageReference>
    </ItemGroup>

    </Project>
    ```

    1. We see some additional project dependencies here, `xunit` being one of them.

    We will add tests to the `tests/hello/UnitTest1.cs` file.

=== "Python"

    Poetry has already created a tests directory for us. Python has a builtin library
    called unit tests to run tests, but there is a better tool for the job. It's called
    [pytest](https://docs.pytest.org/). We can add it to our project by running the
    following command from within the repository.

    ```bash title="From repo root"
    poetry add pytest
    ```

    This will install pytest and its dependencies into our active environment. Our
    `pyproject.toml` file has also been updated to indicate that pytest is a dependency
    for this project.

    ```toml title="hello/pyproject.toml"
    [tool.poetry]
    ...

    [tool.poetry.dependencies]
    python = "^3.10"
    pytest = "^7.2.1"

    ...
    ```

    Let's create a new file called `test_hello.py` in the tests dir. We will add our
    tests to this file. Execute the following command.

    ```bash title="From repo root"
    touch tests/test_hello.py
    ```

    ```bash title="tree"
    hello
    ├── ...
    └── tests
        ├── __init__.py
        └── test_hello.py
    ```

=== "Rust"

    We will create a `tests` directory where we will put our tests. This directory lives
    at the same level as the `src` directory.

    ```bash title="From repo root"
    mkdir tests
    ```

    ```bash title="tree"
    hello
    ├── ...
    ├── src
    │   └── ...
    └── tests
    ```

    Rust has a builtin functionality for [testing](https://doc.rust-lang.org/book/ch11-00-testing.html).
    We will use this functionality to write our tests. We will create a file called
    `test_hello.py` in the `tests` dir we created above.

### Writing our first test

Let's add the actual tests now.

=== "C#"

    ```csharp title="tests/hello/UnitTest1.cs"
    using System;
    using Xunit;  // 1

    namespace hello
    {
        public class UnitTest1  // 2
        {
            [Fact]  // 4
            public void Test1()  // 3
            {
                Assert.Equal(0, 0);  // 5
            }
        }
    }
    ```

    1. We have imported the `Xunit` library.
    2. We have created a class called `UnitTest1`.
    3. We have created a method called `Test1` which contains the actual test.
    4. The `[Fact]` attribute is used to mark it as a test method.
    5. The test method creates an assertion to check that `0 == 0`. We're starting
       simple here.
=== "Python"

    ```python title="tests/test_hello.py"
    def test_hello():  # 1 # (1)!
        assert True  # 2
    ```

    1. The test needs to named as `test_...` for `pytest` to understand that it is a
       test it needs to run.

    Note that pytest doesn't have any annotations to discover tests that it needs to
    run. Any file named `test_...` will be checked for tests. If that file contains
    a function with the name starting with `test_` the function will be picked up as
    a test that needs to be run.

    1. We create a function which will contain the testing logic. We could put the test
       in a class too, but it's not necessary.
    2. Since we just `assert True` the test will always pass. We're starting simple.

=== "Rust"

    ```rust title="tests/test_hello.rs"
    #[test]  // 2
    fn hello() {  // 1
        assert!(true);  // 3
    }
    ```

    1. We define a function named `hello` to hold our test logic.
    2. We need to annotate the function with the `#[test]` attribute to tell Rust to
       run this function when testing.
    3. `assert!` is a macro. Since we're just `assert!(true)`, the test will always pass.
       We're starting simple here.

### Running the tests

Now that we have written our tests, let's run them.

=== "C#"

    ```bash title="From repo root"
    dotnet test
    ```

    You should see the following lines as part of the output.

    ```bash title="Output"
    Starting test execution, please wait...
    A total of 1 test files matched the specified pattern.

    Passed!  - Failed:     0, Passed:     1, Skipped:     0, Total:     1, Duration: < 1 ms
    ```
=== "Python"

    ```bash title="From repo root"
    pytest
    ```

    You should see the following lines as part of the output.

    ```bash title="Output"
    collected 1 item

    tests/test_hello.py .                                                  [100%]

    ============================= 1 passed in 0.01s ==============================
    ```
=== "Rust"

    ```bash title="From repo root"
    cargo test
    ```

    You should see the following lines as part of the output.

    ```bash title="Output"
    running 1 test
    test hello ... ok

    test result: ok. 1 passed; 0 failed; 0 ignored; 0 measured; 0 filtered out; finished in 0.00s
    ```

### Modifying the tests to test the output in the command line

Our test currently passes regardless of whether our program is correct or not. We need
to change it so that it's testing the actual application logic. Let's modify the tests
so that we ensure that the output of the application is indeed "Hello, World!"

=== "C#"

    ```bash title="From repo root"
    dotnet add tests/HelloWorldTests/HelloWorldTests.csproj reference src/HelloWorldApp/HelloWorldApp.csproj
    ```

    ```csharp title="tests/HelloWorldTests/UnitTest1.cs"
    using System;
    using HelloWorldApp;  // 1
    using Xunit;

    namespace HelloWorldTests;

    public class UnitTest1
    {
        [Fact]
        public void Test1()
        {
            // Arrange
            var writer = new StringWriter();  // 3
            Console.SetOut(writer); // 4

            // Act
            Program.Main();  // 2

            // Assert
            var sb = writer.GetStringBuilder();
            Assert.Equal("Hello, World!", sb.ToString().Trim());  // 5
        }
    }
    ```

    1. We're using the `HelloWorldApp` namespace we defined above.
    2. We're calling the `Program.Main()` method to test the code.
    3. We're creating a `StringWriter()` instance to which we will redirect the output
       of the `Console` class.
    4. We're telling `Console` to redirect its output to the `StringWriter` instance
       we created.
    5. We assert that the output of the program as captured by the `StringWriter` is the
       same as the expected output.
=== "Python"

    Let's modify our source code a little so that it's easier to test.

    ```python title="hello/__init__.py"
    def hello_world():
        print("Hello, World!")

    if __name__ == "__main__":  # (1)!
        hello_world()
    ```

    1. This tells python to run the body under the condition only when the file is run
       directly and not when the module (file) is imported in another module. See this
       [article](https://realpython.com/python-main-function/) for more information.

    Now we have a function that we can actually test.

    ```python title="tests/test_hello.py"
    from hello import hello_world  # 1

    def test_hello(capsys):  # 5
        hello_world()  # 2
        captured = capsys.readouterr()  # 3
        assert captured.out == "Hello, World!\n"  # 4
    ```

    1. We import the `hello_world` function from the `hello` module.
    2. We call the `hello_world` function.
    3. We use an object named `capsys` that is "magically" passed into our test function
       to capture the stdout and stderr generated during the execution of the test.
    4. We assert that the stdout resulting from calling the `hello_world` function is
       indeed "Hello, World!".
    5. We declare `capsys` as a parameter of our test function. This is called a
       `fixture` in `pytest`. Pytest provides a set of predefined fixtures, `capsys`
       being one of them. You use fixtures by defining them as parameters in your test
       function. Pytest will take care of passing in the actual objects when running
       the test. See pytest's [documentation](https://docs.pytest.org/en/latest/explanation/fixtures.html)
       for more details on fixtures.
=== "Rust"

    ```rust title="tests/test_hello.rs"
    use std::process::Command;  // 1

    #[test]
    fn hello() {
        let mut cmd = Command::new("./target/debug/hello");  // 2
        let result = cmd.output().unwrap();  // 3
        assert_eq!(String::from_utf8(result.stdout).unwrap(), "Hello, world!\n"); // 4
    }
    ```

    1. We import a builtin struct called `Command` that willl let us run CLI commands
       and capture the output from those commands.
    2. We run the executable that Cargo previously created for us when we ran the
       `cargo run` command. Note that we need to hard code the path to the executable.
       This test would have failed if we hadn't previously already generated the
       executable.
    3. We get the output of running the command. The result of `cmd.output()` is an
       `Result<Output>` type that may either contain the actual result or an error if
       one is raised. We call tye `unwrap()` method on it because we don't expect it to
       raise an error. If getting the output did indeed raise an error, rust would
       panic at this point and exit the program, which would cause the test to fail.
    4. The `Output` struct has a field called `stdout` that contains the output written
       to the STDOUT by our program. The type of this field is `Vec<u8>`. For now, it
       is sufficient to know that we can convert that into a `String` type by calling
       the `String::from_utf8` constructor. Note that this too returns a `Result` type
       and we unwrap it as we did before.

We can execute the tests as before, and ensure that the test is passing. That's it for
this chapter. In the next chapter, we'll build an `echo` clone. We'll improve some of
our tooling to create good command line applications.

## Summary

In this chapter, we created a simple "Hello, World!" application that prints
"Hello, World!" to the console. We added some tests to the application. Through the
process we learned how to:

- Create new projects
- Configure projects
- Add dependencies
- Run the application
- Add tests
- Run the tests

## Code

You can find the code for this chapter here:

=== "C#"
    [Chapter 1](../code/csharp/HelloWorld/)
=== "Python"
    [Chapter 1](../code/python/hello_world/)
=== "Rust"
    [Chapter 1](../code/rust/hello_world/)
