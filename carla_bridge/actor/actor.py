#!/usr/bin/env python

#
# Copyright (c) 2018-2019 Intel Corporation
#
# This work is licensed under the terms of the MIT license.
# For a copy, see <https://opensource.org/licenses/MIT>.
#
"""
Base Classes to handle Actor objects
"""
from carla_bridge.actor.pseudo_actor import PseudoActor
import carla_bridge.utils.transforms as trans


class Actor(PseudoActor):
    """
    Generic base class for all carla actors
    """

    def __init__(self, uid, name, parent, node, carla_actor):
        """
        Constructor

        :param uid: unique identifier for this object
        :type uid: int
        :param name: name identiying this object
        :type name: string
        :param parent: the parent of this
        :type parent: bridge.Parent
        :param node: node-handle
        :type node: CyberNode
        :param carla_actor: carla actor object
        :type carla_actor: carla.Actor
        """
        super().__init__(uid=uid, name=name, parent=parent, node=node)
        self.carla_actor = carla_actor
        self.carla_actor_id = carla_actor.id

    def destroy(self):
        """
        Function (override) to destroy this object.
        Remove the reference to the carla.Actor object.
        :return:
        """
        self.carla_actor = None
        super().destroy()

    def get_current_cyber_pose(self):
        """
        Function to provide the current ROS pose

        :return: the ROS pose of this actor
        :rtype: geometry_msgs.msg.Pose
        """
        return trans.carla_transform_to_cyber_pose(self.carla_actor.get_transform())

    def get_current_cyber_transform(self):
        """
        Function to provide the current ROS pose

        :return: the ROS pose of this actor
        :rtype: geometry_msgs.msg.Pose
        """
        return trans.carla_transform_to_cyber_transform(
            self.carla_actor.get_transform()
        )

    def get_current_cyber_twist_rotated(self):
        """
        Function to provide the current ROS twist rotated

        :return: the ROS twist of this actor
        """
        return trans.carla_velocity_to_cyber_twist(
            self.carla_actor.get_velocity(),
            self.carla_actor.get_angular_velocity(),
            self.carla_actor.get_transform().rotation,
        )

    def get_current_cyber_twist(self):
        """
        Function to provide the current ROS twist

        :return: the ROS twist of this actor
        """
        return trans.carla_velocity_to_cyber_twist(
            self.carla_actor.get_velocity(), self.carla_actor.get_angular_velocity()
        )

    def get_current_cyber_accel(self):
        """
        Function to provide the current ROS accel

        :return: the ROS twist of this actor
        """
        return trans.carla_acceleration_to_cyber_accel(
            self.carla_actor.get_acceleration()
        )

    def get_id(self):
        """
        Getter for the carla_id of this.
        :return: unique carla_id of this object
        :rtype: int64
        """
        return self.carla_actor_id

    def set_carla_actor(self, carla_actor):
        self.carla_actor = carla_actor
