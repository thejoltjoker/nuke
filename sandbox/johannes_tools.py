import sys
import nuke

def auto_write_dailies_video():
    # Create the Write node that will become an AutoWrite
    w = nuke.createNode('Write', inpanel=False)
    # Rename it to AutoWrite
    # (Also, deal with the number problem)
    count = 1
    while nuke.exists('Write_Publish' + str(count)):
        count += 1
    w.knob('name').setValue('Write_Publish' + str(count))

    # Set write node settings
    # png settings
    # w.knob('colorspace').setValue('rec709')
    # w.knob('file_type').setValue('png')
    # w.knob('datatype').setValue('16 bit')

    # w.knob('colorspace').setValue('AlexaV3LogC')
    w.knob('file_type').setValue('mov')
    w.knob('meta_codec').setValue('AVdn')
    w.knob('meta_encoder').setValue('mov64')
    w.knob('mov64_dnxhd_codec_profile').setValue('DNxHD 422 10-bit 220Mbit')

    w.knob('create_directories').setValue(1)

    # Add the tab to hold the variables containing path fragments so we can have a less messy file path.
    t = nuke.Tab_Knob("Path Fragments")
    w.addKnob(t)
    if(sys.platform == 'win32'):
        w.addKnob(nuke.EvalString_Knob('proj_root', 'Project Root', '[join [lrange [split [value root.name] / ] 0 1 ] / ]'))
    elif(sys.platform == 'darwin'):
        w.addKnob(nuke.EvalString_Knob('proj_root', 'Project Root', '[join [lrange [split [value root.name] / ] 0 3 ] / ]'))
    w.addKnob(nuke.EvalString_Knob('seq', 'Sequence', '[lrange [split [value root.name] / ] 3 3 ]'))
    w.addKnob(nuke.EvalString_Knob('shot', 'Shot Name', '[lrange [split [value root.name] / ] 4 4 ]'))
    w.addKnob(nuke.EvalString_Knob('task', 'Shot Task', '[lrange [split [value root.name] / ] 5 5 ]'))
    w.addKnob(nuke.EvalString_Knob('script', 'Script Name', '[file rootname [file tail [value root.name] ] ]'))

    # Display the values of our path fragment knobs on the node in the DAG for error-checking.
    feedback = """
    Output Path: [value file]

    Project Root: [value proj_root]
    Sequence: [value seq]
    Shot Name: [value shot]
    Shot Task: [value task]
    Script Name: [value script]
    """
    w.knob('label').setValue(feedback)

    # Re-assemble the path fragments into a proper output path
    output_path = "[value proj_root]/comp/[value script]/[value script].mov"
    w.knob('file').fromScript(output_path)

def auto_write_dailies_image():
    # Create the Write node that will become an AutoWrite
    w = nuke.createNode('Write', inpanel=False)
    # Rename it to AutoWrite
    # (Also, deal with the number problem)
    count = 1
    while nuke.exists('Write_Publish' + str(count)):
        count += 1
    w.knob('name').setValue('Write_Publish' + str(count))

    # Set write node settings
    # png settings
    # w.knob('colorspace').setValue('rec709')
    # w.knob('file_type').setValue('png')
    # w.knob('datatype').setValue('16 bit')

    # w.knob('colorspace').setValue('AlexaV3LogC')
    w.knob('file_type').setValue('png')

    w.knob('create_directories').setValue(1)

    # Add the tab to hold the variables containing path fragments so we can have a less messy file path.
    t = nuke.Tab_Knob("Path Fragments")
    w.addKnob(t)
    if(sys.platform == 'win32'):
        w.addKnob(nuke.EvalString_Knob('proj_root', 'Project Root', '[join [lrange [split [value root.name] / ] 1 1 ] / ]'))
    w.addKnob(nuke.EvalString_Knob('seq', 'Sequence', '[lrange [split [value root.name] / ] 3 3 ]'))
    w.addKnob(nuke.EvalString_Knob('shot', 'Shot Name', '[lrange [split [value root.name] / ] 4 4 ]'))
    w.addKnob(nuke.EvalString_Knob('task', 'Shot Task', '[lrange [split [value root.name] / ] 5 5 ]'))
    w.addKnob(nuke.EvalString_Knob('script', 'Script Name', '[file rootname [file tail [value root.name] ] ]'))

    # Display the values of our path fragment knobs on the node in the DAG for error-checking.
    feedback = """
    Output Path: [value file]

    Project Root: [value proj_root]
    Sequence: [value seq]
    Shot Name: [value shot]
    Shot Task: [value task]
    Script Name: [value script]
    """
    w.knob('label').setValue(feedback)

    # Re-assemble the path fragments into a proper output path
    output_path = "D:/people/johannes/projects/[value proj_root]/comp/[value script]/[value script].png"
    w.knob('file').fromScript(output_path)

auto_write_dailies_image()