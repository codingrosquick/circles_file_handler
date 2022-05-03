'''
Installation of rosbag in python virtual environment

order to install the dependancies:
    rospkg              https://github.com/rospypi/simple/raw/any/rospkg/rospkg-1.1.10-py2.py3-none-any.whl    
    sensor_msgs         https://github.com/rospypi/simple/raw/any/sensor-msgs/sensor_msgs-1.12.7-py2.py3-none-any.whl
    genmsg              https://github.com/rospypi/simple/raw/any/genpy/genpy-0.6.12-py2.py3-none-any.whl 
    genpy               https://github.com/rospypi/simple/raw/any/genpy/genpy-0.6.12-py2.py3-none-any.whl 
    rosgraph            https://github.com/rospypi/simple/raw/any/rosgraph/rosgraph-1.14.3-py2.py3-none-any.whl   
    roslib              https://github.com/rospypi/simple/raw/any/roslib/roslib-1.14.6-py2.py3-none-any.whl 
    rospy               https://github.com/rospypi/simple/raw/any/rospy/rospy-1.14.3-py2.py3-none-any.whl  
    rosbag              https://github.com/rospypi/simple/raw/any/rosbag/rosbag-1.14.3-py2.py3-none-any.whl     
    catkin              https://github.com/rospypi/simple/raw/any/catkin/catkin-0.7.18-py2.py3-none-any.whl    
    std_msgs            https://github.com/rospypi/simple/raw/any/std-msgs/std_msgs-0.5.13-py2.py3-none-any.whl 
    rosgraph_msgs       https://github.com/rospypi/simple/raw/any/rosgraph-msgs/rosgraph_msgs-1.11.3-py2.py3-none-any.whl
    roscpp              https://github.com/rospypi/simple/raw/any/roscpp/roscpp-1.14.3-py2.py3-none-any.whl
    roslaunch           https://github.com/rospypi/simple/raw/any/roslaunch/roslaunch-1.15.7-py2.py3-none-any.whl
'''

# Download all the packages
wget https://github.com/rospypi/simple/raw/any/rospkg/rospkg-1.1.10-py2.py3-none-any.whl    
wget https://github.com/rospypi/simple/raw/any/sensor-msgs/sensor_msgs-1.12.7-py2.py3-none-any.whl
wget https://github.com/rospypi/simple/raw/any/genpy/genpy-0.6.12-py2.py3-none-any.whl 
wget https://github.com/rospypi/simple/raw/any/genpy/genpy-0.6.12-py2.py3-none-any.whl 
wget https://github.com/rospypi/simple/raw/any/rosgraph/rosgraph-1.14.3-py2.py3-none-any.whl   
wget https://github.com/rospypi/simple/raw/any/roslib/roslib-1.14.6-py2.py3-none-any.whl 
wget https://github.com/rospypi/simple/raw/any/rospy/rospy-1.14.3-py2.py3-none-any.whl  
wget https://github.com/rospypi/simple/raw/any/rosbag/rosbag-1.14.3-py2.py3-none-any.whl     
wget https://github.com/rospypi/simple/raw/any/catkin/catkin-0.7.18-py2.py3-none-any.whl    
wget https://github.com/rospypi/simple/raw/any/std-msgs/std_msgs-0.5.13-py2.py3-none-any.whl 
wget https://github.com/rospypi/simple/raw/any/roscpp/roscpp-1.14.3-py2.py3-none-any.whl
wget https://github.com/rospypi/simple/raw/any/rosgraph-msgs/rosgraph_msgs-1.11.3-py2.py3-none-any.whl
wget https://github.com/rospypi/simple/raw/any/roscpp/roscpp-1.14.3-py2.py3-none-any.whl
wget https://github.com/rospypi/simple/raw/any/roslaunch/roslaunch-1.15.7-py2.py3-none-any.whl

# Activate python environment
source venv/bin/activate

# Install them in order
python3 -m pip rospkg-1.1.10-py2.py3-none-any.whl    
python3 -m pip sensor_msgs-1.12.7-py2.py3-none-any.whl
python3 -m pip genpy-0.6.12-py2.py3-none-any.whl 
python3 -m pip genpy-0.6.12-py2.py3-none-any.whl 
python3 -m pip rosgraph-1.14.3-py2.py3-none-any.whl   
python3 -m pip roslib-1.14.6-py2.py3-none-any.whl 
python3 -m pip rospy-1.14.3-py2.py3-none-any.whl  
python3 -m pip rosbag-1.14.3-py2.py3-none-any.whl     
python3 -m pip catkin-0.7.18-py2.py3-none-any.whl    
python3 -m pip std_msgs-0.5.13-py2.py3-none-any.whl 
python3 -m pip rosgraph_msgs-1.11.3-py2.py3-none-any.whl
python3 -m pip roscpp-1.14.3-py2.py3-none-any.whl
python3 -m pip roslaunch-1.15.7-py2.py3-none-any.whl
