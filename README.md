# SSH KaliLinux
A free SSH KaliLinux server without limited time,You can use this for test any tool or using kali linux tools or other something like building custom roms.
_________________________________________________
# Server specifications
- RAM : `128GB`
- CPU : `AMD Ryzen 7 3700X (16)`
- GPU : `NVIDIA GeForce GT 710`
- Space : `1TB`
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
## Contact US
- Linktree: https://linktr.ee/mrx7014
