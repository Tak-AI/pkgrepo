#!/usr/bin/env python
import rospy
from std_msgs.msg import String
def keyq():
    pub = rospy.Publisher('keyhold', String, queue_size=10)
    rospy.init_node('keyq', anonymous=True)
    rate = rospy.Rate(30) # 10hz
    a = "s"
    pub.publish(a)
    while not rospy.is_shutdown():
        print("If you input 'q', 'tr_sr' is stoped")
        a = raw_input()
        pub.publish(a)
        rate.sleep()

if __name__ == '__main__':
    try:
        keyq()
    except rospy.ROSInterruptException:
        pass