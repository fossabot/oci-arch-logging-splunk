# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class DatabaseConnectionString(object):
    """
    The Oracle Database connection string.
    """

    #: A constant which can be used with the protocol property of a DatabaseConnectionString.
    #: This constant has a value of "TCP"
    PROTOCOL_TCP = "TCP"

    #: A constant which can be used with the protocol property of a DatabaseConnectionString.
    #: This constant has a value of "TCPS"
    PROTOCOL_TCPS = "TCPS"

    def __init__(self, **kwargs):
        """
        Initializes a new DatabaseConnectionString object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param hostname:
            The value to assign to the hostname property of this DatabaseConnectionString.
        :type hostname: str

        :param port:
            The value to assign to the port property of this DatabaseConnectionString.
        :type port: int

        :param service:
            The value to assign to the service property of this DatabaseConnectionString.
        :type service: str

        :param protocol:
            The value to assign to the protocol property of this DatabaseConnectionString.
            Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type protocol: str

        """
        self.swagger_types = {
            'hostname': 'str',
            'port': 'int',
            'service': 'str',
            'protocol': 'str'
        }

        self.attribute_map = {
            'hostname': 'hostname',
            'port': 'port',
            'service': 'service',
            'protocol': 'protocol'
        }

        self._hostname = None
        self._port = None
        self._service = None
        self._protocol = None

    @property
    def hostname(self):
        """
        **[Required]** Gets the hostname of this DatabaseConnectionString.
        The host name of the database.


        :return: The hostname of this DatabaseConnectionString.
        :rtype: str
        """
        return self._hostname

    @hostname.setter
    def hostname(self, hostname):
        """
        Sets the hostname of this DatabaseConnectionString.
        The host name of the database.


        :param hostname: The hostname of this DatabaseConnectionString.
        :type: str
        """
        self._hostname = hostname

    @property
    def port(self):
        """
        **[Required]** Gets the port of this DatabaseConnectionString.
        The port used to connect to the database.


        :return: The port of this DatabaseConnectionString.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this DatabaseConnectionString.
        The port used to connect to the database.


        :param port: The port of this DatabaseConnectionString.
        :type: int
        """
        self._port = port

    @property
    def service(self):
        """
        **[Required]** Gets the service of this DatabaseConnectionString.
        The name of the service alias used to connect to the database.


        :return: The service of this DatabaseConnectionString.
        :rtype: str
        """
        return self._service

    @service.setter
    def service(self, service):
        """
        Sets the service of this DatabaseConnectionString.
        The name of the service alias used to connect to the database.


        :param service: The service of this DatabaseConnectionString.
        :type: str
        """
        self._service = service

    @property
    def protocol(self):
        """
        **[Required]** Gets the protocol of this DatabaseConnectionString.
        The protocol used to connect to the database.

        Allowed values for this property are: "TCP", "TCPS", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The protocol of this DatabaseConnectionString.
        :rtype: str
        """
        return self._protocol

    @protocol.setter
    def protocol(self, protocol):
        """
        Sets the protocol of this DatabaseConnectionString.
        The protocol used to connect to the database.


        :param protocol: The protocol of this DatabaseConnectionString.
        :type: str
        """
        allowed_values = ["TCP", "TCPS"]
        if not value_allowed_none_or_none_sentinel(protocol, allowed_values):
            protocol = 'UNKNOWN_ENUM_VALUE'
        self._protocol = protocol

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
