#!/usr/bin/env python

import rospy
import os
from std_msgs.msg import String

def killNode():
    nodes = os.popen("rosnode list").readlines()

    for i in range(len(nodes)):
        nodes[i] = nodes[i].replace("\n", "")
        print(nodes[i])

    for i in range(len(nodes)):
        if(nodes[i] != '/main_service'):
            os.system("rosnode kill " + nodes[i])


def startNode():
    main_launch = 'rosrun obstacle_avoidance obstacle_avoidance'    
    rospy.loginfo('START')

    os.system(main_launch)


def main():
    rospy.init_node('main_service', anonymous=False)
   
    rospy.spin()


if __name__ == '__main__':
    main()
