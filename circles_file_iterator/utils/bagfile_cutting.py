from argparse import ArgumentError
import os
import subprocess
from ..global_variables.global_variables import local_temp_folder


def get_start_and_end(bagfile_path: str):
    '''
    Gets the start time and end times of a bagfile.

    :param bagfile_path: Absolute or Relative path to the bagfile to evaluate.
    :return: start time, end time (both in seconds)
    '''
    path = os.path.abspath(bagfile_path)
    get_times_script = os.path.abspath('./circles_file_iterator/utils/get_times.sh')

    print('curr', os.getcwd())
    command = f'/bin/bash {get_times_script} {path}'
    print(f'\ncommand is: {command}\n')

    res = subprocess.run(['/bin/bash', get_times_script, path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    print(res.stdout)
    start, end = res.stdout.strip(b'\n').split(b' ')
    print(start, end)
    start, end = float(str(start, encoding='utf-8')), float(str(end, encoding='utf-8'))
    print(start, end, type(start))
    return start, end


def cut_bagfile(beginning_offset_seconds: int, duration_seconds: int, bagfile_path: str, beginning_type: str = 'offset', start: int = None, end: int = None):
    '''
    Cuts a bagfile depending on the provided parameters.

    :param beginning_offset_seconds: Beginning of the cut. Can be set as an offset or as absolute time. (in seconds)
    :param duration_seconds: Duration of the cut to keep. (in seconds)
    :param bagfile_path: Path to the bagfile to cut
    :param beginning_type: Handles how the start cut time is computed.
        set to 'offset': Start cut = start of the bagfile + beginning_offset_seconds
        set to 'absolute': Start cut = beginning_offset_seconds
    :param start: (Optional) Provide this if you already called the get_start_and_end function earlier, or you know the start and end parameters of the bagile to cut.
    :param end: (Optional) Same as for start.

    :return: The local path to the cutted bagfile
    '''
    try:
        print('curr out', os.getcwd())
        in_path = os.path.abspath(bagfile_path)
        filename = 'cutted_' + os.path.basename(in_path)
        out_path = os.path.join(local_temp_folder, filename)
        
        if start is None or end is None:
            start, end = get_start_and_end(in_path)

        if beginning_type == 'offset':
            cut_start = start + beginning_offset_seconds
        elif beginning_type == 'absolute':
            if beginning_offset_seconds < start:
                beginning_offset_seconds = start
                print(ArgumentError(f'Tried to cut a bagfile before its beginning.\
                    Please specify a beginning after the start of the recording.\
                    The start of the cut has hence been set to the start time of the bagfile.'))
            cut_start = beginning_offset_seconds

        cut_end = cut_start + duration_seconds
        if cut_end > end:
            cut_end = end

        cut_bag_script = os.path.abspath('./circles_file_iterator/utils/cut_bag.sh')
        
        subprocess.run(['/bin/bash', cut_bag_script, str(cut_start), str(cut_end), in_path, out_path], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        
        return out_path

    except Exception as e:
        raise Exception(f'Cutting bagfiles failed on {e}')



