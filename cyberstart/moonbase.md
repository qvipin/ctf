# Moon Base

### Level 1

- C1 - Programming 101
    
    ```python
    # This is a code comment
    # Anything with a '#' before it is considered a comment and ignored.
    # You can use these for writing notes about what your code is doing.
    # This is so you can understand it more easily if you
    # come back to it after some time.
    
    # In Python, you can output text to the screen using the print function.
    # The function is print("text")
    
    print("text")
    
    # You can also print numbers out. With numbers, you don't have to
    # put them in quotation marks.
    
    print(42)
    
    # CHALLENGE 1: First print out the text: Hello, World
    print("Hello, World")
    
    # CHALLENGE 2: Next print out the numbers: 1337
    print(1337)
    ```
    
- C2 - Handy Variables
    
    ```python
    # A variable is just a box with a label on it that can hold something.
    
    # What you put in the box is up to you, but no matter what is inside,
    # you can refer to whatever is there by the label on the box.
    
    stuff = "hello"
    print(stuff)
    
    stuff = "world!"
    print(stuff)
    
    # See? The contents of the variable 'stuff' changed, but we can still
    # refer to whatever is there by the label on the box.
    
    # In programming, there are different 'types' of information.
    # Learn the ones below.
    # String - A string is text. Strings usually have to be wrapped
    # in quotation marks.
    # Integer - An integer is a whole number. Integers shouldn't have
    # quotation marks.
    # Float - A float is a number with a decimal point. Floats shouldn't
    # have quotation marks.
    # Boolean - A boolean value can either be True or False. Boolean
    # values shouldn't have quotes.
    
    # Python automatically changes the type of data a variable can hold
    # depending on what you try to put into it.
    # Sometimes it won't be able to do it automatically, and you'll have
    # to convert it yourself.
    
    # CHALLENGE 1: First create a variable called aString and assign it
    # the following text: Testing
    # Remember the format to assign data to a variable
    # ie: variableName = "SomeValue"
    
    aString = "Testing"
    
    # CHALLENGE 2: Next create a variable called anInt and assign it the
    # following number: 899
    # Remember, you don't need quotes for numbers!
    
    anInt = 899
    
    # CHALLENGE 3: Next create a variable called aFloat and assign it the
    # following number: 12.55
    
    aFloat = 12.55
    
    # CHALLENGE 4: Next create a variable called aBool and assign it the
    # value False.
    
    aBool = False
    
    # CHALLENGE 5: Print the variables out in order of the challenge
    # number. i.e Challenge 1 first, then Challenge 2, and so on.
    
    print(aString, anInt, aFloat, aBool)
    ```
    
- C3 - Converting for Fun
    
    ```python
    # Now that you know the different data types, let's look at how to
    # convert between them.
    
    # To convert an integer to a string:
    anInt = 4
    aString = str(anInt)
    
    # To convert a string to an integer:
    aString = "20"
    anInt = int(aString)
    
    # To convert a string to a float:
    aString = "3.333"
    aFloat = float(aString)
    
    # Here's an example...
    carInfo = "Number of Doors: "
    carDoors = "4"
    
    # Now we can print the number of car doors with:
    
    print(carInfo + carDoors)
    
    # You can see that this prints out:
    # Number of Doors: 4
    
    # This works because both carInfo and carDoors are strings.
    # Notice the quotation marks.
    
    carDoors = 4
    
    # Now carDoors is not a string anymore, it's an integer. (No quotation
    # marks)
    # If you tried to do:
    # print(carInfo + carDoors)
    # Then you would see an error:
    # TypeError: cannot concatenate 'str' and 'int' objects.
    # Try it for yourself.
    
    carDoors = 2
    
    # CHALLENGE 1: Convert carDoors to a string using type conversion.
    # Save it in a new variable: carDoorsString
    
    carDoorsString = str(carDoors)
    
    # CHALLENGE 2: Print out the number of doors in the car
    # using print(carInfo + carDoorsString)
    
    print(carInfo + carDoorsString)
    ```
    
- C4 - Maths in Code
    
    ```python
    # You can do maths in programming too...
    
    addition = 5 + 5
    print(addition) # This will print 10.
    
    multiplication = 5 * 5
    print(multiplication) # This will print 25.
    
    division = 5 / 5
    print(division) # This will print 1.
    
    # You can also do maths without saving the result in a variable.
    
    print(100 - 42)
    
    # Here are some mathematical operators you should know about:
    # Addition [+], as in 5 + 5 = 10
    # Subtraction [-], as in 10 - 2 = 8
    # Multiplication [*], as in 5 * 5 = 25
    # Division [/], as in 10 / 2 = 5
    # Power Of [**] as in 2 ** 3 = 8
    
    # CHALLENGE 1: Multiply 80 by 512 and save it to a variable called ch1.
    ch1 = 80 * 512
    
    # CHALLENGE 2: Add 1024 to 768 and save it to a variable called ch2.
    ch2 = 1024 + 768
    
    # CHALLENGE 3: Do 40 minus 100 and save it to a variable called ch3.
    ch3 = 40 - 100
    
    # CHALLENGE 4: Divide 33 by 6 and save it to a variable called ch4.
    ch4 = 33 / 6
    
    # CHALLENGE 5: Do 2 to the power of 6 and save it to a variable called ch5.
    ch5 = 2**6
    
    # CHALLENGE 6: Save 0.33 to a variable called ch6_1, and save 5 to a
    #              variable called ch6_2. Multiply ch6_1 with ch6_2 and save
    #              the result to a variable called ch6.
    ch6_1 = 0.33
    ch6_2 = 5
    ch6 = ch6_1 * ch6_2
    
    # CHALLENGE 7: Print out the following variables in order:
    #              ch1, ch2, ch3, ch4, ch5, ch6
    print(ch1, ch2, ch3, ch4, ch5, ch6)
    ```
    
