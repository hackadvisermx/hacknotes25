
# Task 23  [Day 17] Traffic analysis I Tawt I Taw A C2 Tat!

## Solucion

### Getting Started With the SiLK Suite

```
ubuntu@ip-10-10-196-123:~/Desktop$ silk_config -v
silk_config: part of SiLK 3.19.1; configuration settings:
    * Root of packed data tree:         /var/silk/data
    * Packing logic:                    Run-time plug-in
    * Timezone support:                 UTC
    * Available compression methods:    lzo1x [default], none, zlib
    * IPv6 network connections:         yes
    * IPv6 flow record support:         yes
    * IPset record compatibility:       3.14.0
    * IPFIX/NetFlow9/sFlow collection:  ipfix,netflow9,sflow
    * Transport encryption:             GnuTLS
    * PySiLK support:                   /usr/local/lib/python2.7/site-packages
    * Enable assert():                  no
Copyright (C) 2001-2020 by Carnegie Mellon University
GNU General Public License (GPL) Rights pursuant to Version 2, June 1991.
Some included library code covered by LGPL 2.1; see source for details.
Government Purpose License Rights (GPLR) pursuant to DFARS 252.227-7013.
Send bug reports, feature requests, and comments to netsa-help@cert.org.
ubuntu@ip-10-10-196-123:~/Desktop$ 
```

### Flow File Properties with SilK Suite: rwfileinfo

```
rwfileinfo suspicious-flows.silk 
suspicious-flows.silk:
  format(id)          FT_RWIPV6ROUTING(0x0c)
  version             16
  byte-order          littleEndian
  compression(id)     lzo1x(2)
  header-length       88
  record-length       88
  record-version      1
  silk-version        3.19.1
  count-records       11774
  file-size           152366
  command-lines       
                   1  rwipfix2silk --silk-output=test.silk
```
### Reading Flow Files: rwcut
```
rwcut suspicious-flows.silk  --num-recs=5
                                    sIP|                                    dIP|sPort|dPort|pro|   packets|     bytes|   flags|                  sTime| duration|                  eTime|sen|
                        175.215.235.223|                        175.215.236.223|   80| 3222|  6|         1|        44| S  A   |2023/12/05T09:33:07.719|    0.000|2023/12/05T09:33:07.719| S0|
                        175.215.235.223|                        175.215.236.223|   80| 3220|  6|         1|        44| S  A   |2023/12/05T09:33:07.725|    0.000|2023/12/05T09:33:07.725| S0|
                        175.215.235.223|                        175.215.236.223|   80| 3219|  6|         1|        44| S  A   |2023/12/05T09:33:07.738|    0.000|2023/12/05T09:33:07.738| S0|
                        175.215.235.223|                        175.215.236.223|   80| 3218|  6|         1|        44| S  A   |2023/12/05T09:33:07.741|    0.000|2023/12/05T09:33:07.741| S0|
                        175.215.235.223|                        175.215.236.223|   80| 3221|  6|         1|        44| S  A   |2023/12/05T09:33:07.743|    0.000|2023/12/05T09:33:07.743| S0|
```

```
rwcut suspicious-flows.silk  --fields=protocol,sIP,sPort,dIP,dPort --num-recs=5
pro|                                    sIP|sPort|                                    dIP|dPort|
  6|                        175.215.235.223|   80|                        175.215.236.223| 3222|
  6|                        175.215.235.223|   80|                        175.215.236.223| 3220|
  6|                        175.215.235.223|   80|                        175.215.236.223| 3219|
  6|                        175.215.235.223|   80|                        175.215.236.223| 3218|
  6|                        175.215.235.223|   80|                        175.215.236.223| 3221|
```

- **Source IP:** `sIP`
- **Destination IP:** `dIP`
- **Source port:** `sPort`
- **Destination port:** `dPort`
- **Duration:** `duration`
- **Start time:** `sTime`
- **End time:** `eTime`

### Filtering the Event of Interest: rwfilter

```
rwfilter suspicious-flows.silk --proto=17 --pass=stdout | rwcut --fields=protocol,sIP,sPort,dIP,dPort --num-recs=5
pro|                                    sIP|sPort|                                    dIP|dPort|
 17|                        175.175.173.221|59580|                        175.219.238.243|   53|
 17|                        175.219.238.243|   53|                        175.175.173.221|59580|
 17|                        175.175.173.221|47888|                        175.219.238.243|   53|
 17|                        175.219.238.243|   53|                        175.175.173.221|47888|
 17|                        175.175.173.221|49950|                        175.219.238.243|   53|

```

