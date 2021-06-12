import os
import time
try:
    # required packages
    import colorama
except:
    print("Notice: your required packages are not installed . this can cause errors")
    print('type "install-zshell" to install')

if os.name == "nt":
    symbol =""
else:
    # for super user
    if os.getuid() == 0:
        try:
            from colorama import Fore , Back , Style
            symbol = Fore.GREEN + "[" + Fore.RED + "#" +Fore.GREEN + "]" + Fore.LIGHTWHITE_EX
        except:
            symbol = "[#]"

    else:
        # for normal user
        try:
            from colorama import Fore,Back,Style

            symbol=Fore.GREEN + "[" + Fore.BLUE + "$" + Fore.GREEN + "]" + Fore.LIGHTWHITE_EX
        except:
            symbol = "[$]"
if os.name == "nt":
    pass
else:
    if os.getuid() == 0:
        pass
    else:
        print("Notice: run this script as sudo to avoid errors")

def wrong_option():
    try:
        from colorama import Fore,Back,Style
        print(Fore.RED + "wrong option [X]" + Fore.LIGHTWHITE_EX)
    except:
        print("wrong option [X]")


def clr():
    if os.name == "nt":
        os.system("cls")
    else:
        os.system("clear")

if os.name == "nt":
    #function(windows)
    terminal = "powershell or cmd"
else:
    #function(linux or other)
    terminal = "terminal"


