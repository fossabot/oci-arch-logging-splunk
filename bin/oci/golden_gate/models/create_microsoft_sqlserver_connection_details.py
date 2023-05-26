# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_connection_details import CreateConnectionDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateMicrosoftSqlserverConnectionDetails(CreateConnectionDetails):
    """
    The information about a new Microsoft SQL Server Connection.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateMicrosoftSqlserverConnectionDetails object with values from keyword arguments. The default value of the :py:attr:`~oci.golden_gate.models.CreateMicrosoftSqlserverConnectionDetails.connection_type` attribute
        of this class is ``MICROSOFT_SQLSERVER`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param connection_type:
            The value to assign to the connection_type property of this CreateMicrosoftSqlserverConnectionDetails.
            Allowed values for this property are: "GOLDENGATE", "KAFKA", "KAFKA_SCHEMA_REGISTRY", "MYSQL", "JAVA_MESSAGE_SERVICE", "MICROSOFT_SQLSERVER", "OCI_OBJECT_STORAGE", "ORACLE", "AZURE_DATA_LAKE_STORAGE", "POSTGRESQL", "AZURE_SYNAPSE_ANALYTICS", "SNOWFLAKE", "AMAZON_S3", "HDFS", "ORACLE_NOSQL", "MONGODB"
        :type connection_type: str

        :param display_name:
            The value to assign to the display_name property of this CreateMicrosoftSqlserverConnectionDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this CreateMicrosoftSqlserverConnectionDetails.
        :type description: str

        :param compartment_id:
            The value to assign to the compartment_id property of this CreateMicrosoftSqlserverConnectionDetails.
        :type compartment_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateMicrosoftSqlserverConnectionDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateMicrosoftSqlserverConnectionDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param vault_id:
            The value to assign to the vault_id property of this CreateMicrosoftSqlserverConnectionDetails.
        :type vault_id: str

        :param key_id:
            The value to assign to the key_id property of this CreateMicrosoftSqlserverConnectionDetails.
        :type key_id: str

        :param subnet_id:
            The value to assign to the subnet_id property of this CreateMicrosoftSqlserverConnectionDetails.
        :type subnet_id: str

        :param nsg_ids:
            The value to assign to the nsg_ids property of this CreateMicrosoftSqlserverConnectionDetails.
        :type nsg_ids: list[str]

        :param technology_type:
            The value to assign to the technology_type property of this CreateMicrosoftSqlserverConnectionDetails.
        :type technology_type: str

        :param database_name:
            The value to assign to the database_name property of this CreateMicrosoftSqlserverConnectionDetails.
        :type database_name: str

        :param host:
            The value to assign to the host property of this CreateMicrosoftSqlserverConnectionDetails.
        :type host: str

        :param port:
            The value to assign to the port property of this CreateMicrosoftSqlserverConnectionDetails.
        :type port: int

        :param username:
            The value to assign to the username property of this CreateMicrosoftSqlserverConnectionDetails.
        :type username: str

        :param password:
            The value to assign to the password property of this CreateMicrosoftSqlserverConnectionDetails.
        :type password: str

        :param additional_attributes:
            The value to assign to the additional_attributes property of this CreateMicrosoftSqlserverConnectionDetails.
        :type additional_attributes: list[oci.golden_gate.models.NameValuePair]

        :param security_protocol:
            The value to assign to the security_protocol property of this CreateMicrosoftSqlserverConnectionDetails.
        :type security_protocol: str

        :param ssl_ca:
            The value to assign to the ssl_ca property of this CreateMicrosoftSqlserverConnectionDetails.
        :type ssl_ca: str

        :param should_validate_server_certificate:
            The value to assign to the should_validate_server_certificate property of this CreateMicrosoftSqlserverConnectionDetails.
        :type should_validate_server_certificate: bool

        :param private_ip:
            The value to assign to the private_ip property of this CreateMicrosoftSqlserverConnectionDetails.
        :type private_ip: str

        """
        self.swagger_types = {
            'connection_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'compartment_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'vault_id': 'str',
            'key_id': 'str',
            'subnet_id': 'str',
            'nsg_ids': 'list[str]',
            'technology_type': 'str',
            'database_name': 'str',
            'host': 'str',
            'port': 'int',
            'username': 'str',
            'password': 'str',
            'additional_attributes': 'list[NameValuePair]',
            'security_protocol': 'str',
            'ssl_ca': 'str',
            'should_validate_server_certificate': 'bool',
            'private_ip': 'str'
        }

        self.attribute_map = {
            'connection_type': 'connectionType',
            'display_name': 'displayName',
            'description': 'description',
            'compartment_id': 'compartmentId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'vault_id': 'vaultId',
            'key_id': 'keyId',
            'subnet_id': 'subnetId',
            'nsg_ids': 'nsgIds',
            'technology_type': 'technologyType',
            'database_name': 'databaseName',
            'host': 'host',
            'port': 'port',
            'username': 'username',
            'password': 'password',
            'additional_attributes': 'additionalAttributes',
            'security_protocol': 'securityProtocol',
            'ssl_ca': 'sslCa',
            'should_validate_server_certificate': 'shouldValidateServerCertificate',
            'private_ip': 'privateIp'
        }

        self._connection_type = None
        self._display_name = None
        self._description = None
        self._compartment_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._vault_id = None
        self._key_id = None
        self._subnet_id = None
        self._nsg_ids = None
        self._technology_type = None
        self._database_name = None
        self._host = None
        self._port = None
        self._username = None
        self._password = None
        self._additional_attributes = None
        self._security_protocol = None
        self._ssl_ca = None
        self._should_validate_server_certificate = None
        self._private_ip = None
        self._connection_type = 'MICROSOFT_SQLSERVER'

    @property
    def technology_type(self):
        """
        **[Required]** Gets the technology_type of this CreateMicrosoftSqlserverConnectionDetails.
        The Microsoft SQL Server technology type.


        :return: The technology_type of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._technology_type

    @technology_type.setter
    def technology_type(self, technology_type):
        """
        Sets the technology_type of this CreateMicrosoftSqlserverConnectionDetails.
        The Microsoft SQL Server technology type.


        :param technology_type: The technology_type of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._technology_type = technology_type

    @property
    def database_name(self):
        """
        **[Required]** Gets the database_name of this CreateMicrosoftSqlserverConnectionDetails.
        The name of the database.


        :return: The database_name of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._database_name

    @database_name.setter
    def database_name(self, database_name):
        """
        Sets the database_name of this CreateMicrosoftSqlserverConnectionDetails.
        The name of the database.


        :param database_name: The database_name of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._database_name = database_name

    @property
    def host(self):
        """
        **[Required]** Gets the host of this CreateMicrosoftSqlserverConnectionDetails.
        The name or address of a host.


        :return: The host of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._host

    @host.setter
    def host(self, host):
        """
        Sets the host of this CreateMicrosoftSqlserverConnectionDetails.
        The name or address of a host.


        :param host: The host of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._host = host

    @property
    def port(self):
        """
        **[Required]** Gets the port of this CreateMicrosoftSqlserverConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :return: The port of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: int
        """
        return self._port

    @port.setter
    def port(self, port):
        """
        Sets the port of this CreateMicrosoftSqlserverConnectionDetails.
        The port of an endpoint usually specified for a connection.


        :param port: The port of this CreateMicrosoftSqlserverConnectionDetails.
        :type: int
        """
        self._port = port

    @property
    def username(self):
        """
        **[Required]** Gets the username of this CreateMicrosoftSqlserverConnectionDetails.
        The username Oracle GoldenGate uses to connect to the Microsoft SQL Server.
        This username must already exist and be available by the Microsoft SQL Server to be connected to.


        :return: The username of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._username

    @username.setter
    def username(self, username):
        """
        Sets the username of this CreateMicrosoftSqlserverConnectionDetails.
        The username Oracle GoldenGate uses to connect to the Microsoft SQL Server.
        This username must already exist and be available by the Microsoft SQL Server to be connected to.


        :param username: The username of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._username = username

    @property
    def password(self):
        """
        **[Required]** Gets the password of this CreateMicrosoftSqlserverConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.


        :return: The password of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._password

    @password.setter
    def password(self, password):
        """
        Sets the password of this CreateMicrosoftSqlserverConnectionDetails.
        The password Oracle GoldenGate uses to connect the associated Microsoft SQL Server.


        :param password: The password of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._password = password

    @property
    def additional_attributes(self):
        """
        Gets the additional_attributes of this CreateMicrosoftSqlserverConnectionDetails.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :return: The additional_attributes of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: list[oci.golden_gate.models.NameValuePair]
        """
        return self._additional_attributes

    @additional_attributes.setter
    def additional_attributes(self, additional_attributes):
        """
        Sets the additional_attributes of this CreateMicrosoftSqlserverConnectionDetails.
        An array of name-value pair attribute entries.
        Used as additional parameters in connection string.


        :param additional_attributes: The additional_attributes of this CreateMicrosoftSqlserverConnectionDetails.
        :type: list[oci.golden_gate.models.NameValuePair]
        """
        self._additional_attributes = additional_attributes

    @property
    def security_protocol(self):
        """
        **[Required]** Gets the security_protocol of this CreateMicrosoftSqlserverConnectionDetails.
        Security Type for Microsoft SQL Server.


        :return: The security_protocol of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._security_protocol

    @security_protocol.setter
    def security_protocol(self, security_protocol):
        """
        Sets the security_protocol of this CreateMicrosoftSqlserverConnectionDetails.
        Security Type for Microsoft SQL Server.


        :param security_protocol: The security_protocol of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._security_protocol = security_protocol

    @property
    def ssl_ca(self):
        """
        Gets the ssl_ca of this CreateMicrosoftSqlserverConnectionDetails.
        Database Certificate - The base64 encoded content of pem file
        containing the server public key (for 1-way SSL).


        :return: The ssl_ca of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._ssl_ca

    @ssl_ca.setter
    def ssl_ca(self, ssl_ca):
        """
        Sets the ssl_ca of this CreateMicrosoftSqlserverConnectionDetails.
        Database Certificate - The base64 encoded content of pem file
        containing the server public key (for 1-way SSL).


        :param ssl_ca: The ssl_ca of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._ssl_ca = ssl_ca

    @property
    def should_validate_server_certificate(self):
        """
        Gets the should_validate_server_certificate of this CreateMicrosoftSqlserverConnectionDetails.
        If set to true, the driver validates the certificate that is sent by the database server.


        :return: The should_validate_server_certificate of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: bool
        """
        return self._should_validate_server_certificate

    @should_validate_server_certificate.setter
    def should_validate_server_certificate(self, should_validate_server_certificate):
        """
        Sets the should_validate_server_certificate of this CreateMicrosoftSqlserverConnectionDetails.
        If set to true, the driver validates the certificate that is sent by the database server.


        :param should_validate_server_certificate: The should_validate_server_certificate of this CreateMicrosoftSqlserverConnectionDetails.
        :type: bool
        """
        self._should_validate_server_certificate = should_validate_server_certificate

    @property
    def private_ip(self):
        """
        Gets the private_ip of this CreateMicrosoftSqlserverConnectionDetails.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :return: The private_ip of this CreateMicrosoftSqlserverConnectionDetails.
        :rtype: str
        """
        return self._private_ip

    @private_ip.setter
    def private_ip(self, private_ip):
        """
        Sets the private_ip of this CreateMicrosoftSqlserverConnectionDetails.
        The private IP address of the connection's endpoint in the customer's VCN, typically a
        database endpoint or a big data endpoint (e.g. Kafka bootstrap server).
        In case the privateIp is provided, the subnetId must also be provided.
        In case the privateIp (and the subnetId) is not provided it is assumed the datasource is publicly accessible.
        In case the connection is accessible only privately, the lack of privateIp will result in not being able to access the connection.


        :param private_ip: The private_ip of this CreateMicrosoftSqlserverConnectionDetails.
        :type: str
        """
        self._private_ip = private_ip

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