- **Protocols:** `--proto`
    - Possible values are 0-255.
- **Port filters:**
    - Any port: `--aport`
    - Source port: `--sport`
    - Destination port: `--dport`
    - Possbile values are 0-65535.
- **IP filters:** Any IP address: `--any-address`
    - Source address: `--saddress` 
    - Destination address: `--daddress`
- **Volume filters:** Number of the packets `--packets` number of the bytes `--bytes`

### Quick Statistics: rwstats

```
rwstats suspicious-flows.silk --fields=dPort --values=records,packets,bytes,sIP-Distinct,dIP-Distinct --count=10
INPUT: 11774 Records for 5713 Bins and 11774 Total Records
OUTPUT: Top 10 Bins by Records
dPort|   Records|        Packets|               Bytes|        sIP-Distinct|        dIP-Distinct|  %Records|   cumul_%|
   53|      4160|           4333|              460579|                   1|                   1| 35.332088| 35.332088|
   80|      1658|           1658|               66320|                   1|                   1| 14.081875| 49.413963|
40557|         4|              4|                 720|                   1|                   1|  0.033973| 49.447936|
53176|         3|              3|                 465|                   1|                   1|  0.025480| 49.473416|
50088|         3|              3|                 517|                   1|                   1|  0.025480| 49.498896|
50258|         3|              3|                 517|                   1|                   1|  0.025480| 49.524376|
52345|         3|              3|                 513|                   1|                   1|  0.025480| 49.549856|
47920|         3|              3|                 515|                   1|                   1|  0.025480| 49.575335|
50105|         3|              3|                 563|                   1|                   1|  0.025480| 49.600815|
52167|         3|              3|                 561|                   1|                   1|  0.025480| 49.626295|
```

### Assemble the Toolset and Start Hunting Anomalies!

```
rwstats suspicious-flows.silk --fields=sIP --values=bytes --count=10 --top
INPUT: 11774 Records for 8 Bins and 1412597 Total Bytes
OUTPUT: Top 10 Bins by Bytes
                                    sIP|               Bytes|    %Bytes|   cumul_%|
                        175.219.238.243|              735229| 52.048036| 52.048036|
                        175.175.173.221|              460731| 32.615884| 84.663920|
                        175.215.235.223|              145948| 10.331892| 94.995813|
                        175.215.236.223|               66320|  4.694899| 99.690712|
                         181.209.166.99|                2744|  0.194252| 99.884964|
                         253.254.236.39|                1380|  0.097692| 99.982656|
                         205.213.108.99|                 152|  0.010760| 99.993416|
87d6:ebe3:bdd7:ece3:7dfb:3cb0:83b7:a4fa|                  93|  0.006584|100.000000|

```

```
rwstats suspicious-flows.silk --fields=sIP,dIP --values=records,bytes,packets --count=10
INPUT: 11774 Records for 9 Bins and 11774 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|                                    dIP|   Records|               Bytes|        Packets|  %Records|   cumul_%|
                        175.175.173.221|                        175.219.238.243|      4160|              460579|           4333| 35.332088| 35.332088|
                        175.219.238.243|                        175.175.173.221|      4158|              735229|           4331| 35.315101| 70.647189|
                        175.215.235.223|                        175.215.236.223|      1781|              145948|           3317| 15.126550| 85.773739|
                        175.215.236.223|                        175.215.235.223|      1658|               66320|           1658| 14.081875| 99.855614|
                         253.254.236.39|                         181.209.166.99|         8|                1380|             25|  0.067946| 99.923560|
                         181.209.166.99|                         253.254.236.39|         4|                2744|             24|  0.033973| 99.957534|
                         205.213.108.99|                        175.175.173.221|         2|                 152|              2|  0.016987| 99.974520|
                        175.175.173.221|                         205.213.108.99|         2|                 152|              2|  0.016987| 99.991507|
87d6:ebe3:bdd7:ece3:7dfb:3cb0:83b7:a4fa|ffd2:ece3:bdd7:ece3:bdd7:ece3:bdd7:ec35|         1|                  93|              1|  0.008493|100.000000|

```


