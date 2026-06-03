L3 = ["L3", "L3"]
L2 = [L3,"L2", "L2"]
L1 = [L2, "L1", "L1"]
for C1 in L1:
    if isinstance(C1, list):
        for C2 in C1:
            if isinstance(C2, list):
                for C3 in C2:
                    print (C3, end=" ")
            else:
                print(C2, end=" ")        
    else:
        print(C1, end=" ")