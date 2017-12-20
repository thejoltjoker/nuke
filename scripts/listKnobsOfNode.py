import nuke

myNode = nuke.selectedNode().knobs()

for i in myNode:
    print i
