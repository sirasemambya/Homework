infile = open('scores.txt','r')

for line in infile:
    print(line,end='')
infile.close()

def totalPassingScores(fileName,threshold):
    for line in fileName:
        if threshold>60:
            int(line=+1)
            print(line)
print(totalPassingScores('scores.txt','80'))
