

Hey,

I found an open S3 Amazon bucket `ford-assets`. While I can’t confirm if you own it or not, it appears that it is publicly writable using the aws cli.

When I write to ford-assets, I get: move: ./poc.txt to s3://ford-assets/poc.txt

```
aws s3 cp ./poc.txt s3://ford-dataset// --no-sign-request
upload: ./poc.txt to s3://ford-dataset//poc.txt
```

And also when I remove file, I get: delete: s3://ford-assets/poc.txt

```
aws s3 rm s3://ford-dataset/poc.txt --no-sign-request
delete: s3://ford-dataset/poc.txt
```

Assuming you own it, the security issue is that someone could delete files or write something malicious into the bucket and someone on your team unknowingly opening it.