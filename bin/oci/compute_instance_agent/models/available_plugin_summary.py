# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AvailablePluginSummary(object):
    """
    Describes where the plugin is supported
    """

    def __init__(self, **kwargs):
        """
        Initializes a new AvailablePluginSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param name:
            The value to assign to the name property of this AvailablePluginSummary.
        :type name: str

        :param summary:
            The value to assign to the summary property of this AvailablePluginSummary.
        :type summary: str

        :param is_supported:
            The value to assign to the is_supported property of this AvailablePluginSummary.
        :type is_supported: bool

        :param is_enabled_by_default:
            The value to assign to the is_enabled_by_default property of this AvailablePluginSummary.
        :type is_enabled_by_default: bool

        """
        self.swagger_types = {
            'name': 'str',
            'summary': 'str',
            'is_supported': 'bool',
            'is_enabled_by_default': 'bool'
        }

        self.attribute_map = {
            'name': 'name',
            'summary': 'summary',
            'is_supported': 'isSupported',
            'is_enabled_by_default': 'isEnabledByDefault'
        }

        self._name = None
        self._summary = None
        self._is_supported = None
        self._is_enabled_by_default = None

    @property
    def name(self):
        """
        **[Required]** Gets the name of this AvailablePluginSummary.
        The plugin name


        :return: The name of this AvailablePluginSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this AvailablePluginSummary.
        The plugin name


        :param name: The name of this AvailablePluginSummary.
        :type: str
        """
        self._name = name

    @property
    def summary(self):
        """
        Gets the summary of this AvailablePluginSummary.
        A brief description of the plugin functionality


        :return: The summary of this AvailablePluginSummary.
        :rtype: str
        """
        return self._summary

    @summary.setter
    def summary(self, summary):
        """
        Sets the summary of this AvailablePluginSummary.
        A brief description of the plugin functionality


        :param summary: The summary of this AvailablePluginSummary.
        :type: str
        """
        self._summary = summary

    @property
    def is_supported(self):
        """
        **[Required]** Gets the is_supported of this AvailablePluginSummary.
        Is the plugin supported or not


        :return: The is_supported of this AvailablePluginSummary.
        :rtype: bool
        """
        return self._is_supported

    @is_supported.setter
    def is_supported(self, is_supported):
        """
        Sets the is_supported of this AvailablePluginSummary.
        Is the plugin supported or not


        :param is_supported: The is_supported of this AvailablePluginSummary.
        :type: bool
        """
        self._is_supported = is_supported

    @property
    def is_enabled_by_default(self):
        """
        **[Required]** Gets the is_enabled_by_default of this AvailablePluginSummary.
        Is the plugin enabled or disabled by default


        :return: The is_enabled_by_default of this AvailablePluginSummary.
        :rtype: bool
        """
        return self._is_enabled_by_default

    @is_enabled_by_default.setter
    def is_enabled_by_default(self, is_enabled_by_default):
        """
        Sets the is_enabled_by_default of this AvailablePluginSummary.
        Is the plugin enabled or disabled by default


        :param is_enabled_by_default: The is_enabled_by_default of this AvailablePluginSummary.
        :type: bool
        """
        self._is_enabled_by_default = is_enabled_by_default

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
