# Ejemplos basicos bash


- imprimir el archivo /etc/passwd linea a linea:

```bash
cat /etc/passwd | while read line; do
    echo $line 
done
```
```bash
while read line; do
    echo $line
done < /etc/passwd
```

```bash
strings data.txt | grep '==' | while read line; do echo $line; done
```

- Decompresor multiple
```bash
#!/bin/bash
name_decompressed=$(7z l content.gzip | grep "Name" -A 2 | tail -n 1  | awk 'NF{print $NF}')
while true; do
    7z l $name_compressed > /dev/null 2>&1

    if [ "$(echo $?)" == "0" ]; then
        decompresed_next=$(7z l name_decompressed | grep "Name" -A 2 | tail -n 1  | awk 'NF{print $NF}')
        7z x $name_decompressed > /dev/null 2>&1 && name_decompressed=$decompressed_next
    else
        cat $name_decompressed ; rm data* 2>/dev/null
        exit 1

    fi 
done
```

- Ciclos one liner
```bash
for i in $(seq 1 100); do echo $i; done
for i in {0000..9999}; do echo $i; done
```

- Modificar archivo /etc/hosts y luego eliminando ultima linea
```
echo "10.10.163.131    overwrite.uploadvulns.thm shell.uploadvulns.thm java.uploadvulns.thm annex.uploadvulns.thm magic.uploadvulns.thm jewel.uploadvulns.thm" | sudo tee -a /etc/hosts
sudo sed -i '$d' /etc/hosts
```

