# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseTool(object):
    """
    Summary of database tools of autonomous database.
    """

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "APEX"
    NAME_APEX = "APEX"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "DATABASE_ACTIONS"
    NAME_DATABASE_ACTIONS = "DATABASE_ACTIONS"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "GRAPH_STUDIO"
    NAME_GRAPH_STUDIO = "GRAPH_STUDIO"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "OML"
    NAME_OML = "OML"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "DATA_TRANSFORMS"
    NAME_DATA_TRANSFORMS = "DATA_TRANSFORMS"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "ORDS"
    NAME_ORDS = "ORDS"

    #: A constant which can be used with the name property of a DatabaseTool.
    #: This constant has a value of "MONGODB_API"
    NAME_MONGODB_API = "MONGODB_API"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseTool object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this DatabaseTool.
            Allowed values for this property are: "APEX", "DATABASE_ACTIONS", "GRAPH_STUDIO", "OML", "DATA_TRANSFORMS", "ORDS", "MONGODB_API", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type name: str

        :param is_enabled:
            The value to assign to the is_enabled property of this DatabaseTool.
        :type is_enabled: bool

        :param compute_count:
            The value to assign to the compute_count property of this DatabaseTool.
        :type compute_count: float

        :param max_idle_time_in_minutes:
            The value to assign to the max_idle_time_in_minutes property of this DatabaseTool.
        :type max_idle_time_in_minutes: int

        """
        self.swagger_types = {
            'name': 'str',
            'is_enabled': 'bool',
            'compute_count': 'float',
            'max_idle_time_in_minutes': 'int'
        }

        self.attribute_map = {
            'name': 'name',
            'is_enabled': 'isEnabled',
            'compute_count': 'computeCount',
            'max_idle_time_in_minutes': 'maxIdleTimeInMinutes'
        }

        self._name = None
        self._is_enabled = None
        self._compute_count = None
        self._max_idle_time_in_minutes = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this DatabaseTool.
        Name of database tool.

        Allowed values for this property are: "APEX", "DATABASE_ACTIONS", "GRAPH_STUDIO", "OML", "DATA_TRANSFORMS", "ORDS", "MONGODB_API", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The name of this DatabaseTool.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this DatabaseTool.
        Name of database tool.


        :param name: The name of this DatabaseTool.
        :type: str
        """
        allowed_values = ["APEX", "DATABASE_ACTIONS", "GRAPH_STUDIO", "OML", "DATA_TRANSFORMS", "ORDS", "MONGODB_API"]
        if not value_allowed_none_or_none_sentinel(name, allowed_values):
            name = 'UNKNOWN_ENUM_VALUE'
        self._name = name

    @property
    def is_enabled(self):
        """
        Gets the is_enabled of this DatabaseTool.
        Indicates whether tool is enabled.


        :return: The is_enabled of this DatabaseTool.
        :rtype: bool
        """
        return self._is_enabled

    @is_enabled.setter
    def is_enabled(self, is_enabled):
        """
        Sets the is_enabled of this DatabaseTool.
        Indicates whether tool is enabled.


        :param is_enabled: The is_enabled of this DatabaseTool.
        :type: bool
        """
        self._is_enabled = is_enabled

    @property
    def compute_count(self):
        """
        Gets the compute_count of this DatabaseTool.
        Compute used by database tools.


        :return: The compute_count of this DatabaseTool.
        :rtype: float
        """
        return self._compute_count

    @compute_count.setter
    def compute_count(self, compute_count):
        """
        Sets the compute_count of this DatabaseTool.
        Compute used by database tools.


        :param compute_count: The compute_count of this DatabaseTool.
        :type: float
        """
        self._compute_count = compute_count

    @property
    def max_idle_time_in_minutes(self):
        """
        Gets the max_idle_time_in_minutes of this DatabaseTool.
        The max idle time, in minutes, after which the VM used by database tools will be terminated.


        :return: The max_idle_time_in_minutes of this DatabaseTool.
        :rtype: int
        """
        return self._max_idle_time_in_minutes

    @max_idle_time_in_minutes.setter
    def max_idle_time_in_minutes(self, max_idle_time_in_minutes):
        """
        Sets the max_idle_time_in_minutes of this DatabaseTool.
        The max idle time, in minutes, after which the VM used by database tools will be terminated.


        :param max_idle_time_in_minutes: The max_idle_time_in_minutes of this DatabaseTool.
        :type: int
        """
        self._max_idle_time_in_minutes = max_idle_time_in_minutes

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
