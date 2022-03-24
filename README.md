# TeleOp-implementation

	
Steps for various tasks:
	
	To Launch the model “sfinal” in the given world:
    • copy “sfinal” package into your catkin workspace.
    • Navigate to catkin_ws in terminal
    • run : catkin_make clean && catkin_make
    • run : source ~/catkin_ws/devel/setup.bash
    • run : roslaunch sfinal template_launch.launch
    • This will launch the model in the given world.
	

	To run python scripts to control the robot in the world:
    • navigate in the terminal to your catkin_ws → src → sfinal → src.
    • Run : python3 teleop_template.py
    • This will allow you to control the robot model in the given world.
	
	To run python scripts to check for subscriber and publisher:
    • navigate in the terminal to your catkin_ws → src → sfinal → src.
    • Run : roscore in one terminal and in another 
    • Run : python3 publisher.py  in one terminal and in another
    • Run : python3 subscriber.py 
    • This will allow you to observer the interaction between two nodes. (I.e publisher and subscriber)
