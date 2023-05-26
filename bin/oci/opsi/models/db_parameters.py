# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .database_configuration_metric_group import DatabaseConfigurationMetricGroup
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DBParameters(DatabaseConfigurationMetricGroup):
    """
    Initialization parameters for a database.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new DBParameters object with values from keyword arguments. The default value of the :py:attr:`~oci.opsi.models.DBParameters.metric_name` attribute
        of this class is ``DB_PARAMETERS`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param metric_name:
            The value to assign to the metric_name property of this DBParameters.
            Allowed values for this property are: "DB_EXTERNAL_PROPERTIES", "DB_EXTERNAL_INSTANCE", "DB_OS_CONFIG_INSTANCE", "DB_PARAMETERS"
        :type metric_name: str

        :param time_collected:
            The value to assign to the time_collected property of this DBParameters.
        :type time_collected: datetime

        :param instance_number:
            The value to assign to the instance_number property of this DBParameters.
        :type instance_number: int

        :param parameter_name:
            The value to assign to the parameter_name property of this DBParameters.
        :type parameter_name: str

        :param parameter_value:
            The value to assign to the parameter_value property of this DBParameters.
        :type parameter_value: str

        :param snapshot_id:
            The value to assign to the snapshot_id property of this DBParameters.
        :type snapshot_id: int

        :param is_changed:
            The value to assign to the is_changed property of this DBParameters.
        :type is_changed: str

        :param is_default:
            The value to assign to the is_default property of this DBParameters.
        :type is_default: str

        """
        self.swagger_types = {
            'metric_name': 'str',
            'time_collected': 'datetime',
            'instance_number': 'int',
            'parameter_name': 'str',
            'parameter_value': 'str',
            'snapshot_id': 'int',
            'is_changed': 'str',
            'is_default': 'str'
        }

        self.attribute_map = {
            'metric_name': 'metricName',
            'time_collected': 'timeCollected',
            'instance_number': 'instanceNumber',
            'parameter_name': 'parameterName',
            'parameter_value': 'parameterValue',
            'snapshot_id': 'snapshotId',
            'is_changed': 'isChanged',
            'is_default': 'isDefault'
        }

        self._metric_name = None
        self._time_collected = None
        self._instance_number = None
        self._parameter_name = None
        self._parameter_value = None
        self._snapshot_id = None
        self._is_changed = None
        self._is_default = None
        self._metric_name = 'DB_PARAMETERS'

    @property
    def instance_number(self):
        """
        **[Required]** Gets the instance_number of this DBParameters.
        Database instance number.


        :return: The instance_number of this DBParameters.
        :rtype: int
        """
        return self._instance_number

    @instance_number.setter
    def instance_number(self, instance_number):
        """
        Sets the instance_number of this DBParameters.
        Database instance number.


        :param instance_number: The instance_number of this DBParameters.
        :type: int
        """
        self._instance_number = instance_number

    @property
    def parameter_name(self):
        """
        **[Required]** Gets the parameter_name of this DBParameters.
        Database parameter name.


        :return: The parameter_name of this DBParameters.
        :rtype: str
        """
        return self._parameter_name

    @parameter_name.setter
    def parameter_name(self, parameter_name):
        """
        Sets the parameter_name of this DBParameters.
        Database parameter name.


        :param parameter_name: The parameter_name of this DBParameters.
        :type: str
        """
        self._parameter_name = parameter_name

    @property
    def parameter_value(self):
        """
        **[Required]** Gets the parameter_value of this DBParameters.
        Database parameter value.


        :return: The parameter_value of this DBParameters.
        :rtype: str
        """
        return self._parameter_value

    @parameter_value.setter
    def parameter_value(self, parameter_value):
        """
        Sets the parameter_value of this DBParameters.
        Database parameter value.


        :param parameter_value: The parameter_value of this DBParameters.
        :type: str
        """
        self._parameter_value = parameter_value

    @property
    def snapshot_id(self):
        """
        Gets the snapshot_id of this DBParameters.
        AWR snapshot id for the parameter value


        :return: The snapshot_id of this DBParameters.
        :rtype: int
        """
        return self._snapshot_id

    @snapshot_id.setter
    def snapshot_id(self, snapshot_id):
        """
        Sets the snapshot_id of this DBParameters.
        AWR snapshot id for the parameter value


        :param snapshot_id: The snapshot_id of this DBParameters.
        :type: int
        """
        self._snapshot_id = snapshot_id

    @property
    def is_changed(self):
        """
        Gets the is_changed of this DBParameters.
        Indicates whether the parameter's value changed in given snapshot or not.


        :return: The is_changed of this DBParameters.
        :rtype: str
        """
        return self._is_changed

    @is_changed.setter
    def is_changed(self, is_changed):
        """
        Sets the is_changed of this DBParameters.
        Indicates whether the parameter's value changed in given snapshot or not.


        :param is_changed: The is_changed of this DBParameters.
        :type: str
        """
        self._is_changed = is_changed

    @property
    def is_default(self):
        """
        Gets the is_default of this DBParameters.
        Indicates whether this value is the default value or not.


        :return: The is_default of this DBParameters.
        :rtype: str
        """
        return self._is_default

    @is_default.setter
    def is_default(self, is_default):
        """
        Sets the is_default of this DBParameters.
        Indicates whether this value is the default value or not.


        :param is_default: The is_default of this DBParameters.
        :type: str
        """
        self._is_default = is_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
