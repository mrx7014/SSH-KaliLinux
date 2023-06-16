# SSH KaliLinux
A free SSH KaliLinux server without limited time. You can use this for test any tool or using kali linux tools or other something like building custom roms.

All network traffic goes via VPN and is anonymized (e.g. for `reconftw,...etc`). Masscan is allowed using your [own exit node](https://thc.org/segfault/wireguard).
_________________________________________________
# Server specifications
- RAM : `128GB`
- CPU : `AMD Ryzen 7 3700X (16)`
- GPU : `NVIDIA GeForce GT 710`
- Hard Size : `16GB` ==> If you want to increase this, contact a [SysCop](https://t.me/thcorg) on their Telegram Channel.
_________________________________________________
# First: Install Packages
_________________________________________________
- You should use this scripts to install packages to connect to server if you using termux or linux.
______________________

- i made a script for `Linux` and `termux` to install packages and connect to server with very easy way.

- Termux <a href="https://github.com/termux/termux-app/releases">Download it from here</a> For Android.
```sh
curl https://raw.githubusercontent.com/mrx7014/SSH-KaliLinux/main/termux.sh >> termux.sh
bash termux.sh
```

- Linux

```sh
curl https://raw.githubusercontent.com/mrx7014/SSH-KaliLinux/main/linux.sh >> linux.sh
bash linux.sh
```

- Windows

1: Download <a href="https://www.chiark.greenend.org.uk/~sgtatham/putty/latest.html">Putty</a> and choose pkg `32-bit x86`.

2: Open it and type `ssh root@segfault.net` in Hostname Or Ip address bar.

3: The server will ask you password to connect. Type `segfault` and press enter.

4: Now server connected successfully. 

5: Read the [Segfault PuTTY Guide](https://www.thc.org/segfault/faq/putty/).

____________________________________

- ios

You can use Termuis app to connect to server and use vnc viewer too connect to gui `Both are available on the App store`

And you don't need to install any packages,just connect to server from termius app with this command `ssh root@segfault.net`.

Download Termius from <a href="https://apps.apple.com/us/app/termius-terminal-ssh-client/id549039908">Here</a>

Download VNC Viewer from <a href="https://apps.apple.com/us/app/vnc-viewer-remote-desktop/id352019548">Here</a>

_______________________

- Password for connect
```sh
segfault
```
<img src="img/server.png"></a>
______________________________
- You have now successfully connected to your server. Write down the SECRET shown on the screen. You need this SECRET to connect back to YOUR server.
______________________________
# You should copy this ssh line from ssh -o to segfault.net
- Like This `ssh -o "SetEnv SECRET=PlPtAROaKlMNmnlsMwSbyb" root@teso.segfault.net`
- <img src="img/ssh.jpg"></a>
___________________________________________________________________________________
- You must use this string `ssh -o SetEnv SECRET=...` to connect back to _your_ server. Your data/work is associated with this `SECRET`. You can only access your data if you use the SECRET from the `ssh -o` line. Do not use `ssh root@segfault.net` again.
___________________________________________________________________________________
# Now if you want to connect to server with vnc server follow steps:
- Add `-L5900:0:5900` to your ssh line and connect to your server like this: `ssh -L5900:0:5900 -o 'SetEnv SECRET=...' root@...`.

- Type this command in terminal
```sh 
startxvnc
```
- Then it will look like this:  
<img src="img/sshvnc.jpg"></a>
- Then open any vnc viewer. I'm using Remmina who is coming with Linux.

- You can download VNC Viewer for android from <a href="https://play.google.com/store/apps/details?id=com.realvnc.viewer.android&hl=en_US&pli=1">Here</a>

- For Windows From <a href="https://www.realvnc.com/en/connect/download/viewer/windows/">Here</a>

- For Linux Remmina installed already.

_________________________________________

- Then Type this ip in VNC Viewer

```sh
127.0.0.1:5900
```
<img src="img/sshdisplay.png"></a>
- Now you are successfully connected to the server with VNC server,Enjoy it.
___________________________________________________________________________________
# Contact US
- Linktree: https://linktr.ee/mrx7014
- Join our telegram channel: https://t.me/goosetech7014
___________________________________________________________________________________
# Thanks to 
- [THC](https://www.thc.org) for this free server
- join his telegram group https://t.me/thcorg
- Website: https://www.thc.org
