# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OpensearchClusterBackup(object):
    """
    An OpenSearch cluster backup resource. An cluster is set of instances that provide OpenSearch functionality in OCI Search Service with OpenSearch.
    For more information, see `Cluster Backups`__.

    __ https://docs.cloud.oracle.com/iaas/Content/search-opensearch/Concepts/ociopensearchbackups.htm
    """

    #: A constant which can be used with the backup_type property of a OpensearchClusterBackup.
    #: This constant has a value of "SCHEDULED"
    BACKUP_TYPE_SCHEDULED = "SCHEDULED"

    #: A constant which can be used with the backup_type property of a OpensearchClusterBackup.
    #: This constant has a value of "MANUAL"
    BACKUP_TYPE_MANUAL = "MANUAL"

    #: A constant which can be used with the lifecycle_state property of a OpensearchClusterBackup.
    #: This constant has a value of "CREATING"
    LIFECYCLE_STATE_CREATING = "CREATING"

    #: A constant which can be used with the lifecycle_state property of a OpensearchClusterBackup.
    #: This constant has a value of "UPDATING"
    LIFECYCLE_STATE_UPDATING = "UPDATING"

    #: A constant which can be used with the lifecycle_state property of a OpensearchClusterBackup.
    #: This constant has a value of "ACTIVE"
    LIFECYCLE_STATE_ACTIVE = "ACTIVE"

    #: A constant which can be used with the lifecycle_state property of a OpensearchClusterBackup.
    #: This constant has a value of "DELETING"
    LIFECYCLE_STATE_DELETING = "DELETING"

    #: A constant which can be used with the lifecycle_state property of a OpensearchClusterBackup.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a OpensearchClusterBackup.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    def __init__(self, **kwargs):
        """
        Initializes a new OpensearchClusterBackup object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OpensearchClusterBackup.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this OpensearchClusterBackup.
        :type display_name: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OpensearchClusterBackup.
        :type compartment_id: str

        :param backup_type:
            The value to assign to the backup_type property of this OpensearchClusterBackup.
            Allowed values for this property are: "SCHEDULED", "MANUAL", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type backup_type: str

        :param time_created:
            The value to assign to the time_created property of this OpensearchClusterBackup.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OpensearchClusterBackup.
        :type time_updated: datetime

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OpensearchClusterBackup.
            Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecyle_details:
            The value to assign to the lifecyle_details property of this OpensearchClusterBackup.
        :type lifecyle_details: str

        :param source_cluster_id:
            The value to assign to the source_cluster_id property of this OpensearchClusterBackup.
        :type source_cluster_id: str

        :param namespace:
            The value to assign to the namespace property of this OpensearchClusterBackup.
        :type namespace: str

        :param bucket_name:
            The value to assign to the bucket_name property of this OpensearchClusterBackup.
        :type bucket_name: str

        :param prefix:
            The value to assign to the prefix property of this OpensearchClusterBackup.
        :type prefix: str

        :param time_expired:
            The value to assign to the time_expired property of this OpensearchClusterBackup.
        :type time_expired: datetime

        :param backup_size:
            The value to assign to the backup_size property of this OpensearchClusterBackup.
        :type backup_size: float

        :param source_cluster_display_name:
            The value to assign to the source_cluster_display_name property of this OpensearchClusterBackup.
        :type source_cluster_display_name: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this OpensearchClusterBackup.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this OpensearchClusterBackup.
        :type defined_tags: dict(str, dict(str, object))

        :param system_tags:
            The value to assign to the system_tags property of this OpensearchClusterBackup.
        :type system_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'compartment_id': 'str',
            'backup_type': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime',
            'lifecycle_state': 'str',
            'lifecyle_details': 'str',
            'source_cluster_id': 'str',
            'namespace': 'str',
            'bucket_name': 'str',
            'prefix': 'str',
            'time_expired': 'datetime',
            'backup_size': 'float',
            'source_cluster_display_name': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))',
            'system_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'compartment_id': 'compartmentId',
            'backup_type': 'backupType',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated',
            'lifecycle_state': 'lifecycleState',
            'lifecyle_details': 'lifecyleDetails',
            'source_cluster_id': 'sourceClusterId',
            'namespace': 'namespace',
            'bucket_name': 'bucketName',
            'prefix': 'prefix',
            'time_expired': 'timeExpired',
            'backup_size': 'backupSize',
            'source_cluster_display_name': 'sourceClusterDisplayName',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags',
            'system_tags': 'systemTags'
        }

        self._id = None
        self._display_name = None
        self._compartment_id = None
        self._backup_type = None
        self._time_created = None
        self._time_updated = None
        self._lifecycle_state = None
        self._lifecyle_details = None
        self._source_cluster_id = None
        self._namespace = None
        self._bucket_name = None
        self._prefix = None
        self._time_expired = None
        self._backup_size = None
        self._source_cluster_display_name = None
        self._freeform_tags = None
        self._defined_tags = None
        self._system_tags = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OpensearchClusterBackup.
        The OCID of the cluster backup.


        :return: The id of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OpensearchClusterBackup.
        The OCID of the cluster backup.


        :param id: The id of this OpensearchClusterBackup.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this OpensearchClusterBackup.
        The name of the cluster backup. Avoid entering confidential information.


        :return: The display_name of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this OpensearchClusterBackup.
        The name of the cluster backup. Avoid entering confidential information.


        :param display_name: The display_name of this OpensearchClusterBackup.
        :type: str
        """
        self._display_name = display_name

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OpensearchClusterBackup.
        The OCID of the compartment where the cluster backup is located.


        :return: The compartment_id of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OpensearchClusterBackup.
        The OCID of the compartment where the cluster backup is located.


        :param compartment_id: The compartment_id of this OpensearchClusterBackup.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def backup_type(self):
        """
        **[Required]** Gets the backup_type of this OpensearchClusterBackup.
        Specifies whether the cluster backup was created manually, or automatically as a scheduled backup.

        Allowed values for this property are: "SCHEDULED", "MANUAL", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The backup_type of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._backup_type

    @backup_type.setter
    def backup_type(self, backup_type):
        """
        Sets the backup_type of this OpensearchClusterBackup.
        Specifies whether the cluster backup was created manually, or automatically as a scheduled backup.


        :param backup_type: The backup_type of this OpensearchClusterBackup.
        :type: str
        """
        allowed_values = ["SCHEDULED", "MANUAL"]
        if not value_allowed_none_or_none_sentinel(backup_type, allowed_values):
            backup_type = 'UNKNOWN_ENUM_VALUE'
        self._backup_type = backup_type

    @property
    def time_created(self):
        """
        Gets the time_created of this OpensearchClusterBackup.
        The date and time the cluster backup was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_created of this OpensearchClusterBackup.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OpensearchClusterBackup.
        The date and time the cluster backup was created. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_created: The time_created of this OpensearchClusterBackup.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OpensearchClusterBackup.
        The date and time the cluster backup was updated. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_updated of this OpensearchClusterBackup.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OpensearchClusterBackup.
        The date and time the cluster backup was updated. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_updated: The time_updated of this OpensearchClusterBackup.
        :type: datetime
        """
        self._time_updated = time_updated

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OpensearchClusterBackup.
        The current state of the cluster backup.

        Allowed values for this property are: "CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OpensearchClusterBackup.
        The current state of the cluster backup.


        :param lifecycle_state: The lifecycle_state of this OpensearchClusterBackup.
        :type: str
        """
        allowed_values = ["CREATING", "UPDATING", "ACTIVE", "DELETING", "DELETED", "FAILED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecyle_details(self):
        """
        Gets the lifecyle_details of this OpensearchClusterBackup.
        Additional information about the current lifecycle state of the cluster backup.


        :return: The lifecyle_details of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._lifecyle_details

    @lifecyle_details.setter
    def lifecyle_details(self, lifecyle_details):
        """
        Sets the lifecyle_details of this OpensearchClusterBackup.
        Additional information about the current lifecycle state of the cluster backup.


        :param lifecyle_details: The lifecyle_details of this OpensearchClusterBackup.
        :type: str
        """
        self._lifecyle_details = lifecyle_details

    @property
    def source_cluster_id(self):
        """
        **[Required]** Gets the source_cluster_id of this OpensearchClusterBackup.
        The OCID of the source OpenSearch cluster for the cluster backup.


        :return: The source_cluster_id of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._source_cluster_id

    @source_cluster_id.setter
    def source_cluster_id(self, source_cluster_id):
        """
        Sets the source_cluster_id of this OpensearchClusterBackup.
        The OCID of the source OpenSearch cluster for the cluster backup.


        :param source_cluster_id: The source_cluster_id of this OpensearchClusterBackup.
        :type: str
        """
        self._source_cluster_id = source_cluster_id

    @property
    def namespace(self):
        """
        Gets the namespace of this OpensearchClusterBackup.
        The Object Storage namespace for the cluster backup.


        :return: The namespace of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._namespace

    @namespace.setter
    def namespace(self, namespace):
        """
        Sets the namespace of this OpensearchClusterBackup.
        The Object Storage namespace for the cluster backup.


        :param namespace: The namespace of this OpensearchClusterBackup.
        :type: str
        """
        self._namespace = namespace

    @property
    def bucket_name(self):
        """
        Gets the bucket_name of this OpensearchClusterBackup.
        The name of the Object Storage bucket for the cluster backup.


        :return: The bucket_name of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._bucket_name

    @bucket_name.setter
    def bucket_name(self, bucket_name):
        """
        Sets the bucket_name of this OpensearchClusterBackup.
        The name of the Object Storage bucket for the cluster backup.


        :param bucket_name: The bucket_name of this OpensearchClusterBackup.
        :type: str
        """
        self._bucket_name = bucket_name

    @property
    def prefix(self):
        """
        Gets the prefix of this OpensearchClusterBackup.
        The prefix within the Object Storage bucket for the cluster backup.


        :return: The prefix of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._prefix

    @prefix.setter
    def prefix(self, prefix):
        """
        Sets the prefix of this OpensearchClusterBackup.
        The prefix within the Object Storage bucket for the cluster backup.


        :param prefix: The prefix of this OpensearchClusterBackup.
        :type: str
        """
        self._prefix = prefix

    @property
    def time_expired(self):
        """
        Gets the time_expired of this OpensearchClusterBackup.
        The date and time the cluster backup expires. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_expired of this OpensearchClusterBackup.
        :rtype: datetime
        """
        return self._time_expired

    @time_expired.setter
    def time_expired(self, time_expired):
        """
        Sets the time_expired of this OpensearchClusterBackup.
        The date and time the cluster backup expires. Format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_expired: The time_expired of this OpensearchClusterBackup.
        :type: datetime
        """
        self._time_expired = time_expired

    @property
    def backup_size(self):
        """
        Gets the backup_size of this OpensearchClusterBackup.
        The size in GB of the cluster backup.


        :return: The backup_size of this OpensearchClusterBackup.
        :rtype: float
        """
        return self._backup_size

    @backup_size.setter
    def backup_size(self, backup_size):
        """
        Sets the backup_size of this OpensearchClusterBackup.
        The size in GB of the cluster backup.


        :param backup_size: The backup_size of this OpensearchClusterBackup.
        :type: float
        """
        self._backup_size = backup_size

    @property
    def source_cluster_display_name(self):
        """
        Gets the source_cluster_display_name of this OpensearchClusterBackup.
        The name of the source OpenSearch cluster for the cluster backup.


        :return: The source_cluster_display_name of this OpensearchClusterBackup.
        :rtype: str
        """
        return self._source_cluster_display_name

    @source_cluster_display_name.setter
    def source_cluster_display_name(self, source_cluster_display_name):
        """
        Sets the source_cluster_display_name of this OpensearchClusterBackup.
        The name of the source OpenSearch cluster for the cluster backup.


        :param source_cluster_display_name: The source_cluster_display_name of this OpensearchClusterBackup.
        :type: str
        """
        self._source_cluster_display_name = source_cluster_display_name

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this OpensearchClusterBackup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this OpensearchClusterBackup.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this OpensearchClusterBackup.
        Simple key-value pair that is applied without any predefined name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this OpensearchClusterBackup.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this OpensearchClusterBackup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this OpensearchClusterBackup.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this OpensearchClusterBackup.
        Defined tags for this resource. Each key is predefined and scoped to a namespace.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this OpensearchClusterBackup.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    @property
    def system_tags(self):
        """
        Gets the system_tags of this OpensearchClusterBackup.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :return: The system_tags of this OpensearchClusterBackup.
        :rtype: dict(str, dict(str, object))
        """
        return self._system_tags

    @system_tags.setter
    def system_tags(self, system_tags):
        """
        Sets the system_tags of this OpensearchClusterBackup.
        Usage of system tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"orcl-cloud\": {\"free-tier-retained\": \"true\"}}`


        :param system_tags: The system_tags of this OpensearchClusterBackup.
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