- C5 - Super Strings
    
    ```python
    # You've already seen how we can use strings.
    
    # We can concatenate strings (join them up) like so:
    
    firstString = "Hello, "
    secondString = "World!"
    
    print(firstString + secondString)
    
    # But we can go further. We can use a format string.
    # Look at this example:
    
    count = "first"
    
    print("Hello for the %s time." % (count))
    
    # The %s is a format string specifier for a String.
    # It tells Python that there is a string that needs to replace the %s.
    # The string that replaces the %s comes after the %.
    
    # There are other format string specifiers.
    # Some of the ones you might need are:
    # %s is for strings.
    # %d is for integers. Think d is for digits.
    # %f is for floats.
    
    integer = 10
    
    print("There are %d crates." % (integer))
    
    floatpoint = 2.22
    
    print("There are %f humans who understand code." % (floatpoint))
    
    # You can also use multiple format string specifiers at once.
    
    print("String: %s, Num: %d, Float: %f." % (count, integer, floatpoint))
    
    # CHALLENGE 1: Save the integer 5 in the variable ch1_1, and
    #              the string "robots" in the variable ch1_2
    #              Use a format string to print the following sentence:
    #              There are 5 robots in the room
    ch1_1 = 5
    ch1_2 = "robots"
    print(f"There are {ch1_1} {ch1_2} in the room")
    ```
    

### Level 2

- C1 - Flow with Conditionals
    
    ```python
    # Programs aren't always static.
    # Sometimes a program has to behave differently based on the
    # information it gets. We can control the flow of a program
    # using conditionals.
    
    fun = 3
    hacking = 5
    
    if fun < hacking:
        print("Not enough fun!")
    
    # Here we have an if statement.
    # It says: if the value of fun is less than the value of hacking...
    #          then print "Not enough fun!"
    
    # Did you notice that there is a tab before print in our example?
    # This is called a code block.
    # The ':' after hacking means the start of the code block.
    # And the tab at the start of every line after that means that code
    # belongs to that block.
    
    if fun < hacking:
        print("This code belongs to the if statement...")
        print("That's because there is a tab at the beginning.")
    print("This code does not belong to the if statement.")
    print("It will run no matter if the statement is true or not.")
    
    # Let's prove it...
    
    hacking = 2
    fun = 10
    
    if fun < hacking:
        print("Fun is not less than hacking, so this line will never print.")
    print("But this line does not belong to the if statement.")
    print("So it will print no matter what.")
    
    # Here are the conditional operators you should know.
    # You might recognise them from Maths class.
    
    # < - Less than
    # > - Greater than
    # <= - Less than or equal to
    # >= - Greater than or equal to
    # == - Equals To
    
    fun = 5
    hacking = 5
    
    if fun == hacking:
        print("The value of fun is equal to the value of hacking...")
    
    # That's not all! We can also chain if statements together.
    
    if fun < hacking:
        print("The value of fun is less than the value of hacking...")
    elif fun > hacking:
        print("The value of hacking is greater than the value of fun...")
    else:
        print("The value of hacking and the value of fun are equal...")
    
    # In the above example we can see first we check if fun is less than
    # hacking.
    # If it is then it runs the code in the block that belongs to it.
    # If it isn't, then we go on to the next if statement.
    
    # The next statement checks if fun is greater than hacking.
    # If it is then it runs the code in the block that belongs to it.
    # If it isn't then it moves on to the last statement.
    
    # The last statement is an 'else'. That just means if it didn't match
    # any of the other if statements, then run the code in the block that
    # belongs to it. Note that we also combine 'else' and 'if' into 'elif'.
    
    # In this case, if it isn't greater than or less than then it must be
    # equal to, it's the only thing left.
    # You can have multiple 'elif's also.
    
    people = 5
    capacity = 50
    
    def check_capacity():
      if people < capacity:
        print("success")
      elif people == capacity:
        print("maximum people")
      else:
        print("too full")
    
    # CHALLENGE 1: Check if the number of people is lower than the capacity.
    #              If it is, print "success"
    #              If the number of people is higher than the capacity,
    #              print "too full"
    #              If the number of people is equal to the capacity,
    #              print "maximum people"
    
    check_capacity()
    
    # CHALLENGE 2: Set the value of the people variable to 500.
    #              Then run the same check from CHALLENGE 1 again.
    
    people = 500
    check_capacity()
    
    # CHALLENGE 3; Set the value of the people variable to 50.
    #              Then run the same check from CHALLENGE 1 again.
    
    people = 50
    check_capacity()
    ```
    
- C2 - Logical
    
    ```python
    # You can't really understand conditionals without understanding logic.
    # Computers are binary, they think in 1s and 0s. Or put another way,
    # True or False.
    # If a 1 is a True, then a 0 is a False.
    
    # Logic is Maths. So it's not surprising that calculating logic looks
    # a lot like solving Maths problems.
    # True AND False = False
    # It looks very similar to:
    # 1 + 3 = 4
    
    # There are several logical operators which you should know:
    # and - Logical AND. Both sides of the equation have to be True for it
    # to be True. If not it's False.
    # or - Logical OR. If either side of the equation is True then it's
    # True. If not it's False.
    # not - Logical NOT. Turns a True result into False and a False into
    # a True.
    
    print(True and True) # This prints 'True'
    print(True and False) # This prints 'False'
    print(True or False) # This prints 'True'
    print(False and True) # This prints 'False'
    print(False and False) # This prints 'False'
    print(False or False) # This prints 'False'
    
    # This prints 'False', because the 'not' reverses it.
    print(not(True and True))
    # This prints 'True', because the 'not' reverses it.
    print(not(False and False))
    
    # Did you notice how every time we open a bracket '(' we have to close it ')'?
    # This is called bracket matching. If you leave open brackets that
    # never get closed, you will start seeing errors.
    
    # You can also see how this works in conditionals. Let's use our
    # example from the previous challenge.
    
    fun = 2
    hacking = 6
    
    if hacking > fun:
        print("more hacking")
    
    # hacking > fun is the key here. What does hacking > fun come out to?
    print(hacking > fun) # This prints 'True'.
    
    # So actually what is happening here is we're saying if something
    # is true, then continue into the code block.
    # What happens if we negate it with not?
    
    print(not(hacking > fun)) # This prints 'False'
    
    # So if we used that in a conditional?
    
    if not(hacking > fun):
        print("This isn't going to run...")
    
    # How about checking for two things in one if statement?
    
    pizza = 4
    
    if (hacking > fun) and (pizza > fun):
        print("more hacking and more pizza...")
    
    # Here, hacking > fun is True. pizza > fun is also True.
    # True and True = True, so the if statement is True.
    
    if (hacking < fun) or (pizza > fun):
        print("at least there's pizza.")
    
    # Here hacking < fun = False. pizza > fun is True.
    # So it ends up being: False or True, which equals True.
    
    # CHALLENGE 1: Print the result of true or true.
    print(True or True)
    
    # CHALLENGE 2: Print the result of true or false.
    print(True or False)
    
    # CHALLENGE 3: Print the result of false or true.
    print(False or True)
    
    # CHALLENGE 4: Print the result of false or false.
    print(False or False)
    
    # CHALLENGE 5: Use not to negate the result of true OR false and
    # print the result.
    print(not(True or False))
    ```
    
