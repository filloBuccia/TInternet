import speedtest
import sys 

try:

    script_name, flag = sys.argv

except ValueError:
    
    print("Flag required")
    script_name, flag = sys.argv, "-h" 

test = speedtest.Speedtest()


print("Loading server list...")
test.get_servers()   #get list of servers avaible for speedtest

print("Choosing the best server...")
best = test.get_best_server()   #choose the best server

print(f"Found: {best['host']} located in {best['country']}")


if flag == "-d":

    print("Performing download test...")
    download_result = test.download()
    print(f"Download speed: {download_result/1024/1024:.2f} Mbit/s")

elif flag == "-u":

    print("Performing upload test...")
    upload_result = test.upload()
    print(f"Upload speed: {upload_result/1024/1024:.2f} Mbit/s")

elif flag == "-p":

    print("Performing ping test...")
    ping_result = test.results.ping 
    print(f"Ping speed: {ping_result:.2f} ms")

elif flag == "-all":
    print("Performing download test...")
    download_result = test.download()

    print("Performing upload test...")
    upload_result = test.upload()

    print("Performing ping test...")
    ping_result = test.results.ping 

    print(f"Download speed: {download_result/1024/1024:.2f} Mbit/s")
    print(f"Upload speed: {upload_result/1024/1024:.2f} Mbit/s")
    print(f"Ping speed: {ping_result:.2f} ms")

elif flag == "-h":
    print('''
    Help section:

    TInternet is a user-friendly tool designed by BucciaFillo
    It allows to check download, upload and ping network speed 

    Flag:
    -h     Help section (where you are now)
    -d     Download test
    -u     Upload test
    -p     Ping test
    -all   Download, upload and ping test

''')
else:
    print("Flag nonexistent")
