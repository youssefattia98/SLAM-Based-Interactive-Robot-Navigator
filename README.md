# Research Track Assignment 3 description:
Assignment 3 for Research Track course, the project consists of a simulation in which a robot can operate in three different modes according to the user choice. Either Autonomous mode of going to a specific correnaties that the user choice or manual mode driving with or without obstacle avoidance.
This repo consists of the following points:  
 1)How to Setup the Simulator.   
 2)Algorithm used to solve the problem, truth table and graphs.  
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


2)Algorithm used to solve the problem and flowchart. 
================================
to be written. 

Graphs of node and services
---------

![immagine](https://github.com/youssefattia98/Research-Track-Assignment-3/blob/main/1.png)  
![immagine](https://github.com/youssefattia98/Research-Track-Assignment-3/blob/main/2.png)
![immagine](https://github.com/youssefattia98/Research-Track-Assignment-3/blob/main/3.png)


To be edited: The above Flowchart describes more details the communication between the ROS nodes and how data is transferred. Note that, the client can control the speed of the robot to a certain limit to assure that the robot will never crash and if the user chooses to increase the speed more than this limits the simulation will reset with minimum speed. Also, if the user input any wrong input then that he should the simulation will reset the robots position and speed.

3)Final Output. 
================================

https://user-images.githubusercontent.com/69837845/151676908-20da9d25-f871-45e3-bbac-c1fe4be5ec13.mp4


to be editied The speed up video below shows the robot behaving in the environment doing its intended task, this simulation can run for ever in which the robot will stay in this loop. Furthermore, this assignment enhanced my skills in using Linux, docker, GitHub, ROS and Cpp and I am very happy with the output I have reached.
Finally, I really wanted to mention how much I enjoyed working on this project with my collages.
