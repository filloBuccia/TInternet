import speedtest
import sys 
import getopt
from rich.console import Console
from rich import print
import time
import psutil 


HELP_TEXT = '''
Help section:

TInternet is a user-friendly tool designed by filloBuccia
It allows to check the download, upload and ping speed of your network 

How to use the command: python3 TInternet.py [Flag]

Flag:
-h  --help      Help section (where you're now)
-d              Download test
-u              Upload test
-p              Ping test
--all           Download, upload and ping test all together
--monitor       Monitor how much data are being received and sent on your network

Exit:
Press Ctrl-C
'''



def main(argv):
    try:
        opts, args = getopt.getopt(argv,"hdup",["all","help", "monitor"])


    except getopt.GetoptError:
        print(HELP_TEXT)
        sys.exit(2)
    
    for opt, arg in opts:
        
        if opt in ("-h", "--help"):
            print(HELP_TEXT)
            sys.exit()

        else:
            console = Console(highlight=False)
            
            if opt in ("--monitor"):

                last_received = psutil.net_io_counters().bytes_recv 
                last_sent = psutil.net_io_counters().bytes_sent 
                last_total = last_received + last_sent

                while True:
                    try:
                        bytes_received = psutil.net_io_counters().bytes_recv 
                        bytes_sent = psutil.net_io_counters().bytes_sent 
                        bytes_total = bytes_received + bytes_sent
                       

                        new_received = (bytes_received - last_received) /1024 /1024
                        new_sent = (bytes_sent - last_sent) /1024 /1024 
                        new_total = new_received + new_sent 

                        console.print(f"[bold red]{new_received:.2f}[/bold red] MB received, [bold blue]{new_sent:.2f}[/bold blue] MB sent, [yellow]{new_total:.2f}[/yellow] MB total")

                        last_received = bytes_received
                        last_sent = bytes_sent
                        last_total = bytes_total
                        time.sleep(1)

                    except KeyboardInterrupt:
                        print("\nBye Bye...")
                        sys.exit(2)
            else:

                test = speedtest.Speedtest()
                
                print("Loading server list...")
                test.get_servers()   #get list of servers avaible for speedtest

                print("Choosing the best server...")
                best = test.get_best_server()   #choose the best server
                console.print(f"Found: {best['host']} located in [bold yellow]{best['country']} [/bold yellow]")

                if opt in ("-d", "--all"):
                    
                    print("Performing download test...")
                    download_result = test.download()
                    console.print(f"Download speed: [bold cyan]{download_result/1024/1024:.2f}[/bold cyan] Mbit/s", style = "bold red")

                if opt in ("-u", "--all"):

                    print("Performing upload test...")
                    upload_result = test.upload()
                    console.print(f"Upload speed: [bold cyan]{upload_result/1024/1024:.2f}[/bold cyan] Mbit/s", style = "bold blue")
                
                if opt in ("-p", "--all"):

                    print("Performing ping test...")
                    ping_result = test.results.ping 
                    console.print(f"Ping speed: [bold cyan]{ping_result:.2f}[/bold cyan] ms", style = "bold orange1")

           

if __name__ == "__main__": 
    main(sys.argv[1:])












