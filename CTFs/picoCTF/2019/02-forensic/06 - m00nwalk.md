# m00nwalk
Decode this [message](https://jupiter.challenges.picoctf.org/static/d6fcea5e3c6433680ea4f914e24fab61/message.wav) from the moon.

Hint1: How did pictures from the moon landing get sent back to Earth?

Hint2: What is the CMU mascot?, that might help select a RX option

## Solucion

~ How did pictures from the moon landing get sent back to Earth?
	sstv
 
~ SSTV Decoder github> https://github.com/colaclanth/sstv

```bash
sudo git clone https://github.com/colaclanth/sstv.git
sudo python setup.py install
sstv -d message.wav -o resultado.png
```

- la bandera esa en a imgagen para verla mejor rotada
- rotar imagen, abrirla con majeador de imagenes de linux

way 1
	- g> imagemagick linux
	- apt install imagemagick
	- convert resultado.png -rotate 180 out.png

way 2
	Image viewer en XFCE
	View - Rotation 


# Referencias

- apolo 11 - sstv : https://en.wikipedia.org/wiki/Apollo_11_missing_tapes
- sstv decoder git repo : https://github.com/colaclanth/sstv