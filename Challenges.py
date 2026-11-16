import sys
if len(sys.argv)==3:
    username = (sys.argv[1])
    password = (sys.argv[2])
    if password=="Password123" and username=="Zunaira Fatima": 
        print("Acess granted. Welcome Admin.")
    else:
        print("Error: Wrong Details.")
else:
    print("Missing Details.")