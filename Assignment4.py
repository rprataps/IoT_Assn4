from svmutil import *
import sys

FILE_TO_PROCESS_1 = sys.argv[1]
TEST_FILE = sys.argv[2]

#FILE_TO_PROCESS_2 = sys.argv[2]
TRAINFILE_LIBSVM_FORMAT = "LIBSVM_FORMAT_TRAIN"
TESTFILE_LIBSVM_FORMAT = "LIBSVM_FORMAT_TEST"

lines = []

# Method to create the LIB SVM format file from the given dataset
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
   
 

with open(FILE_TO_PROCESS_1) as f:
    lines = f.readlines()
f.close()

outFp = open(TRAINFILE_LIBSVM_FORMAT,"w")
createLibSVMFile(outFp);

with open(TEST_FILE) as f:
    lines = f.readlines()
f.close()

outFp2 = open(TESTFILE_LIBSVM_FORMAT, "w")
createLibSVMFile(outFp2)

y, x = svm_read_problem(TRAINFILE_LIBSVM_FORMAT)
m = svm_train(y, x, '-t 0 -c 4 -b 1')
#m = svm_train(y, x, '-s 0 -c 4')

p,q = svm_read_problem(TESTFILE_LIBSVM_FORMAT)

p_label, p_acc, p_val = svm_predict(p, q, m)

print p_acc[0]
