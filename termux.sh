#!/bin/bash


# Coded By MRX7014


base64 -d <<<"IF9fX19fIF9fX19fX19fX19fX19fICBfX19fICAgX19fICAgX18KfF8gICBffCAgX19ffCBfX18g
XCAgXC8gIHwgfCB8IFwgXCAvIC8KICB8IHwgfCB8X18gfCB8Xy8gLyAuICAuIHwgfCB8IHxcIFYg
LyAKICB8IHwgfCAgX198fCAgICAvfCB8XC98IHwgfCB8IHwvICAgXCAKICB8IHwgfCB8X19ffCB8
XCBcfCB8ICB8IHwgfF98IC8gL15cIFwKICBcXy8gXF9fX18vXF98IFxfXF98ICB8Xy9cX19fL1wv
ICAgXC8KICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAKICAgICAgICAgICAg
ICAgICAgICAgICAgICAgICAgICAgICAgICAKIF9fX19fIF9fX19fIF9fX19fIF8gICBfX19fX19f
ICAgICAgICAKLyAgX19ffCAgX19ffF8gICBffCB8IHwgfCBfX18gXCAgICAgICAKXCBgLS0ufCB8
X18gICB8IHwgfCB8IHwgfCB8Xy8gLyAgICAgICAKIGAtLS4gXCAgX198ICB8IHwgfCB8IHwgfCAg
X18vICAgICAgICAKL1xfXy8gLyB8X19fICB8IHwgfCB8X3wgfCB8ICAgICAgICAgICAKXF9fX18v
XF9fX18vICBcXy8gIFxfX18vXF98ICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAg
ICAgICAgICAgICAgICAKICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICAgICA="

sleep 2
echo -e "\033[1;36m
		  
1] Setup and FiX Errors

2] Run as GUI

3] My linktree

====== MRX7014 =====
              
"
echo -e "\033[33m"
                
read -p "Choose : " mrx

                 
if [ $mrx == 1 ]
              
then
    echo ""

    echo -e "\033[1;31 WWelcome At Linux Setup\n"

    sleep 2


    echo -e "\033[34mThis Script Made By mrx7014\n"


    sleep 2


    echo -e "\033[1;33mNow, I recommend you follow me on facebook\n"


    echo -e " \033[31m                  [*] Wait ...                  "


    echo ""

    sleep 5


    xdg-open https://www.facebook.com/kemo.beah.73

    sleep 2


    echo ""


    sleep 1



    echo -e "\033[1;31m Now Enter 'segfault'\n "


    pkg update && pkg install openssh && ssh root@segfault.net



elif [ $mrx == 2 ]
 		
then
    echo ""
    echo -e  "\033[1;31m after setup type 'startxvnc'"

elif [ $mrx == 3 ]

then

    echo""

    xdg-open https://linktr.ee/mrx7014

	      
fi