- C3 - Let's Get Functional
    
    ```python
    # A function is just a bit of code that is taken out of the main
    # program so it can be used over and over again.
    
    # You've already been using functions. print() is a function.
    # The print function takes in what you want to print as a parameter.
    # Then it runs code that prints that to your screen.
    
    # We're going to learn how to write our own functions.
    # First we need to define a function with def:
    
    def myfunction():
        print("This is my first function...")
    
    # On it's own, this program doesn't do anything. We have to call the
    # function first.
    
    myfunction()
    
    # Now this program should print "This is my first function..."
    
    def myfunction(name):
        print("Hello " + name + ".")
    
    # We've changed the function to take a parameter this time.
    # Let's see how that works...
    
    myfunction("Bob")
    
    # Now this program will print "Hello Bob."
    
    def myfunction(name):
        formatted = "Hello " + name + "."
        return formatted
    
    # Now we've changed the function again. This time it doesn't print,
    # it saves a string into the variable formatted. Then it returns the
    # variable. By returning something, that just means you can save
    # the output into a variable,
    
    result = myfunction("Bob")
    
    # Here we are returning "Hello Bob." and saving it into the variable
    # 'result'. Let's check:
    
    print(result)
    
    # We can also take in multiple parameters:
    
    def myfunction(name, age):
        return "I am " + name + " and I am " + str(age) + " years old."
    
    # Now the function takes in a name and an age and returns the result.
    
    result = myfunction("Bob", 26)
    
    print(result)
    
    # CHALLENGE 1: Write a function that takes in two integers and
    #              multiplies them together then returns the result.
    
    multiply = lambda a, b: a * b
    
    # CHALLENGE 2: Run the function from CHALLENGE 1, passing in the
    #              integers 99 and 52 and print the result.
    
    print(multiply(99, 52))
    
    # CHALLENGE 3: Write a function that takes two integers and prints
    #              the string "I am X ft Y inches tall", replacing the
    #              X and Y with the numbers passed into the function.
    
    height = lambda X, Y: print(f"I am {X} ft {Y} inches tall")
    
    # CHALLENGE 4: Run the function from CHALLENGE 3, passing in 6 and 2
    #              as the parameters.
    
    height(6, 2)
    
    # You should end up with 2 lines output from these 4 challenges.
    ```
    
- C4 - Hooray for Arrays
    
    ```python
    # An array is just a collection of data.
    # Let's look at an example:
    
    myarray = ["Hello", "World!", 28, 22.5]
    print(myarray) # This prints all the values in the array.
    print(myarray[0]) # This prints the first value in the array
    # (We start counting from 0)
    print(myarray[1]) # This prints the second value in the array.
    print(myarray[2]) # This prints the third value in the array.
    print(myarray[3]) # This prints the fourth value in the array.
    
    # We can see we can access positions in the array using square
    # brackets [].You can also add to an array...
    
    myarray.append("morestuff")
    print(myarray) # We can see "morestuff" got added to the end
    # of the array.
    
    # We can also change the values in a specific position of the array:
    
    myarray[3] = "changed"
    print(myarray) # We can see the fourth value in the array was
    # changed to "changed".
    
    # We can also remove from the array:
    
    myarray.pop(3) # This removes the fourth item from the array
    print(myarray)
    
    # Similar to arrays are dicts or dictionaries.
    # With arrays, you can only reference positions in the array using
    # numbers.
    # With a dict, you associate one value with another, a key-value pair.
    # The colon ':' differentiates the key from the value.
    # In the example below, name is a key. Bob is the value associated with name.
    
    mydict = {"name": "Bob", "age": 23, "height": 180}
    
    # In this example, name is the key and Bob is the value. If you
    # want to find out the name you can just do:
    
    print(mydict["name"])
    
    # To get the age:
    
    print(mydict["age"])
    
    # CHALLENGE 1: Create an array with the following values in it in
    #             order:
    #             42, 1337, "Coffee", "Anonymous" then print the array.
    array = [42, 1337, "Coffee", "Anonymous"]
    print(array)
    
    # CHALLENGE 2: Add two more values to the end of the array you created
    #              in CHALLENGE 1: "Blue", "Sky" then print the array.
    array.append("Blue")
    array.append("Sky")
    print(array)
    
    # CHALLENGE 3: Print the fourth value in the array you created in
    #              CHALLENGE 1.
    print(array[3])
    
    # CHALLENGE 4: Create a dict that includes the following values in
    #              order: "Subject": "Hacking", "Grade": "A".
    mydict = {"Subject": "Hacking", "Grade": "A"}
    
    # CHALLENGE 5: Print the grade value in the dictionary you created in
    #              CHALLENGE 4.
    print(mydict['Grade'])
    ```
    
