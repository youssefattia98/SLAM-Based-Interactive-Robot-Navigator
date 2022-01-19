#! /usr/bin/env python

import rospy
from ass3.srv import Cordinates_srv
import actionlib
from move_base_msgs.msg import *
from actionlib_msgs.msg import *
 

#read the request provided by the user
#create a goal (using user's data)
#send the goal and wait for a result
#a timeout is set to prevent infinite waiting in case the target is out of the range
#of the robot
#if the target is reached or if the timeout is over the service return to user_controller 
#if the target is not reached call cancel_goal for the action
def SSR(req):
    x = req.x
    y = req.y
    print("moving to X: ",x," Y: ",y)
    client = actionlib.SimpleActionClient('move_base', MoveBaseAction) #start movebaseaction
    client.wait_for_server() #waiting for response
    
    #create the goal
    goal = MoveBaseGoal()
    #set the goal parameter
    goal.target_pose.header.frame_id = 'map'
    goal.target_pose.pose.orientation.w = 1
    goal.target_pose.pose.position.x = x
    goal.target_pose.pose.position.y = y
    #send the goal
    client.send_goal(goal)
    #wait for result
    wait = client.wait_for_result(timeout=rospy.Duration(50.0))
    if not wait:
        #target not reached, calling cancle goal and return
        print("Mission failed, robot didn't reach goal")
        client.cancel_goal()
        return -1
    return 1 #if reahced the target

def coordinates_srv():
    print("Autonomous node.")
    rospy.init_node('coordinate_controller') #seting up the node
    s = rospy.Service('cordinates_srv' ,Cordinates_srv ,SSR) #calling server service routine
    print("service ready")
    rospy.spin()

if __name__=="__main__":
    coordinates_srv()