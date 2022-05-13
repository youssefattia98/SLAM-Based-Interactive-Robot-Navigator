#! /usr/bin/env python
"""
.. module:: controller
    :platform: Unix
    :synopsis: Python code for the user Interface
.. moduleauthor:: Youssef Attia youssef-attia@live.com

Service:
    /cordinates_srv
    /kb_input_srv

This node implements an user interface and launches other luanch files and runs other .py files
"""
import rospy
from ass3.srv import Cordinates_srv
from ass3.srv import KB_input_srv

def case1():
    """
    This Function is to handle to first case which is: *autonomously reach a x,y coordinate provided by the user*
    It askes the user to enter the x and y cordinates and send these cordinates to the service.

    Service:
        /cordinates_srv

    If 1 is returned from the service then the robot had reached its target else it did not.
    This is handled by :mod 'case_one'

    """
    x = float(input("please enter x coordinates: "))
    y = float(input("please enter y coordinates: "))
    rospy.wait_for_service('cordinates_srv')
    cordinates_srv = rospy.ServiceProxy('cordinates_srv', Cordinates_srv)
    rt = cordinates_srv(x , y)
    if rt.return_ == 1:
        print("Target reached successfully!")
    else:
        print("Target not reached")

def case2():
    """
    This Function is to handle to Second case which is: *drive the robot using the keyboard*
    It uses the Service to take the keyboard bottoms pressed by the user to move the robot.

    Service:
        /kb_input_srv

    This is handled by :mod 'kb_ctr'

    """
    print("case 2")
    rospy.wait_for_service('kb_input_srv')
    kb_input_srv = rospy.ServiceProxy('kb_input_srv', KB_input_srv)
    kb_input_srv(1)

def case3():
    """
    This Function is to handle to Third case which is: *drive the robot using the keyboard with collisions avoidance*
    It uses the Service to take the keyboard bottoms pressed by the user to move the robot.

    Service:
        /kb_input_srv

    It can also avoid the collision of the robot and this is handled by :mod 'kb_ctr'
    If the message sent to the service is 2 the controle of the robot has obstacle avoidance capabilities *ON*.

    """
    print("case 3")
    rospy.wait_for_service('kb_input_srv')
    kb_input_srv = rospy.ServiceProxy('kb_input_srv', KB_input_srv)
    kb_input_srv(2)

if __name__=="__main__":
    """
    Initialize the Ros node, and askes the user about his/her choice and therefore runs the corresponding function.
    If the user inputs a wrong choice it is printed out for the user and the while loop starts over again.
    The four choices are:
        *1) autonomously reach a x,y coordinate provided by the user*
        *2) drive the robot using the keyboard*
        *3) drive the robot using the keyboard with collisions avoidance*
        *4) quit the program*
    And the code is written relying on this package: `rospy <http://wiki.ros.org/rospy/>`_ 
    """
    rospy.init_node('controller')
    flag = 1
    while(flag):
        print("Please enter your choice:")
        print("1) autonomously reach a x,y coordinate provided by the user")
        print("2) drive the robot using the keyboard")
        print("3) drive the robot using the keyboard with collisions avoidance")
        print("4) quit the program")
        choice = int(input())
        if (choice == 1):
            #case one
            print("[case one]")
            case1()
        elif (choice == 2):
            #case two
            print("[case two]")
            case2()
        elif (choice == 3):
            #case three
            print("[case two]")
            case3()
        elif (choice == 4):
            #quiting case
            flag = 0
            print("press ctrl-C to quit")
        else:
            #worng choice
            print("Wrong choice")