# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaskingSchemaSummary(object):
    """
    Summary of a masking schema present in masking policy.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaskingSchemaSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schema_name:
            The value to assign to the schema_name property of this MaskingSchemaSummary.
        :type schema_name: str

        """
        self.swagger_types = {
            'schema_name': 'str'
        }

        self.attribute_map = {
            'schema_name': 'schemaName'
        }

        self._schema_name = None

    @property
    def schema_name(self):
        """
        **[Required]** Gets the schema_name of this MaskingSchemaSummary.
        The database schema that contains the masking column.


        :return: The schema_name of this MaskingSchemaSummary.
        :rtype: str
        """
        return self._schema_name

    @schema_name.setter
    def schema_name(self, schema_name):
        """
        Sets the schema_name of this MaskingSchemaSummary.
        The database schema that contains the masking column.


        :param schema_name: The schema_name of this MaskingSchemaSummary.
        :type: str
        """
        self._schema_name = schema_name

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
