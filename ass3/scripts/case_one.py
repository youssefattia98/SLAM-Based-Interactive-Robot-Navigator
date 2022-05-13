#! /usr/bin/env python
"""
.. module:: case_one
    :platform: Unix
    :synopsis: Python code for case one
.. moduleauthor:: Youssef Attia youssef-attia@live.com

Service:
    /cordinates_srv
        
Messages:
    /move_base_msgs
    /actionlib_msgs

This node handles the first case which is *autonomously reach a x,y coordinate provided by the user*
if chossen by the user in the controller script
"""
import rospy
from ass3.srv import Cordinates_srv
import actionlib
from move_base_msgs.msg import *
from actionlib_msgs.msg import *
 


def SSR(req):
    """
    This Function is Service Routine Function and it does the following:
    1) Read the request provided by the user from :mod 'controller'.
    2) Create a goal using the user data.
    3) Sends the goal and waits for the result.
    4) A timeout is used to prevent infinite waiting in case the target is out of the range of the robot.
    5) If the target is reached or if the timeout is over the service return to user_controller.
    6)if the target is not reached call cancel_goal for the action.

    Topic:
        /move_base
    """
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
    """
    This Function is to setup the node and also call the server service routine function.

    Service:
        /cordinates_srv
    """
    print("Autonomous node.")
    rospy.init_node('coordinate_controller') #seting up the node
    s = rospy.Service('cordinates_srv' ,Cordinates_srv ,SSR) #calling server service routine
    print("service ready")
    rospy.spin()

if __name__=="__main__":
    coordinates_srv()