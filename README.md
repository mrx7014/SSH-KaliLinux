# SSH KaliLinux
A free SSH Kali Linux server without limited time. You can use this for test any tool or using kali linux tools or other somethings like building custom roms or any another thing.
____________

- **If you want to use Ubuntu in this server check this repo https://github.com/mrx7014/Ubuntu_on_Segfault**

- All network traffic goes via VPN and is anonymized (e.g. for `reconftw,...etc`).

- Masscan is allowed using your <a href="https://thc.org/segfault/wireguard">own exit node</a>.
____________

# Server specifications

- RAM : `2GB`
- Kernel: `5.15.0-73-generic`
- Shell: `zsh 5.9`
- CPU : `AMD Ryzen 9 7950X3D (32) @ 4.200GHz`
- GPU : `AMD ATI 0e:00.0 Raphael`
- Hard Size : `16GB`

**If you want to increase this, contact a <a href="https://t.me/thcorg">SysCop</a> on their Telegram Channel.**
____________

# First: Install Packages

- You should install this packages to connect to server if you are using termux or linux.

# Termux

```sh
pkg update && pkg upgrade && pkg install openssh
```
<small>Download Termux from <a href="https://github.com/termux/termux-app/releases">here</a></small>
  
# Linux

```sh
sudo apt update && sudo apt install openssh-client
```
____

# Windows

- You can connect to the server from CMD,if it not working use this guide here.

1: Download <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html">Putty</a> and choose pkg `32-bit x86`.

2: Open it and type `ssh root@segfault.net` in Hostname Or Ip address bar.

3: The server will ask you password to connect. Type `segfault` and press enter.

4: Now server connected successfully. 

5: Read the <a href="https://www.thc.org/segfault/faq/putty/">Segfault PuTTY Guide.</a>

- You can use https://shell.segfault.net to connect to the server from browser too if you have any errors with this guides.
_______

# ios

- You can use **ISH** 'it's like termux' to connect to server, And RVNC Viewer to use GUI.

<b>Both of them are available on the App store</b>

- Download ISH From <a href="https://apps.apple.com/us/app/ish-shell/id1436902243">Here</a>

- Download RVNC from <a href="https://apps.apple.com/us/app/vnc-viewer-remote-desktop/id352019548">Here</a>

**You don't need to install any packages on ISH,just connect to the server with this command:**
```sh
ssh root@segfault.net
```
____

- Password for connect
```sh
segfault
```
<img src="img/server.png"></a>
____________

>You have now successfully connected to your server. Write down the SECRET shown on the screen. You need this SECRET to connect back to YOUR server.
>
____________

# You should copy this ssh line from ssh -o to segfault.net
- Like This `ssh -o "SetEnv SECRET=PlPtAROaKlMNmnlsMwSbyb" root@8lgm.segfault.net`

<img src="img/ssh.jpg"></a>

- You must use this string `ssh -o SetEnv SECRET=...` to connect back to _your_ server. Your data/work is associated with this `SECRET`. You can only access your data if you use the SECRET from the `ssh -o` line. Do not use `ssh root@segfault.net` again.

# Now if you want to connect to server with vnc server follow steps:

- Add `-L5900:0:5900` to your ssh line and connect to your server like this: `ssh -L5900:0:5900 -o 'SetEnv SECRET=...' root@...`.

- Type this command in terminal

```sh 
startxvnc
```
- Then it will look like this:  
<img src="img/sshvnc.jpg"></a>

- Now open another terminal and enter the ssh that gives to you after enter `startxvnc`, enter password `segfault`.

<small>ssh should be like this `ssh -L5900:0:5900 -o 'SetEnv SECRET=...' root@...`</small>

- Then open any vnc viewer.

- You can download VNC Viewer for
Android from <a href="https://play.google.com/store/apps/details?id=com.realvnc.viewer.android&hl=en_US&pli=1">Here</a>

- For Windows From <a href="https://www.realvnc.com/en/connect/download/viewer/windows/">Here</a>

- For Linux **Remmina** is installed already on ubuntu, if it not installed check this website <a href="https://remmina.org/how-to-install-remmina/">Here</a>

- You can use RVNC Viewer on Linux too, See <a href="https://www.realvnc.com/en/connect/download/viewer/linux/">This</a>
____________

- Enter this ip in your VNC Viewer

```sh
127.0.0.1:5900
```
<img src="img/sshdisplay.png"></a>
- Now you are successfully connected to the server with VNC server,Enjoy it.
____________

# Contact US
- Linktree: https://linktr.ee/mrx7014
- Donate: https://bmc.link/mrx7014

____________

# Thanks To:
- <a href="https://www.thc.org/">THC</a> for this free server
- join telegram group: https://t.me/thcorg
- Website: https://www.thc.org
