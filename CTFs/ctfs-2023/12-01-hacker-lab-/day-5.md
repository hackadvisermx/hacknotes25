
## Introduction

The Northern Lights appeared at exceptionally low latitudes this year due to the high level of solar activity. But from Santa's grotto at the North Pole, it's not unusual at all to see them stretching across the sky. Snowball the elf tried to capture a video of the aurora for his Instagram feed, but his phone doesn't work well in poor light, and the results were rather grainy and disappointing. Is there anything you can do to obtain a clearer image?

---

Download the attachment and find the flag.

Flag format: `HV23{}`

---

_This challenge was written by **monkey9508**. Live could be a dream..._


## Solución

- Nos dan un video que se ve poco, aplique un filtro y se arreglo

```
ffmpeg -i aurora.mp4 -vf "hqdn3d=150" out.mp4

ffmpeg -i aurora.mp4 -vf "atadenoise,hqdn3d=150,unsharp=3:7:0.5" out.mp4
```

```
HV23{M4gn3t0sph3r1c_d1sturb4nc3}
```

## Referencias

- https://www.youtube.com/watch?v=I9-VEUs1ZsE
- https://ffmpeg.org/ffmpeg-filters.html
- 