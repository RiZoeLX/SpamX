<h1> Termux hosting guide </h1>

----

<h3>Commands</h3>

<b>1) pkg update & upgrade</b>

```python
pkg upgrade && pkg update
```

<b>2) Install python3, git, screen </b>

```python
pkg install python3 && pkg install git && pkg install screen 
```

<b>3) clone repo and open dictionary </b>

```python
git clone https://github.com/RiZoeLX/SpamX && cd SpamX
```

<b>4) Install requirements </b>

```python
python3 -m pip install --upgrade pip && pip3 install -r requirements.txt
```

<b>5) Run screen </b>

```python
screen -S SpamX
```

<b>6) Run sh.py to fill values and start SpamX </b>

```python
python3 sh.py
```
