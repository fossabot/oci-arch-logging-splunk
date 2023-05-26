# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ParameterDefinition(object):
    """
    A parameter to a resource.
    """

    #: A constant which can be used with the type property of a ParameterDefinition.
    #: This constant has a value of "STRING"
    TYPE_STRING = "STRING"

    #: A constant which can be used with the type property of a ParameterDefinition.
    #: This constant has a value of "URI"
    TYPE_URI = "URI"

    #: A constant which can be used with the type property of a ParameterDefinition.
    #: This constant has a value of "URL"
    TYPE_URL = "URL"

    #: A constant which can be used with the type property of a ParameterDefinition.
    #: This constant has a value of "NUMBER"
    TYPE_NUMBER = "NUMBER"

    #: A constant which can be used with the type property of a ParameterDefinition.
    #: This constant has a value of "BOOLEAN"
    TYPE_BOOLEAN = "BOOLEAN"

    #: A constant which can be used with the direction property of a ParameterDefinition.
    #: This constant has a value of "INPUT"
    DIRECTION_INPUT = "INPUT"

    #: A constant which can be used with the direction property of a ParameterDefinition.
    #: This constant has a value of "OUTPUT"
    DIRECTION_OUTPUT = "OUTPUT"

    def __init__(self, **kwargs):
        """
        Initializes a new ParameterDefinition object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this ParameterDefinition.
        :type name: str

        :param type:
            The value to assign to the type property of this ParameterDefinition.
            Allowed values for this property are: "STRING", "URI", "URL", "NUMBER", "BOOLEAN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param description:
            The value to assign to the description property of this ParameterDefinition.
        :type description: str

        :param is_required:
            The value to assign to the is_required property of this ParameterDefinition.
        :type is_required: bool

        :param is_sensitive:
            The value to assign to the is_sensitive property of this ParameterDefinition.
        :type is_sensitive: bool

        :param default_value:
            The value to assign to the default_value property of this ParameterDefinition.
        :type default_value: str

        :param min_length:
            The value to assign to the min_length property of this ParameterDefinition.
        :type min_length: int

        :param max_length:
            The value to assign to the max_length property of this ParameterDefinition.
        :type max_length: int

        :param pattern:
            The value to assign to the pattern property of this ParameterDefinition.
        :type pattern: str

        :param direction:
            The value to assign to the direction property of this ParameterDefinition.
            Allowed values for this property are: "INPUT", "OUTPUT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type direction: str

        :param ui_placement_hint:
            The value to assign to the ui_placement_hint property of this ParameterDefinition.
        :type ui_placement_hint: str

        :param resource_type_metadata:
            The value to assign to the resource_type_metadata property of this ParameterDefinition.
        :type resource_type_metadata: object

        """
        self.swagger_types = {
            'name': 'str',
            'type': 'str',
            'description': 'str',
            'is_required': 'bool',
            'is_sensitive': 'bool',
            'default_value': 'str',
            'min_length': 'int',
            'max_length': 'int',
            'pattern': 'str',
            'direction': 'str',
            'ui_placement_hint': 'str',
            'resource_type_metadata': 'object'
        }

        self.attribute_map = {
            'name': 'name',
            'type': 'type',
            'description': 'description',
            'is_required': 'isRequired',
            'is_sensitive': 'isSensitive',
            'default_value': 'defaultValue',
            'min_length': 'minLength',
            'max_length': 'maxLength',
            'pattern': 'pattern',
            'direction': 'direction',
            'ui_placement_hint': 'uiPlacementHint',
            'resource_type_metadata': 'resourceTypeMetadata'
        }

        self._name = None
        self._type = None
        self._description = None
        self._is_required = None
        self._is_sensitive = None
        self._default_value = None
        self._min_length = None
        self._max_length = None
        self._pattern = None
        self._direction = None
        self._ui_placement_hint = None
        self._resource_type_metadata = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this ParameterDefinition.
        The name of the parameter


        :return: The name of this ParameterDefinition.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this ParameterDefinition.
        The name of the parameter


        :param name: The name of this ParameterDefinition.
        :type: str
        """
        self._name = name

    @property
    def type(self):
        """
        **[Required]** Gets the type of this ParameterDefinition.
        Enumerated parameter type.

        Allowed values for this property are: "STRING", "URI", "URL", "NUMBER", "BOOLEAN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this ParameterDefinition.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this ParameterDefinition.
        Enumerated parameter type.


        :param type: The type of this ParameterDefinition.
        :type: str
        """
        allowed_values = ["STRING", "URI", "URL", "NUMBER", "BOOLEAN"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def description(self):
        """
        Gets the description of this ParameterDefinition.
        Description of the parameter.


        :return: The description of this ParameterDefinition.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this ParameterDefinition.
        Description of the parameter.


        :param description: The description of this ParameterDefinition.
        :type: str
        """
        self._description = description

    @property
    def is_required(self):
        """
        Gets the is_required of this ParameterDefinition.
        Is this parameter required. Ignored for parameters with direction = OUTPUT.


        :return: The is_required of this ParameterDefinition.
        :rtype: bool
        """
        return self._is_required

    @is_required.setter
    def is_required(self, is_required):
        """
        Sets the is_required of this ParameterDefinition.
        Is this parameter required. Ignored for parameters with direction = OUTPUT.


        :param is_required: The is_required of this ParameterDefinition.
        :type: bool
        """
        self._is_required = is_required

    @property
    def is_sensitive(self):
        """
        Gets the is_sensitive of this ParameterDefinition.
        Is the data for this parameter sensitive (e.g. should the data be hidden in UI, encrypted if stored, etc.)


        :return: The is_sensitive of this ParameterDefinition.
        :rtype: bool
        """
        return self._is_sensitive

    @is_sensitive.setter
    def is_sensitive(self, is_sensitive):
        """
        Sets the is_sensitive of this ParameterDefinition.
        Is the data for this parameter sensitive (e.g. should the data be hidden in UI, encrypted if stored, etc.)


        :param is_sensitive: The is_sensitive of this ParameterDefinition.
        :type: bool
        """
        self._is_sensitive = is_sensitive

    @property
    def default_value(self):
        """
        Gets the default_value of this ParameterDefinition.
        Default value for the parameter.


        :return: The default_value of this ParameterDefinition.
        :rtype: str
        """
        return self._default_value

    @default_value.setter
    def default_value(self, default_value):
        """
        Sets the default_value of this ParameterDefinition.
        Default value for the parameter.


        :param default_value: The default_value of this ParameterDefinition.
        :type: str
        """
        self._default_value = default_value

    @property
    def min_length(self):
        """
        Gets the min_length of this ParameterDefinition.
        Used for character string types such as STRING to constrain the length of the value


        :return: The min_length of this ParameterDefinition.
        :rtype: int
        """
        return self._min_length

    @min_length.setter
    def min_length(self, min_length):
        """
        Sets the min_length of this ParameterDefinition.
        Used for character string types such as STRING to constrain the length of the value


        :param min_length: The min_length of this ParameterDefinition.
        :type: int
        """
        self._min_length = min_length

    @property
    def max_length(self):
        """
        Gets the max_length of this ParameterDefinition.
        Used for character string types such as STRING to constrain the length of the value


        :return: The max_length of this ParameterDefinition.
        :rtype: int
        """
        return self._max_length

    @max_length.setter
    def max_length(self, max_length):
        """
        Sets the max_length of this ParameterDefinition.
        Used for character string types such as STRING to constrain the length of the value


        :param max_length: The max_length of this ParameterDefinition.
        :type: int
        """
        self._max_length = max_length

    @property
    def pattern(self):
        """
        Gets the pattern of this ParameterDefinition.
        Regular expression used to validate the value of a string type such as STRING


        :return: The pattern of this ParameterDefinition.
        :rtype: str
        """
        return self._pattern

    @pattern.setter
    def pattern(self, pattern):
        """
        Sets the pattern of this ParameterDefinition.
        Regular expression used to validate the value of a string type such as STRING


        :param pattern: The pattern of this ParameterDefinition.
        :type: str
        """
        self._pattern = pattern

    @property
    def direction(self):
        """
        Gets the direction of this ParameterDefinition.
        Is this parameter an input parameter, output parameter, or both?

        Allowed values for this property are: "INPUT", "OUTPUT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The direction of this ParameterDefinition.
        :rtype: str
        """
        return self._direction

    @direction.setter
    def direction(self, direction):
        """
        Sets the direction of this ParameterDefinition.
        Is this parameter an input parameter, output parameter, or both?


        :param direction: The direction of this ParameterDefinition.
        :type: str
        """
        allowed_values = ["INPUT", "OUTPUT"]
        if not value_allowed_none_or_none_sentinel(direction, allowed_values):
            direction = 'UNKNOWN_ENUM_VALUE'
        self._direction = direction

    @property
    def ui_placement_hint(self):
        """
        Gets the ui_placement_hint of this ParameterDefinition.
        A forward-slash-delimited 'path' in an imaginary hierarchy, at which this parameter's UI widgets should be placed


        :return: The ui_placement_hint of this ParameterDefinition.
        :rtype: str
        """
        return self._ui_placement_hint

    @ui_placement_hint.setter
    def ui_placement_hint(self, ui_placement_hint):
        """
        Sets the ui_placement_hint of this ParameterDefinition.
        A forward-slash-delimited 'path' in an imaginary hierarchy, at which this parameter's UI widgets should be placed


        :param ui_placement_hint: The ui_placement_hint of this ParameterDefinition.
        :type: str
        """
        self._ui_placement_hint = ui_placement_hint

    @property
    def resource_type_metadata(self):
        """
        Gets the resource_type_metadata of this ParameterDefinition.
        Any configuration needed to help the resource type process this parameter (e.g. link to manifest, etc.).


        :return: The resource_type_metadata of this ParameterDefinition.
        :rtype: object
        """
        return self._resource_type_metadata

    @resource_type_metadata.setter
    def resource_type_metadata(self, resource_type_metadata):
        """
        Sets the resource_type_metadata of this ParameterDefinition.
        Any configuration needed to help the resource type process this parameter (e.g. link to manifest, etc.).


        :param resource_type_metadata: The resource_type_metadata of this ParameterDefinition.
        :type: object
        """
        self._resource_type_metadata = resource_type_metadata

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
