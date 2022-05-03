#!/bin/bash
# reference: https://answers.ros.org/question/99711/how-to-split-a-recorded-rosbag-file/

# arguments:
# $1 start
# $2 end
# $3 input_bagfile_name
# $4 output_bagfile_name

echo 'start time: '$1, 'end time: ', $2, 'input file name: ', $3, 'output file name: ', $4;
rosbag filter $3 $4 "t.secs >= $1 and t.secs <= $2";
