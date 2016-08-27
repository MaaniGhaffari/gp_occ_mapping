#!/usr/bin/python

import rospy
from geometry_msgs.msg import PoseStamped
from tf import TransformListener


class PoseFromMapTF:
    """This class publishes the robot pose form map tf."""
    def __init__(self):
        rospy.init_node('pose_from_map_tf', anonymous=True)

        self.listener = TransformListener()
        self.map_frame = 'map'
        self.base_link = 'base_link'

        self.pose_pub = rospy.Publisher('pose_from_map', PoseStamped, queue_size=10)

        self.run()

    def run(self):
        loop_rate = rospy.Rate(100)
        while not rospy.is_shutdown():
            self.get_pose_from_map()
            loop_rate.sleep()

    def get_pose_from_map(self):
        now = rospy.Time.now()
        self.listener.waitForTransform(self.map_frame, self.base_link, rospy.Time(0), rospy.Duration(0.1))
        (trans, rot) = self.listener.lookupTransform(self.map_frame, self.base_link, rospy.Time(0))

        pose_msg = PoseStamped()
        pose_msg.header.stamp = now
        pose_msg.header.frame_id = self.map_frame

        pose_msg.pose.position.x = trans[0]
        pose_msg.pose.position.y = trans[1]
        pose_msg.pose.position.z = trans[2]

        pose_msg.pose.orientation.x = rot[0]
        pose_msg.pose.orientation.y = rot[1]
        pose_msg.pose.orientation.z = rot[2]
        pose_msg.pose.orientation.w = rot[3]

        self.pose_pub.publish(pose_msg)


if __name__ == '__main__':
    try:
        m = PoseFromMapTF()

    except rospy.ROSInterruptException:
        pass
