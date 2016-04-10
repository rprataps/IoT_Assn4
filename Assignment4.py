from svmutil import *
import sys

FILE_TO_PROCESS_1 = sys.argv[1]
#FILE_TO_PROCESS_2 = sys.argv[2]
FILE_LIBSVM_FORMAT = sys.argv[2]
SECOND_FILE = sys.argv[3]

lines = []

def createLibSVMFile(outFp):
    global lines
    lineNumber = 0
    for line in lines:
        lineNumber = lineNumber + 1
        if lineNumber == 1:
            continue
        a = line.rstrip('\n').rstrip('\r').split(",")
        occupancy = 0
        if a[len(a)-1] == "present":
            occupancy = 1
        elif a[len(a)-1] == "absent":
            occupancy = 0
        else:
            continue
        outLine = str(occupancy)
        i = 1
        for x in range(len(a)-1):
            outLine = outLine + " " + str(i) + ":" + a[i-1]  
            i = i + 1
        outFp.write(outLine)
        outFp.write("\n")
    
outFp = open(FILE_LIBSVM_FORMAT,"w")

with open(FILE_TO_PROCESS_1) as f:
    lines = f.readlines()
f.close()

createLibSVMFile(outFp);

"""
with open(FILE_TO_PROCESS_1) as f:
    lines = f.readlines()
f.close()

createLibSVMFile(outFp);
"""
f.close()

#outFp.write("Occupancy Temperature Humidity Light CO2 HumidityRatio")
#outFp.write("\n")
#print lines[0].rstrip('\n').rstrip('\r').split(",")


with open(SECOND_FILE) as f:
    lines = f.readlines()
f.close()

outFp2 = open("temp2", "w")
createLibSVMFile(outFp2)

y, x = svm_read_problem(FILE_LIBSVM_FORMAT)
#m = svm_train(y, x, '-t 0 -c 4 -b 1')
m = svm_train(y, x, '-s 4 -c 4')

p,q = svm_read_problem("temp2")

p_label, p_acc, p_val = svm_predict(p, q, m)

print p_acc[0]
