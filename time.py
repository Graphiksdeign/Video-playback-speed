dur=str(input("Enter the duration in HH:MM:SS format: "))
ps=float(input("Enter playback speed(e.g., 1.2): "))
lis=dur.split(":")
lis = [float(i) for i in lis]
#print(lis[2])
lis[0]*=3600
lis[1]*=60
tot=0.0
for i in range(0, len(lis)): 
    tot = tot+lis[i] 
taken=round(tot/ps)
rem=tot-taken
#print(taken, rem,"\n")

def convert(seconds): #converts seconds to hours minutes and seconds
    min, sec = divmod(seconds, 60) 
    hour, min = divmod(min, 60) 
    return "%d:%02d:%02d" % (hour, min, sec)

print("\nTime you spent: {}".format(convert(taken)))
print("Time you saved: {}".format(convert(rem)))
