# Forensics Base

- L2C3 Trojan Horse
    - All startup apps run in `SOFTWARE\Microsoft\Windows\CurrentVersion\Run` and I found a malicious process
    
    Flag: 1238HgulsjtuwGF
    
- L2C5 Moving Mix-Up
    - Ran `volatility -f suspect-memdump.zip imageinfo` and entered the suggested profiles
    
    Flag: Win81U1x64
    
- L3C5 Volatile Memory
    - Install Volatility
    - Find the memory profile using the imageinfo plugin
    [`vol.py](http://vol.py/) -f memdump.mem imageinfo`
    Run the pslist plugin to list all processes
    [`vol.py](http://vol.py/) -f memdump.mem --profile=Win81U1x64 pslist`
    Skim through the output to find the process name that looks unusual
    - Syntax: [vol.py](http://vol.py/) -f <memoryfile> --profile=<profilename> <plugin>
    
    Flag: 19hglski!hg
    
- L4C2 Hidden Hyena
    - find a http packet that has a “=” sign
    - After finding this `ZmxhZyBpcyBoZ2prczJKRnUhaGY=` convert to Base64
    - and you will get this “flag is hgjks2JFu!hf”.
    
    Flag: hgjks2JFu!hf
    
- L4C5 Masai Mystery
    
    ![kcFLTs7.png](Forensics%20Base%20c3ce88ee7d684e4aaa3b669e46aab15a/kcFLTs7.png)
    
- L5C1 Start Line Setback
    - Lets start by opening the image with Notepad++, if we look at the bottom there is text that says `passwordforsteghideisgivemetheflag` We now know that we need to use steghide and the password is `givemetheflag` .
    - In the Kali VM, we can run `steghide —info runner.jpg` and also try to get info about embedded data as we now have the password.
    - Inside the image it seems that there is a .txt file embedded and in there is the flag.
    
    Flag: QQPhgns98&"!
    
- L5C2 New Racer
    - Found this hash and used [hashes.com](http://hashes.com) to decrypt `sshd_server:1003:aad3b435b51404eeaad3b435b51404ee:8d0a16cfc061c3359db455d00ec27035:`
    
    Flag: D@rj33l1ng
    
- L5C3 Running Report
    - Answers to the questions
        
        Which type of reconnaissance scan is the traffic indicative of? Vertical, Horizontal, Aggressive or Passive?
        Vertical
        
        What are the six open ports?
        135, 139, 445, 5357, 6666, 7443
        
        What operating system is installed on victim VM?
        Windows
        
    
    Flag: Varies
    
- L5C5 Uphill Section
    - Fix the pcap file by running `pcapfix -v Taipei\ malicious\ capture.pcapng` to un-corrupt.
    - The flag is in HTTP packet no. 4307 at the end.
    
    Flag: Scor3dAwin0nPCAPfor3ns!cs
    
- L6C1 Argentine Ambush
    - I used Aperi’solve and it told me some common passwords, I put the first one as the password in steghide and I got the flag.txt but I entered it and it didn’t work but I noticed the `=` sign and I put it in a base64 decoder and I got the flag
    
    Flag: w1n_4_st3g0
    
- L6C2 Missing Image
    - Used [Hexed.it](http://Hexed.it) to add the jpg header(FF D8 FF) and saved the fixed image and on the top there is some text and I entered it and it was the flag.
    
    Flag: H3ad3r$_4_W1nn3r$
    
- L6C3 Brazilian Blather
    - Convert `pcapng` file to pcap, use Network Miner to extract all files from `pcap` file. Extract flag-gen03 and run file inside. Input 1997 to get the flag.
    
    Flag: C4Tch_M3_1F_Y0u_c4N
    
- L6C4 Island Image
    - Use Autopsy to export the files, the last file looked off because it had 11 characters so I decrypted it with Caeser Cipher
    
    Flag: PREFETCHWIN
    
- L6C5 Urgent Escalation
    - This challenge is hella difficult
    - Look through the entire log and find something at the end that looks off, which was this `U2gzbGxfU2gwY2tlZF9ieV9TMW1wbDFjMXR5IQo=`
    - Decoded it with Base64 and got the flag
    
    Flag: Sh3ll_Sh0cked_by_S1mpl1c1ty!
    
- L7C1 Icy Admin
    - Used Volatility
    - Commands used to solve
        
        `sudo ./volatility_2.6_lin64_standalone imageinfo -f memdump.mem`
        
        `sudo ./volatility_2.6_lin64_standalone --profile=Win81U1x64 -f memdump.mem hivelist`
        
        `sudo ./volatility_2.6_lin64_standalone --profile=Win81U1x64 -f memdump.mem hashdump -y 0xffffc00006e2c000 -s 0xffffc0000bedb000 >hashes.txt`
        
    
    Flag: fc525c9683e8fe067095ba2ddc971889
    
- L7C3 Footprints in the snow
    - I used a tool [https://blog.didierstevens.com/programs/pdf-tools/](https://blog.didierstevens.com/programs/pdf-tools/)  ran `chmod +x [pdf-parser.py](http://pdf-parser.py/)` and `./pdf-parser.py emptyPDF.pdf` and I noticed Decimal and put it into cyberchef to get thef flag.
    
    Flag: h1d1ng_am0ng_t3h_f0nt5
    
- L7C4 Chilly Command
    - Opened file with Notepad++ and searched "command" given the tip is to find the command. I found an encoded command `JwBUAGgAMwBfAEIAMwBzAFQAXwBGAGwANABnAHMAXwBSAF8ARgAwAHIAMwBuADUAMQBjACcA`and I decoded with cyberchef and that was the flag.
    
    Flag: Th3_B3sT_Fl4gs_R_F0r3n51c
    
- L8C2 Ancient Attachment
    - Opened the email with [https://goldfynch.com/pst-viewer/](https://goldfynch.com/pst-viewer/) and found a zip in deleted items which was password protected and I found a base64 string in notes and put that as the zip password and inside was the flag.
    
    Flag: Ema1l_f0r3ns1cs
    
- L8C3 Final Bid
    - I decoded the bottom base64 text into plain text and asked Bard to extract any readable text from that and I got this and I put the details in to get the flag.
    - Results from Bard
        
        ![Screenshot 2023-12-31 at 9.50.18 PM.png](Forensics%20Base%20c3ce88ee7d684e4aaa3b669e46aab15a/Screenshot_2023-12-31_at_9.50.18_PM.png)
        
    - Answers
        
        ![Screenshot 2023-12-31 at 9.51.05 PM.png](Forensics%20Base%20c3ce88ee7d684e4aaa3b669e46aab15a/Screenshot_2023-12-31_at_9.51.05_PM.png)
        
    
    Flag: Varies