```
rwfilter suspicious-flows.silk --aport=53 --pass=stdout | rwstats --fields=sIP,dIP --values=records,bytes,packets --count=10 
INPUT: 8318 Records for 2 Bins and 8318 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|                                    dIP|   Records|               Bytes|        Packets|  %Records|   cumul_%|
                        175.175.173.221|                        175.219.238.243|      4160|              460579|           4333| 50.012022| 50.012022|
                        175.219.238.243|                        175.175.173.221|      4158|              735229|           4331| 49.987978|100.000000|
```

```
rwfilter suspicious-flows.silk --saddress=175.175.173.221 --dport=53 --pass=stdout | rwcut --fields=sIP,dIP,stime | head -10
                                    sIP|                                    dIP|                  sTime|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:44.825|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:45.678|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:45.833|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:46.743|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:46.898|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:47.753|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:47.903|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:48.764|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:48.967|

```

```
rwfilter suspicious-flows.silk --saddress=175.219.238.243 --dport=53 --pass=stdout | rwcut --fields=sIP,dIP,stime | head -10
                                    sIP|                                    dIP|                  sTime|

```


```
rwfilter suspicious-flows.silk --any-address=175.175.173.221 --pass=stdout | rwstats --fields=sIP,dIP --count=10
INPUT: 8322 Records for 4 Bins and 8322 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|                                    dIP|   Records|  %Records|   cumul_%|
                        175.175.173.221|                        175.219.238.243|      4160| 49.987984| 49.987984|
                        175.219.238.243|                        175.175.173.221|      4158| 49.963951| 99.951935|
                         205.213.108.99|                        175.175.173.221|         2|  0.024033| 99.975967|
                        175.175.173.221|                         205.213.108.99|         2|  0.024033|100.000000|
```

```
rwfilter suspicious-flows.silk --any-address=205.213.108.99 --pass=stdout | rwstats --fields=sIP,sPort,dIP,dPort,proto --count=10
INPUT: 4 Records for 4 Bins and 4 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|sPort|                                    dIP|dPort|pro|   Records|  %Records|   cumul_%|
                         205.213.108.99|  123|                        175.175.173.221|47640| 17|         1| 25.000000| 25.000000|
                         205.213.108.99|  123|                        175.175.173.221|43210| 17|         1| 25.000000| 50.000000|
                        175.175.173.221|47640|                         205.213.108.99|  123| 17|         1| 25.000000| 75.000000|
                        175.175.173.221|43210|                         205.213.108.99|  123| 17|         1| 25.000000|100.000000|

```

- Puerto 80
```
rwfilter suspicious-flows.silk --aport=80 --pass=stdout | rwstats --fields=sIP,dIP --count=10
INPUT: 3439 Records for 2 Bins and 3439 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|                                    dIP|   Records|  %Records|   cumul_%|
                        175.215.235.223|                        175.215.236.223|      1781| 51.788311| 51.788311|
                        175.215.236.223|                        175.215.235.223|      1658| 48.211689|100.000000|

```

```
rwfilter suspicious-flows.silk --aport=80 --pass=stdout | rwstats --fields=sIP,dIP,dPort --count=10
INPUT: 3439 Records for 1782 Bins and 3439 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|                                    dIP|dPort|   Records|  %Records|   cumul_%|
                        175.215.236.223|                        175.215.235.223|   80|      1658| 48.211689| 48.211689|
                        175.215.235.223|                        175.215.236.223| 3290|         1|  0.029078| 48.240768|
                        175.215.235.223|                        175.215.236.223| 4157|         1|  0.029078| 48.269846|
                        175.215.235.223|                        175.215.236.223| 4871|         1|  0.029078| 48.298924|
                        175.215.235.223|                        175.215.236.223| 4515|         1|  0.029078| 48.328002|
                        175.215.235.223|                        175.215.236.223| 4629|         1|  0.029078| 48.357081|
                        175.215.235.223|                        175.215.236.223| 4138|         1|  0.029078| 48.386159|
                        175.215.235.223|                        175.215.236.223| 4765|         1|  0.029078| 48.415237|
                        175.215.235.223|                        175.215.236.223| 4020|         1|  0.029078| 48.444315|
                        175.215.235.223|                        175.215.236.223| 3248|         1|  0.029078| 48.473393|

```

