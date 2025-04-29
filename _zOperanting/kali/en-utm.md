Instalar kali en UTM

https://medium.com/womenintechnology/install-kali-linux-virtual-machine-on-apple-m1-with-utm-6c80d930bdb0

## SPICE Agent


```
sudo apt install qemu-guest-agent
sudo apt install spice-vdagent
```



## Compartir la carpeta de utm a kali
```
```

## VirtFS

VirtFS enables [QEMU directory sharing](https://docs.getutm.app/settings-qemu/sharing/#virtfs) as an alternative to SPICE WebDAV.

After making sure your Linux installation [supports 9pfs](https://docs.getutm.app/guest-support/linux/#drivers), you can mount the share with the following command:

```

```
$ sudo mkdir [mount point]
$ sudo mount -t 9p -o trans=virtio share [mount point] -oversion=9p2000.L
```

Where `[mount point]` is the desired destination path. For example: `/media/share`.

You can also modify `/etc/fstab` and add the following line to automatically mount the share on startup:

```
share	[mount point]	9p	trans=virtio,version=9p2000.L,rw,_netdev,nofail	0	0
```

### [](https://docs.getutm.app/guest-support/linux/#fixing-permission-errors)Fixing permission errors

You may notice that accessing the mount point fails with “access denied” unless you’re the root user. This is because by default the directory inherits the UID/GID from macOS/iOS which has a different numbering scheme. You can fix the error with the following command:

```
$ sudo chown -R $USER [mount poins
```

This will not change the permissions on your host system but will store the guest ownership in a file attribute.

## Spice guest tools

```
sudo systemctl start spice-vdagent
sudo mkdir -p /etc/systemd/system/spice-vdagent.service.d/

```
https://medium.com/@max.kombarov/install-the-spice-guest-agent-tools-on-a-debian-based-system-in-vm-2bc66fc2d95b