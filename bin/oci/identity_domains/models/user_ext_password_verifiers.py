# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserExtPasswordVerifiers(object):
    """
    Password Verifiers for DB User.

    **Added In:** 18.2.2

    **SCIM++ Properties:**
    - idcsCompositeKey: [type]
    - idcsSearchable: true
    - multiValued: true
    - mutability: readOnly
    - required: false
    - returned: request
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UserExtPasswordVerifiers object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param type:
            The value to assign to the type property of this UserExtPasswordVerifiers.
        :type type: str

        :param value:
            The value to assign to the value property of this UserExtPasswordVerifiers.
        :type value: str

        """
        self.swagger_types = {
            'type': 'str',
            'value': 'str'
        }

        self.attribute_map = {
            'type': 'type',
            'value': 'value'
        }

        self._type = None
        self._value = None

    @property
    def type(self):
        """
        **[Required]** Gets the type of this UserExtPasswordVerifiers.
        Type of database password verifier (for example, MR-SHA512 or SSHA).

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The type of this UserExtPasswordVerifiers.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this UserExtPasswordVerifiers.
        Type of database password verifier (for example, MR-SHA512 or SSHA).

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: false
         - idcsSearchable: true
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param type: The type of this UserExtPasswordVerifiers.
        :type: str
        """
        self._type = type

    @property
    def value(self):
        """
        **[Required]** Gets the value of this UserExtPasswordVerifiers.
        Hash value of database password verifier.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :return: The value of this UserExtPasswordVerifiers.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """
        Sets the value of this UserExtPasswordVerifiers.
        Hash value of database password verifier.

        **Added In:** 18.2.2

        **SCIM++ Properties:**
         - caseExact: true
         - idcsSearchable: false
         - idcsSensitive: none
         - multiValued: false
         - mutability: readOnly
         - required: true
         - returned: default
         - type: string
         - uniqueness: none


        :param value: The value of this UserExtPasswordVerifiers.
        :type: str
        """
        self._value = value

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
