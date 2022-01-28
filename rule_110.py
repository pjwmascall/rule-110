inputs = [0,0,0,0,0,1,0,0,0,0,0]

def rules(segment):
    if segment == [1,1,1]:
        output = 0;
    if segment == [1,1,0]:
        output = 1;
    if segment == [1,0,1]:
        output = 1;
    if segment == [1,0,0]:
        output = 0;
    if segment == [0,1,1]:
        output = 1;
    if segment == [0,1,0]:
        output = 1;
    if segment == [0,0,1]:
        output = 1;
    if segment == [0,0,0]:
        output = 0;
    return output;

newlist = inputs

for permutation in range(100):
    templist = [newlist[-1]] + newlist + [newlist[0]]
    newlist = []
    outputlist = []
    for i in range(1, len(templist)-1):
        segment = [templist[i-1]] + [templist[i]] + [templist[i+1]]
        newlist.append(rules(segment));
    for i in newlist:
        if i == 1:
            output = '*'
            outputlist.append(output)
        if i == 0:
            output = " "
            outputlist.append(output)
    print(''.join(outputlist))