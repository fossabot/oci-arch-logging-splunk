# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .data_object_column_unit import DataObjectColumnUnit
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DataObjectPowerColumnUnit(DataObjectColumnUnit):
    """
    Unit details of a data object column of POWER unit category.
    """

    #: A constant which can be used with the unit property of a DataObjectPowerColumnUnit.
    #: This constant has a value of "AMP"
    UNIT_AMP = "AMP"

    #: A constant which can be used with the unit property of a DataObjectPowerColumnUnit.
    #: This constant has a value of "WATT"
    UNIT_WATT = "WATT"

    #: A constant which can be used with the unit property of a DataObjectPowerColumnUnit.
    #: This constant has a value of "KILO_WATT"
    UNIT_KILO_WATT = "KILO_WATT"

    #: A constant which can be used with the unit property of a DataObjectPowerColumnUnit.
    #: This constant has a value of "MEGA_WATT"
    UNIT_MEGA_WATT = "MEGA_WATT"

    #: A constant which can be used with the unit property of a DataObjectPowerColumnUnit.
    #: This constant has a value of "GIGA_WATT"
    UNIT_GIGA_WATT = "GIGA_WATT"

    def __init__(self, **kwargs):
        """
        Initializes a new DataObjectPowerColumnUnit object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DataObjectPowerColumnUnit.unit_category` attribute
        of this class is ``POWER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param unit_category:
            The value to assign to the unit_category property of this DataObjectPowerColumnUnit.
            Allowed values for this property are: "DATA_SIZE", "TIME", "POWER", "TEMPERATURE", "CORE", "RATE", "FREQUENCY", "OTHER_STANDARD", "CUSTOM", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit_category: str

        :param display_name:
            The value to assign to the display_name property of this DataObjectPowerColumnUnit.
        :type display_name: str

        :param unit:
            The value to assign to the unit property of this DataObjectPowerColumnUnit.
            Allowed values for this property are: "AMP", "WATT", "KILO_WATT", "MEGA_WATT", "GIGA_WATT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type unit: str

        """
        self.swagger_types = {
            'unit_category': 'str',
            'display_name': 'str',
            'unit': 'str'
        }

        self.attribute_map = {
            'unit_category': 'unitCategory',
            'display_name': 'displayName',
            'unit': 'unit'
        }

        self._unit_category = None
        self._display_name = None
        self._unit = None
        self._unit_category = 'POWER'

    @property
    def unit(self):
        """
        Gets the unit of this DataObjectPowerColumnUnit.
        Power unit.

        Allowed values for this property are: "AMP", "WATT", "KILO_WATT", "MEGA_WATT", "GIGA_WATT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The unit of this DataObjectPowerColumnUnit.
        :rtype: str
        """
        return self._unit

    @unit.setter
    def unit(self, unit):
        """
        Sets the unit of this DataObjectPowerColumnUnit.
        Power unit.


        :param unit: The unit of this DataObjectPowerColumnUnit.
        :type: str
        """
        allowed_values = ["AMP", "WATT", "KILO_WATT", "MEGA_WATT", "GIGA_WATT"]
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