- C5 - Going Loopy
    
    ```python
    # In programming, there are many situations where we have to repeat a
    # task over and over until a condition is met. We use loops for this.
    
    # The first type of loop we will look at is a while loop.
    # Like the name suggests, a while loop will keep repeating while a
    # condition is true.
    
    count = 0
    while count < 10:
        print("The count is: " + str(count))
        count = count + 1
    
    # In our example, the condition is that count should always be
    # less than 10.
    # When count is more than 10, the loop will stop executing.
    # Our example will print "The count is 0" then "The count is 1" and
    # so on until "The count is 9"
    
    hungryPeople = 8
    pizza = 10
    
    while hungryPeople > 0:
        pizza -= 1
        hungryPeople -= 1
        print("Someone ate a pizza.")
    print("There are no more hungry people")
    
    # In this second example we are using pizza -= 1 instead of
    # pizza = pizza - 1.
    # It's the same thing, it's just a short way of writing it.
    # You can use the same shortcut for addition.
    # For example pizza += 1 is the same as pizza = pizza + 1
    # You will see when the loop exits that
    # "There are no more hungry people" will print.
    # That is because hungryPeople > 0 is no longer true so the
    # code moves on to line 24.
    
    # It's very important that you make sure the condition where a loop
    # exits will always be met. If it doesn't get met, you will have an
    # infinite loop. If you have an infinite loop, the program will never
    # stop running unless you force it to quit.
    
    # The other type of loop is a for loop. For loops are particularly
    # useful for going through arrays. Let's look at an example:
    
    myarray = ["Strong", "Coffee", "Is", "The", "Best"]
    
    for x in myarray:
        print(x)
    
    # This is the most basic form of a for loop. Here, each time the loop
    # executes, x will be the next value in the array. The loop will exit
    # on it's own when there are no more array values.
    
    # So for example, the first time the loop runs, x will be "Strong",
    # the second time x will be "Coffee" and so on...
    
    # We can also do ranges in for loops.
    # This will print 0 through to 49.
    for x in range(0, 50):
        print(x)
    
    # CHALLENGE 1: Create an empty array called numbers.
    
    numbers = []
    
    # CHALLENGE 2: Write a while loop that will add 100 numbers to the
    #              array, starting from the number 100 and incrementing by
    #              2 each time. For example, start from 100, then the next
    #              number added will be 102, then 104 and so on.
    
    numbers = [i for i in range(100, 300, 2)]
    
    # CHALLENGE 3: Write a for loop that will look through your numbers
    #              array and print out each value in the array.
    
    [print(i) for i in numbers]
    ```
    

### Level 3

- C1 - Fun with Files
    
    ```python
    # Working with files is a common task for a programming language
    # Python makes it easy. Let's look at an example:
    
    myfile = open("/tmp/newfile.txt", "w")
    
    # Our program will open a file called newfile.txt in /tmp.
    # If no file exists it will be created for us.
    # The "w" is the mode, in this case "w" is for write. You could use "r"
    # for read.
    # There are various other modes, we will cover them briefly later.
    
    myfile.write("Here is my message.\n")
    myfile.write("Here is my second message.")
    
    # Here we write "Here is my message\n" to the file we opened. \n is a
    # newline character.
    # You need to add a \n every time you want to add a new line,
    # otherwise everything will be on one line.
    
    myfile.close()
    
    # Since we opened the file, we need to close it when we're done with it.
    
    # There are many different modes for opening a file in Python.
    # Here are just a few useful ones:
    # w - Allows you to write to a file only. If the file exists, it will
    # be overwritten.
    # r - Allows you to read the file only.
    # r+ - Allows you to read and write to the file.
    # w+ - Allows you to read and write to the file, but if the file
    # already exists it will overwrite it.
    # a - Allows you to append to the file
    # (write to the end of an existing file)
    # a+ - Allows you to append to the file, and read from the file.
    
    myfile = open("/tmp/newfile.txt", "r")
    filecontents = myfile.read()
    print(filecontents)
    myfile.close()
    
    # Here we are reading the file we created previously.
    
    # You can also use the 'with' syntax. It's better.
    # Here is an example of reading a file line by line instead of all
    # at once.
    
    with open("/tmp/newfile.txt", "r") as myfile:
        for line in myfile:
            print(line)
    
    # The major benefit of using 'with' is that it handles closing the
    # file for you.
    # We used a for loop to read the file line by line.
    
    # CHALLENGE 1: Write a for loop that will create a file called
    #              /tmp/cars.txt. There should be 50 lines of text in the
    #              file. The first line should be "There are 0 cars"
    #              and 1 car should be added every line. Until
    #              the last line which should read "There are 49 cars"
    
    with open("/tmp/cars.txt", "w") as f:
      [f.write(f"There are {i} cars\n") for i in range(50)]
    
    # CHALLENGE 2: Open the file at /tmp/cars.txt and read the contents.
    #              Print the contents to the screen.
    with open("/tmp/cars.txt", "r") as f:
      print(f.read())
    ```
    
- C2 - Sockets and Servers
    
    ```python
    from time import sleep
    
    # Sockets are a way of sending data over a network.
    # There are two main types of sockets, TCP and UDP.
    # Which to use depends on the application you are communicating with.
    
    # You will need to import the socket library first.
    import socket
    
    # To make a connection to a TCP server:
    
    # Create a socket. AF_INET means you're connecting to an IPv4 IP
    # address.
    # SOCK_STREAM means you are connecting over TCP and not UDP.
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Tell the socket what IP address and Port number to connect to.
    clientsocket.connect(('127.0.0.1', 9987))
    # Send some data over the socket.
    clientsocket.send('hello'.encode())
    # Receive some data back. The 1024 is the max number of bytes of data
    # to accept.
    data = clientsocket.recv(1024)
    print(data)
    
    # You should see "You said: hello" printed out. That's because our
    # server is setup to respond to whatever you send it by adding
    # 'You said:' to the front of it and sending it back.
    
    # To make a TCP Server:
    
    # Create a socket.
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # Bind the socket to listen to a port.
    serversocket.bind(("127.0.0.1", 9985))
    # Tell the socket to start listening.
    # The 10 is the maximum number of connections.
    serversocket.listen(10)
    
    # Setup an infinite loop so the socket will keep listening for
    # incoming connections.
    while True:
        # If it gets a new connection, accept it and save the connection
        # and address.
        connection, address = serversocket.accept()
        # Read 1024 bytes of data from the connection.
        data = connection.recv(1024).decode()
        # Check the length of data. If the length is more than 0 then
        # that means something was sent, so print it out.
        if len(data) > 0:
            print("Received: " + data)
    
        # Close the connection.
        connection.close()
        # We don't need to keep listening any more so break out of the
        # infinite loop
        break
    
    # Close the socket.
    serversocket.close()
    
    sleep(0.05)
    
    # CHALLENGE 1: Write a TCP Client that will connect to 127.0.0.1 on
    #              port 9990.
    #              Your client must send "Knock, knock" to the server.
    #              Then get the response, and print it out.
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('127.0.0.1', 9990))
    clientsocket.send('Knock, knock'.encode())
    data = clientsocket.recv(1024)
    print(data)
    ```
    
