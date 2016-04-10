from svmutil import *
import sys
import sklearn.preprocessing

FILE_TO_PROCESS_1 = sys.argv[1]
FILE_TO_PROCESS_2 = sys.argv[2]
FILE_TO_PROCESS_3 = sys.argv[3]
#FILE_LIBSVM_FORMAT = sys.argv[4]
FILE_LIBSVM_FORMAT = "combined_crossfold_libsvm_format"
attr_array = []
out_array = []

def createAttrArray():
    global lines
    global attr_array
    global out_array
    lineNumber = 0
    for line in lines:
        lineNumber = lineNumber + 1
        if lineNumber == 1:
            continue
        a = line.rstrip('\n').rstrip('\r').split(",")
        y = 0
        if a[len(a)-1] == "present":
            y = 1
        elif a[len(a)-1] == "absent":
            y = 0
        else:
            continue
        out_array.append(int(y))

        i = 1
        attributes = []
        for x in range(len(a)-1):
            attributes.append(float(a[i-1]))
            i = i + 1

        attr_array.append(attributes)

outFp = open(FILE_LIBSVM_FORMAT,"w")

with open(FILE_TO_PROCESS_1) as f:
    lines = f.readlines()
createAttrArray()
f.close()

with open(FILE_TO_PROCESS_2) as f:
    lines = f.readlines()
createAttrArray()
f.close()

with open(FILE_TO_PROCESS_3) as f:
    lines = f.readlines()
createAttrArray()
f.close()

normalized_attr_array = sklearn.preprocessing.normalize(attr_array, norm = 'l2')

for j in range(len(attr_array)):
    outLine = str(out_array[j])
    for i in range(5):
        outLine =  outLine + " " + str(i+1) + ":" + '{0:.10f}'.format(normalized_attr_array[j][i])
        i = i + 1
    outFp.write(outLine)
    outFp.write("\n")
    j = j + 1

outFp.close()

y, x = svm_read_problem(FILE_LIBSVM_FORMAT)

m = svm_train(y, x, '-t 0 -c 40 -h 0 -b 1 -v 10')

print "m = \n", m

