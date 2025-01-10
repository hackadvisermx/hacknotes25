
```python
def pizza(pedido):
	ingr = { "T":1.50, "O":1.25, "P":3.50, "M":3.75, "A":0.40}
	sur = { "T":0,"O":0,"P":0,"M":0,"A":0 }
	base = 15
	total=0
	subtotal=0
	for c in pedido:
		if c in 'TOPMA' and sur[c]==0:
			subtotal += ingr[c]
			sur[c] +=1

	total = base + subtotal
	if total>20 : total = total - (total * 0.05)
	print('{:.2f}'.format((round(total,2)))

while True:
    try:
        line = input()
    except EOFError:
        break
    pizza(line)

print()

```