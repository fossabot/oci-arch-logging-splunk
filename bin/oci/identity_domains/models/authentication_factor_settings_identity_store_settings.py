# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsIdentityStoreSettings(object):
    """
    Settings related to the use of a user's profile details from the identity store

    **SCIM++ Properties:**
    - idcsSearchable: false
    - multiValued: false
    - mutability: readWrite
    - required: false
    - returned: default
    - type: complex
    - uniqueness: none
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsIdentityStoreSettings object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param mobile_number_enabled:
            The value to assign to the mobile_number_enabled property of this AuthenticationFactorSettingsIdentityStoreSettings.
        :type mobile_number_enabled: bool

        :param mobile_number_update_enabled:
            The value to assign to the mobile_number_update_enabled property of this AuthenticationFactorSettingsIdentityStoreSettings.
        :type mobile_number_update_enabled: bool

        """
        self.swagger_types = {
            'mobile_number_enabled': 'bool',
            'mobile_number_update_enabled': 'bool'
        }

        self.attribute_map = {
            'mobile_number_enabled': 'mobileNumberEnabled',
            'mobile_number_update_enabled': 'mobileNumberUpdateEnabled'
        }

        self._mobile_number_enabled = None
        self._mobile_number_update_enabled = None

    @property
    def mobile_number_enabled(self):
        """
        Gets the mobile_number_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        If true, indicates that Multi-Factor Authentication should use the mobile number in the identity store

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The mobile_number_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        :rtype: bool
        """
        return self._mobile_number_enabled

    @mobile_number_enabled.setter
    def mobile_number_enabled(self, mobile_number_enabled):
        """
        Sets the mobile_number_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        If true, indicates that Multi-Factor Authentication should use the mobile number in the identity store

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param mobile_number_enabled: The mobile_number_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        :type: bool
        """
        self._mobile_number_enabled = mobile_number_enabled

    @property
    def mobile_number_update_enabled(self):
        """
        Gets the mobile_number_update_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        If true, indicates that the user can update the mobile number in the user's Multi-Factor Authentication profile

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :return: The mobile_number_update_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        :rtype: bool
        """
        return self._mobile_number_update_enabled

    @mobile_number_update_enabled.setter
    def mobile_number_update_enabled(self, mobile_number_update_enabled):
        """
        Sets the mobile_number_update_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        If true, indicates that the user can update the mobile number in the user's Multi-Factor Authentication profile

        **SCIM++ Properties:**
         - idcsSearchable: false
         - multiValued: false
         - mutability: readWrite
         - required: false
         - returned: default
         - type: boolean
         - uniqueness: none


        :param mobile_number_update_enabled: The mobile_number_update_enabled of this AuthenticationFactorSettingsIdentityStoreSettings.
        :type: bool
        """
        self._mobile_number_update_enabled = mobile_number_update_enabled

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