```
wfilter suspicious-flows.silk --saddress=175.215.236.223 --pass=stdout | rwcut --fields=sIP,dIP,dPort,flag,stime | head
                                    sIP|                                    dIP|dPort|   flags|                  sTime|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.723|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.732|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.748|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.740|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.715|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.774|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.757|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.765|
                        175.215.236.223|                        175.215.235.223|   80| S      |2023/12/05T09:33:07.782|
rwfilter: Error writing to stream 'stdout': Broken pipe

```

```
rwfilter suspicious-flows.silk --saddress=175.215.236.223 --pass=stdout | rwstats --fields=sIP,flag,dIP --count=10
INPUT: 1658 Records for 1 Bin and 1658 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|   flags|                                    dIP|   Records|  %Records|   cumul_%|
                        175.215.236.223| S      |                        175.215.235.223|      1658|100.000000|100.000000|

```

```
rwfilter suspicious-flows.silk --saddress=175.215.235.223 --pass=stdout | rwstats --fields=sIP,flag,dIP --count=10
INPUT: 1781 Records for 1 Bin and 1781 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|   flags|                                    dIP|   Records|  %Records|   cumul_%|
                        175.215.235.223| S  A   |                        175.215.236.223|      1781|100.000000|100.000000|

```

```
rwfilter suspicious-flows.silk --any-address=175.215.236.223 --pass=stdout | rwstats --fields=sIP,dIP --count=10
INPUT: 3439 Records for 2 Bins and 3439 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|                                    dIP|   Records|  %Records|   cumul_%|
                        175.215.235.223|                        175.215.236.223|      1781| 51.788311| 51.788311|
                        175.215.236.223|                        175.215.235.223|      1658| 48.211689|100.000000|
```
## Respuestas

### Answer the questions below

Which version of SiLK is installed on the VM? 
3.19.1

What is the size of the flows in the count records?  
11774

What is the start time (sTime) of the sixth record in the file?  
 2023/12/05T09:33:07.755

```
ubuntu@ip-10-10-114-224:~/Desktop$ !3
rwcut suspicious-flows.silk  --fields=sTime,protocol,sIP,sPort,dIP,dPort --num-recs=6
                  sTime|pro|                                    sIP|sPort|                                    dIP|dPort|
2023/12/05T09:33:07.719|  6|                        175.215.235.223|   80|                        175.215.236.223| 3222|
2023/12/05T09:33:07.725|  6|                        175.215.235.223|   80|                        175.215.236.223| 3220|
2023/12/05T09:33:07.738|  6|                        175.215.235.223|   80|                        175.215.236.223| 3219|
2023/12/05T09:33:07.741|  6|                        175.215.235.223|   80|                        175.215.236.223| 3218|
2023/12/05T09:33:07.743|  6|                        175.215.235.223|   80|                        175.215.236.223| 3221|
2023/12/05T09:33:07.755|  6|                        175.215.235.223|   80|                        175.215.236.223| 3225|
ubuntu@ip-10-10-114-224:~/Desktop$ 
```

What is the destination port of the sixth UDP record?   
49950

```
rwfilter suspicious-flows.silk --proto=17 --pass=stdout | rwcut --fields=protocol,sIP,sPort,dIP,dPort --num-recs=6
pro|                                    sIP|sPort|                                    dIP|dPort|
 17|                        175.175.173.221|59580|                        175.219.238.243|   53|
 17|                        175.219.238.243|   53|                        175.175.173.221|59580|
 17|                        175.175.173.221|47888|                        175.219.238.243|   53|
 17|                        175.219.238.243|   53|                        175.175.173.221|47888|
 17|                        175.175.173.221|49950|                        175.219.238.243|   53|
 17|                        175.219.238.243|   53|                        175.175.173.221|49950|

```
  

What is the record value (%) of the dport 53?  

35.332088


```
rwstats suspicious-flows.silk --fields=dPort --values=records,packets,bytes,sIP-Distinct,dIP-Distinct --count=6 
INPUT: 11774 Records for 5713 Bins and 11774 Total Records
OUTPUT: Top 6 Bins by Records
dPort|   Records|        Packets|               Bytes|        sIP-Distinct|        dIP-Distinct|  %Records|   cumul_%|
   53|      4160|           4333|              460579|                   1|                   1| 35.332088| 35.332088|
   80|      1658|           1658|               66320|                   1|                   1| 14.081875| 49.413963|
40557|         4|              4|                 720|                   1|                   1|  0.033973| 49.447936|
50088|         3|              3|                 517|                   1|                   1|  0.025480| 49.473416|
50105|         3|              3|                 563|                   1|                   1|  0.025480| 49.498896|
52345|         3|              3|                 513|                   1|                   1|  0.025480| 49.524376|

```


