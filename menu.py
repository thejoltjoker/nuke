import nuke
from sandbox import johannes_tools

# Sequence Menu
seqMenu = nuke.menu('Nuke').addMenu('Johannes')
seqMenu.addCommand('Render and publish', 'johannes_tools.autoWritePublish()')
# seqMenu.addCommand('Set selected to linear', 'customTools.set_read_linear()')
# seqMenu.addCommand('Reload all read nodes', 'reloadAllRead()')
# seqMenu.addCommand('Set all read nodes to nearest frame', 'readNodeNearestFrame()')