- C3 - Don't Forget HTTP
    
    ```python
    # You aren't limited to using raw sockets to make network connections.
    # Python can make HTTP requests quite easily.
    
    # First you'll need to import the necessary urllib modules.
    import urllib.request, urllib.error, urllib.parse
    
    # Then you need to open the URL:
    response = urllib.request.urlopen("http://127.0.0.1:8080")
    
    # Now you just need to read the contents of the response:
    html = response.read()
    print(html)
    
    # CHALLENGE 1: Make a connection to: 127.0.0.1:8080/winning and print
    #              the response.
    
    response = urllib.request.urlopen("http://127.0.0.1:8080/winning")
    print(response.read())
    ```
    
- C4 - ASCII Encoding
    
    ```python
    # As you know, computers only think in numbers. That means, when it
    # comes to dealing with text, the computer has to have some way of
    # converting numbers into letters. This is a form of encoding.
    
    # The most common form of encoding is ASCII. In ASCII, a specific
    # number maps to a letter. So for example, the number 65 is a capital
    # A.
    
    # Sometimes we need to be able to convert between the number a letter
    # represents and the letter itself.
    
    num = 65
    
    # chr allows us to convert a decimal number to it's ASCII value.
    char = chr(num)
    # ord allows us to convert the ASCII character to it's decimal value.
    dec = ord(char)
    
    print("Character: " + char + ", Decimal: " + str(dec))
    
    # CHALLENGE 1: Write a loop that prints the ASCII characters of all
    #              the decimal values between the range 49 and 127
    [print(chr(i)) for i in range(49, 128]
    ```
    
- C5 - Ready for Regex
    
    ```python
    # A regular expression or regex for short is a way of searching text
    # for a pattern. Most people look at regex and get scared away, and
    # it does look confusing at first. But it's also an incredibly useful
    # tool to add to your programming arsenal.
    
    # First you need to import the 're' library:
    import re
    
    # In it's most basic form, you can use regex to search for words in
    # some text:
    pattern = "flag"
    text = "The flag is: this is a fake flag: bajhdasdohaudsnasdaasd"
    
    if re.findall(pattern, text):
        print("Found match!")
    
    # Just telling you if something is there is not that useful though.
    # Ideally we want to extract some information out of the text you are
    # searching.
    
    pattern = "flag: (.*)"
    data = re.findall(pattern, text)
    print(data[0])
    
    # In this case, we managed to extract the flag from the text provided.
    # Let's look more closely at how this happened.
    
    # The key is the pattern: flag: (.*).
    # First we're looking for any text that starts with 'flag: '
    # Next, the brackets surround the bit we want to extract. We know the
    # flag we want to get comes after, so the brackets are after 'flag: '.
    # The . inside the brackets means match any character.
    # The * means any number of times.
    # So put it together and you're extracting any series of characters
    # after the text 'flag: ' .
    
    # What re.findall returns is an array. That's because it find all
    # possible matches, so if there was more than one match, it would
    # put them in the other positions in the array.
    # For example data[1] for the second match, data[2] for the third
    # match and so on...
    
    # Regex is a whole language on it's own, but that is the basics.
    # You can find out how to do more things with it at:
    # https://regexone.com/
    
    html = """
    <html>
    <head>
        <title>Regex Demo</title>
    </head>
    <body>
        <div class='firstDiv'>Hello</div>
        <div class='secondDiv'>Hello</div>
    </body>
    </html>
    """
    
    # CHALLENGE 1: Write a regex search that extracts all the classes from
    #             the divs and saves them into an array.
    data = re.findall("class='(.*)", html)
    
    # CHALLENGE 2: Write a loop that goes through the array from
    #              CHALLENGE 1 and prints the contents.
    [print(item[:-13]) for item in data]
    ```
    

### Level 4

- C1 - Strange File
    
    ```python
    #
    # Ok, quick task for you agent - we've received a strange file from
    # the first alien communication.
    # It's at /tmp/alien-signal.txt, we need you to open and read the file.
    #
    #
    
    with open("/tmp/alien-signal.txt", "r") as f:
      [print(line) for line in f]
    ```
    
- C2 - Agent Profiles
    
    ```python
    #
    # Fix the below script to read from each agent file found in /tmp.
    # Example agent profile would be /tmp/agent-1.txt
    # The contents of each of the agent files makes up the flag
    #
    
    import os.path
    
    count = 1
    
    for i in range(20):
      fname = "/tmp/agent-" + str(count)+".txt"
      if os.path.isfile(fname):
        with open(fname, 'r') as content_file:
          content = content_file.read()
          print(content.rstrip())
      count += 1
    ```
    
- C3 - Broken Robot
    
    ```python
    #
    #  Robot Control Map
    #
    #  +-------------------+
    # 9|                   |
    # 8|S                  |
    # 7|            x x x x|
    # 6|            x      |
    # 5|            x F    |
    # 4|                   |
    # 3|                   |
    # 2|                   |
    # 1|                   |
    # 0|                   |
    #  +-------------------+
    #   0 1 2 3 4 5 6 7 8 9
    #
    #  S = Start position (0,8) F = Target destination (7,5),
    #  x = Ravine, robot will be lost if hits these coords
    #
    # import robot module and use the robot.left(), robot.right(),
    # robot.up() and robot.down() functions
    #
    import robot
    
    [robot.down()  for i in range(4)]
    [robot.right() for i in range(7)]
    robot.up()
    ```
    
- C4 - Unlocking the Message
    
    ```python
    #
    # Alien Signal API listening on http://127.0.0.1:8082
    # Use HTTP GET with x-api-key header to get signal
    # We have narrowed down the key to be in the range of 5500 to 5600
    # Note: The script can timeout. If this occurs try narrowing
    # down your search
    #
    
    from urllib.request import Request, urlopen
    req = Request('http://127.0.0.1:8082') # create a request object linked to the url
    
    for i in range(5500, 5601):
      req.add_header('x-api-key', str(i)) # send a message to port i
      content = urlopen(req).read()       # read the content
      print(content)                      # print the content of the page
    ```
    
