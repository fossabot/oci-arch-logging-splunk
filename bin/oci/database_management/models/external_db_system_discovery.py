# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class ExternalDbSystemDiscovery(object):
    """
    The details of an external DB system discovery.
    """

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemDiscovery.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemDiscovery.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemDiscovery.
    #: This constant has a value of "INACTIVE"
    LIFECYCLE_STATE_INACTIVE = "INACTIVE"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemDiscovery.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemDiscovery.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemDiscovery.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a ExternalDbSystemDiscovery.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new ExternalDbSystemDiscovery object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this ExternalDbSystemDiscovery.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this ExternalDbSystemDiscovery.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this ExternalDbSystemDiscovery.
        :type compartment_id: str

        :param agent_id:
            The value to assign to the agent_id property of this ExternalDbSystemDiscovery.
        :type agent_id: str

        :param grid_home:
            The value to assign to the grid_home property of this ExternalDbSystemDiscovery.
        :type grid_home: str

        :param discovered_components:
            The value to assign to the discovered_components property of this ExternalDbSystemDiscovery.
        :type discovered_components: list[oci.database_management.models.DiscoveredExternalDbSystemComponent]

        :param resource_id:
            The value to assign to the resource_id property of this ExternalDbSystemDiscovery.
        :type resource_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this ExternalDbSystemDiscovery.
            Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this ExternalDbSystemDiscovery.
        :type lifecycle_details: str

        :param time_created:
            The value to assign to the time_created property of this ExternalDbSystemDiscovery.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this ExternalDbSystemDiscovery.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'agent_id': 'str',
            'grid_home': 'str',
            'discovered_components': 'list[DiscoveredExternalDbSystemComponent]',
            'resource_id': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'agent_id': 'agentId',
            'grid_home': 'gridHome',
            'discovered_components': 'discoveredComponents',
            'resource_id': 'resourceId',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._agent_id = None
        self._grid_home = None
        self._discovered_components = None
        self._resource_id = None
        self._lifecycle_state = None
        self._lifecycle_details = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The id of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param id: The id of this ExternalDbSystemDiscovery.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        **[Required]** Gets the display_name of this ExternalDbSystemDiscovery.
        The user-friendly name for the DB system. The name does not have to be unique.


        :return: The display_name of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this ExternalDbSystemDiscovery.
        The user-friendly name for the DB system. The name does not have to be unique.


        :param display_name: The display_name of this ExternalDbSystemDiscovery.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the compartment.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this ExternalDbSystemDiscovery.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def agent_id(self):
        """
        **[Required]** Gets the agent_id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the management agent
        used for the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The agent_id of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._agent_id

    @agent_id.setter
    def agent_id(self, agent_id):
        """
        Sets the agent_id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the management agent
        used for the external DB system discovery.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param agent_id: The agent_id of this ExternalDbSystemDiscovery.
        :type: str
        """
        self._agent_id = agent_id

    @property
    def grid_home(self):
        """
        Gets the grid_home of this ExternalDbSystemDiscovery.
        The directory in which Oracle Grid Infrastructure is installed.


        :return: The grid_home of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._grid_home

    @grid_home.setter
    def grid_home(self, grid_home):
        """
        Sets the grid_home of this ExternalDbSystemDiscovery.
        The directory in which Oracle Grid Infrastructure is installed.


        :param grid_home: The grid_home of this ExternalDbSystemDiscovery.
        :type: str
        """
        self._grid_home = grid_home

    @property
    def discovered_components(self):
        """
        Gets the discovered_components of this ExternalDbSystemDiscovery.
        The list of DB system components that were found in the DB system discovery.


        :return: The discovered_components of this ExternalDbSystemDiscovery.
        :rtype: list[oci.database_management.models.DiscoveredExternalDbSystemComponent]
        """
        return self._discovered_components

    @discovered_components.setter
    def discovered_components(self, discovered_components):
        """
        Sets the discovered_components of this ExternalDbSystemDiscovery.
        The list of DB system components that were found in the DB system discovery.


        :param discovered_components: The discovered_components of this ExternalDbSystemDiscovery.
        :type: list[oci.database_management.models.DiscoveredExternalDbSystemComponent]
        """
        self._discovered_components = discovered_components

    @property
    def resource_id(self):
        """
        Gets the resource_id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the existing OCI resource matching the discovered DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :return: The resource_id of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._resource_id

    @resource_id.setter
    def resource_id(self, resource_id):
        """
        Sets the resource_id of this ExternalDbSystemDiscovery.
        The `OCID`__ of the existing OCI resource matching the discovered DB system.

        __ https://docs.cloud.oracle.com/Content/General/Concepts/identifiers.htm


        :param resource_id: The resource_id of this ExternalDbSystemDiscovery.
        :type: str
        """
        self._resource_id = resource_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this ExternalDbSystemDiscovery.
        The current lifecycle state of the external DB system discovery resource.

        Allowed values for this property are: "CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this ExternalDbSystemDiscovery.
        The current lifecycle state of the external DB system discovery resource.


        :param lifecycle_state: The lifecycle_state of this ExternalDbSystemDiscovery.
        :type: str
        """
        allowed_values = ["CREATING", "ACTIVE", "INACTIVE", "UPDATING", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this ExternalDbSystemDiscovery.
        Additional information about the current lifecycle state.


        :return: The lifecycle_details of this ExternalDbSystemDiscovery.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this ExternalDbSystemDiscovery.
        Additional information about the current lifecycle state.


        :param lifecycle_details: The lifecycle_details of this ExternalDbSystemDiscovery.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this ExternalDbSystemDiscovery.
        The date and time the external DB system discovery was created.


        :return: The time_created of this ExternalDbSystemDiscovery.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this ExternalDbSystemDiscovery.
        The date and time the external DB system discovery was created.


        :param time_created: The time_created of this ExternalDbSystemDiscovery.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        **[Required]** Gets the time_updated of this ExternalDbSystemDiscovery.
        The date and time the external DB system discovery was last updated.


        :return: The time_updated of this ExternalDbSystemDiscovery.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this ExternalDbSystemDiscovery.
        The date and time the external DB system discovery was last updated.


        :param time_updated: The time_updated of this ExternalDbSystemDiscovery.
        :type: datetime
        """
        self._time_updated = time_updated

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
