#!/usr/bin/env python
import rospy
from minicurso_ros.msg import MyMessage

def callback(data):
	print('Received ID: {}'.format(data.id))
	print('Received Vector: {}'.format(data.my_vector))
    
def listener():
    rospy.init_node('subscriber', anonymous=True)

    rospy.Subscriber('my_topic', MyMessage, callback)

    # spin() simply keeps python from exiting until this node is stopped
    rospy.spin()

if __name__ == '__main__':
    listener()
