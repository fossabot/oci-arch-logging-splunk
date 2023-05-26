# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MediaAssetSummary(object):
    """
    Summary of the MediaAsset.
    """

    #: A constant which can be used with the lifecycle_state property of a MediaAssetSummary.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a MediaAssetSummary.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a MediaAssetSummary.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a MediaAssetSummary.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a MediaAssetSummary.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a MediaAssetSummary.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the type property of a MediaAssetSummary.
    #: This constant has a value of "AUDIO"
    TYPE_AUDIO = "AUDIO"

    #: A constant which can be used with the type property of a MediaAssetSummary.
    #: This constant has a value of "VIDEO"
    TYPE_VIDEO = "VIDEO"

    #: A constant which can be used with the type property of a MediaAssetSummary.
    #: This constant has a value of "PLAYLIST"
    TYPE_PLAYLIST = "PLAYLIST"

    #: A constant which can be used with the type property of a MediaAssetSummary.
    #: This constant has a value of "IMAGE"
    TYPE_IMAGE = "IMAGE"

    #: A constant which can be used with the type property of a MediaAssetSummary.
    #: This constant has a value of "CAPTION_FILE"
    TYPE_CAPTION_FILE = "CAPTION_FILE"

    #: A constant which can be used with the type property of a MediaAssetSummary.
    #: This constant has a value of "UNKNOWN"
    TYPE_UNKNOWN = "UNKNOWN"

    def __init__(self, **kwargs):
        """
        Initializes a new MediaAssetSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this MediaAssetSummary.
        :type id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this MediaAssetSummary.
        :type compartment_id: str

        :param display_name:
            The value to assign to the display_name property of this MediaAssetSummary.
        :type display_name: str

        :param time_created:
            The value to assign to the time_created property of this MediaAssetSummary.
        :type time_created: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this MediaAssetSummary.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param type:
            The value to assign to the type property of this MediaAssetSummary.
            Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type type: str

        :param time_updated:
            The value to assign to the time_updated property of this MediaAssetSummary.
        :type time_updated: datetime

        :param master_media_asset_id:
            The value to assign to the master_media_asset_id property of this MediaAssetSummary.
        :type master_media_asset_id: str

        :param parent_media_asset_id:
            The value to assign to the parent_media_asset_id property of this MediaAssetSummary.
        :type parent_media_asset_id: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this MediaAssetSummary.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this MediaAssetSummary.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this MediaAssetSummary.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'compartment_id': 'str',
            'display_name': 'str',
            'time_created': 'datetime',
            'lifecycle_state': 'str',
            'type': 'str',
            'time_updated': 'datetime',
            'master_media_asset_id': 'str',
            'parent_media_asset_id': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'compartment_id': 'compartmentId',
            'display_name': 'displayName',
            'time_created': 'timeCreated',
            'lifecycle_state': 'lifecycleState',
            'type': 'type',
            'time_updated': 'timeUpdated',
            'master_media_asset_id': 'masterMediaAssetId',
            'parent_media_asset_id': 'parentMediaAssetId',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._compartment_id = None
        self._display_name = None
        self._time_created = None
        self._lifecycle_state = None
        self._type = None
        self._time_updated = None
        self._master_media_asset_id = None
        self._parent_media_asset_id = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this MediaAssetSummary.
        Unique identifier that is immutable on creation.


        :return: The id of this MediaAssetSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this MediaAssetSummary.
        Unique identifier that is immutable on creation.


        :param id: The id of this MediaAssetSummary.
        :type: str
        """
        self._id = id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this MediaAssetSummary.
        The ID of the compartment containing the MediaAsset.


        :return: The compartment_id of this MediaAssetSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this MediaAssetSummary.
        The ID of the compartment containing the MediaAsset.


        :param compartment_id: The compartment_id of this MediaAssetSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def display_name(self):
        """
        Gets the display_name of this MediaAssetSummary.
        MediaAsset name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :return: The display_name of this MediaAssetSummary.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this MediaAssetSummary.
        MediaAsset name. Does not have to be unique, and it's changeable. Avoid entering confidential information.


        :param display_name: The display_name of this MediaAssetSummary.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_created(self):
        """
        Gets the time_created of this MediaAssetSummary.
        The time the the MediaAsset was created. An RFC3339 formatted datetime string.


        :return: The time_created of this MediaAssetSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this MediaAssetSummary.
        The time the the MediaAsset was created. An RFC3339 formatted datetime string.


        :param time_created: The time_created of this MediaAssetSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this MediaAssetSummary.
        The current state of the MediaAsset.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this MediaAssetSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this MediaAssetSummary.
        The current state of the MediaAsset.


        :param lifecycle_state: The lifecycle_state of this MediaAssetSummary.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def type(self):
        """
        **[Required]** Gets the type of this MediaAssetSummary.
        The type of the media asset.

        Allowed values for this property are: "AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The type of this MediaAssetSummary.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MediaAssetSummary.
        The type of the media asset.


        :param type: The type of this MediaAssetSummary.
        :type: str
        """
        allowed_values = ["AUDIO", "VIDEO", "PLAYLIST", "IMAGE", "CAPTION_FILE", "UNKNOWN"]
        if not value_allowed_none_or_none_sentinel(type, allowed_values):
            type = 'UNKNOWN_ENUM_VALUE'
        self._type = type

    @property
    def time_updated(self):
        """
        Gets the time_updated of this MediaAssetSummary.
        The time the MediaAsset was updated. An RFC3339 formatted datetime string.


        :return: The time_updated of this MediaAssetSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this MediaAssetSummary.
        The time the MediaAsset was updated. An RFC3339 formatted datetime string.


        :param time_updated: The time_updated of this MediaAssetSummary.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def master_media_asset_id(self):
        """
        Gets the master_media_asset_id of this MediaAssetSummary.
        The ID of the senior most asset from which this asset is derived.


        :return: The master_media_asset_id of this MediaAssetSummary.
        :rtype: str
        """
        return self._master_media_asset_id

    @master_media_asset_id.setter
    def master_media_asset_id(self, master_media_asset_id):
        """
        Sets the master_media_asset_id of this MediaAssetSummary.
        The ID of the senior most asset from which this asset is derived.


        :param master_media_asset_id: The master_media_asset_id of this MediaAssetSummary.
        :type: str
        """
        self._master_media_asset_id = master_media_asset_id

    @property
    def parent_media_asset_id(self):
        """
        Gets the parent_media_asset_id of this MediaAssetSummary.
        The ID of the parent asset from which this asset is derived.


        :return: The parent_media_asset_id of this MediaAssetSummary.
        :rtype: str
        """
        return self._parent_media_asset_id

    @parent_media_asset_id.setter
    def parent_media_asset_id(self, parent_media_asset_id):
        """
        Sets the parent_media_asset_id of this MediaAssetSummary.
        The ID of the parent asset from which this asset is derived.


        :param parent_media_asset_id: The parent_media_asset_id of this MediaAssetSummary.
        :type: str
        """
        self._parent_media_asset_id = parent_media_asset_id

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this MediaAssetSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this MediaAssetSummary.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this MediaAssetSummary.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this MediaAssetSummary.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this MediaAssetSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this MediaAssetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this MediaAssetSummary.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this MediaAssetSummary.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this MediaAssetSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this MediaAssetSummary.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this MediaAssetSummary.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this MediaAssetSummary.
        :type: dict(str, dict(str, object))
        """
        self._system_tags = system_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
