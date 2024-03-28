# Challenges

- Obedient Cat
    - Run `wget [https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag](https://mercury.picoctf.net/static/33996e32dce022205a6a36f69aba56f0/flag)` to get the file
    - The Flag is in the file
- Mod 26
    - decipher with rot-13
- Python Wrangling
    - download the file with wget and also download the flag and the password
    - Run `❯ python3 [ende.py](http://ende.py/) -d ./flag.txt.en`
- Wave a flag
    - use the webshell for this (tip)
    - `chmod +x warm` to make a executable
    - run `./warm -h`
- Information
    - Used aperi-solve for this and found the license unusual
    - License: `cGljb0NURnt0aGVfbTN0YWRhdGFfMXNfbW9kaWZpZWR9`
    - decrypted the license with base64
- Nice netcat...
    - netcat into the server
    - ascii to text to get the flag
- What Lies Within
    - I put it into aperi’solve and looked in zSteg and I found the flag.
    
    Flag: `picoCTF{h1d1ng_1n_th3_b1t5}`
    
- Matryoshka doll
    - Binwalked the initial image and kept doing them like 4 more times until i got flag.txt
    
    Flag: `picoCTF{ac0072c423ee13bfc0b166af72e25b61}`
    
- Lookey here
    - Downloaded the file and searched for `pico`
    
    Flag: `picoCTF{gr3p_15_@w3s0m3_4c479940}`
    
- hideme
    
    Downloaded the image and binwalked it with aperisolve and got the flag
    
    flag: `picoCTF{Hiddinng_An_imag3_within_@n_ima9e_cda72af0}`
    
- So Meta
    - put it through aperisolve and found the flag in zSteg metadata
    
    Flag: `picoCTF{s0_m3ta_fec06741}`
    
- extensions
    - ran `file flag.txt` and learned it was a .png and changed its file extension to get the flag.
- Insp3ct0r
    - Found the first part of the flag on the HTML after inspecting, found the second part in Style Editor `mycss.css` and found the 3rd part in Debugger `myjs.js`
    
    Flag: `picoCTF{tru3_d3t3ct1ve_0r_ju5t_lucky?832b0699}`
    
- login
    - Looked in page sources and found `index.js` look towards the end and found this suspicious at the end (seen in *fig. 1)*  I put it in cyberchef and I got the flag
    - *fig. 1*
        
        ![Screenshot 2023-12-11 at 11.17.05 AM.png](Challenges%205141a6cc16614dd0a1cf6be1315f89b6/Screenshot_2023-12-11_at_11.17.05_AM.png)
        
    
    Flag: `picoCTF{53rv3r_53rv3r_53rv3r_53rv3r_53rv3r}`
    
- Inspect HTML
    - legit just inspect it to find the flag 🤣
    
    Flag: `picoCTF{1n5p3t0r_0f_h7ml_fd5d57bd}`
    
- Includes
    - Look at page source, found the first part of the flag in `style.css` and the second part in `script.js`
    
    Flag: `picoCTF{1nclu51v17y_1of2_f7w_2of2_df589022}`
    
- Local Authority
    - looked in secure.js and found the username and password in there
    
    Flag: `picoCTF{j5_15_7r4n5p4r3n7_a8788e61}`
    
- Safe opener
    - opened the java file, found something encrypted and used cyberchef to decode
    
    flag: `picoCTF{pl3as3_l3t_m3_1nt0_th3_saf3}`
    
- Wireshark doo dooo do doo...
    - put a display filter for http and searched for line/html, then found some text put it into rot-13 decoder and got the flag.
    
    Flag: `picoCTF{p33kab00_1_s33_u_deadbeef}`
    
- Glitchcat
    
    flag: `picoCTF{gl17ch_m3_n07_a4392d2e}`
    
    ![Screenshot 2023-12-12 at 10.02.45 AM.png](Challenges%205141a6cc16614dd0a1cf6be1315f89b6/Screenshot_2023-12-12_at_10.02.45_AM.png)
    
- runme.py
    - legit opened the file and got the flag.
    
    Flag: `picoCTF{run_s4n1ty_run}`
    
- Serpentine
    - asked gpt to fix it and i pasted it into vscode and got the flag
    
    Flag: `picoCTF{7h3_r04d_l355_7r4v3l3d_aa2340b2}`
    
- Big zip
    - cd into the folder and ran `grep “pico” -i - r` and found the flag
    
    Flag: `picoCTF{gr3p_15_m4g1c_ef8790dc}`
    
- money-ware
    - copied the address and searched in google and learn it was the petya attack and got the flag.
    
    flag: `picoCTF{petya}`
    
- repetitions
    - opened cyberchef and pasted it into base 64 and pasted the output back into the input over and over until i found the flag.
    
    Flag: `picoCTF{base64_n3st3d_dic0d!n8_d0wnl04d3d_492767d2}`
    
- ASCII Numbers
    - put it into cyberchef and decoded it from hex to get the flag
    
    Flag: `picoCTF{45c11_n0_qu35710n5_1ll_t311_y3_n0_l135_445d4180}`
    
- Based
    - decode everything fast enough
    
    Flag: `picoCTF{learning_about_converting_values_00a975ff}`
    
- The Numbers
    - it’s letter to number, decode it
    
    Flag: `PICOCTF{THENUMBERSMASON}`
    
- 13
    
    decode from rot 13
    
    Flag: `picoCTF{not_too_bad_of_a_problem}`
    
- Vignere
    
    Flag: `picoCTF{D0NT_US3_V1G3N3R3_C1PH3R_ae82272q}`
    
    ![Screenshot 2023-12-13 at 11.28.41 AM.png](Challenges%205141a6cc16614dd0a1cf6be1315f89b6/Screenshot_2023-12-13_at_11.28.41_AM.png)
    
- HideToSee
    - Used Aperi’solve to extract encrypted.txt and I decode the encrypted text with the cipher in *fig 1.*
    - *Fig 1.*
        
        ![Screenshot 2023-12-13 at 12.43.23 PM.png](Challenges%205141a6cc16614dd0a1cf6be1315f89b6/Screenshot_2023-12-13_at_12.43.23_PM.png)
        
    
    Flag: `picoCTF{atbash_crack_7142fde9}`
    
- rotation
    - used [dcode.fr](http://dcode.fr) rot decoder and got the flag
    
    Flag: `picoCTF{r0tat1on_d3crypt3d_555957f3}`
    
- fixme1.py
    - needed to fix a indentation error
    
    Flag: `picoCTF{1nd3nt1ty_cr1515_6a476c8f}`
    
- fixme2.py
    - the operator was = instead of ==
    
    Flag: `picoCTF{3qu4l1ty_n0t_4551gnm3nt_f6a5aefc}`
    
- where are the robots
    - go to robots.txt and u can find a place where u arent supposed to go and if u go there u get the flag
    
    Flag: `picoCTF{ca1cu1at1ng_Mach1n3s_477ce}`
    
- crackme-py
    - Chatgpt prompt: How do I crack this code (with pasted code)
    
    Flag: `picoCTF{1|\/|_4_p34|\|ut_8c551048}`
    
- speeds and feeds
    
    nc’ed into it and used a gcode simulator to get the flag
    
    Flag: picoCTF{num3r1cal_c0ntr0l_84d2d117}