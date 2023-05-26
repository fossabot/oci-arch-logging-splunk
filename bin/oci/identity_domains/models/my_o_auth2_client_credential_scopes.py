# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MyOAuth2ClientCredentialScopes(object):
    """
    Scopes
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MyOAuth2ClientCredentialScopes object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param audience:
            The value to assign to the audience property of this MyOAuth2ClientCredentialScopes.
        :type audience: str

        :param scope:
            The value to assign to the scope property of this MyOAuth2ClientCredentialScopes.
        :type scope: str

        """
        self.swagger_types = {
            'audience': 'str',
            'scope': 'str'
        }

        self.attribute_map = {
            'audience': 'audience',
            'scope': 'scope'
        }

        self._audience = None
        self._scope = None

    @property
    def audience(self):
        """
        **[Required]** Gets the audience of this MyOAuth2ClientCredentialScopes.
        Audience

        **SCIM++ Properties:**
         - caseExact: false
         - type: string
         - mutability: readWrite
         - required: true
         - returned: default


        :return: The audience of this MyOAuth2ClientCredentialScopes.
        :rtype: str
        """
        return self._audience

    @audience.setter
    def audience(self, audience):
        """
        Sets the audience of this MyOAuth2ClientCredentialScopes.
        Audience

        **SCIM++ Properties:**
         - caseExact: false
         - type: string
         - mutability: readWrite
         - required: true
         - returned: default


        :param audience: The audience of this MyOAuth2ClientCredentialScopes.
        :type: str
        """
        self._audience = audience

    @property
    def scope(self):
        """
        **[Required]** Gets the scope of this MyOAuth2ClientCredentialScopes.
        Scope

        **SCIM++ Properties:**
         - caseExact: false
         - idcsScimCompliant: false
         - type: string
         - mutability: readWrite
         - multiValued: false
         - required: true
         - returned: default


        :return: The scope of this MyOAuth2ClientCredentialScopes.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this MyOAuth2ClientCredentialScopes.
        Scope

        **SCIM++ Properties:**
         - caseExact: false
         - idcsScimCompliant: false
         - type: string
         - mutability: readWrite
         - multiValued: false
         - required: true
         - returned: default


        :param scope: The scope of this MyOAuth2ClientCredentialScopes.
        :type: str
        """
        self._scope = scope

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
