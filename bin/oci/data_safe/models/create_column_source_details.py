# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateColumnSourceDetails(object):
    """
    Details to associate a column source with a masking policy.
    """

    #: A constant which can be used with the column_source property of a CreateColumnSourceDetails.
    #: This constant has a value of "TARGET"
    COLUMN_SOURCE_TARGET = "TARGET"

    #: A constant which can be used with the column_source property of a CreateColumnSourceDetails.
    #: This constant has a value of "SENSITIVE_DATA_MODEL"
    COLUMN_SOURCE_SENSITIVE_DATA_MODEL = "SENSITIVE_DATA_MODEL"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateColumnSourceDetails object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_safe.models.CreateColumnSourceFromTargetDetails`
        * :class:`~oci.data_safe.models.CreateColumnSourceFromSdmDetails`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param column_source:
            The value to assign to the column_source property of this CreateColumnSourceDetails.
            Allowed values for this property are: "TARGET", "SENSITIVE_DATA_MODEL"
        :type column_source: str

        """
        self.swagger_types = {
            'column_source': 'str'
        }

        self.attribute_map = {
            'column_source': 'columnSource'
        }

        self._column_source = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['columnSource']

        if type == 'TARGET':
            return 'CreateColumnSourceFromTargetDetails'

        if type == 'SENSITIVE_DATA_MODEL':
            return 'CreateColumnSourceFromSdmDetails'
        else:
            return 'CreateColumnSourceDetails'

    @property
    def column_source(self):
        """
        **[Required]** Gets the column_source of this CreateColumnSourceDetails.
        The source of masking columns.

        Allowed values for this property are: "TARGET", "SENSITIVE_DATA_MODEL"


        :return: The column_source of this CreateColumnSourceDetails.
        :rtype: str
        """
        return self._column_source

    @column_source.setter
    def column_source(self, column_source):
        """
        Sets the column_source of this CreateColumnSourceDetails.
        The source of masking columns.


        :param column_source: The column_source of this CreateColumnSourceDetails.
        :type: str
        """
        allowed_values = ["TARGET", "SENSITIVE_DATA_MODEL"]
        if not value_allowed_none_or_none_sentinel(column_source, allowed_values):
            raise ValueError(
                "Invalid value for `column_source`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._column_source = column_source

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
