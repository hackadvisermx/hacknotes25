## Task 1Screens wishes it was this cool.

### First things first, let's go ahead and install tmux. This can be done on Ubuntu/Kali with the command: apt-get install tmux

```
sudo apt install tmux


```

### Once tmux is installed, let's launch a new session. What command do we use to launch a new session without a custom name?

tmux

### All tmux commands start with a keyboard button combination. What is the first key in this combination?

control

## How about the second key? Note, these keys must be pressed at the same time and released before pressing the next target key in the combination. 

b

### Lets go ahead and detach from our newly created tmux session. What key do we need to add to the combo in order to detach?

d

(Ctrl + b + d)


### Well shoot, we've detached from our session. How do we list all of our sessions?

tmux ls

### What did our session name default to when we created one without a set name?

0

## Now that we've found the name of our session, how do we attach to it?


tmux a -t 0

### Let's go ahead and make a new window in this session. What key do we add to the combo in order to do this?

c

( Ctrl + b + c)

### Seems like we have plenty of windows and nothing to fill them up with. Let's remedy that problem by deploying the VM above and running and nmap scan against it. Deploy the VM now.

l> Deployamos la VM o nos aseguramos este deployada

### Run the following scan against the VM: nmap -sV -vv -sC TARGET_IP

nmap -sV -vv -sC 10.10.117.95 


### Whew! Plenty of output to work with now! If you work with a relatively small terminal like me, this output might not all fit on screen at once. To fix that, let's enter 'copy mode'. What key do we add to the combo to enter copy mode?

[

( Ctrl + b + [)

### Copy mode is very similar to 'less' and allows up to scroll up and down using the arrow keys. What if we want to go up to the very top?

g

fn + flecha arriba
fn + flecha abajo
las flecjas


### How about the bottom?

G

### What key do we press to exit 'copy mode'?

q


### This window we're working in is nice and all but I think we need an upgrade. What key do we add to the combo to split the window vertically?

%


### How about horizontally?

"

### We can now move between these panes using the key combo and arrow keys, try it out!

Ctrl + B + flechas

## We can also resize these panes by holding down the key combo and pressing the arrow keys, try it out now! 


Ctrl + B + hold + flechas


### Say one of these newly minted panes becomes unresponsive or we're just done working in it, what key do we add to the combo to 'kill' the pane?

x


### Now that's we've finished out work, what can we type to close the session?

exit


### Last but not least, how do we spawn a named tmux session named 'neat'?

tmux new -s neat



## PRobar los


```

ctrl + b + ,   ---- Renombar ventanas
Ctrl + b + w   ---- Listar ventanas

>> activar mouse

ctrl + b + :
: set -g mouse on


```