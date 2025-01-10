

## **How does it happen?**

Security misconfiguration depicts an implementation of **incorrect and poorly configured security controls** that put the security of the whole API at stake. Several factors can result in security misconfiguration, including improper/incomplete default configuration, publically accessible cloud storage, [Cross-Origin Resource Sharing (CORS)](https://developer.mozilla.org/en-US/docs/Web/HTTP/CORS), and error messages displayed with sensitive data. Intruders can take advantage of these misconfigurations to perform detailed reconnaissance and get unauthorised access to the system. 

Security misconfigurations are usually detected by vulnerability scanners or auditing tools and thus can be curtailed at the initial level. API documentation, a list of endpoints, error logs etc., **must not be publically accessible** to ensure safety against security misconfigurations. Typically, companies deploy security controls like web application firewalls, which are not configured to block undesired requests and attacks.  

## **Likely Impact** 

Security misconfiguration can give intruders complete knowledge of API components. Firstly, it allows intruders to bypass security mechanisms. **Stack trace or other detailed errors** can provide the malicious actor access to confidential data and essential system details, further aiding the intruder in profiling the system and gaining entry.    


## Practical Example  

-   Continue to use the Chrome browser and Talend API Tester for debugging in the VM.      
-   The company MHT is facing serious server availability issues. Therefore, they assigned Bob to develop an API endpoint `/apirule7/ping_v` (GET) that will share details regarding server health and status.
-   Bob successfully designed the endpoint; however, he forgot to implement any error handling to avoid any information leakage.

```curl http://localhost/MHT/apirule7/ping_v
string(6269) "#0 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Controller.php(54): App\Http\Controllers\API7UsersController->auth_v(Object(Illuminate\Http\Request))
#1 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\ControllerDispatcher.php(45): Illuminate\Routing\Controller->callAction('auth_v', Array)
#2 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Route.php(261): Illuminate\Routing\ControllerDispatcher->dispatch(Object(Illuminate\Routing\Route), Object(App\Http\Controllers\API7UsersController), 'auth_v')
#3 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Route.php(204): Illuminate\Routing\Route->runController()
#4 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(695): Illuminate\Routing\Route->run()
#5 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(128): Illuminate\Routing\Router->Illuminate\Routing\{closure}(Object(Illuminate\Http\Request))
#6 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Middleware\SubstituteBindings.php(50): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#7 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Routing\Middleware\SubstituteBindings->handle(Object(Illuminate\Http\Request), Object(Closure))
#8 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(103): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#9 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(697): Illuminate\Pipeline\Pipeline->then(Object(Closure))
#10 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(672): Illuminate\Routing\Router->runRouteWithinStack(Object(Illuminate\Routing\Route), Object(Illuminate\Http\Request))
#11 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(636): Illuminate\Routing\Router->runRoute(Object(Illuminate\Http\Request), Object(Illuminate\Routing\Route))
#12 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Routing\Router.php(625): Illuminate\Routing\Router->dispatchToRoute(Object(Illuminate\Http\Request))
#13 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Kernel.php(166): Illuminate\Routing\Router->dispatch(Object(Illuminate\Http\Request))
#14 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(128): Illuminate\Foundation\Http\Kernel->Illuminate\Foundation\Http\{closure}(Object(Illuminate\Http\Request))
#15 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\TransformsRequest.php(21): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#16 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull.php(31): Illuminate\Foundation\Http\Middleware\TransformsRequest->handle(Object(Illuminate\Http\Request), Object(Closure))
#17 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Foundation\Http\Middleware\ConvertEmptyStringsToNull->handle(Object(Illuminate\Http\Request), Object(Closure))
#18 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\TransformsRequest.php(21): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#19 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\TrimStrings.php(40): Illuminate\Foundation\Http\Middleware\TransformsRequest->handle(Object(Illuminate\Http\Request), Object(Closure))
#20 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Foundation\Http\Middleware\TrimStrings->handle(Object(Illuminate\Http\Request), Object(Closure))
#21 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\ValidatePostSize.php(27): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#22 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Foundation\Http\Middleware\ValidatePostSize->handle(Object(Illuminate\Http\Request), Object(Closure))
#23 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Middleware\PreventRequestsDuringMaintenance.php(86): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#24 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Foundation\Http\Middleware\PreventRequestsDuringMaintenance->handle(Object(Illuminate\Http\Request), Object(Closure))
#25 C:\xampp\htdocs\mht\vendor\fruitcake\laravel-cors\src\HandleCors.php(38): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#26 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Fruitcake\Cors\HandleCors->handle(Object(Illuminate\Http\Request), Object(Closure))
#27 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Http\Middleware\TrustProxies.php(39): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#28 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(167): Illuminate\Http\Middleware\TrustProxies->handle(Object(Illuminate\Http\Request), Object(Closure))
#29 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Pipeline\Pipeline.php(103): Illuminate\Pipeline\Pipeline->Illuminate\Pipeline\{closure}(Object(Illuminate\Http\Request))
#30 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Kernel.php(141): Illuminate\Pipeline\Pipeline->then(Object(Closure))
#31 C:\xampp\htdocs\mht\vendor\laravel\framework\src\Illuminate\Foundation\Http\Kernel.php(110): Illuminate\Foundation\Http\Kernel->sendRequestThroughRouter(Object(Illuminate\Http\Request))
#32 C:\xampp\htdocs\mht\public\index.php(52): Illuminate\Foundation\Http\Kernel->handle(Object(Illuminate\Http\Request))
#33 C:\xampp\htdocs\mht\server.php(21): require_once('C:\\xampp\\htdocs...')
#34 {main}"

```

- segura

```
curl http://localhost/MHT/apirule7/ping_s
{"success":"false","msg":"Network Server @ 2 - Malfunctioned - Errod ID #1401. Please contact administator at support@mht.com for further queries."}
```