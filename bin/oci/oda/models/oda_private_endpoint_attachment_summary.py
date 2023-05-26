# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class OdaPrivateEndpointAttachmentSummary(object):
    """
    Summary of the ODA private endpoint attachment.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new OdaPrivateEndpointAttachmentSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this OdaPrivateEndpointAttachmentSummary.
        :type id: str

        :param oda_instance_id:
            The value to assign to the oda_instance_id property of this OdaPrivateEndpointAttachmentSummary.
        :type oda_instance_id: str

        :param oda_private_endpoint_id:
            The value to assign to the oda_private_endpoint_id property of this OdaPrivateEndpointAttachmentSummary.
        :type oda_private_endpoint_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this OdaPrivateEndpointAttachmentSummary.
        :type compartment_id: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this OdaPrivateEndpointAttachmentSummary.
        :type lifecycle_state: str

        :param time_created:
            The value to assign to the time_created property of this OdaPrivateEndpointAttachmentSummary.
        :type time_created: datetime

        :param time_updated:
            The value to assign to the time_updated property of this OdaPrivateEndpointAttachmentSummary.
        :type time_updated: datetime

        """
        self.swagger_types = {
            'id': 'str',
            'oda_instance_id': 'str',
            'oda_private_endpoint_id': 'str',
            'compartment_id': 'str',
            'lifecycle_state': 'str',
            'time_created': 'datetime',
            'time_updated': 'datetime'
        }

        self.attribute_map = {
            'id': 'id',
            'oda_instance_id': 'odaInstanceId',
            'oda_private_endpoint_id': 'odaPrivateEndpointId',
            'compartment_id': 'compartmentId',
            'lifecycle_state': 'lifecycleState',
            'time_created': 'timeCreated',
            'time_updated': 'timeUpdated'
        }

        self._id = None
        self._oda_instance_id = None
        self._oda_private_endpoint_id = None
        self._compartment_id = None
        self._lifecycle_state = None
        self._time_created = None
        self._time_updated = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the ODA Private Endpoint Attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this OdaPrivateEndpointAttachmentSummary.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the ODA Private Endpoint Attachment.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this OdaPrivateEndpointAttachmentSummary.
        :type: str
        """
        self._id = id

    @property
    def oda_instance_id(self):
        """
        **[Required]** Gets the oda_instance_id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the attached ODA Instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The oda_instance_id of this OdaPrivateEndpointAttachmentSummary.
        :rtype: str
        """
        return self._oda_instance_id

    @oda_instance_id.setter
    def oda_instance_id(self, oda_instance_id):
        """
        Sets the oda_instance_id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the attached ODA Instance.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param oda_instance_id: The oda_instance_id of this OdaPrivateEndpointAttachmentSummary.
        :type: str
        """
        self._oda_instance_id = oda_instance_id

    @property
    def oda_private_endpoint_id(self):
        """
        **[Required]** Gets the oda_private_endpoint_id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the ODA Private Endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The oda_private_endpoint_id of this OdaPrivateEndpointAttachmentSummary.
        :rtype: str
        """
        return self._oda_private_endpoint_id

    @oda_private_endpoint_id.setter
    def oda_private_endpoint_id(self, oda_private_endpoint_id):
        """
        Sets the oda_private_endpoint_id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the ODA Private Endpoint.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param oda_private_endpoint_id: The oda_private_endpoint_id of this OdaPrivateEndpointAttachmentSummary.
        :type: str
        """
        self._oda_private_endpoint_id = oda_private_endpoint_id

    @property
    def compartment_id(self):
        """
        **[Required]** Gets the compartment_id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the compartment that the ODA private endpoint attachment belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The compartment_id of this OdaPrivateEndpointAttachmentSummary.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this OdaPrivateEndpointAttachmentSummary.
        The `OCID`__ of the compartment that the ODA private endpoint attachment belongs to.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param compartment_id: The compartment_id of this OdaPrivateEndpointAttachmentSummary.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def lifecycle_state(self):
        """
        **[Required]** Gets the lifecycle_state of this OdaPrivateEndpointAttachmentSummary.
        The current state of the ODA Private Endpoint attachment.


        :return: The lifecycle_state of this OdaPrivateEndpointAttachmentSummary.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this OdaPrivateEndpointAttachmentSummary.
        The current state of the ODA Private Endpoint attachment.


        :param lifecycle_state: The lifecycle_state of this OdaPrivateEndpointAttachmentSummary.
        :type: str
        """
        self._lifecycle_state = lifecycle_state

    @property
    def time_created(self):
        """
        **[Required]** Gets the time_created of this OdaPrivateEndpointAttachmentSummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_created of this OdaPrivateEndpointAttachmentSummary.
        :rtype: datetime
        """
        return self._time_created

    @time_created.setter
    def time_created(self, time_created):
        """
        Sets the time_created of this OdaPrivateEndpointAttachmentSummary.
        When the resource was created. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_created: The time_created of this OdaPrivateEndpointAttachmentSummary.
        :type: datetime
        """
        self._time_created = time_created

    @property
    def time_updated(self):
        """
        Gets the time_updated of this OdaPrivateEndpointAttachmentSummary.
        When the resource was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :return: The time_updated of this OdaPrivateEndpointAttachmentSummary.
        :rtype: datetime
        """
        return self._time_updated

    @time_updated.setter
    def time_updated(self, time_updated):
        """
        Sets the time_updated of this OdaPrivateEndpointAttachmentSummary.
        When the resource was last updated. A date-time string as described in `RFC 3339`__, section 14.29.

        __ https://tools.ietf.org/rfc/rfc3339


        :param time_updated: The time_updated of this OdaPrivateEndpointAttachmentSummary.
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
