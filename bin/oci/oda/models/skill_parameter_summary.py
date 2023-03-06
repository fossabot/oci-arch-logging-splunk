# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class SkillParameterSummary(object):
    """
    Metadata for a Skill Parameter property.
    """

    #: A constant which can be used with the type property of a SkillParameterSummary.
    #: This constant has a value of "STRING"
    TYPE_STRING = "STRING"

    #: A constant which can be used with the type property of a SkillParameterSummary.
    #: This constant has a value of "INTEGER"
    TYPE_INTEGER = "INTEGER"

    #: A constant which can be used with the type property of a SkillParameterSummary.
    #: This constant has a value of "FLOAT"
    TYPE_FLOAT = "FLOAT"

    #: A constant which can be used with the type property of a SkillParameterSummary.
    #: This constant has a value of "BOOLEAN"
    TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the type property of a SkillParameterSummary.
    #: This constant has a value of "SECURE"
    TYPE_SECURE = "SECURE"

    #: A constant which can be used with the lifecycle_state property of a SkillParameterSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a SkillParameterSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a SkillParameterSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SkillParameterSummary.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a SkillParameterSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a SkillParameterSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a SkillParameterSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new SkillParameterSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this SkillParameterSummary.
        :type name: str

        :param display_name:
            The value to assign to the display_name property of this SkillParameterSummary.
        :type display_name: str

        :param description:
            The value to assign to the description property of this SkillParameterSummary.
        :type description: str

        :param type:
            The value to assign to the type property of this SkillParameterSummary.
            Allowed values for this property are: "STRING", "INTEGER", "FLOAT", "BOOLEAN", "SECURE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param value:
            The value to assign to the value property of this SkillParameterSummary.
        :type value: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this SkillParameterSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        """
        self.swagger_types = {
            'name': 'str',
            'display_name': 'str',
            'description': 'str',
            'type': 'str',
            'value': 'str',
            'lifecycle_state': 'str'
        }

        self.attribute_map = {
            'name': 'name',
            'display_name': 'displayName',
            'description': 'description',
            'type': 'type',
            'value': 'value',
            'lifecycle_state': 'lifecycleState'
        }

        self._name = None
        self._display_name = None
        self._description = None
        self._type = None
        self._value = None
        self._lifecycle_state = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this SkillParameterSummary.
        The Parameter name.  This must be unique within the parent resource.


        :return: The name of this SkillParameterSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this SkillParameterSummary.
        The Parameter name.  This must be unique within the parent resource.


        :param name: The name of this SkillParameterSummary.
        :type: str
        """
        self._name = name

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this SkillParameterSummary.
        The display name for the Parameter.


        :return: The display_name of this SkillParameterSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this SkillParameterSummary.
        The display name for the Parameter.


        :param display_name: The display_name of this SkillParameterSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this SkillParameterSummary.
        A description of the Parameter.


        :return: The description of this SkillParameterSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this SkillParameterSummary.
        A description of the Parameter.


        :param description: The description of this SkillParameterSummary.
        :type: str
        """
        self._description = description

    @property
    def type(self):
        """
        **[Required]** Gets the type of this SkillParameterSummary.
        The value type.

        Allowed values for this property are: "STRING", "INTEGER", "FLOAT", "BOOLEAN", "SECURE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this SkillParameterSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this SkillParameterSummary.
        The value type.


        :param type: The type of this SkillParameterSummary.
        :type: str
        """
        allowed_values = ["STRING", "INTEGER", "FLOAT", "BOOLEAN", "SECURE"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def value(self):
        """
        Gets the value of this SkillParameterSummary.
        The current value.  The value will be interpreted based on the `type`.


        :return: The value of this SkillParameterSummary.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this SkillParameterSummary.
        The current value.  The value will be interpreted based on the `type`.


        :param value: The value of this SkillParameterSummary.
        :type: str
        """
        self._value = value

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this SkillParameterSummary.
        The Parameter's current state.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this SkillParameterSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this SkillParameterSummary.
        The Parameter's current state.


        :param lifecycle_state: The lifecycle_state of this SkillParameterSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "INACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