- C5 - Alien Server
    
    ```python
    #
    # Connect to alien server ('localhost', 10000)
    #
    # Then send each of these values...
    # USER
    # aliensignal
    # PASS
    # unlockserver
    # SEND
    # moonbase
    # END
    # ...and receive the response from each.
    #
    # Note: You must receive data back from the server after you send each value
    #
    import socket
    
    messages = ["USER", "aliensignal", "PASS", "unlockserver", "SEND", "moonbase", "END"]
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(('localhost', 10000))
    
    for message in messages:
      clientsocket.send(message.encode())
      print(clientsocket.recv(1024))
    ```
    

### Level 5

- C1 - Listen Up
    
    ```python
    #
    # The aliens seem to be trying to make direct contact, so it's time
    # for us to properly listen.
    # Write a server that listens on ('localhost', 10000).
    # The flag will be sent to that address.
    # Record signal to /tmp/aliensignallog.txt
    #
    # If you get an address already in use error then try again in a few
    # moments.
    #
    
    def debugMsg(msg):
      # Use this function if you need any debug messages
      with open("/tmp/userdebug.log", "a") as myfile:
        myfile.write(msg + "\\n")
    
    import socket
    serversocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    serversocket.bind(("localhost", 10000))
    serversocket.listen(10)
    
    while True:
        connection, address = serversocket.accept()
        data = connection.recv(1024).decode()
        if len(data) > 0:
            with open("/tmp/aliensignallog.txt", "w") as f:
              f.write(data)
    
        connection.close()
        break
    ```
    
- C2 - Defence Data
    
    ```python
    #
    # Generate a valid xml file at /tmp/vulnerable-countries.xml.
    # It should contain a list of country nodes attached to a root node.
    # Each country node should have a name attribute.
    # The third node name should be Panama.
    #
    
    from xml.dom import minidom
    import os 
      
    root = minidom.Document()
      
    xml = root.createElement('root') 
    root.appendChild(xml)
    
    def add_country(name):
    	productChild = root.createElement('country')
    	productChild.setAttribute('name', name)
    	xml.appendChild(productChild)
    
    add_country("USA")
    add_country("China")
    add_country("Panama")
      
    xml_str = root.toprettyxml(indent ="\t") 
      
    save_path_file = "/tmp/vulnerable-countries.xml"
      
    with open(save_path_file, "w") as f:
        f.write(xml_str)
    ```
    
- C3 - Alien Zip
    
    ```python
    #
    # Sample Alien Zip file found at /tmp/alien-zip-2092.zip is password protected
    # We have worked out they are using three digit code
    # Brute force the Zip file to extract to /tmp
    #
    # Note: The script can timeout if this occurs try narrowing
    # down your search
    
    import zipfile
    
    def try_password(password):
    	try:
    		with zipfile.ZipFile('/tmp/alien-zip-2092.zip', 'r') as zip_ref:
    			zip_ref.extractall(path="/tmp", pwd=password.encode('utf-8'))
    		return True
    	except Exception:
    		return
    
    def brute_force_zip():
      # for some reason this list comprehension doesn't work even though its the same thing???
      # return [str(i).zfill(3) for i in range(1000) if try_password(str(i).zfill(3))][0]
    	for i in range(1000):  # password range from 100 to 999
    		if try_password(str(i).zfill(3)):
    			return str(i).zfill(3)
    
    brute_force_zip()
    ```
    
- C4 - Passphrase Panic
    
    ```python
    #
    # Write a script to generate a passphrase by taking words from
    # /tmp/words.txt
    # The wordNumbers array holds three random numbers. Each number
    # corresponds to a word in words.txt. So for example
    # wordNumbers[1] is the second word in /tmp/words.txt.
    # Put a space between each word and print it out
    #
    
    with open("/tmp/randomwordsnumbers.txt", "r") as file:
        data = file.read()
    
    wordNumbers = data.rstrip().split("\n")
    
    file = open("/tmp/words.txt")
    content = file.readlines()
    print(''.join([content[int(n)].strip('\n') + ' ' for n in wordNumbers]))
    ```
    
- C5 - Jovian Tweets
    
    ```python
    #
    # The Tweet Bot API can be found at http://127.0.0.1:8082
    #
    # GET method sent to that URL:
    # ...returns basic info about API
    #
    # POST method sent to that URL, with:
    # - x-api-key:{KEY} in header
    # - user={USER} in querystring
    # - status-update={TEXT} in querystring
    # ...creates a new social media post
    
    from urllib.request import Request, urlopen
    from urllib.parse import urlencode
    
    url = 'http://127.0.0.1:8082'
    data = {"user": "tweetbotuser", "status-update": "alientest"}
    data = urlencode(data).encode('utf-8')
    
    req = Request(url, data=data, headers={'x-api-key': 'tweetbotkeyv1'})
    
    content = urlopen(req).read()
    print(content)
    ```
    

### Level 6

- C1 - Foreign Filesystem
    
    ```python
    #
    # Find the file in the alien directories in /tmp/aliendir to get the flag
    #
    
    import os
    
    # its so long lol
    [[print(file) for file in files] for root, dirs, files in os.walk("/tmp/aliendir")]
    ```
    
- C2 - Watched by the Eye
    
    ```python
    #
    # Hide text in the image /tmp/image.gif
    # Append the word alieneye to end of the file.
    #
    
    # easiest challenge by far
    with open("/tmp/image.gif", "a") as f:
      f.write("alieneye")
    ```
    
- C3 - A Way Back In
    
    ```python
    #
    # Write a script that connects to 'localhost' port 10000
    # You then need to send a command to list the files in the /tmp directory
    #
    
    # another easy challenge
    import socket
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    clientsocket.connect(("127.0.0.1", 10000))
    clientsocket.send("ls -al /tmp\n".encode())
    print(clientsocket.recv(1024).decode())
    ```
    
