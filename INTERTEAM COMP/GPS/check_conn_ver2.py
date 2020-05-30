
import subprocess 
import time 
  
def check_conn(address):
    while True: 
        res = subprocess.call(['ping', '-c', '1', address]) 
        if res == 0: 
            #print( "ping to", address, "OK")
            #return True
            print('\nconnected to network')
        elif res == 2: 
            #print("no response from", address)
            #return False
            print('\nnot connected to network')
        time.sleep(5)

'''
if(check_conn("192.168.43.127")):
    print('\nConnected\n')
else:
    print('\nFalse\n')
'''

hotspot = "192.168.43.127"
check_conn(hotspot)
