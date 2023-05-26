# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyTrustedUserAgentTrustedFactors(object):
    """
    Trusted 2FA Factors
    """

    #: A constant which can be used with the category property of a MyTrustedUserAgentTrustedFactors.
    #: This constant has a value of "SAML"
    CATEGORY_SAML = "SAML"

    #: A constant which can be used with the category property of a MyTrustedUserAgentTrustedFactors.
    #: This constant has a value of "LOCAL"
    CATEGORY_LOCAL = "LOCAL"

    #: A constant which can be used with the category property of a MyTrustedUserAgentTrustedFactors.
    #: This constant has a value of "SOCIAL"
    CATEGORY_SOCIAL = "SOCIAL"

    #: A constant which can be used with the category property of a MyTrustedUserAgentTrustedFactors.
    #: This constant has a value of "X509"
    CATEGORY_X509 = "X509"

    #: A constant which can be used with the category property of a MyTrustedUserAgentTrustedFactors.
    #: This constant has a value of "THIRDPARTY"
    CATEGORY_THIRDPARTY = "THIRDPARTY"

    def __init__(self, **kwargs):
        """
        Initializes a new MyTrustedUserAgentTrustedFactors object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this MyTrustedUserAgentTrustedFactors.
        :type type: str

        :param category:
            The value to assign to the category property of this MyTrustedUserAgentTrustedFactors.
            Allowed values for this property are: "SAML", "LOCAL", "SOCIAL", "X509", "THIRDPARTY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type category: str

        :param creation_time:
            The value to assign to the creation_time property of this MyTrustedUserAgentTrustedFactors.
        :type creation_time: str

        """
        self.swagger_types = {
            'type': 'str',
            'category': 'str',
            'creation_time': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'category': 'category',
            'creation_time': 'creationTime'
        }

        self._type = None
        self._category = None
        self._creation_time = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MyTrustedUserAgentTrustedFactors.
        Trusted Factor

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The type of this MyTrustedUserAgentTrustedFactors.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MyTrustedUserAgentTrustedFactors.
        Trusted Factor

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this MyTrustedUserAgentTrustedFactors.
        :type: str
        """
        self._type = type

    @property
    def category(self):
        """
        Gets the category of this MyTrustedUserAgentTrustedFactors.
        Trusted Factor Type. Local, X509, SAML SOCIAL

        **Added In:** 2111190457

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none

        Allowed values for this property are: "SAML", "LOCAL", "SOCIAL", "X509", "THIRDPARTY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The category of this MyTrustedUserAgentTrustedFactors.
        :rtype: str
        """
        return self._category

    @category.setter
    def category(self, category):
        """
        Sets the category of this MyTrustedUserAgentTrustedFactors.
        Trusted Factor Type. Local, X509, SAML SOCIAL

        **Added In:** 2111190457

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param category: The category of this MyTrustedUserAgentTrustedFactors.
        :type: str
        """
        allowed_values = ["SAML", "LOCAL", "SOCIAL", "X509", "THIRDPARTY"]
        if not value_allowed_none_or_none_sentinel(category, allowed_values):
            category = 'UNKNOWN_ENUM_VALUE'
        self._category = category

    @property
    def creation_time(self):
        """
        **[Required]** Gets the creation_time of this MyTrustedUserAgentTrustedFactors.
        trust factor creation time

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: dateTime
         - uniqueness: none


        :return: The creation_time of this MyTrustedUserAgentTrustedFactors.
        :rtype: str
        """
        return self._creation_time

    @creation_time.setter
    def creation_time(self, creation_time):
        """
        Sets the creation_time of this MyTrustedUserAgentTrustedFactors.
        trust factor creation time

        **Added In:** 19.2.1

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: dateTime
         - uniqueness: none


        :param creation_time: The creation_time of this MyTrustedUserAgentTrustedFactors.
        :type: str
        """
        self._creation_time = creation_time

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
