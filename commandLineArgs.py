# program to take command line arguments(word count)
import sys
print("\n\n\t Script Name:",sys.argv[0])
print("\n")
le=len(sys.argv)
for i in range(le):
    print("\t\tWord : ",i," :",sys.argv[i])
print("\n\n\tWord Count:",len(sys.argv)-1)