if __name__ == "__main__":
    program = " "
    while program != "1":

        # shell interference
        if os.name == "nt":
            try:
               from colorama import Fore,Back,Style
               prompt=input(symbol + Fore.LIGHTBLUE_EX + "zshell" + Fore.RED + ">" + Fore.LIGHTWHITE_EX)

            except:
                prompt=input(f"{symbol}zshell>")
        else:


            try:
                from colorama import Fore,Back,Style

                prompt=input(symbol + Fore.BLUE + "zshell" + Fore.RED + ">" + Fore.LIGHTWHITE_EX)

            except:
                prompt=input(f"{symbol}zshell>")

        if "help" in prompt:
            #the help massage
            print("help:-                   ")
            print("connection          the command connection tells your state is online or offline     ")
            print("net                 the command which tells about your network                       ")
            print("set                 set a target to attack or scan                                   ")
            print("ping                pings a server                                                   ")
            print(f"new                 starts new window of {terminal}                                 ")
            print("clr                 to clear the screen                                              ")
            print("about               gives all information about Zshell                               ")
            print("sysinfo             gives information about your system                              ")
            print("install-zshell      installs or updates requirements for your system                 ")
            print("exec                execute a system command                                         ")
            print("exit                end this program                                                 ")

        elif "connection" in prompt:
            import urllib.request

            def connect(host='http://google.com'):
                print("testing connection...")
                time.sleep(0.03)
                try:
                    urllib.request.urlopen(host)
                    return True
                except:
                    return False

            print("pinging 'www.google.com'")
            if connect():
                print("successfully connect() to server (www.google.com)")
                print("status : connected")
            else:
                print("server un-connectable")
                print("status : non connected")

        elif "net" in prompt:
            if os.name == "nt":
                os.system("ipconfig")
            else:
                os.system("ifconfig")

        elif 'ping' in prompt:
            try:
                from colorama import Fore , Style , Back
                server = input(symbol + Fore.LIGHTBLUE_EX + "zshell" + Fore.RED + ">"+ Fore.LIGHTGREEN_EX +"ping>""server>" + Fore.LIGHTWHITE_EX)
            except:
                server=input("zshell>ping>server>")

            if 'help' in server:
                print("pings a server,enter server name")
                print("example:")
                print("zshell>ping>server>www.google.com  #to ping google.com")
                print("zshell>ping")
            elif 'cancle' in server:
                pass
            else:
                os.system(f"ping {server}")

        elif 'clr' in prompt:
            clr()

        elif 'exit' in prompt:
            exit()

        elif 'about' in prompt:
            print("what is dis? and what the heck do i do? and who made this :-                                                                 ")
            print("Zshell is a open-source shell kanda thing which is used for hacking(lol, it's a piece of shi-) and it is under devlopment    ")
            print("it is very case sensitive and do all basic kind of stuff . it is developed by Debanjan Das ,and i am only 14yo lol           ")
            print("it comes with automated commands or even scrips in just-in-one-command .it is made with python so is kinda easy to understand")
            print("[*] you are totally secure ,we use proxychains to hide your ip address")
            print("don't forget to meet vector ;)                                                                                               ")
        elif 'vector' in prompt:
            print("(-_-)       # ah sh!t theywe go again")
            print("meet vector at https://github/mincha9999/vector")

        elif 'sysinfo' in prompt:
            if os.name == "nt":
                print("                                                 ")
                print("______________________       os:windows(nt)     ")
                print("|          |         |                             ")
                print("|          |         |                            ")
                print("|----------|---------|                           ")
                print("|          |         |                             ")
                print("|__________|_________|                            ")
                print("                                                     ")
            else:
                os.system("neofetch")
        elif "install-zshell" in prompt:
            print("starting installation...")
            time.sleep(0.15)
            print("detecting os...")
            time.sleep(0.20)

            # connection check function
            import urllib.request
            def connect(host='http://google.com'):
                try:
                    urllib.request.urlopen(host)
                    return True
                except:
                    return False

            if os.name == "nt":
                # windows installation
                print("windows detected")
                if connect():
                    choice=input("are you sure that you want to download? [Y/n]>")
                    if "y" in choice:
                        os.system("pip install colorama")
                        print("everything seems good...")
                    else:
                        print("Abroad")
                else:
                    try:
                        from colorama import Style , Back , Fore
                        print(Fore.RED + "ERROR : unable to connect : no internet [X]" + Fore.LIGHTWHITE_EX)
                    except:
                        print("ERROR: unable to connect : no internet [X]")


            else:
                # linux installation
                print("linux detected")

                # noinspection PyBroadExceptio
                if connect():
                    choice = input("are you sure that you want to download? [Y/n]>")
                    if "y" or "ye" or "yes" in choice:
                        print("downloading necessary packages")

                        # required packages

                        os.system("sudo apt install neofetch python3-pip net-tools qterminal termit gnome-terminal curl git proxychains ")
                        os.system("pip3 install colorama")
                        print("everything seems good...")

                    else:
                        print("Abort")

                else:
                    try:
                        from colorama import Style , Back , Fore
                        print(Fore.RED + "ERROR : unable to connect : no internet [X]" + Fore.LIGHTWHITE_EX)
                    except:
                        print("ERROR: unable to connect : no internet [X]")

        elif "exec" in prompt:
            program3=" "
            while program3 != "off":
                try:
                    from colorama import Style , Back , Fore
                    command = input(symbol + Fore.LIGHTBLUE_EX + "zshell" + Fore.RED + ">" + Fore.LIGHTGREEN_EX + "command>" + Fore.LIGHTWHITE_EX)
                except:
                    command = input("zshell>command>")
                if "back" in command:
                    program3 = "off"
                elif "exit" in command:
                    exit()
                elif 'help' in command:
                    print('type "back" to exit this command without exiting zshell or type "exit" to exit zshell')
                else:
                    print(f"*executing :{command}")
                    print("")
                    os.system(f"{command}")
                    print("")
        elif "new" in prompt:
            if os.name == "nt":
                # for windows
                print("which one to open:")
                print("[1]cmd      [2]powershell")
                try:
                    from colorama import Fore , Back , Style
                    choice = input(Fore.LIGHTBLUE_EX + "zshell" + Fore.RED + ">"+ Fore.LIGHTGREEN_EX +"choice>"+ Fore.LIGHTWHITE_EX)
                except:
                    choice = input("zshell>choice>")
                if "1" in choice:
                    os.system("start cmd.exe")
                elif '2' in choice:
                    os.system("start powershell.exe")
                elif str() in choice:
                    wrong_option()
                else:
                    wrong_option()

            else:
                # for linux
                print("which one to open:")
                print("[1]qterminal   [2]gnome-terminal   [3]termit")
                try:
                    from colorama import Fore , Back , Style
                    choice = input(Fore.LIGHTBLUE_EX + "zshell" + Fore.RED + ">"+ Fore.LIGHTGREEN_EX +"choice>"+ Fore.LIGHTWHITE_EX)
                except:
                    choice = input("zshell>choice>")
                if "1" in choice:
                    os.system("qterminal")

                elif '2' in choice:
                    os.system("gnome-terminal")
                elif '3' in choice:
                    os.system("termit")
                elif str() in choice:
                    wrong_option()
                else:
                    wrong_option()

        elif "set" in prompt:
            # set command
            # prompt
            # loop

            try:
                from colorama import Fore , Back ,Style
                target = input(
                    Fore.LIGHTBLUE_EX + "zshell" +Fore.LIGHTWHITE_EX + "("+Fore.RED + "target" + Fore.LIGHTWHITE_EX +")"+ Fore.RED + ">" +
                    Fore.LIGHTWHITE_EX
                )
            except:
                target = input("zshell(target)>")
            if 'help' in target:
                print("set a target on an ip address or to perform tasks")
                print("type 'cancle' to back and 'exit' to exit")
                print("enter an ip address or web address")
            elif 'cancel' in target:
                pass
                program = "off"
            elif 'exit' in target:
                exit()
            else:
               try:
                   from colorama import Fore, Back , Style
                   task = input(
                       Fore.LIGHTBLUE_EX + "zshell" + Fore.LIGHTWHITE_EX + "(" + Fore.RED + f"target={target}"
                       + Fore.LIGHTWHITE_EX + ")" + Fore.RED + ">" + Fore.LIGHTWHITE_EX
                   )
               except:
                   task = input(f"{symbol}zshell(target={target})>")
               if "geo-locate" in task:
                   if os.name == "nt":
                       print("sorry this is not available for windows    , yet")
                   else:
                       try:
                           from colorama import Fore,Back,Style
                           web1="www.freegeoip.app"
                           print("")
                           print(
                               Fore.YELLOW + "[" + Fore.RED + "*" + Fore.YELLOW + "]" + Fore.LIGHTWHITE_EX + f"sending request to {web1}"
                           )
                           os.system(f"proxychains curl https://freegeoip.app/xml/{target}")
                       except:
                           web1="www.freegeoip.app"
                           print("")
                           print(
                               f"[*] sending request to {web1}"
                           )
                           os.system(f"proxychains curl https://freegeoip.app/xml/{target}")
               elif 'help' in task:
                   print("geo-locate          scan the location of ip address")

        else:
            print("command :",prompt,"not found")
