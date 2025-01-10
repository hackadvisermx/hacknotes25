# Hunt [Web]

### 150

Agent, it looks like ARIA has spun up a simple website. Is there anything you can find to give more information about it's plans?

[https://uscybercombine-s4-hunt.chals.io/](https://uscybercombine-s4-hunt.chals.io/)


## Solve

```
https://uscybercombine-s4-hunt.chals.io/robots.txt
User-agent: Humans

Disallow: /secret-bot-spot

p2: 0f_th3_
```

```
https://uscybercombine-s4-hunt.chals.io/secret-bot-spot
```


```
SIVBGR{r1s3_0f_th3_r0b0ts!}
```