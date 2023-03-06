# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .traffic_protocol_parameters import TrafficProtocolParameters
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IcmpTrafficProtocolParameters(TrafficProtocolParameters):
    """
    Defines the `ProtocolParameters` configuration for the `ICMP`__ protocol.

    __ https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml
    """

    def __init__(self, **kwargs):
        """
        Initializes a new IcmpTrafficProtocolParameters object with values from keyword arguments. The default value of the :py:attr:`~oci.vn_monitoring.models.IcmpTrafficProtocolParameters.type` attribute
        of this class is ``ICMP`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this IcmpTrafficProtocolParameters.
            Allowed values for this property are: "TCP", "UDP", "ICMP"
        :type type: str

        :param icmp_code:
            The value to assign to the icmp_code property of this IcmpTrafficProtocolParameters.
        :type icmp_code: int

        :param icmp_type:
            The value to assign to the icmp_type property of this IcmpTrafficProtocolParameters.
        :type icmp_type: int

        """
        self.swagger_types = {
            'type': 'str',
            'icmp_code': 'int',
            'icmp_type': 'int'
        }

        self.attribute_map = {
            'type': 'type',
            'icmp_code': 'icmpCode',
            'icmp_type': 'icmpType'
        }

        self._type = None
        self._icmp_code = None
        self._icmp_type = None
        self._type = 'ICMP'

    @property
    def icmp_code(self):
        """
        Gets the icmp_code of this IcmpTrafficProtocolParameters.
        The `ICMP`__ code.

        __ https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


        :return: The icmp_code of this IcmpTrafficProtocolParameters.
        :rtype: int
        """
        return self._icmp_code

    @icmp_code.setter
    def icmp_code(self, icmp_code):
        """
        Sets the icmp_code of this IcmpTrafficProtocolParameters.
        The `ICMP`__ code.

        __ https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


        :param icmp_code: The icmp_code of this IcmpTrafficProtocolParameters.
        :type: int
        """
        self._icmp_code = icmp_code

    @property
    def icmp_type(self):
        """
        **[Required]** Gets the icmp_type of this IcmpTrafficProtocolParameters.
        The `ICMP`__ type.

        __ https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


        :return: The icmp_type of this IcmpTrafficProtocolParameters.
        :rtype: int
        """
        return self._icmp_type

    @icmp_type.setter
    def icmp_type(self, icmp_type):
        """
        Sets the icmp_type of this IcmpTrafficProtocolParameters.
        The `ICMP`__ type.

        __ https://www.iana.org/assignments/icmp-parameters/icmp-parameters.xhtml


        :param icmp_type: The icmp_type of this IcmpTrafficProtocolParameters.
        :type: int
        """
        self._icmp_type = icmp_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
