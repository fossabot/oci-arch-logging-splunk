# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class FolderTagCollection(object):
    """
    Results of a folders tag listing. Folder tags allow association of folder objects to business terms.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new FolderTagCollection object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param count:
            The value to assign to the count property of this FolderTagCollection.
        :type count: int

        :param items:
            The value to assign to the items property of this FolderTagCollection.
        :type items: list[oci.data_catalog.models.FolderTagSummary]

        """
        self.swagger_types = {
            'count': 'int',
            'items': 'list[FolderTagSummary]'
        }

        self.attribute_map = {
            'count': 'count',
            'items': 'items'
        }

        self._count = None
        self._items = None

    @property
    def count(self):
        """
        Gets the count of this FolderTagCollection.
        Total number of items returned.


        :return: The count of this FolderTagCollection.
        :rtype: int
        """
        return self._count

    @count.setter
    def count(self, count):
        """
        Sets the count of this FolderTagCollection.
        Total number of items returned.


        :param count: The count of this FolderTagCollection.
        :type: int
        """
        self._count = count

    @property
    def items(self):
        """
        **[Required]** Gets the items of this FolderTagCollection.
        Collection of folder tags.


        :return: The items of this FolderTagCollection.
        :rtype: list[oci.data_catalog.models.FolderTagSummary]
        """
        return self._items

    @items.setter
    def items(self, items):
        """
        Sets the items of this FolderTagCollection.
        Collection of folder tags.


        :param items: The items of this FolderTagCollection.
        :type: list[oci.data_catalog.models.FolderTagSummary]
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
