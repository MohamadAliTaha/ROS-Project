#!/usr/bin/env python

import rospy
from std_msgs.msg import String


def send():
    rospy.init_node("sender", anonymous=True)
    pub = rospy.Publisher("data_line", String, queue_size=5)

    while not rospy.is_shutdown():
        text = raw_input("Enter your message: ")
        pub.publish(text)


if __name__ == '__main__':
    try:
        send()
    except rospy.ROSInterruptException:
        pass
