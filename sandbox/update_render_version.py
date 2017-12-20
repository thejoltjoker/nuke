#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
update_render_version.py
Description of script_name.py.
"""
import os
# import nuke


def main():
    """docstring for main"""
    render = '//seq-live/live_projects/StarWarsHammer/sequences/SWR_01/SWR_020/Light/work/maya/images/SWR_01_SWR_020_Light_v077/SWR_01_SWR_020_Light_v077_env/SWR_01_SWR_020_Light_v077_env.%04d.exr'
    render_folder, render_file = os.path.split(render)
    renders_path = os.path.abspath(os.path.join(
        os.path.dirname(render), '..', '..'))

    # latest_subdir = max(all_subdirs, key=os.path.getmtime)
    # print latest_subdir

    # for root, dirs, files in os.walk(render_folder):


if __name__ == '__main__':
    main()


# for filename in os.listdir(cache_folder_path):
#         if not filename.endswith('.png'):
#             cached_files.append(os.path.join(cache_folder_path, filename))
