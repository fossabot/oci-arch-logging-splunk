# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class AuthenticationFactorSettingsSearchRequest(object):
    """
    Clients MAY execute queries without passing parameters on the URL by using the HTTP POST verb combined with the **.search** path extension. The inclusion of **.search** on the end of a valid SCIM endpoint SHALL be used to indicate the HTTP POST verb is intended to be a query operation. To create a new query result set, a SCIM client sends an HTTP POST request to the desired SCIM resource endpoint (ending in **.search**). The body of the POST request MAY include any of the parameters.
    """

    #: A constant which can be used with the attribute_sets property of a AuthenticationFactorSettingsSearchRequest.
    #: This constant has a value of "all"
    ATTRIBUTE_SETS_ALL = "all"

    #: A constant which can be used with the attribute_sets property of a AuthenticationFactorSettingsSearchRequest.
    #: This constant has a value of "always"
    ATTRIBUTE_SETS_ALWAYS = "always"

    #: A constant which can be used with the attribute_sets property of a AuthenticationFactorSettingsSearchRequest.
    #: This constant has a value of "never"
    ATTRIBUTE_SETS_NEVER = "never"

    #: A constant which can be used with the attribute_sets property of a AuthenticationFactorSettingsSearchRequest.
    #: This constant has a value of "request"
    ATTRIBUTE_SETS_REQUEST = "request"

    #: A constant which can be used with the attribute_sets property of a AuthenticationFactorSettingsSearchRequest.
    #: This constant has a value of "default"
    ATTRIBUTE_SETS_DEFAULT = "default"

    def __init__(self, **kwargs):
        """
        Initializes a new AuthenticationFactorSettingsSearchRequest object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param schemas:
            The value to assign to the schemas property of this AuthenticationFactorSettingsSearchRequest.
        :type schemas: list[str]

        :param attributes:
            The value to assign to the attributes property of this AuthenticationFactorSettingsSearchRequest.
        :type attributes: list[str]

        :param attribute_sets:
            The value to assign to the attribute_sets property of this AuthenticationFactorSettingsSearchRequest.
            Allowed values for items in this list are: "all", "always", "never", "request", "default"
        :type attribute_sets: list[str]

        """
        self.swagger_types = {
            'schemas': 'list[str]',
            'attributes': 'list[str]',
            'attribute_sets': 'list[str]'
        }

        self.attribute_map = {
            'schemas': 'schemas',
            'attributes': 'attributes',
            'attribute_sets': 'attributeSets'
        }

        self._schemas = None
        self._attributes = None
        self._attribute_sets = None

    @property
    def schemas(self):
        """
        **[Required]** Gets the schemas of this AuthenticationFactorSettingsSearchRequest.
        The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. Query requests MUST be identified using the following URI: \"urn:ietf:params:scim:api:messages:2.0:SearchRequest\" REQUIRED.


        :return: The schemas of this AuthenticationFactorSettingsSearchRequest.
        :rtype: list[str]
        """
        return self._schemas

    @schemas.setter
    def schemas(self, schemas):
        """
        Sets the schemas of this AuthenticationFactorSettingsSearchRequest.
        The schemas attribute is an array of Strings which allows introspection of the supported schema version for a SCIM representation as well any schema extensions supported by that representation. Each String value must be a unique URI. Query requests MUST be identified using the following URI: \"urn:ietf:params:scim:api:messages:2.0:SearchRequest\" REQUIRED.


        :param schemas: The schemas of this AuthenticationFactorSettingsSearchRequest.
        :type: list[str]
        """
        self._schemas = schemas

    @property
    def attributes(self):
        """
        Gets the attributes of this AuthenticationFactorSettingsSearchRequest.
        A multi-valued list of strings indicating the names of resource attributes to return in the response overriding the set of attributes that would be returned by default. Attribute names MUST be in standard attribute notation (`Section 3.10`__) form. See (`additional retrieval query parameters`__). OPTIONAL.

        __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.10
        __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.9


        :return: The attributes of this AuthenticationFactorSettingsSearchRequest.
        :rtype: list[str]
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """
        Sets the attributes of this AuthenticationFactorSettingsSearchRequest.
        A multi-valued list of strings indicating the names of resource attributes to return in the response overriding the set of attributes that would be returned by default. Attribute names MUST be in standard attribute notation (`Section 3.10`__) form. See (`additional retrieval query parameters`__). OPTIONAL.

        __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.10
        __ https://tools.ietf.org/html/draft-ietf-scim-api-19#section-3.9


        :param attributes: The attributes of this AuthenticationFactorSettingsSearchRequest.
        :type: list[str]
        """
        self._attributes = attributes

    @property
    def attribute_sets(self):
        """
        Gets the attribute_sets of this AuthenticationFactorSettingsSearchRequest.
        A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If \"attributes\" query parameter is also available, union of the two is fetched. Valid values : all, always, never, request, default. Values are case-insensitive. OPTIONAL.

        Allowed values for items in this list are: "all", "always", "never", "request", "default"


        :return: The attribute_sets of this AuthenticationFactorSettingsSearchRequest.
        :rtype: list[str]
        """
        return self._attribute_sets

    @attribute_sets.setter
    def attribute_sets(self, attribute_sets):
        """
        Sets the attribute_sets of this AuthenticationFactorSettingsSearchRequest.
        A multi-valued list of strings indicating the return type of attribute definition. The specified set of attributes can be fetched by the return type of the attribute. One or more values can be given together to fetch more than one group of attributes. If \"attributes\" query parameter is also available, union of the two is fetched. Valid values : all, always, never, request, default. Values are case-insensitive. OPTIONAL.


        :param attribute_sets: The attribute_sets of this AuthenticationFactorSettingsSearchRequest.
        :type: list[str]
        """
        allowed_values = ["all", "always", "never", "request", "default"]

        if attribute_sets and attribute_sets is not NONE_SENTINEL:
            for value in attribute_sets:
                if not value_allowed_none_or_none_sentinel(value, allowed_values):
                    raise ValueError(
                        "Invalid value for `attribute_sets`, must be None or one of {0}"
                        .format(allowed_values)
                    )
        self._attribute_sets = attribute_sets

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
