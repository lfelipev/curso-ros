#!/usr/bin/env python
import rospy
from minicurso_ros.msg import Num

def publishing():

    # 
    pub = rospy.Publisher('my_topic', Num, queue_size=10)
    rospy.init_node('my_node', anonymous=True)
    rate = rospy.Rate(10) # 10hz

    my_message = MyMessage()

    _id = 0
    while not rospy.is_shutdown():
        my_message.id = _id + 1
        my_message.my_vector = [12.0, 2, _id+1]

        rospy.loginfo(my_message)
        pub.publish(my_message)
        rate.sleep()

if __name__ == '__main__':
    try:
        publishing()
    except rospy.ROSInterruptException:
        pass