- C4 - Tough Zip
    
    ```python
    #
    # Zip file found at /tmp/alien-sample-42.zip is password protected
    # We have worked out they are using one of the passwords
    # in the provided list
    # Brute force the Zip file to extract to /tmp
    #
    # Note: The script can timeout. If this occurs try narrowing
    # down your search
    #
    possiblePasswordList = [
      'pant', 'papa', 'paps', 'para', 'path', 'pats', 'paty',
      'pard', 'pare', 'park', 'parr', 'pars', 'part', 'pase',
      'pash', 'past', 'pate', 'peal', 'pean', 'pear', 'peas',
      'pave', 'pawl', 'pawn', 'paws', 'pays', 'peag', 'peak',
      'peck', 'pele', 'peat', 'pech', 'peke', 'perm', 'perp',
      'pecs', 'peds', 'peed', 'peek', 'peel', 'peen', 'peep',
      'pelf', 'pelt', 'pend', 'pens', 'pent', 'pass', 'pepo',
      'pert', 'phon', 'phot', 'phut', 'peer', 'pegs', 'pehs',
      'pere', 'peri', 'perk', 'phat', 'phew', 'phis', 'phiz',
      'perv', 'peso', 'pest', 'pets', 'pews', 'pfft', 'pfui',
      'pial', 'pian', 'pias', 'pica', 'pice', 'pick', 'pics',
      'pied', 'pier', 'pies', 'pigs', 'plan', 'plat', 'ploy',
      'pika', 'pike', 'piki', 'pint', 'piny', 'pion', 'pith',
      'pile', 'pili', 'pill', 'pily', 'pima', 'pimp', 'pina',
      'pine', 'ping', 'pink', 'pins', 'plug', 'plum', 'pein',
      'poll', 'peps', 'pits', 'pity', 'pixy', 'plop', 'plot',
      'pipe', 'pips', 'pipy', 'pirn', 'pish', 'piso', 'pita',
      'pole', 'plow', 'plod', 'pois', 'poke', 'poky',
      'play', 'plea', 'pleb', 'pled', 'plew', 'plex', 'plie',
      'plus', 'pock', 'poco', 'pods', 'poem', 'poet', 'pogy',
    ]
    
    import zipfile
    
    def try_password(password):
    	try:
    		with zipfile.ZipFile('/tmp/alien-sample-42.zip', 'r') as zip_ref:
    			zip_ref.extractall(path="/tmp", pwd=password.encode('utf-8'))
    		return True
    	except Exception:
    		return False
    
    def brute_force_zip():
      # for some reason this list comprehension doesn't work
      # return [password for password in possiblePasswordList if try_password(password)][0]
    	for password in possiblePasswordList:
    		if try_password(password):
    			return password
    
    password = brute_force_zip()
    ```
    
- C5 - Server Key
    
    ```python
    #
    # Send server ('localhost', 10000) GET_KEY to retrieve key,
    # user needs to reverse and send back to server to get flag.
    # It will change each execution so the
    # user can not manually achieve this.
    #
    
    import socket
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(("localhost", 10000))
    client.send("GET_KEY".encode())
    client.send(client.recv(1024)[::-1])
    print(client.recv(1024))
    client.close()
    ```
    

### Level 7

- C1 - Magic File
    
    ```python
    #
    # Find the valid png file in the /tmp directory using magic bytes.
    # The code is hidden in this file.
    #
    
    import os
    
    def is_valid_png(filepath):
    	with open(filepath, 'rb') as file:
    		header = file.read(8)
    
    	return header == b'\x89PNG\r\n\x1a\n'
    
    def find_valid_png():
    	for filename in os.listdir('/tmp'):
    		filepath = os.path.join('/tmp', filename)
    
    		if is_valid_png(filepath):
    			with open(filepath, 'rb') as f:
    				[print(line) for line in f]
    
    find_valid_png()
    ```
    
- C2 - Cookie Cutter
    
    ```python
    #
    # Write a script that can guess cookie values
    # and send them to the url http://127.0.0.1:8082/cookiestore
    # Read the response from the logged in cookie value to get the flag.
    # The cookie name the aliens are using is alien_id
    # we believe the id is a number between 1 and 75
    #
    # Note: The script can timeout. If this occurs try narrowing
    # down your search
    #
    
    from urllib.request import Request, urlopen
    req = Request('http://127.0.0.1:8082/cookiestore')
    
    for i in range(76):
      req.add_header('Cookie', f'alien_id={i}')
      print(urlopen(req).read())
    ```
    
- C3 - Alien Transfer
    
    ```python
    #
    # Setup server listening on ('localhost', 10000)
    # receive data then send data back after XORing with the key
    # attackthehumans
    #
    # If you get an address already in use error then try again in a few
    # moments.
    #
    
    # ---------------------- WARNING ----------------------
    # For some reason this code only works SOMEIMES. If
    # this code doesn't work don't complain about it to me.
    # It will constantly say "Incorrect code provided", the
    # only solution is to keep submitting the code over and
    # over again
    
    import socket
    
    # super compressed xor encrypt function because list comprehension is my lord and savior
    def xor_encrypt(message, key):
      return bytes([message[i] ^ key[i % len(key)] for i in range(len(message))])
    
    # connect to the server that induces homicidal thoughts
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('localhost', 10000))
    server.listen(1)
    
    while True:
      # accept the server for who it is (its in the closet)
    	connection, address = server.accept()
    
      # listen to the server's problems
    	data = connection.recv(1024)
    	if not data:
    		continue
    
      # putting a b infront of a string makes it a bytes string
    	encrypted_data = xor_encrypt(b"attackthehumans", key)
    	connection.sendall(encrypted_data)
    
    	connection.close()
    ```
    
- C4 - Hidden Message
    
    ```python
    #
    # One of the agents has intercepted a file from the aliens
    # The flag is hidden in large amount of non alphanumeric characters.
    # The file lives at /tmp/destroymoonbase.gif
    #
    
    with open("/tmp/destroymoonbase.gif", "r") as f:
      print(f.read().replace("$", '').replace("#", ''))
    ```
    
