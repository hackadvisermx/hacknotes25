
# Task 25 - Game hacking - Day 19: I merely noticed that you’re improperly stored, my dear secret!

## Learning Objectives

- Understand how to interact with an executable's API.
- Intercept and modify internal APIs using Frida.
- Hack a game with the help of Frida.

## Game Hacking

 Even while penetration testing is becoming increasingly popular, game hacking only makes up a small portion of the larger cyber security field. With its 2023 revenue reaching approximately $183.9 billion, the game industry can easily attract attackers. They can do various malicious activities, such as providing illegitimate ways to activate a game, providing bots to automate game actions, or misusing the game logic to simplify it. Therefore, hacking a game can be pretty complex since it requires different skills, including memory management, reverse engineering, and networking knowledge if the game runs online.

## Executables and Libraries

The **executable** file of an application is generally understood as a standalone binary file containing the compiled code we want to run. While some applications contain all the code they need to run in their executables, many applications usually rely on external code in library files with the "so" extension.

Library files are collections of functions that many applications can reuse. Unlike applications, they can't be directly executed as they serve no purpose by themselves. For a library function to be run, an executable will need to call it. The main idea behind libraries is to pack commonly used functions so developers don't need to reimplement them for every new application they develop.

For example, imagine you are developing a game that requires adding two numbers together. Since mathematical functions are so commonly used, you could implement a library called `libmaths` to handle all your math functions, one of which could be called `add()`. The function would take two arguments (`x` and `y`) and return the `sum` of both numbers.

Note that the application trusts the library to perform the requested operation correctly. From an attacker's standpoint, if we could somehow intercept the function calls from the executable to the library, we could alter the arguments sent or the return value. This would allow us to force the application to behave in strange ways.

## Hacking with Frida

Frida is a powerful instrumentation tool that allows us to analyze, modify, and interact with running applications. How does it do that? Frida creates a thread in the target process; that thread will execute some bootstrap code that allows the interaction. This interaction, known as the agent, permits the injection of JavaScript code, controlling the application's behaviour in real-time. One of the most crucial functionalities of Frida is the Interceptor. This functionality lets us alter internal functions' input or output or observe their behaviour. In the example above, Frida would allow us to intercept and change the values of `x` and `y` that the library would receive on the fly. It would also allow us to change the returned `sum` value that is sent to the executable:

Let's take a look at a hypothetical example. In this example, a number is simply printed on the console.

Let's take a look at a hypothetical example. In this example, a number is simply printed on the console.

VMTerminal

```shell-session
ubuntu@tryhackme:~$ ./main
Hello, 1!
Hello, 1!
Hello, 1!
Hello, 1!
Hello, 1!
Hello, 1!
Hello, 1!
Hello, 1!
```

What we want to achieve is replacing that value with an arbitrary one, let's say 1337.

Before proceeding, we will run `frida-trace` for the first time so that it creates **handlers** for each library function used by the game. By editing the handler files, we can tell Frida what to do with the intercepted values of a function call. To have Frida create the handler files, you would run the following command:

`frida-trace ./main -i '*'`

You will now see the `__handlers__` directory, containing JavaScript files for each function your application calls from a library. One such function will be called `say_hello()` and have a corresponding handler at `__handlers__/libhello.so/say_hello.js`, allowing us to interact with the target application in real-time.

We don't need to understand what the file does just yet; we will review this later in the task.

Each handler will have two functions known as hooks since they are hooked into the function respectively before and after the function call:

- **onEnter:** From this function, we are mainly interested in the `args` variable, an array of pointers to the parameters used by our target function - a pointer is just an address to a value.
- **onLeave:** here, we are interested in the `retval` variable, which will contain a pointer to the variable returned.

```javascript
// Frida JavaScript script to intercept `say_hello` 
Interceptor.attach(Module.getExportByName(null, "say_hello"), { 
    onEnter: function (log, args, state) { }, 
    onLeave: function (log, retval, state) { } 
});
```

We have pointers and not just variables because if we change any value, it has to be permanent; otherwise, we will modify a copy of the value, which will not be persistent.

Returning to our objective, we want to set the parameter with 1337. To do so, we must replace the first arguments of the args array: `args[0]` with a pointer to a variable containing 1337.

Frida has a function called `ptr()` that does exactly what we need: allocate some space for a variable and return its pointer. We also want to log the value of the original argument, and we have to use the function `toInt32()`, which reads the value of that pointer.

```javascript
// say_hello.js
// Hook the say_hello function from libhello.so

// Attach to the running process of "main"
Interceptor.attach(Module.findExportByName(null, "say_hello"), {
    onEnter: function (args) {
        // Intercept the original argument (args[0] is the first argument)
        var originalArgument = args[0].toInt32();
        console.log("Original argument: " + originalArgument);
        // Replace the original value with 1337
        args[0] = ptr(1337);
        log('say_hello()');
    }
});
```

When we rerun the executable with Frida, we notice that we can intercept the program's logic, setting 1337 as the parameter function. The original value is logged as expected using the following command:

VMTerminal

```shell-session
ubuntu@tryhackme:~$ frida-trace ./main -i 'say*'
Hello, 1337!
Original argument: 1
/* TID 0x5ec9 */
11 ms  say_hello()
Hello, 1337!
Original argument: 1
```

Now that we better understand Frida's capabilities, we can return to `frida-trace`. We have already seen that it generates the JavaScript script to hook a specific function automatically, but how does it know which function needs to be hooked? The parameter `-i` tells Frida which library to hook, and it can filter using the wildcard, tracing all the functions in all the libraries loaded.






### Answer the questions below

What is the OTP flag?

`THM{one_tough_password}`

What is the billionaire item flag?

 `THM{credit_card_undeclined}`

What is the biometric flag?

`THM{dont_smash_your_keyboard}`