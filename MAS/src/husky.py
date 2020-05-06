#!/usr/bin/env python

# Ros libraries
import rospy

# Python libs
import sys, time

#ROS Messages
from geometry_msgs.msg import PoseStamped



class husky_control:
    def __init__(self):
        # Initialize Publisher
        self.pose_pub1 = rospy.Publisher("/h1/move_base_simple/goal",PoseStamped)
        self.pose_pub2 = rospy.Publisher("/h2/move_base_simple/goal",PoseStamped)
        time.sleep(5)


    def send_pos(self,id,x,y,z):
        pose_msg = PoseStamped()
        pose_msg.header.stamp = rospy.Time.now()
        pose_msg.header.frame_id = 'map'
        pose_msg.pose.position.x = x
        pose_msg.pose.position.y = y
        pose_msg.pose.position.z = z
        pose_msg.pose.orientation.x = 0
        pose_msg.pose.orientation.y = 0
        pose_msg.pose.orientation.z = 0
        pose_msg.pose.orientation.w = 1

        if id == 1:
            self.pose_pub1.publish(pose_msg)
        elif id ==2:
            self.pose_pub2.publish(pose_msg)
        else:
            print("please enter valid pose")
        

    # def callback(self,ros_data):
    #     pass



# husky_field_1 = [[2,5.0,2.6],
#                  [1,5.0,0.0],
#                  [2,9.9,1.3],
#                  [1,5.0,2.6],
#                  [2,9.9,4.7],
#                  [1,5.0,4.7],
#                  [2,9.9,7.0],
#                  [1,5.0,7.0],]


husky_field_1 = [[2,5.0,2.6],
                 [1,5.0,0.0],
                 [2,9.9,2.6],
                 [1,4.5,2.6],
                 [2,9.9,4.7],
                 [1,5.0,4.7],
                 [2,9.9,7.0], 
                 [1,5.0,7.0],]


husky_field_2 = [[2,4.7,5.5],
                 [1,.17,5.7],
                 [2,4.7,9.4],
                 [1,-3.8,5.7],
                 [2,.19,9.4],
                 [2,-3.5,9.4]]

def main(args):

    rospy.init_node('husky_control', anonymous=True)

    '''Initializes and cleanup ros node'''
    hc= husky_control()


    for waypoints in husky_field_1:
        id = waypoints[0]
        x = waypoints[1]
        y = waypoints[2]

        hc.send_pos(id,x,y,0)
        
        time.sleep(10)



    # Start of Sweep
    # qc.send_pos(2,-2,7)
    # time.sleep(3)

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

