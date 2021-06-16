#!/usr/bin/env python

import rospy
from std_msgs.msg import Float64MultiArray, String

def talker3():
    pub = rospy.Publisher('chatter', Float64MultiArray, queue_size=10)
    msg = rospy.Publisher('UPorSIDE', String, queue_size=10)
    rospy.init_node('talker3', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    array = list(range(4))
    while not rospy.is_shutdown():
        print("Enter the object's position and the object's width.")
        a = map(float, raw_input().split())
        array[0] = a[0]
        array[1] = a[1]
        array[2] = a[2]
        array[3] = a[3]
        array_forPublish = Float64MultiArray(data=array)
        pub.publish(array_forPublish)
        print("Which the object's direction is up or side?\nAnswer by typing up or side.")
        str = raw_input()
        msg.publish(str) 
        rate.sleep()

if __name__ == '__main__':
    try:
        talker3()
    except rospy.ROSInterruptException:
        pass
