#!/usr/bin/python

# Project 3 Tests for CS 6250: Computer Networks
#

files = [
    'SimpleTopo',
    'SingleLoopTopo',
    'SimpleNegativeCycle',
    'ComplexTopo'
]

for testFile in files:
    answer = {}
    with open("{}.answer".format(testFile)) as inputfile:
        for line in inputfile:
            tempLine = line.rstrip()
            tempSplit = tempLine.split(':')
            tempSplitSplit = tempSplit[1].split(',')
            answer[tempSplit[0]] = { 'raw': tempSplit[1], 'split': tempSplitSplit, 'length': len(tempSplitSplit) }
    topo = {}
    with open("{}.log".format(testFile)) as inputfile:
        for line in inputfile:
            tempLine = line.rstrip()
            tempSplit = tempLine.split(':')
            if len(tempSplit) > 1:
                tempSplitSplit = tempSplit[1].split(',')
                topo[tempSplit[0]] = {'raw': tempSplit[1], 'split': tempSplitSplit, 'length': len(tempSplitSplit)}

    if len(topo.keys()) != len(answer.keys()):
        raise SystemExit("{} has the incorrect number of nodes".format(testFile))

    for key, value in answer.iteritems():
        if key not in topo:
            raise SystemExit("{0} is missing the node {1}".format(testFile, key))
        if int(topo[key]['length']) != int(value['length']):
            raise SystemExit("{0}'s {1} node is the wrong length".format(testFile, key))
        i = 0
        for link in value['split']:
            if link not in topo[key]['split']:
                raise SystemExit("{0}'s {1} node is missing link {2}".format(testFile, key, link))
            else:
                i = i + 1
        if i != int(value['length']):
            raise SystemExit("{0}'s {1} node didn't have all the links".format(testFile, key))

    print "{} looks good!".format(testFile)