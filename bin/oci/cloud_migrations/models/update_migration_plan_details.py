# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateMigrationPlanDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateMigrationPlanDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param display_name:
            The value to assign to the display_name property of this UpdateMigrationPlanDetails.
        :type display_name: str

        :param strategies:
            The value to assign to the strategies property of this UpdateMigrationPlanDetails.
        :type strategies: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]

        :param target_environments:
            The value to assign to the target_environments property of this UpdateMigrationPlanDetails.
        :type target_environments: list[oci.cloud_migrations.models.TargetEnvironment]

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateMigrationPlanDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateMigrationPlanDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'display_name': 'str',
            'strategies': 'list[ResourceAssessmentStrategy]',
            'target_environments': 'list[TargetEnvironment]',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'display_name': 'displayName',
            'strategies': 'strategies',
            'target_environments': 'targetEnvironments',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._display_name = None
        self._strategies = None
        self._target_environments = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def display_name(self):
        """
        Gets the display_name of this UpdateMigrationPlanDetails.
        Migration plan identifier


        :return: The display_name of this UpdateMigrationPlanDetails.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this UpdateMigrationPlanDetails.
        Migration plan identifier


        :param display_name: The display_name of this UpdateMigrationPlanDetails.
        :type: str
        """
        self._display_name = display_name

    @property
    def strategies(self):
        """
        Gets the strategies of this UpdateMigrationPlanDetails.
        List of strategies for the resources to be migrated.


        :return: The strategies of this UpdateMigrationPlanDetails.
        :rtype: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]
        """
        return self._strategies

    @strategies.setter
    def strategies(self, strategies):
        """
        Sets the strategies of this UpdateMigrationPlanDetails.
        List of strategies for the resources to be migrated.


        :param strategies: The strategies of this UpdateMigrationPlanDetails.
        :type: list[oci.cloud_migrations.models.ResourceAssessmentStrategy]
        """
        self._strategies = strategies

    @property
    def target_environments(self):
        """
        Gets the target_environments of this UpdateMigrationPlanDetails.
        List of target environments.


        :return: The target_environments of this UpdateMigrationPlanDetails.
        :rtype: list[oci.cloud_migrations.models.TargetEnvironment]
        """
        return self._target_environments

    @target_environments.setter
    def target_environments(self, target_environments):
        """
        Sets the target_environments of this UpdateMigrationPlanDetails.
        List of target environments.


        :param target_environments: The target_environments of this UpdateMigrationPlanDetails.
        :type: list[oci.cloud_migrations.models.TargetEnvironment]
        """
        self._target_environments = target_environments

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateMigrationPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateMigrationPlanDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateMigrationPlanDetails.
        Simple key-value pair that is applied without any predefined name, type or scope. It exists only for cross-compatibility.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateMigrationPlanDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateMigrationPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateMigrationPlanDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateMigrationPlanDetails.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateMigrationPlanDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
