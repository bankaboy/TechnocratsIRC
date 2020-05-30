default_host = "localhost"
 
def ping(host=default_host, verbose=False):
 
    """
    True if host responds to a ping request
    """
    import os, sys, subprocess, platform
    
 
    # some standard reliable targets
	# Level 3 anycast (default)
    if host == "Level3": host = "4.2.2.1"     
    elif host == "localhost": host = "127.0.0.1" # internal 
    elif host == "Google": host = "8.8.4.4" # googles DNS
    else: pass
  
    ping_str = "-c 1" # just one ping
    need_sh = True    # for Linux
 
    # platform specifics  "Windows" "Linux" "Darwin" #
    platfrm =  platform.system() 
    if platfrm == "Windows":
        ping_str = "-n 1"
        need_sh = False
 
 
    # build a command
    cmd = "ping " + " " + ping_str + " " + host
 
    result = ""
 
    # do not show ping output
    if not verbose:
        # output suppressed to bit bucket
        devnul =open(os.devnull, 'w') 
        result = subprocess.call(cmd, stdout=devnul, shell=need_sh)
    else:
        # show ping results
        result = subprocess.call(cmd,  shell=need_sh)
 
 
    # call returns 0 on success
    if  result == 0: return True
    return False
    
# check basic network subsystem
# loc = ping("localhost")
# if loc: 
#    print( "networking is working")
# else:
#    print( "networking is broken")
 
if __name__ == "main":
 
	if len(sys.argv) > 1:
		up = ping(sys.argv[1])
	else:
	   up = ping()	
 
	if up:print( "Internet is up and reachable")
	else:print( "Internet is NOT reachable")
