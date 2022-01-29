# Research Track Assignment 3 description:
Assignment 3 for Research Track course, the project consists of a simulation in which a robot can operate in three different modes according to the user choice. Either Autonomous mode of going to a specific correnaties that the user choice or manual mode driving with or without obstacle avoidance.
This repo consists of the following points:  
 1)How to Setup the Simulator.   
 2)Nodes and servcies graphs.  
 3)Final output.   

1)How to Setup the Simulator.  
================================

Installing and running
----------------------

The simulator requires specific ROS version and I recommend using the Docker image dedicated to this course to make installation and running easier. After cloning the repo to the ROS work space the following commands should be used in the workspace directory to install.

```bash
$ sudo apt-get install konsole
$ sudo bash run.sh
```
If console application is not preferred installed the simulation can be run using the following commands.

```bash
$ sudo roslaunch final_assignment simulation_gmapping.launch 
$ sudo roslaunch final_assignment move_base.launch
$ sudo roslaunch ass3 launcheverything.launch
```


2)Nodes and servcies graphs. 
================================
As the controller works in three diffrent modes according to the user choice.
Firslty, the bash scripts starts the simualtion along with a roslaunch file which is launcheverything.launch, this lauch file runs controller.py, case_one.py and kb_ctr.py.
Secondly, the controller.py askes the user for his/her choice which are as follow:

```python
print("1) autonomously reach a x,y coordinate provided by the user")
print("2) drive the robot using the keyboard")
print("3) drive the robot using the keyboard with collisions avoidance")
print("4) quit the program")
```
For choice one, the user gets asked for the coordinates he/she whishes the robot to reach and are sent through the service called "Cordinates_srv" in which case_one.py receives these coordinates message and drive the robot to it and in return send 1 or 0 if the robot reached its destination or not.

For choice two, will wait for service (KB_input_srv) and send to it 1 this message will make the kb_ctr.py run the command roslaunch for case_two.launch which will start the (teleop_twist_keyboard.py) controlling the robot manually

For choice three, same as choice two but roslaunch for case_three.launch which not only runs (teleop_twist_keyboard.py) but also (case_three.py) and (remap_cmd_vel) which controllers the robot with obsticale avoidance.

Lastly, the following graphs shows how the nodes are communicating with each other and what services are running in each case.

Graphs of node and services
---------

![immagine](https://github.com/youssefattia98/Research-Track-Assignment-3/blob/main/1.png)  
![immagine](https://github.com/youssefattia98/Research-Track-Assignment-3/blob/main/2.png)
![immagine](https://github.com/youssefattia98/Research-Track-Assignment-3/blob/main/3.png)


3)Final Output. 
================================

https://user-images.githubusercontent.com/69837845/151676908-20da9d25-f871-45e3-bbac-c1fe4be5ec13.mp4


The speed up video above shows the robot behaving in the environment doing its intended task, also shows the thre diffrent cases that the user can show for the robot.  
Furthermore, this assignment enhanced my skills in using Linux, docker, GitHub, ROS and Cpp and I am very happy with the output I have reached.
