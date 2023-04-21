# SSH KaliLinux
A free SSH KaliLinux server without limited time,You can use this for test any tool or using kali linux tools or other something like building custom roms.

# You should use vpn while using Hacking Tools like `reconftw` to avoid ban.
_________________________________________________
# Server specifications
- RAM : `128GB`
- CPU : `AMD Ryzen 7 3700X (16)`
- GPU : `NVIDIA GeForce GT 710`
- Space : `16GB`
_________________________________________________
# First:You should install `openssh`

- For Termux
```sh
pkg update && pkg install openssh
```
- For Linux
```sh
sudo apt update && sudo apt install openssh
```
- Then connect server with this command
```sh
ssh root@segfault.net
```
- Password for connect
```sh
segfault
```
<img src="img/server.png"></a>
______________________________
- Now you connected to server successfully.
- Type this command `bash` after login to use it instade of zsh
```sh
bash
```
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
- Then open any vnc viewer i'm using Remmina who is coming with ubuntu,And put this ip
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
