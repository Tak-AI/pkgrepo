#!/usr/bin/env python
import rospy
import std_msgs.msg

def callback(data):
    pub = rospy.Publisher('chatter', std_msgs.msg.Float64MultiArray, queue_size=10)
    rate = rospy.Rate(10) # 10hz
    array = list(range(3))
    array[0] = data.data[0]*0.01
    array[1] = data.data[1]*0.01
    array[2] = data.data[2]*0.01
def Sub_rs():
    rospy.init_node('Sub_rs', anonymous=True)
    rospy.Subscriber("point", std_msgs.msg.Float64MultiArray, callback)
    