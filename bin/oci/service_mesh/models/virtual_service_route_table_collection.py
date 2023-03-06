# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class VirtualServiceRouteTableCollection(object):
    """
    Results of a mesh search. Contains both VirtualServiceRouteTableSummary items and other information, such as metadata.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new VirtualServiceRouteTableCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param items:
            The value to assign to the items property of this VirtualServiceRouteTableCollection.
        :type items: list[oci.service_mesh.models.VirtualServiceRouteTableSummary]

        """
        self.swagger_types = {
            'items': 'list[VirtualServiceRouteTableSummary]'
        }

        self.attribute_map = {
            'items': 'items'
        }

        self._items = None

    @property
    def items(self):
        """
        **[Required]** Gets the items of this VirtualServiceRouteTableCollection.
        List of virtual service route tables.


        :return: The items of this VirtualServiceRouteTableCollection.
        :rtype: list[oci.service_mesh.models.VirtualServiceRouteTableSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this VirtualServiceRouteTableCollection.
        List of virtual service route tables.


        :param items: The items of this VirtualServiceRouteTableCollection.
        :type: list[oci.service_mesh.models.VirtualServiceRouteTableSummary]
        """
        self._items = items

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
