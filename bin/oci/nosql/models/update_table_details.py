# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UpdateTableDetails(object):
    """
    The information to be updated.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new UpdateTableDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param compartment_id:
            The value to assign to the compartment_id property of this UpdateTableDetails.
        :type compartment_id: str

        :param ddl_statement:
            The value to assign to the ddl_statement property of this UpdateTableDetails.
        :type ddl_statement: str

        :param table_limits:
            The value to assign to the table_limits property of this UpdateTableDetails.
        :type table_limits: oci.nosql.models.TableLimits

        :param freeform_tags:
            The value to assign to the freeform_tags property of this UpdateTableDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this UpdateTableDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'compartment_id': 'str',
            'ddl_statement': 'str',
            'table_limits': 'TableLimits',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'compartment_id': 'compartmentId',
            'ddl_statement': 'ddlStatement',
            'table_limits': 'tableLimits',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._compartment_id = None
        self._ddl_statement = None
        self._table_limits = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this UpdateTableDetails.
        The OCID of the table's current compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and compartmentId is supplied, the latter
        must match the identified table's compartmentId.


        :return: The compartment_id of this UpdateTableDetails.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this UpdateTableDetails.
        The OCID of the table's current compartment.  Required
        if the tableNameOrId path parameter is a table name.
        Optional if tableNameOrId is an OCID.  If tableNameOrId
        is an OCID, and compartmentId is supplied, the latter
        must match the identified table's compartmentId.


        :param compartment_id: The compartment_id of this UpdateTableDetails.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def ddl_statement(self):
        """
        Gets the ddl_statement of this UpdateTableDetails.
        Complete ALTER TABLE DDL statement.


        :return: The ddl_statement of this UpdateTableDetails.
        :rtype: str
        """
        return self._ddl_statement

    @ddl_statement.setter
    def ddl_statement(self, ddl_statement):
        """
        Sets the ddl_statement of this UpdateTableDetails.
        Complete ALTER TABLE DDL statement.


        :param ddl_statement: The ddl_statement of this UpdateTableDetails.
        :type: str
        """
        self._ddl_statement = ddl_statement

    @property
    def table_limits(self):
        """
        Gets the table_limits of this UpdateTableDetails.

        :return: The table_limits of this UpdateTableDetails.
        :rtype: oci.nosql.models.TableLimits
        """
        return self._table_limits

    @table_limits.setter
    def table_limits(self, table_limits):
        """
        Sets the table_limits of this UpdateTableDetails.

        :param table_limits: The table_limits of this UpdateTableDetails.
        :type: oci.nosql.models.TableLimits
        """
        self._table_limits = table_limits

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this UpdateTableDetails.
        Simple key-value pair that is applied without any predefined
        name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this UpdateTableDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this UpdateTableDetails.
        Simple key-value pair that is applied without any predefined
        name, type or scope. Exists for cross-compatibility only.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this UpdateTableDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this UpdateTableDetails.
        Defined tags for this resource. Each key is predefined and
        scoped to a namespace.  Example: `{\"foo-namespace\":
        {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this UpdateTableDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this UpdateTableDetails.
        Defined tags for this resource. Each key is predefined and
        scoped to a namespace.  Example: `{\"foo-namespace\":
        {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this UpdateTableDetails.
        :type: dict(str, dict(str, object))
        """
        self._defined_tags = defined_tags

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
