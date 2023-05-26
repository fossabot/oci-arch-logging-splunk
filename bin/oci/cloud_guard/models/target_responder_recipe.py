# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TargetResponderRecipe(object):
    """
    Details of Target ResponderRecipe
    """

    #: A constant which can be used with the owner property of a TargetResponderRecipe.
    #: This constant has a value of "CUSTOMER"
    OWNER_CUSTOMER = "CUSTOMER"

    #: A constant which can be used with the owner property of a TargetResponderRecipe.
    #: This constant has a value of "ORACLE"
    OWNER_ORACLE = "ORACLE"

    def __init__(self, **kwargs):
        """
        Initializes a new TargetResponderRecipe object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TargetResponderRecipe.
        :type id: str

        :param responder_recipe_id:
            The value to assign to the responder_recipe_id property of this TargetResponderRecipe.
        :type responder_recipe_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this TargetResponderRecipe.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this TargetResponderRecipe.
        :type display_name: str

        :param description:
            The value to assign to the description property of this TargetResponderRecipe.
        :type description: str

        :param owner:
            The value to assign to the owner property of this TargetResponderRecipe.
            Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type owner: str

        :param time_created:
            The value to assign to the time_created property of this TargetResponderRecipe.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this TargetResponderRecipe.
        :type time_updated: datetime

        :param responder_rules:
            The value to assign to the responder_rules property of this TargetResponderRecipe.
        :type responder_rules: list[oci.cloud_guard.models.TargetResponderRecipeResponderRule]

        :param effective_responder_rules:
            The value to assign to the effective_responder_rules property of this TargetResponderRecipe.
        :type effective_responder_rules: list[oci.cloud_guard.models.TargetResponderRecipeResponderRule]

        """
        self.swagger_types = {
            'id': 'str',
            'responder_recipe_id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'description': 'str',
            'owner': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'responder_rules': 'list[TargetResponderRecipeResponderRule]',
            'effective_responder_rules': 'list[TargetResponderRecipeResponderRule]'
        }

        self.attribute_map = {
            'id': 'id',
            'responder_recipe_id': 'responderRecipeId',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'description': 'description',
            'owner': 'owner',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'responder_rules': 'responderRules',
            'effective_responder_rules': 'effectiveResponderRules'
        }

        self._id = None
        self._responder_recipe_id = None
        self._compartment_id = None
        self._display_name = None
        self._description = None
        self._owner = None
        self._time_created = None
        self._time_updated = None
        self._responder_rules = None
        self._effective_responder_rules = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TargetResponderRecipe.
        Unique identifier of TargetResponderRecipe that can't be changed after creation.


        :return: The id of this TargetResponderRecipe.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TargetResponderRecipe.
        Unique identifier of TargetResponderRecipe that can't be changed after creation.


        :param id: The id of this TargetResponderRecipe.
        :type: str
        """
        self._id = id

    @property
    def responder_recipe_id(self):
        """
        **[Required]** Gets the responder_recipe_id of this TargetResponderRecipe.
        Unique identifier for Responder Recipe of which this is an extension.


        :return: The responder_recipe_id of this TargetResponderRecipe.
        :rtype: str
        """
        return self._responder_recipe_id

    @responder_recipe_id.setter
    def responder_recipe_id(self, responder_recipe_id):
        """
        Sets the responder_recipe_id of this TargetResponderRecipe.
        Unique identifier for Responder Recipe of which this is an extension.


        :param responder_recipe_id: The responder_recipe_id of this TargetResponderRecipe.
        :type: str
        """
        self._responder_recipe_id = responder_recipe_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this TargetResponderRecipe.
        Compartment Identifier


        :return: The compartment_id of this TargetResponderRecipe.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this TargetResponderRecipe.
        Compartment Identifier


        :param compartment_id: The compartment_id of this TargetResponderRecipe.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this TargetResponderRecipe.
        ResponderRecipe display name.


        :return: The display_name of this TargetResponderRecipe.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TargetResponderRecipe.
        ResponderRecipe display name.


        :param display_name: The display_name of this TargetResponderRecipe.
        :type: str
        """
        self._display_name = display_name

    @property
    def description(self):
        """
        **[Required]** Gets the description of this TargetResponderRecipe.
        ResponderRecipe description.


        :return: The description of this TargetResponderRecipe.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this TargetResponderRecipe.
        ResponderRecipe description.


        :param description: The description of this TargetResponderRecipe.
        :type: str
        """
        self._description = description

    @property
    def owner(self):
        """
        **[Required]** Gets the owner of this TargetResponderRecipe.
        Owner of ResponderRecipe

        Allowed values for this property are: "CUSTOMER", "ORACLE", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The owner of this TargetResponderRecipe.
        :rtype: str
        """
        return self._owner

    @owner.setter
    def owner(self, owner):
        """
        Sets the owner of this TargetResponderRecipe.
        Owner of ResponderRecipe


        :param owner: The owner of this TargetResponderRecipe.
        :type: str
        """
        allowed_values = ["CUSTOMER", "ORACLE"]
        if not value_allowed_none_or_none_sentinel(owner, allowed_values):
            owner = 'UNKNOWN_ENUM_VALUE'
        self._owner = owner

    @property
    def time_created(self):
        """
        Gets the time_created of this TargetResponderRecipe.
        The date and time the target responder recipe rule was created. Format defined by RFC3339.


        :return: The time_created of this TargetResponderRecipe.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this TargetResponderRecipe.
        The date and time the target responder recipe rule was created. Format defined by RFC3339.


        :param time_created: The time_created of this TargetResponderRecipe.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this TargetResponderRecipe.
        The date and time the target responder recipe rule was updated. Format defined by RFC3339.


        :return: The time_updated of this TargetResponderRecipe.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this TargetResponderRecipe.
        The date and time the target responder recipe rule was updated. Format defined by RFC3339.


        :param time_updated: The time_updated of this TargetResponderRecipe.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def responder_rules(self):
        """
        Gets the responder_rules of this TargetResponderRecipe.
        List of responder rules associated with the recipe - user input


        :return: The responder_rules of this TargetResponderRecipe.
        :rtype: list[oci.cloud_guard.models.TargetResponderRecipeResponderRule]
        """
        return self._responder_rules

    @responder_rules.setter
    def responder_rules(self, responder_rules):
        """
        Sets the responder_rules of this TargetResponderRecipe.
        List of responder rules associated with the recipe - user input


        :param responder_rules: The responder_rules of this TargetResponderRecipe.
        :type: list[oci.cloud_guard.models.TargetResponderRecipeResponderRule]
        """
        self._responder_rules = responder_rules

    @property
    def effective_responder_rules(self):
        """
        Gets the effective_responder_rules of this TargetResponderRecipe.
        List of responder rules associated with the recipe after applying all defaults


        :return: The effective_responder_rules of this TargetResponderRecipe.
        :rtype: list[oci.cloud_guard.models.TargetResponderRecipeResponderRule]
        """
        return self._effective_responder_rules

    @effective_responder_rules.setter
    def effective_responder_rules(self, effective_responder_rules):
        """
        Sets the effective_responder_rules of this TargetResponderRecipe.
        List of responder rules associated with the recipe after applying all defaults


        :param effective_responder_rules: The effective_responder_rules of this TargetResponderRecipe.
        :type: list[oci.cloud_guard.models.TargetResponderRecipeResponderRule]
        """
        self._effective_responder_rules = effective_responder_rules

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
