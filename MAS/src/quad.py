#!/usr/bin/env python

# Ros libraries
import rospy

# Python libs
import sys, time

#ROS Messages
from geometry_msgs.msg import PoseStamped



class quad_control:
    def __init__(self):
        # Initialize Publisher
        self.pose_pub = rospy.Publisher("/quadcopter/command/pose",PoseStamped)
        time.sleep(5)


    def send_pos(self,x,y,z):
        pose_msg = PoseStamped()
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.header.frame_id = 'world'
        pose_msg.pose.position.x = x
        pose_msg.pose.position.y = y
        pose_msg.pose.position.z = z
        pose_msg.pose.orientation.x = 0
        pose_msg.pose.orientation.y = 0
        pose_msg.pose.orientation.z = 0
        pose_msg.pose.orientation.w = 1
        self.pose_pub.publish(pose_msg)
        

    # def callback(self,ros_data):
    #     pass




def main(args):


    
    
    rospy.init_node('quad_control', anonymous=True)

    '''Initializes and cleanup ros node'''
    qc = quad_control()

    # Start of Sweep
    qc.send_pos(2,-2,7)
    time.sleep(3)

    # x = 0

    # while x < 10:
    #     qc.send_pos(x,-4,7)
    #     x += .5
    #     time.sleep(3)
    
    # try:
    #     rospy.spin()
    # except KeyboardInterrupt:
    #     print "Shutting down ROS Node"

    

if __name__ == '__main__':
    main(sys.argv)

