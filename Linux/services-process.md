# Service and Process Management

- Manejo de procesos con systemctl

```bash
systemctl start ssh
systemctl status ssh
systemctl enable ssh
systemctl list-units --type=service
```



- Matar un proceso

Un proceso puede estar en uno de los siguientes estados:

- Running
- Waiting
- Stopped
- Zombie


```bash
kill -l
kill 9 PID

