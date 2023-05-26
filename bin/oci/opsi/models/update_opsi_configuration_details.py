# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateOpsiConfigurationDetails(object):
    """
    Information to be updated in OPSI configuration resource.
    """

    #: A constant which can be used with the opsi_config_type property of a UpdateOpsiConfigurationDetails.
    #: This constant has a value of "UX_CONFIGURATION"
    OPSI_CONFIG_TYPE_UX_CONFIGURATION = "UX_CONFIGURATION"

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateOpsiConfigurationDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.opsi.models.UpdateOpsiUxConfigurationDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param opsi_config_type:
            The value to assign to the opsi_config_type property of this UpdateOpsiConfigurationDetails.
            Allowed values for this property are: "UX_CONFIGURATION"
        :type opsi_config_type: str

        :param display_name:
            The value to assign to the display_name property of this UpdateOpsiConfigurationDetails.
        :type display_name: str

        :param description:
            The value to assign to the description property of this UpdateOpsiConfigurationDetails.
        :type description: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateOpsiConfigurationDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateOpsiConfigurationDetails.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this UpdateOpsiConfigurationDetails.
        :type system_tags: dict(str, dict(str, object))

        :param config_items:
            The value to assign to the config_items property of this UpdateOpsiConfigurationDetails.
        :type config_items: list[oci.opsi.models.UpdateConfigurationItemDetails]

        """
        self.swagger_types = {
            'opsi_config_type': 'str',
            'display_name': 'str',
            'description': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))',
            'config_items': 'list[UpdateConfigurationItemDetails]'
        }

        self.attribute_map = {
            'opsi_config_type': 'opsiConfigType',
            'display_name': 'displayName',
            'description': 'description',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags',
            'config_items': 'configItems'
        }

        self._opsi_config_type = None
        self._display_name = None
        self._description = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None
        self._config_items = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['opsiConfigType']

        if type == 'UX_CONFIGURATION':
            return 'UpdateOpsiUxConfigurationDetails'
        else:
            return 'UpdateOpsiConfigurationDetails'

    @property
    def opsi_config_type(self):
        """
        **[Required]** Gets the opsi_config_type of this UpdateOpsiConfigurationDetails.
        OPSI configuration type.

        Allowed values for this property are: "UX_CONFIGURATION"


        :return: The opsi_config_type of this UpdateOpsiConfigurationDetails.
        :rtype: str
        """
        return self._opsi_config_type

    @opsi_config_type.setter
    def opsi_config_type(self, opsi_config_type):
        """
        Sets the opsi_config_type of this UpdateOpsiConfigurationDetails.
        OPSI configuration type.


        :param opsi_config_type: The opsi_config_type of this UpdateOpsiConfigurationDetails.
        :type: str
        """
        allowed_values = ["UX_CONFIGURATION"]
        if not value_allowed_none_or_none_sentinel(opsi_config_type, allowed_values):
            raise ValueError(
                "Invalid value for `opsi_config_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._opsi_config_type = opsi_config_type

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateOpsiConfigurationDetails.
        User-friendly display name for the OPSI configuration. The name does not have to be unique.


        :return: The display_name of this UpdateOpsiConfigurationDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateOpsiConfigurationDetails.
        User-friendly display name for the OPSI configuration. The name does not have to be unique.


        :param display_name: The display_name of this UpdateOpsiConfigurationDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        Gets the description of this UpdateOpsiConfigurationDetails.
        Description of OPSI configuration.


        :return: The description of this UpdateOpsiConfigurationDetails.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UpdateOpsiConfigurationDetails.
        Description of OPSI configuration.


        :param description: The description of this UpdateOpsiConfigurationDetails.
        :type: str
        """
        self._description = description

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateOpsiConfigurationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateOpsiConfigurationDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateOpsiConfigurationDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateOpsiConfigurationDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateOpsiConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateOpsiConfigurationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateOpsiConfigurationDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateOpsiConfigurationDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this UpdateOpsiConfigurationDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this UpdateOpsiConfigurationDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this UpdateOpsiConfigurationDetails.
        System tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this UpdateOpsiConfigurationDetails.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    @property
    def config_items(self):
        """
        Gets the config_items of this UpdateOpsiConfigurationDetails.
        Array of configuration items with custom values. All and only configuration items requiring custom values should be part of this array.
        This array overwrites the existing custom configuration items array for this resource.


        :return: The config_items of this UpdateOpsiConfigurationDetails.
        :rtype: list[oci.opsi.models.UpdateConfigurationItemDetails]
        """
        return self._config_items

    @config_items.setter
    def config_items(self, config_items):
        """
        Sets the config_items of this UpdateOpsiConfigurationDetails.
        Array of configuration items with custom values. All and only configuration items requiring custom values should be part of this array.
        This array overwrites the existing custom configuration items array for this resource.


        :param config_items: The config_items of this UpdateOpsiConfigurationDetails.
        :type: list[oci.opsi.models.UpdateConfigurationItemDetails]
        """
        self._config_items = config_items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
