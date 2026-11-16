import sys
if len(sys.argv)==3:
    ip_address =(sys.argv[1])
    port =(sys.argv[2])
    print("Scanning IP", ip_address, "on Port", port)
else:
    print("Error: Missing characters.")
