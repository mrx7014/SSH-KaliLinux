# SSH KaliLinux
A free SSH KaliLinux server without limited time,You can use this for test any tool or using kali linux tools or other something like building custom roms.

You should use vpn while using Hacking Tools like `reconftw,...etc` to avoid ban.
_________________________________________________
# Server specifications
- RAM : `128GB`
- CPU : `AMD Ryzen 7 3700X (16)`
- GPU : `NVIDIA GeForce GT 710`
- Hard Size : `16GB` -->> If you want to increase this, text skyper in telegram and ask him to increase your server space, you can find the telegram group link at the bottom of the repo.
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
3: Now,server will ask you password to connect type `segfault` then press enter.
4: Now server connected successfully. 

- ios

You can use Termuis app to connect to server and use vnc viewer too connect to gui `Both are available on the App store`,and you don't need to install any packages,just connect to server from termius app with this command `ssh root@segfault.net`

_______________________

- Password for connect
```sh
segfault
```
<img src="img/server.png"></a>
______________________________
- Now you connected to server successfully.
______________________________
# You should copy this ssh line from ssh -O to segfault.net
- Like This `ssh -o "SetEnv SECRET=PlPtAROaKlMNmnlsMwSbyb" \root@teso.segfault.net`
- <img src="img/ssh.jpg"></a>
___________________________________________________________________________________
- You must keep this ssh with you, in order to connect to the server using it again. Do not connect using the ssh root@segfault.net command. You must connect using the ssh that you copied in order to save the work that you have done on the server.
___________________________________________________________________________________
# Now if you want to connect to server with vnc server follow steps:
- Type this command in terminal
```sh 
startxvnc
```
- Then it will give you an SSH command again like this
<img src="img/sshvnc.jpg"></a>
- Take this ssh and open it at a new terminal and type passwd
```sh
segfault
```
- Then open any vnc viewer i'm using Remmina who is coming with Linux.

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
___________________________________________________________________________________
# Thanks to 
- `Skyper` for this free server
- join his telegram group https://t.me/thcorg
- Website: https://www.thc.org
