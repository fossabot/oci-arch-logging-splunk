# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class IngestStreamDistributionChannelDetails(object):
    """
    Ingest Payload Information.
    """

    #: A constant which can be used with the ingest_payload_type property of a IngestStreamDistributionChannelDetails.
    #: This constant has a value of "ASSET_METADATA_MEDIA_ASSET"
    INGEST_PAYLOAD_TYPE_ASSET_METADATA_MEDIA_ASSET = "ASSET_METADATA_MEDIA_ASSET"

    def __init__(self, **kwargs):
        """
        Initializes a new IngestStreamDistributionChannelDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.media_services.models.AssetMetadataEntryDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param ingest_payload_type:
            The value to assign to the ingest_payload_type property of this IngestStreamDistributionChannelDetails.
            Allowed values for this property are: "ASSET_METADATA_MEDIA_ASSET"
        :type ingest_payload_type: str

        """
        self.swagger_types = {
            'ingest_payload_type': 'str'
        }

        self.attribute_map = {
            'ingest_payload_type': 'ingestPayloadType'
        }

        self._ingest_payload_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['ingestPayloadType']

        if type == 'ASSET_METADATA_MEDIA_ASSET':
            return 'AssetMetadataEntryDetails'
        else:
            return 'IngestStreamDistributionChannelDetails'

    @property
    def ingest_payload_type(self):
        """
        **[Required]** Gets the ingest_payload_type of this IngestStreamDistributionChannelDetails.
        Ingest Payload Type

        Allowed values for this property are: "ASSET_METADATA_MEDIA_ASSET"


        :return: The ingest_payload_type of this IngestStreamDistributionChannelDetails.
        :rtype: str
        """
        return self._ingest_payload_type

    @ingest_payload_type.setter
    def ingest_payload_type(self, ingest_payload_type):
        """
        Sets the ingest_payload_type of this IngestStreamDistributionChannelDetails.
        Ingest Payload Type


        :param ingest_payload_type: The ingest_payload_type of this IngestStreamDistributionChannelDetails.
        :type: str
        """
        allowed_values = ["ASSET_METADATA_MEDIA_ASSET"]
        if not value_allowed_none_or_none_sentinel(ingest_payload_type, allowed_values):
            raise ValueError(
                "Invalid value for `ingest_payload_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._ingest_payload_type = ingest_payload_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
