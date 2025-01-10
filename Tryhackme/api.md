
- maquinas corriendo

https://tryhackme.com/api/vm/running


- terminar todas las máquinas activas 

```javascript
fetch('/api/vm/running')
  .then(r => r.json())
  .then(vms =>
    vms.forEach(vm =>
      fetch('/api/vm/terminate', {
        method: 'POST',
        body: JSON.stringify({ code: vm.roomId }),
        headers: {
          'csrf-token': csrfToken,
          'Content-Type': 'application/json'
        }
      })
    )
  )
```

```javascript
fetch('/api/vm/running')
  .then(r => r.json())
  .then(vms =>
    vms.forEach(vm => { 
      if (confirm('Terminate ' + vm.roomId + '?'))
        fetch('/api/vm/terminate', {
          method: 'POST',
          body: JSON.stringify({ code: vm.roomId }),
          headers: {
            'csrf-token': csrfToken,
            'Content-Type': 'application/json'
          }
        });
    });
  );
```