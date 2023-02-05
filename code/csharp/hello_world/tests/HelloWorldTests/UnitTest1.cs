namespace HelloWorldTests;
using System;
using Xunit;
using HelloWorldApp;

public class UnitTest1
{
    [Fact]
    public void Test1()
    {
        // Arrange
        var writer = new StringWriter();
        Console.SetOut(writer);

        // Act
        Program.Main();

        // Assert
        var sb = writer.GetStringBuilder();
        Assert.Equal("Hello, World!\n", sb.ToString());

    }
}
