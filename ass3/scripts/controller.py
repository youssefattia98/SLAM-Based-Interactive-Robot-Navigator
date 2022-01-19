#! /usr/bin/env python

import rospy
from ass3.srv import Cordinates_srv
from ass3.srv import KB_input_srv

def case1():
    x = float(input("please enter x coordinates: "))
    y = float(input("please enter y coordinates: "))
    rospy.wait_for_service('cordinates_srv')
    cordinates_srv = rospy.ServiceProxy('cordinates_srv', Cordinates_srv)
    rt = cordinates_srv(x , y)
    if rt.return_ == 1:
        print("target reached successfully!")
    else:
        print("target not reached")

def case2():
    print("case 2")
    print("i will wait for service")
    rospy.wait_for_service('kb_input_srv')
    print("finished waiting")
    kb_input_srv = rospy.ServiceProxy('kb_input_srv', KB_input_srv)
    print("used the service proxy thing")
    kb_input_srv(1)
    print("finished ur stupid function")

def case3():
    print("case 3")
    rospy.wait_for_service('kb_input_srv')
    kb_input_srv = rospy.ServiceProxy('kb_input_srv', KB_input_srv)
    kb_input_srv(2)

if __name__=="__main__":
    #initialize the ros node
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
            print("wrong choice")