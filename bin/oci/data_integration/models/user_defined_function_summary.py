# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UserDefinedFunctionSummary(object):
    """
    The user defined function summary type contains the audit summary information and the definition of the user defined function.
    """

    #: A constant which can be used with the model_type property of a UserDefinedFunctionSummary.
    #: This constant has a value of "DIS_USER_DEFINED_FUNCTION"
    MODEL_TYPE_DIS_USER_DEFINED_FUNCTION = "DIS_USER_DEFINED_FUNCTION"

    def __init__(self, **kwargs):
        """
        Initializes a new UserDefinedFunctionSummary object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param key:
            The value to assign to the key property of this UserDefinedFunctionSummary.
        :type key: str

        :param model_type:
            The value to assign to the model_type property of this UserDefinedFunctionSummary.
            Allowed values for this property are: "DIS_USER_DEFINED_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param model_version:
            The value to assign to the model_version property of this UserDefinedFunctionSummary.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UserDefinedFunctionSummary.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this UserDefinedFunctionSummary.
        :type name: str

        :param identifier:
            The value to assign to the identifier property of this UserDefinedFunctionSummary.
        :type identifier: str

        :param object_version:
            The value to assign to the object_version property of this UserDefinedFunctionSummary.
        :type object_version: int

        :param signatures:
            The value to assign to the signatures property of this UserDefinedFunctionSummary.
        :type signatures: list[oci.data_integration.models.FunctionSignature]

        :param expr:
            The value to assign to the expr property of this UserDefinedFunctionSummary.
        :type expr: oci.data_integration.models.Expression

        :param description:
            The value to assign to the description property of this UserDefinedFunctionSummary.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this UserDefinedFunctionSummary.
        :type object_status: int

        :param metadata:
            The value to assign to the metadata property of this UserDefinedFunctionSummary.
        :type metadata: oci.data_integration.models.ObjectMetadata

        :param key_map:
            The value to assign to the key_map property of this UserDefinedFunctionSummary.
        :type key_map: dict(str, str)

        """
        self.swagger_types = {
            'key': 'str',
            'model_type': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'identifier': 'str',
            'object_version': 'int',
            'signatures': 'list[FunctionSignature]',
            'expr': 'Expression',
            'description': 'str',
            'object_status': 'int',
            'metadata': 'ObjectMetadata',
            'key_map': 'dict(str, str)'
        }

        self.attribute_map = {
            'key': 'key',
            'model_type': 'modelType',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'identifier': 'identifier',
            'object_version': 'objectVersion',
            'signatures': 'signatures',
            'expr': 'expr',
            'description': 'description',
            'object_status': 'objectStatus',
            'metadata': 'metadata',
            'key_map': 'keyMap'
        }

        self._key = None
        self._model_type = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._identifier = None
        self._object_version = None
        self._signatures = None
        self._expr = None
        self._description = None
        self._object_status = None
        self._metadata = None
        self._key_map = None

    @property
    def key(self):
        """
        Gets the key of this UserDefinedFunctionSummary.
        Generated key that can be used in API calls to identify user defined function. On scenarios where reference to the user defined function is needed, a value can be passed in create.


        :return: The key of this UserDefinedFunctionSummary.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this UserDefinedFunctionSummary.
        Generated key that can be used in API calls to identify user defined function. On scenarios where reference to the user defined function is needed, a value can be passed in create.


        :param key: The key of this UserDefinedFunctionSummary.
        :type: str
        """
        self._key = key

    @property
    def model_type(self):
        """
        Gets the model_type of this UserDefinedFunctionSummary.
        The type of the object.

        Allowed values for this property are: "DIS_USER_DEFINED_FUNCTION", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this UserDefinedFunctionSummary.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this UserDefinedFunctionSummary.
        The type of the object.


        :param model_type: The model_type of this UserDefinedFunctionSummary.
        :type: str
        """
        allowed_values = ["DIS_USER_DEFINED_FUNCTION"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def model_version(self):
        """
        Gets the model_version of this UserDefinedFunctionSummary.
        The model version of an object.


        :return: The model_version of this UserDefinedFunctionSummary.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this UserDefinedFunctionSummary.
        The model version of an object.


        :param model_version: The model_version of this UserDefinedFunctionSummary.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this UserDefinedFunctionSummary.

        :return: The parent_ref of this UserDefinedFunctionSummary.
        :rtype: oci.data_integration.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this UserDefinedFunctionSummary.

        :param parent_ref: The parent_ref of this UserDefinedFunctionSummary.
        :type: oci.data_integration.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this UserDefinedFunctionSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this UserDefinedFunctionSummary.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UserDefinedFunctionSummary.
        Free form text without any restriction on permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this UserDefinedFunctionSummary.
        :type: str
        """
        self._name = name

    @property
    def identifier(self):
        """
        Gets the identifier of this UserDefinedFunctionSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :return: The identifier of this UserDefinedFunctionSummary.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """
        Sets the identifier of this UserDefinedFunctionSummary.
        Value can only contain upper case letters, underscore, and numbers. It should begin with upper case letter or underscore. The value can be modified.


        :param identifier: The identifier of this UserDefinedFunctionSummary.
        :type: str
        """
        self._identifier = identifier

    @property
    def object_version(self):
        """
        Gets the object_version of this UserDefinedFunctionSummary.
        The version of the object that is used to track changes in the object instance.


        :return: The object_version of this UserDefinedFunctionSummary.
        :rtype: int
        """
        return self._object_version

    @object_version.setter
    def object_version(self, object_version):
        """
        Sets the object_version of this UserDefinedFunctionSummary.
        The version of the object that is used to track changes in the object instance.


        :param object_version: The object_version of this UserDefinedFunctionSummary.
        :type: int
        """
        self._object_version = object_version

    @property
    def signatures(self):
        """
        Gets the signatures of this UserDefinedFunctionSummary.
        An array of function signature.


        :return: The signatures of this UserDefinedFunctionSummary.
        :rtype: list[oci.data_integration.models.FunctionSignature]
        """
        return self._signatures

    @signatures.setter
    def signatures(self, signatures):
        """
        Sets the signatures of this UserDefinedFunctionSummary.
        An array of function signature.


        :param signatures: The signatures of this UserDefinedFunctionSummary.
        :type: list[oci.data_integration.models.FunctionSignature]
        """
        self._signatures = signatures

    @property
    def expr(self):
        """
        Gets the expr of this UserDefinedFunctionSummary.

        :return: The expr of this UserDefinedFunctionSummary.
        :rtype: oci.data_integration.models.Expression
        """
        return self._expr

    @expr.setter
    def expr(self, expr):
        """
        Sets the expr of this UserDefinedFunctionSummary.

        :param expr: The expr of this UserDefinedFunctionSummary.
        :type: oci.data_integration.models.Expression
        """
        self._expr = expr

    @property
    def description(self):
        """
        Gets the description of this UserDefinedFunctionSummary.
        Detailed description for the object.


        :return: The description of this UserDefinedFunctionSummary.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """
        Sets the description of this UserDefinedFunctionSummary.
        Detailed description for the object.


        :param description: The description of this UserDefinedFunctionSummary.
        :type: str
        """
        self._description = description

    @property
    def object_status(self):
        """
        Gets the object_status of this UserDefinedFunctionSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this UserDefinedFunctionSummary.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this UserDefinedFunctionSummary.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this UserDefinedFunctionSummary.
        :type: int
        """
        self._object_status = object_status

    @property
    def metadata(self):
        """
        Gets the metadata of this UserDefinedFunctionSummary.

        :return: The metadata of this UserDefinedFunctionSummary.
        :rtype: oci.data_integration.models.ObjectMetadata
        """
        return self._metadata

    @metadata.setter
    def metadata(self, metadata):
        """
        Sets the metadata of this UserDefinedFunctionSummary.

        :param metadata: The metadata of this UserDefinedFunctionSummary.
        :type: oci.data_integration.models.ObjectMetadata
        """
        self._metadata = metadata

    @property
    def key_map(self):
        """
        Gets the key_map of this UserDefinedFunctionSummary.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :return: The key_map of this UserDefinedFunctionSummary.
        :rtype: dict(str, str)
        """
        return self._key_map

    @key_map.setter
    def key_map(self, key_map):
        """
        Sets the key_map of this UserDefinedFunctionSummary.
        A key map. If provided, key is replaced with generated key. This structure provides mapping between user provided key and generated key.


        :param key_map: The key_map of this UserDefinedFunctionSummary.
        :type: dict(str, str)
        """
        self._key_map = key_map

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
