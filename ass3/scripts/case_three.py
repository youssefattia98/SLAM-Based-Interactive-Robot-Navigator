#! /usr/bin/env python

import rospy
import numpy
from geometry_msgs.msg import Twist, Vector3
from sensor_msgs.msg import LaserScan

#obstacle avoidnce threashold
threashold = 0.5

#initialize a Twist object for the publisher
init = Vector3(0, 0, 0)
repost = Twist( init, init)

def callingback_map(data):
    global repost
    repost = data  

def callingback_scans(data):
    global repost
    pub = rospy.Publisher('cmd_vel',Twist, queue_size=10) #initlaizing the the publisher 
    #compute the minimun obsable distance to the right, left and in front of the robot
    sub_right = data.ranges[0:240]
    sub_mid = data.ranges[240:480]
    sub_left = data.ranges[480:721]
    R = min(sub_right)
    F = min(sub_mid)
    L = min(sub_left)

    if R < threashold :
        if repost.angular.z < 0 :
            #avoid turning right -> w = -1   
            repost.angular.z = 0    
    if F < threashold:
        if repost.linear.x > 0 :
            #deny moving toward an obstacle
            repost.linear.x = 0
    if L < threashold :
        if repost.angular.z > 0 :
            #avoid turning left -> w = 1
            repost.angular.z = 0
    #pubblic on topic cmd_vel to the robot
    pub.publish(repost)

  
def keyboard_input():
    #initialize the node
    rospy.init_node('keyboard_remap_node')
    #subscriber to topic remap_cmd_vel    
    rospy.Subscriber("/remap_cmd_vel", Twist, callingback_map)
    #subscriber to topic scan
    rospy.Subscriber("/scan", LaserScan, callingback_scans)
    rospy.spin()
    
#main 
if __name__=="__main__":
    keyboard_input()