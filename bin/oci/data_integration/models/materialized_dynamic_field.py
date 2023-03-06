# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .typed_object import TypedObject
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class MaterializedDynamicField(TypedObject):
    """
    A materialized dynamic field, rules have been applied and all fields are concrete.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new MaterializedDynamicField object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.MaterializedDynamicField.model_type` attribute
        of this class is ``MATERIALIZED_DYNAMIC_FIELD`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this MaterializedDynamicField.
            Allowed values for this property are: "SHAPE", "INPUT_PORT", "SHAPE_FIELD", "INPUT_FIELD", "DERIVED_FIELD", "MACRO_FIELD", "OUTPUT_FIELD", "DYNAMIC_PROXY_FIELD", "OUTPUT_PORT", "DYNAMIC_INPUT_FIELD", "PROXY_FIELD", "PARAMETER", "PIVOT_FIELD", "MACRO_PIVOT_FIELD", "CONDITIONAL_OUTPUT_PORT", "INPUT_PROXY_FIELD", "MATERIALIZED_DYNAMIC_FIELD", "DECISION_OUTPUT_PORT"
        :type model_type: str

        :param key:
            The value to assign to the key property of this MaterializedDynamicField.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this MaterializedDynamicField.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this MaterializedDynamicField.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param config_values:
            The value to assign to the config_values property of this MaterializedDynamicField.
        :type config_values: oci.data_integration.models.ConfigValues

        :param object_status:
            The value to assign to the object_status property of this MaterializedDynamicField.
        :type object_status: int

        :param name:
            The value to assign to the name property of this MaterializedDynamicField.
        :type name: str

        :param description:
            The value to assign to the description property of this MaterializedDynamicField.
        :type description: str

        :param scope:
            The value to assign to the scope property of this MaterializedDynamicField.
        :type scope: str

        :param type:
            The value to assign to the type property of this MaterializedDynamicField.
        :type type: oci.data_integration.models.MaterializedCompositeType

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'config_values': 'ConfigValues',
            'object_status': 'int',
            'name': 'str',
            'description': 'str',
            'scope': 'str',
            'type': 'MaterializedCompositeType'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'config_values': 'configValues',
            'object_status': 'objectStatus',
            'name': 'name',
            'description': 'description',
            'scope': 'scope',
            'type': 'type'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._config_values = None
        self._object_status = None
        self._name = None
        self._description = None
        self._scope = None
        self._type = None
        self._model_type = 'MATERIALIZED_DYNAMIC_FIELD'

    @property
    def scope(self):
        """
        Gets the scope of this MaterializedDynamicField.
        Reference key value to an object within the document.


        :return: The scope of this MaterializedDynamicField.
        :rtype: str
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """
        Sets the scope of this MaterializedDynamicField.
        Reference key value to an object within the document.


        :param scope: The scope of this MaterializedDynamicField.
        :type: str
        """
        self._scope = scope

    @property
    def type(self):
        """
        Gets the type of this MaterializedDynamicField.

        :return: The type of this MaterializedDynamicField.
        :rtype: oci.data_integration.models.MaterializedCompositeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """
        Sets the type of this MaterializedDynamicField.

        :param type: The type of this MaterializedDynamicField.
        :type: oci.data_integration.models.MaterializedCompositeType
        """
        self._type = type

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
