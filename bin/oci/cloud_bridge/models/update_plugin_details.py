# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdatePluginDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdatePluginDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param desired_state:
            The value to assign to the desired_state property of this UpdatePluginDetails.
        :type desired_state: str

        """
        self.swagger_types = {
            'desired_state': 'str'
        }

        self.attribute_map = {
            'desired_state': 'desiredState'
        }

        self._desired_state = None

    @property
    def desired_state(self):
        """
        Gets the desired_state of this UpdatePluginDetails.
        State to which the customer wants the plugin to move to.


        :return: The desired_state of this UpdatePluginDetails.
        :rtype: str
        """
        return self._desired_state

    @desired_state.setter
    def desired_state(self, desired_state):
        """
        Sets the desired_state of this UpdatePluginDetails.
        State to which the customer wants the plugin to move to.


        :param desired_state: The desired_state of this UpdatePluginDetails.
        :type: str
        """
        self._desired_state = desired_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
