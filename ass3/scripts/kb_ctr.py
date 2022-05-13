#! /usr/bin/env python
"""
.. module:: kb_ctr
    :platform: Unix
    :synopsis: Python code for keyborad control of the robot used in both case two or three
.. moduleauthor:: Youssef Attia youssef-attia@live.com

Service:
    /kb_input_srv

This node handles the Second and the third case which are *drive the robot using the keyboard* and *drive the robot using the keyboard with collisions avoidance*
if chossen by the user in the controller script
"""

import rospy
#service server
from ass3.srv import KB_input_srv
import os   #call in terminal

#read the request parameter and choose whether it is case 2 or case 3 of the
#user option menu, then call the dedicated launch file
def SSR(req):
    """
    This Function is Service Routine Function and it does the following:
    1) Read the request provided by the user from :mod 'controller'.
    2) If receives 1 then its case two else if it receives 2 then its case three *same as case two but with obstacle avoidance*
    3) If Its case two it runs the roslaunch file for :mod 'case_two'
    4) If Its case three it runs the roslaunch file for :mod 'case_three'
    """
    if req.keyboard_case == 1:
       #call keyboard teleop w/o obstacle avoidance
       print("Calling teleop twist keyboard")
       os.system("roslaunch ass3 case_two.launch") 
       
    elif req.keyboard_case == 2:
        #call keyboard teleop and the osbstacle avoidance
        print("Calling teleop twist keyboard with obstacle avoidance control")
        os.system("roslaunch ass3 case_three.launch")
    else:
        print("Incorrect input")
    return 0         
   
def kb_server():
    """
    This Function is to setup the node and also call the server service routine function.

    Service:
        /kb_input_srv
    """
    #print general information about the node
    print("Keyboard controlling for robot...")
    #initialize the node
    rospy.init_node('keyboard_controller')
    s = rospy.Service('kb_input_srv' ,KB_input_srv ,SSR) #server service routine
    #print("service ready")
    rospy.spin()

#main
if __name__=="__main__":
    kb_server()