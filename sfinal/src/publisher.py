#!/usr/bin/env python3
import rospy
from std_msgs.msg import Float64
import math

def talker():
    pubr = rospy.Publisher('/sfinal/back_right_wheel_controller/command', Float64, queue_size=10)
    publ = rospy.Publisher('/sfinal/back_left_wheel_controller/command', Float64, queue_size=10)
    pub_sl = rospy.Publisher('/sfinal/left_steering_controller/command', Float64, queue_size=10)
    pub_sr = rospy.Publisher('/sfinal/right_steering_controller/command', Float64, queue_size=10)

    rospy.init_node('talker', anonymous=True)
    rate = rospy.Rate(10) # 10hz
    while not rospy.is_shutdown():
        hello_str = "hello world %s" % rospy.get_time()
        vel = -8
        steer = 0
        rospy.loginfo(vel)
        publ.publish(-vel)
        pubr.publish(vel)
        pub_sl.publish(steer)
        pub_sr.publish(-steer)
        rate.sleep()

if __name__ == '__main__':
    try:
        talker()
    except rospy.ROSInterruptException:
        pass