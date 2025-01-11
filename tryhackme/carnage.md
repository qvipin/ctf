# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# Carnage | KOTH Experience

KOTH with GodderE2D

Released: 2024-04-14


## Foreword

I competed against [GodderE2D](https://www.godder.xyz) for this KOTH. This is my second KOTH ever, if you want to read about my first KOTH (Space Jam), click [here](https://www.vipinb.xyzblog/spacejam). Anyways hope you enjoy this writeup!

## NMAP Scan

```bash
┌──(vipin㉿vipin)-[~]
└─$ sudo nmap -sV -sS 10.10.115.109
[sudo] password for vipin: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-04-14 00:52 EDT
Nmap scan report for 10.10.115.109
Host is up (0.093s latency).
Not shown: 994 closed tcp ports (reset)
PORT     STATE SERVICE VERSION
22/tcp   open  ssh     OpenSSH 6.7p1 Debian 5+deb8u8 (protocol 2.0)
80/tcp   open  http    Apache httpd 2.4.10 ((Debian))
81/tcp   open  http    Apache httpd 2.4.10 ((Debian))
82/tcp   open  http    Apache httpd 2.4.10 ((Debian))
83/tcp   open  http    Apache httpd 2.4.10 ((Debian))
9999/tcp open  abyss?
```

## Dirsearch

```bash
┌──(vipin㉿vipin)-[~]
└─$ dirsearch -u 10.10.115.109 --exclude-status 403,404
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3
 (_||| _) (/_(_|| (_| )

Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/vipin/reports/_10.10.115.109/_24-04-14_00-52-50.txt

Target: http://10.10.115.109/

[00:52:50] Starting: 
[00:53:09] 301 -  315B  - /assets  ->  http://10.10.115.109/assets/         
[00:53:09] 200 -  470B  - /assets/                                          
[00:53:12] 200 -  209B  - /changelog.txt                                    
[00:53:19] 200 -   38B  - /flag.txt                                         
[00:53:19] 301 -  314B  - /forms  ->  http://10.10.115.109/forms/           
[00:53:33] 200 -  151B  - /Readme.txt                                       
[00:53:40] 301 -  315B  - /upload  ->  http://10.10.115.109/upload/         
[00:53:41] 200 -  402B  - /upload/                                          
[00:53:41] 200 -    1B  - /upload.php                                       
                                                                             
Task Completed
```

## First Flag

- I got the first flag from */flag.txt* 

![Image showing flag](blog/carnage/firstflag.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

## Getting User

- In port 82 there is an upload form, we are going to intercept that with Burpsuite.

- I didn't take a screenshot so I cannot show it, but you need to use a reverse shell php script (like from pentestmonkey) and rename it to *.gif*. Then turn on intercept on Burp and upload it on the upload form on port. Then modify the *.gif* to a *.gif.php* in Burpsuite Proxy tool after it was intercepted and **forward** it. 

- Make sure you have a listener setup before you run the php script (```nc -lnvp 6969```)

![Image showing /images](blog/carnage/slashimages.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2</small>
</div>

- Now click on the *.gif.php* and you have user‼️

## Flags & Final Thoughts

- I found a flag in */home/duke*

![Image showing flag3](blog/carnage/flag3.png 'Fig.3')
<div style={{ textAlign: 'center' }}>
  <small>Fig.3</small>
</div>

- Finding SUID Binaries was difficult as the *find* command was disabled.

- I didn't get root and Godder did manage to find a second flag on port 82 in */flag.txt*. And that was worth a lot more than the user flag. Godder ended up winning, so congrats to him! I think if I wasn't stuck on getting root I would have won, other than that thats it! 

### MACHINE NOT PWN'ED 😔

