# How to build the circuit

# Running on a Raspberry PI

## Connect to the Raspberry PI
```
ssh pi@192.168.1.46
```

## git clone
1. Install git: https://linuxize.com/post/how-to-install-git-on-raspberry-pi/
2. Install github CLI: https://github.com/frobscottle/r2d2.git
3. Change to home directory: `cd ~`
4. Create a projects directsory: `mkdir projects`
5. Change directory to projects: `cd projects`
6. Clone: `git clone https://github.com/frobscottle/r2d2.git`

## install libraries
``` bash
$ sudo apt-get update
$ sudo apt-get install python3-pygame
```

## setup
```
$ amixer set PCM unmute
$ amixer set PCM 100%
```

## run
```
ssh pi@192.168.1.46

cd projects
cd r2d2
git pull
python3 main.py
```