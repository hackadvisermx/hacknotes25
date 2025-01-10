Do you know how to use the web inspector?Start searching [here](http://titan.picoctf.net:58480/) to find the flag

### Hints
- Use the web inspector on other files included by the web page.
- The flag may or may not be encoded
## Solve

Ir a la pagina: view-source:http://titan.picoctf.net:58480/about.html

```
section class="about" notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDdiOTFjNzl9">
   <h1>
    Try inspecting the page!! You might find it there
   </h1>
   <!-- .about-container -->
  </section>

notify_true="cGljb0NURnt3ZWJfc3VjYzNzc2Z1bGx5X2QzYzBkZWRfMDdiOTFjNzl9">


picoCTF{web_succ3ssfully_d3c0ded_07b91c79}
```