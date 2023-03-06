# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class QuarterlyUpgradeBeginTimes(object):
    """
    Determines the quarterly upgrade begin times (monthly maintenance group schedule ) of the Fusion environment.
    """

    #: A constant which can be used with the override_type property of a QuarterlyUpgradeBeginTimes.
    #: This constant has a value of "OVERRIDDEN"
    OVERRIDE_TYPE_OVERRIDDEN = "OVERRIDDEN"

    #: A constant which can be used with the override_type property of a QuarterlyUpgradeBeginTimes.
    #: This constant has a value of "INHERITED"
    OVERRIDE_TYPE_INHERITED = "INHERITED"

    def __init__(self, **kwargs):
        """
        Initializes a new QuarterlyUpgradeBeginTimes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param override_type:
            The value to assign to the override_type property of this QuarterlyUpgradeBeginTimes.
            Allowed values for this property are: "OVERRIDDEN", "INHERITED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type override_type: str

        :param begin_times_value:
            The value to assign to the begin_times_value property of this QuarterlyUpgradeBeginTimes.
        :type begin_times_value: str

        """
        self.swagger_types = {
            'override_type': 'str',
            'begin_times_value': 'str'
        }

        self.attribute_map = {
            'override_type': 'overrideType',
            'begin_times_value': 'beginTimesValue'
        }

        self._override_type = None
        self._begin_times_value = None

    @property
    def override_type(self):
        """
        Gets the override_type of this QuarterlyUpgradeBeginTimes.
        Determines if the maintenance schedule of the Fusion environment is inherited from the Fusion environment family.

        Allowed values for this property are: "OVERRIDDEN", "INHERITED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The override_type of this QuarterlyUpgradeBeginTimes.
        :rtype: str
        """
        return self._override_type

    @override_type.setter
    def override_type(self, override_type):
        """
        Sets the override_type of this QuarterlyUpgradeBeginTimes.
        Determines if the maintenance schedule of the Fusion environment is inherited from the Fusion environment family.


        :param override_type: The override_type of this QuarterlyUpgradeBeginTimes.
        :type: str
        """
        allowed_values = ["OVERRIDDEN", "INHERITED"]
        if not value_allowed_none_or_none_sentinel(override_type, allowed_values):
            override_type = 'UNKNOWN_ENUM_VALUE'
        self._override_type = override_type

    @property
    def begin_times_value(self):
        """
        Gets the begin_times_value of this QuarterlyUpgradeBeginTimes.
        The frequency and month when maintenance occurs for the Fusion environment.


        :return: The begin_times_value of this QuarterlyUpgradeBeginTimes.
        :rtype: str
        """
        return self._begin_times_value

    @begin_times_value.setter
    def begin_times_value(self, begin_times_value):
        """
        Sets the begin_times_value of this QuarterlyUpgradeBeginTimes.
        The frequency and month when maintenance occurs for the Fusion environment.


        :param begin_times_value: The begin_times_value of this QuarterlyUpgradeBeginTimes.
        :type: str
        """
        self._begin_times_value = begin_times_value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
