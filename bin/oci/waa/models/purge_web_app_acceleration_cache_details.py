# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PurgeWebAppAccelerationCacheDetails(object):
    """
    Specifies options for a cache purge.
    """

    #: A constant which can be used with the purge_type property of a PurgeWebAppAccelerationCacheDetails.
    #: This constant has a value of "ENTIRE_CACHE"
    PURGE_TYPE_ENTIRE_CACHE = "ENTIRE_CACHE"

    def __init__(self, **kwargs):
        """
        Initializes a new PurgeWebAppAccelerationCacheDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.waa.models.PurgeEntireWebAppAccelerationCacheDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param purge_type:
            The value to assign to the purge_type property of this PurgeWebAppAccelerationCacheDetails.
            Allowed values for this property are: "ENTIRE_CACHE"
        :type purge_type: str

        """
        self.swagger_types = {
            'purge_type': 'str'
        }

        self.attribute_map = {
            'purge_type': 'purgeType'
        }

        self._purge_type = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['purgeType']

        if type == 'ENTIRE_CACHE':
            return 'PurgeEntireWebAppAccelerationCacheDetails'
        else:
            return 'PurgeWebAppAccelerationCacheDetails'

    @property
    def purge_type(self):
        """
        **[Required]** Gets the purge_type of this PurgeWebAppAccelerationCacheDetails.
        Type of cache purge to perform.

        Allowed values for this property are: "ENTIRE_CACHE"


        :return: The purge_type of this PurgeWebAppAccelerationCacheDetails.
        :rtype: str
        """
        return self._purge_type

    @purge_type.setter
    def purge_type(self, purge_type):
        """
        Sets the purge_type of this PurgeWebAppAccelerationCacheDetails.
        Type of cache purge to perform.


        :param purge_type: The purge_type of this PurgeWebAppAccelerationCacheDetails.
        :type: str
        """
        allowed_values = ["ENTIRE_CACHE"]
        if not value_allowed_none_or_none_sentinel(purge_type, allowed_values):
            raise ValueError(
                "Invalid value for `purge_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._purge_type = purge_type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
