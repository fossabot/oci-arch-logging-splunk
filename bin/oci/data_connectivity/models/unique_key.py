# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class UniqueKey(object):
    """
    The unqique key object.
    """

    #: A constant which can be used with the model_type property of a UniqueKey.
    #: This constant has a value of "PRIMARY_KEY"
    MODEL_TYPE_PRIMARY_KEY = "PRIMARY_KEY"

    #: A constant which can be used with the model_type property of a UniqueKey.
    #: This constant has a value of "UNIQUE_KEY"
    MODEL_TYPE_UNIQUE_KEY = "UNIQUE_KEY"

    def __init__(self, **kwargs):
        """
        Initializes a new UniqueKey object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_connectivity.models.PrimaryKey`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this UniqueKey.
            Allowed values for this property are: "PRIMARY_KEY", "UNIQUE_KEY", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type model_type: str

        :param key:
            The value to assign to the key property of this UniqueKey.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this UniqueKey.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this UniqueKey.
        :type parent_ref: oci.data_connectivity.models.ParentReference

        :param name:
            The value to assign to the name property of this UniqueKey.
        :type name: str

        :param attribute_refs:
            The value to assign to the attribute_refs property of this UniqueKey.
        :type attribute_refs: list[oci.data_connectivity.models.KeyAttribute]

        :param object_status:
            The value to assign to the object_status property of this UniqueKey.
        :type object_status: int

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'attribute_refs': 'list[KeyAttribute]',
            'object_status': 'int'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'attribute_refs': 'attributeRefs',
            'object_status': 'objectStatus'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._attribute_refs = None
        self._object_status = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['modelType']

        if type == 'PRIMARY_KEY':
            return 'PrimaryKey'
        else:
            return 'UniqueKey'

    @property
    def model_type(self):
        """
        **[Required]** Gets the model_type of this UniqueKey.
        The key type.

        Allowed values for this property are: "PRIMARY_KEY", "UNIQUE_KEY", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The model_type of this UniqueKey.
        :rtype: str
        """
        return self._model_type

    @model_type.setter
    def model_type(self, model_type):
        """
        Sets the model_type of this UniqueKey.
        The key type.


        :param model_type: The model_type of this UniqueKey.
        :type: str
        """
        allowed_values = ["PRIMARY_KEY", "UNIQUE_KEY"]
        if not value_allowed_none_or_none_sentinel(model_type, allowed_values):
            model_type = 'UNKNOWN_ENUM_VALUE'
        self._model_type = model_type

    @property
    def key(self):
        """
        Gets the key of this UniqueKey.
        The object key.


        :return: The key of this UniqueKey.
        :rtype: str
        """
        return self._key

    @key.setter
    def key(self, key):
        """
        Sets the key of this UniqueKey.
        The object key.


        :param key: The key of this UniqueKey.
        :type: str
        """
        self._key = key

    @property
    def model_version(self):
        """
        Gets the model_version of this UniqueKey.
        The model version of the object.


        :return: The model_version of this UniqueKey.
        :rtype: str
        """
        return self._model_version

    @model_version.setter
    def model_version(self, model_version):
        """
        Sets the model_version of this UniqueKey.
        The model version of the object.


        :param model_version: The model_version of this UniqueKey.
        :type: str
        """
        self._model_version = model_version

    @property
    def parent_ref(self):
        """
        Gets the parent_ref of this UniqueKey.

        :return: The parent_ref of this UniqueKey.
        :rtype: oci.data_connectivity.models.ParentReference
        """
        return self._parent_ref

    @parent_ref.setter
    def parent_ref(self, parent_ref):
        """
        Sets the parent_ref of this UniqueKey.

        :param parent_ref: The parent_ref of this UniqueKey.
        :type: oci.data_connectivity.models.ParentReference
        """
        self._parent_ref = parent_ref

    @property
    def name(self):
        """
        Gets the name of this UniqueKey.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :return: The name of this UniqueKey.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this UniqueKey.
        Free form text without any restriction on the permitted characters. Name can have letters, numbers, and special characters. The value is editable and is restricted to 1000 characters.


        :param name: The name of this UniqueKey.
        :type: str
        """
        self._name = name

    @property
    def attribute_refs(self):
        """
        Gets the attribute_refs of this UniqueKey.
        An array of attribute references.


        :return: The attribute_refs of this UniqueKey.
        :rtype: list[oci.data_connectivity.models.KeyAttribute]
        """
        return self._attribute_refs

    @attribute_refs.setter
    def attribute_refs(self, attribute_refs):
        """
        Sets the attribute_refs of this UniqueKey.
        An array of attribute references.


        :param attribute_refs: The attribute_refs of this UniqueKey.
        :type: list[oci.data_connectivity.models.KeyAttribute]
        """
        self._attribute_refs = attribute_refs

    @property
    def object_status(self):
        """
        Gets the object_status of this UniqueKey.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :return: The object_status of this UniqueKey.
        :rtype: int
        """
        return self._object_status

    @object_status.setter
    def object_status(self, object_status):
        """
        Sets the object_status of this UniqueKey.
        The status of an object that can be set to value 1 for shallow references across objects, other values reserved.


        :param object_status: The object_status of this UniqueKey.
        :type: int
        """
        self._object_status = object_status

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
