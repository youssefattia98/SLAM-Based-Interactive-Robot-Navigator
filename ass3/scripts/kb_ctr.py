#! /usr/bin/env python

import rospy
#service server
from ass3.srv import KB_input_srv
import os   #call in terminal

#read the request parameter and choose whether it is case 2 or case 3 of the
#user option menu, then call the dedicated launch file
def SSR(req):
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