- C5 - Alien Email
    
    ```python
    #
    # We need you to send a spoofed email.
    # Use smtp server at '127.0.0.1', port 1025.
    # Author needs to be bob-roswell-1947@ship-shape-security.com
    # Recipient needs to be zultron@cyberdarkart.com
    #
    
    import socket
    
    def sendall(message=None):
      if message: server.sendall(message)
      response = server.recv(1024).decode()
      print(response)
      
    
    from_address = 'bob-roswell-1947@ship-shape-security.com'
    to_address = 'zultron@cyberdarkart.com'
    smtp_server = '127.0.0.1'
    smtp_port = 1025
    email_data = (
      f"From: {from_address}\r\n"
      f"To: {to_address}\r\n"
      "Subject: Spoofed Email\r\n"
      "\r\n"
      "This is a spoofed email\r\n"
      ".\r\n"  # End of email
    )
    
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.connect((smtp_server, smtp_port))
    
    sendall()
    sendall(b'HELO local\r\n')
    sendall(f'MAIL FROM: <{from_address}>\r\n'.encode())
    sendall(f'RCPT TO: <{to_address}>\r\n'.encode())
    sendall(b'DATA\r\n')
    
    server.sendall(email_data.encode())
    
    sendall(b'\r\n.\r\n')
    
    server.sendall(b'QUIT\r\n')
    server.close()
    ```
    

### Level 8

- C1 - New Line of Communication
    
    ```python
    #
    # Connect over TCP to the following server: 'localhost', 10000
    # Initiate communication with 'GET' to retrieve the encrypted messages.
    # Then return the messages decrypted to the server,
    # taking care to ensure each message is split on to a newline
    #
    import socket
    
    def decode(ciphertext, shift):
        result = ""
        for char in ciphertext:
            if char.isalpha():
                # Determine whether the character is uppercase or lowercase
                is_upper = char.isupper()
    
                # Shift the character by the specified amount
                char_code = ord(char)
                decoded_code = (char_code - shift - ord('A' if is_upper else 'a')) % 26 + ord('A' if is_upper else 'a')
    
                # Append the decoded character to the result string
                result += chr(decoded_code)
            else:
                # If the character is not a letter, leave it unchanged
                result += char
    
        return result
    
    clientsocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    
    clientsocket.connect(('localhost', 10000))
    
    clientsocket.send('GET'.encode())
    
    sentences = str(clientsocket.recv(1024))
    
    sentences = sentences.split("\\n")
    
    decoded = []
    
    for i in sentences[1:4]:
      for j in range(26):
        d = decode(i, j)
        if ("THE" in d):
            decoded.append(d)
          
    x = ""
    for i in decoded:
      x += i + "\n"
    
    print(x)
    clientsocket.send(x.encode())
    print(str(clientsocket.recv(1024)))
    ```
    
- C2 - Vulnerable String
    
    ```python
    #
    # Write a script which can connect to the following server
    # 'localhost', 10000 over TFP send 'GET_KEY' to download a string.
    # The string is compressed with a common algorithm found in many
    # websites. Decompress the string and print it to get the flag.
    #
    
    import socket
    import zlib
    
    client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    client.connect(('localhost', 10000))
    print(zlib.decompress(client.recv(1024), 16.zlib+MAX_WBITS)
    ```
    
- C3 - Getting Access
    
    ```python
    #
    # There is a directory traversal vulnerability in the
    # following page http://127.0.0.1:8082/humantechconfig?file=human.conf
    # Write a script which will attempt various levels of directory
    # traversal to find the right amount that will give access
    # to the root directory. Inside will be a human.conf with the flag.
    #
    # Note: The script can timeout. If this occurs try narrowing
    # down your search
    
    from urllib.request import Request, urlopen
    
    dir_level = "human.conf"
    
    for i in range(20):
      req = Request(f"http://127.0.0.1:8082/humantechconfig?file={dir_level}")
      content = urlopen(req).read().decode()
      print(content)
      
      dir_level = f"../{dir_level}"
    ```
    
- C4 - Unlocking the Mothership
    
    ```python
    #
    # Connect to the  server at 'localhost', 10000 send any data,
    # the server will respond with the required word codes
    # You will find a passage of text in the file backdoor.txt write a script
    # which will use that text to build a message using the received word codes.
    # Each word code is sent on a new line and contains
    # paragraph_number, line_number, word_number
    # Send the expected words back to the server to retrieve the flag.
    # The server expects all the words in a single transmission.
    # The words should have punctuation stripped from them.
    # And the words should be separated by newline characters (\\n)
    #
    #
    
    import socket
    
    text_file = open("backdoor.txt", "r")
    text = text_file.read()
    text_file.close()
    paragraphs = text.split("\n\n")
    for x in range(len(paragraphs)):
      paragraphs[x] = paragraphs[x].split("\n")
      for a in range(len(paragraphs[x])):
        paragraphs[x][a] = paragraphs[x][a].split(" ")
    		
      
    
    s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    HOST = 'localhost'
    PORT = 10000
    s.connect((HOST,PORT))
    s.send("any data".encode())
    
    word_codes = s.recv(1024).decode().replace(",","").split("\n")[0:6]
    for x in range(len(word_codes)):
      word_codes[x] = word_codes[x].split(" ")
    
    message =""
    for a in word_codes: 
      message+=paragraphs[int(a[0])-1][int(a[1])-1][int(a[2])-1].replace(".","").replace("!","").replace(",","").replace("\"","") + "\n"
    
    s.send(message.encode())
    print(message)
    flag = s.recv(1024).decode()
    print(flag)
    ```
    
- C5 - Self Destruct
    
    ```python
    #
    # Write a script that makes HTTP requests to the server
    # http://127.0.0.1:8082/selfdestruct until the numbers match
    # and read the response to get the flag.
    # You can easily run out of execution time in this challenge.
    # You will need to check the response and stop your attack
    # once you see the flag.
    #
    
    # import request module
    from urllib.request import Request, urlopen
    
    # make a request instance
    req = Request("http://127.0.0.1:8082/selfdestruct")
    
    # repeat a bunch of times
    for i in range(100):
      
      # get the content
      content = urlopen(req).read().decode()
     	
      # split the content by newlines
      split_data = content.splitlines()
      
      # get the numbers on the page and print them
      num_1, num_2 = split_data[21], split_data[24]
      print(f"Numbers: {num_1}, {num_2}")
      
      # if the criteria is met then print the flag and stop the loop
      if num_1 == num_2:
        print(f"Flag: {split_data[28]}")
        break
    ```