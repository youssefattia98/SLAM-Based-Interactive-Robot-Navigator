konsole  -e roslaunch final_assignment simulation_gmapping.launch &
sleep 7
konsole  -e roslaunch final_assignment move_base.launch &
sleep 7
konsole  -e roslaunch ass3 launcheverything.launch