What is the number of bytes transmitted by the top talker on the network?  
735229
```
rwstats suspicious-flows.silk --fields=sIP --values=bytes --count=10 --top
INPUT: 11774 Records for 8 Bins and 1412597 Total Bytes
OUTPUT: Top 10 Bins by Bytes
                                    sIP|               Bytes|    %Bytes|   cumul_%|
                        175.219.238.243|              735229| 52.048036| 52.048036|
                        175.175.173.221|              460731| 32.615884| 84.663920|
                        175.215.235.223|              145948| 10.331892| 94.995813|
                        175.215.236.223|               66320|  4.694899| 99.690712|
                         181.209.166.99|                2744|  0.194252| 99.884964|
                         253.254.236.39|                1380|  0.097692| 99.982656|
                         205.213.108.99|                 152|  0.010760| 99.993416|
87d6:ebe3:bdd7:ece3:7dfb:3cb0:83b7:a4fa|                  93|  0.006584|100.000000| 
```

What is the sTime value of the first DNS record going to port 53?  

```
rwfilter suspicious-flows.silk --dport=53 --pass=stdout | rwcut --fields=sTime --num-recs=6
                  sTime|
2023/12/08T04:28:44.825|
2023/12/08T04:28:45.678|
2023/12/08T04:28:45.833|
2023/12/08T04:28:46.743|
2023/12/08T04:28:46.898|
2023/12/08T04:28:47.753|


```

What is the IP address of the host that the C2 potentially controls? (In defanged format: 123[.]456[.]789[.]0 )  
175[.]175[.]173[.]221

```
 rwfilter suspicious-flows.silk --saddress=175.175.173.221 --dport=53 --pass=stdout | rwcut --fields=sIP,dIP,stime | head -10
                                    sIP|                                    dIP|                  sTime|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:44.825|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:45.678|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:45.833|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:46.743|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:46.898|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:47.753|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:47.903|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:48.764|
                        175.175.173.221|                        175.219.238.243|2023/12/08T04:28:48.967|

```

Which IP address is suspected to be the flood attacker? (In defanged format: 123[.]456[.]789[.]0 )  
 

```
rwfilter suspicious-flows.silk --aport=80 --pass=stdout | rwstats --fields=sIP,dIP,dPort --count=10
INPUT: 3439 Records for 1782 Bins and 3439 Total Records
OUTPUT: Top 10 Bins by Records
                                    sIP|                                    dIP|dPort|   Records|  %Records|   cumul_%|
                        175.215.236.223|                        175.215.235.223|   80|      1658| 48.211689| 48.211689|
                        175.215.235.223|                        175.215.236.223| 3290|         1|  0.029078| 48.240768|
                        175.215.235.223|                        175.215.236.223| 4157|         1|  0.029078| 48.269846|
                        175.215.235.223|                        175.215.236.223| 4871|         1|  0.029078| 48.298924|
                        175.215.235.223|                        175.215.236.223| 4515|         1|  0.029078| 48.328002|
                        175.215.235.223|                        175.215.236.223| 4629|         1|  0.029078| 48.357081|
                        175.215.235.223|                        175.215.236.223| 4138|         1|  0.029078| 48.386159|
                        175.215.235.223|                        175.215.236.223| 4765|         1|  0.029078| 48.415237|
                        175.215.235.223|                        175.215.236.223| 4020|         1|  0.029078| 48.444315|
                        175.215.235.223|                        175.215.236.223| 3248|         1|  0.029078| 48.473393|
 
```


What is the sent SYN packet's number of records?  

 1658


Task 23  [Day 17] Traffic analysis I Tawt I Taw A C2 Tat!


I completed Task 23  [Day 17] Traffic analysis I Tawt I Taw A C2 Tat!, Don't miss out Tryhackme #AdventOfCyber @RealTryHackMe https://tryhackme.com/room/adventofcyber2023

## Referencias
- SiLK, the System for Internet-Level Knowledge: https://tools.netsa.cert.org/silk/

- 