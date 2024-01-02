import socket

def print_wolf_banner():
    wolf_banner = '''
      / \\__
     (    @\\___
     /         O
    /   (_____/ 
   /_____/   U
    '''
    print(wolf_banner)
    print("coded by Greenw00lf\n")

def portScanner(ip_address, port):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    result = sock.connect_ex((ip_address, port))
    if result == 0:
        print(f'PORT {port} is open :)')
    else:
        print(f'PORT {port} is closed : ')
    sock.close()

if __name__ == "__main__":
    print_wolf_banner()
    ip_address = input("Enter the IP: ")
    port = int(input("Enter Port: "))
    portScanner(ip_address, port)
