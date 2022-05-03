#!/bin/bash
# reference: https://answers.ros.org/question/99711/how-to-split-a-recorded-rosbag-file/
# arguments:
# $1 = bagfile path

t0=`rosbag info -y -k start $1`;
t1=`rosbag info -y -k end $1`;

echo $t0 $t1;
