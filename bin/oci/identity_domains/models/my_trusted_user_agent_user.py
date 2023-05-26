# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyTrustedUserAgentUser(object):
    """
    user for whom the trust-token was issued

    **SCIM++ Properties:**
    - caseExact: false
    - idcsSearchable: true
    - multiValued: false
    - mutability: readWrite
    - required: true
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MyTrustedUserAgentUser object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param value:
            The value to assign to the value property of this MyTrustedUserAgentUser.
        :type value: str

        :param ref:
            The value to assign to the ref property of this MyTrustedUserAgentUser.
        :type ref: str

        :param display:
            The value to assign to the display property of this MyTrustedUserAgentUser.
        :type display: str

        :param ocid:
            The value to assign to the ocid property of this MyTrustedUserAgentUser.
        :type ocid: str

        """
        self.swagger_types = {
            'value': 'str',
            'ref': 'str',
            'display': 'str',
            'ocid': 'str'
        }

        self.attribute_map = {
            'value': 'value',
            'ref': '$ref',
            'display': 'display',
            'ocid': 'ocid'
        }

        self._value = None
        self._ref = None
        self._display = None
        self._ocid = None

    @property
    def value(self):
        """
        **[Required]** Gets the value of this MyTrustedUserAgentUser.
        The SCIM ID of the user for whom the trust-token was issued.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this MyTrustedUserAgentUser.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this MyTrustedUserAgentUser.
        The SCIM ID of the user for whom the trust-token was issued.

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this MyTrustedUserAgentUser.
        :type: str
        """
        self._value = value

    @property
    def ref(self):
        """
        **[Required]** Gets the ref of this MyTrustedUserAgentUser.
        Full URI to the user for whom the trust-token was issued.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: reference
         - uniqueness: none


        :return: The ref of this MyTrustedUserAgentUser.
        :rtype: str
        """
        return self._ref

    @ref.setter
    def ref(self, ref):
        """
        Sets the ref of this MyTrustedUserAgentUser.
        Full URI to the user for whom the trust-token was issued.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: reference
         - uniqueness: none


        :param ref: The ref of this MyTrustedUserAgentUser.
        :type: str
        """
        self._ref = ref

    @property
    def display(self):
        """
        Gets the display of this MyTrustedUserAgentUser.
        Friendly name of the User to be used for purposes of display.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :return: The display of this MyTrustedUserAgentUser.
        :rtype: str
        """
        return self._display

    @display.setter
    def display(self, display):
        """
        Sets the display of this MyTrustedUserAgentUser.
        Friendly name of the User to be used for purposes of display.

        **SCIM++ Properties:**
         - caseExact: false
         - multiValued: false
         - mutability: readOnly
         - required: false
         - returned: default
         - type: string
         - uniqueness: none


        :param display: The display of this MyTrustedUserAgentUser.
        :type: str
        """
        self._display = display

    @property
    def ocid(self):
        """
        Gets the ocid of this MyTrustedUserAgentUser.
        The OCID of the user

        **Added In:** 2105091740

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :return: The ocid of this MyTrustedUserAgentUser.
        :rtype: str
        """
        return self._ocid

    @ocid.setter
    def ocid(self, ocid):
        """
        Sets the ocid of this MyTrustedUserAgentUser.
        The OCID of the user

        **Added In:** 2105091740

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: true
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: always
         - type: string
         - uniqueness: none


        :param ocid: The ocid of this MyTrustedUserAgentUser.
        :type: str
        """
        self._ocid = ocid

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
