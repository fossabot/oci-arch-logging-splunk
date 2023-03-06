# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class RateLimit(object):
    """
    Rate-limiting policy for a usage plan.
    """

    #: A constant which can be used with the unit property of a RateLimit.
    #: This constant has a value of "SECOND"
    UNIT_SECOND = "SECOND"

    def __init__(self, **kwargs):
        """
        Initializes a new RateLimit object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this RateLimit.
        :type value: int

        :param unit:
            The value to assign to the unit property of this RateLimit.
            Allowed values for this property are: "SECOND", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        """
        self.swagger_types = {
            'value': 'int',
            'unit': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'unit': 'unit'
        }

        self._value = None
        self._unit = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this RateLimit.
        The number of requests that can be made per time period.


        :return: The value of this RateLimit.
        :rtype: int
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this RateLimit.
        The number of requests that can be made per time period.


        :param value: The value of this RateLimit.
        :type: int
        """
        self._value = value

    @property
    def unit(self):
        """
        **[Required]** Gets the unit of this RateLimit.
        The unit of time over which rate limits are calculated.
        Example: `SECOND`

        Allowed values for this property are: "SECOND", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this RateLimit.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this RateLimit.
        The unit of time over which rate limits are calculated.
        Example: `SECOND`


        :param unit: The unit of this RateLimit.
        :type: str
        """
        allowed_values = ["SECOND"]
        if not value_allowed_none_or_none_sentinel(unit, allowed_values):
            unit = 'UNKNOWN_ENUM_VALUE'
        self._unit = unit

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
