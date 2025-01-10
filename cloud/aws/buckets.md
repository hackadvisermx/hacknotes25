```
cat 2-subdomains-live.txt |  httpx -title -web-server -status-code -follow-redirects -vhost -ip | grep -i AmazonS3
```


```
aws s3 ls s3://volaris.com/ --no-sign-request
```



```
aws s3 ls s3://cdmxassets/storage/ --no-sign-request
aws s3 cp s3://cdmxassets/storage/.gitignore . --no-sign-request

```

```
 git clone https://github.com/0xSearches/sandcastle.git
 sudo apt install python2
 curl https://bootstrap.pypa.io/pip/2.7/get-pip.py --output get-pip.p
 pip2 install requests
 
```

```
https://github.com/nahamsec/lazys3

```

- nuclei s3 detect
```
nuclei -l uaz.txt -t /root/.local/nuclei-templates/http/technologies/s3-detect.yaml
```


## Referencias
- https://medium.com/@qaafqasim/the-ultimate-guide-to-hack-s3-buckets-data-leaks-and-discovery-techniques-40a29641d18b
- https://securitycipher.medium.com/s3-bucket-recon-2d7c2bbf41ef
- https://github.com/mxm0z/awesome-sec-s3
- https://docs.aws.amazon.com/cli/latest/reference/s3api/

## Tools
- https://github.com/0xmoot/s3sec
- 