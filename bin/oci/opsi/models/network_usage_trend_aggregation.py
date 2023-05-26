# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class NetworkUsageTrendAggregation(object):
    """
    Usage data per network interface.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new NetworkUsageTrendAggregation object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param interface_name:
            The value to assign to the interface_name property of this NetworkUsageTrendAggregation.
        :type interface_name: str

        :param ip_address:
            The value to assign to the ip_address property of this NetworkUsageTrendAggregation.
        :type ip_address: str

        :param mac_address:
            The value to assign to the mac_address property of this NetworkUsageTrendAggregation.
        :type mac_address: str

        :param usage_data:
            The value to assign to the usage_data property of this NetworkUsageTrendAggregation.
        :type usage_data: list[oci.opsi.models.NetworkUsageTrend]

        """
        self.swagger_types = {
            'interface_name': 'str',
            'ip_address': 'str',
            'mac_address': 'str',
            'usage_data': 'list[NetworkUsageTrend]'
        }

        self.attribute_map = {
            'interface_name': 'interfaceName',
            'ip_address': 'ipAddress',
            'mac_address': 'macAddress',
            'usage_data': 'usageData'
        }

        self._interface_name = None
        self._ip_address = None
        self._mac_address = None
        self._usage_data = None

    @property
    def interface_name(self):
        """
        **[Required]** Gets the interface_name of this NetworkUsageTrendAggregation.
        Name of interface.


        :return: The interface_name of this NetworkUsageTrendAggregation.
        :rtype: str
        """
        return self._interface_name

    @interface_name.setter
    def interface_name(self, interface_name):
        """
        Sets the interface_name of this NetworkUsageTrendAggregation.
        Name of interface.


        :param interface_name: The interface_name of this NetworkUsageTrendAggregation.
        :type: str
        """
        self._interface_name = interface_name

    @property
    def ip_address(self):
        """
        **[Required]** Gets the ip_address of this NetworkUsageTrendAggregation.
        Address that is connected to a computer network that uses the Internet Protocol for communication.


        :return: The ip_address of this NetworkUsageTrendAggregation.
        :rtype: str
        """
        return self._ip_address

    @ip_address.setter
    def ip_address(self, ip_address):
        """
        Sets the ip_address of this NetworkUsageTrendAggregation.
        Address that is connected to a computer network that uses the Internet Protocol for communication.


        :param ip_address: The ip_address of this NetworkUsageTrendAggregation.
        :type: str
        """
        self._ip_address = ip_address

    @property
    def mac_address(self):
        """
        **[Required]** Gets the mac_address of this NetworkUsageTrendAggregation.
        Unique identifier assigned to a network interface.


        :return: The mac_address of this NetworkUsageTrendAggregation.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this NetworkUsageTrendAggregation.
        Unique identifier assigned to a network interface.


        :param mac_address: The mac_address of this NetworkUsageTrendAggregation.
        :type: str
        """
        self._mac_address = mac_address

    @property
    def usage_data(self):
        """
        **[Required]** Gets the usage_data of this NetworkUsageTrendAggregation.
        List of usage data samples for a network interface.


        :return: The usage_data of this NetworkUsageTrendAggregation.
        :rtype: list[oci.opsi.models.NetworkUsageTrend]
        """
        return self._usage_data

    @usage_data.setter
    def usage_data(self, usage_data):
        """
        Sets the usage_data of this NetworkUsageTrendAggregation.
        List of usage data samples for a network interface.


        :param usage_data: The usage_data of this NetworkUsageTrendAggregation.
        :type: list[oci.opsi.models.NetworkUsageTrend]
        """
        self._usage_data = usage_data

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
