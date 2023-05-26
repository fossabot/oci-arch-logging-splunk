# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateAuthenticationProviderDetails(object):
    """
    Properties required to create a new Authentication Provider.
    """

    #: A constant which can be used with the grant_type property of a CreateAuthenticationProviderDetails.
    #: This constant has a value of "CLIENT_CREDENTIALS"
    GRANT_TYPE_CLIENT_CREDENTIALS = "CLIENT_CREDENTIALS"

    #: A constant which can be used with the grant_type property of a CreateAuthenticationProviderDetails.
    #: This constant has a value of "AUTHORIZATION_CODE"
    GRANT_TYPE_AUTHORIZATION_CODE = "AUTHORIZATION_CODE"

    #: A constant which can be used with the identity_provider property of a CreateAuthenticationProviderDetails.
    #: This constant has a value of "GENERIC"
    IDENTITY_PROVIDER_GENERIC = "GENERIC"

    #: A constant which can be used with the identity_provider property of a CreateAuthenticationProviderDetails.
    #: This constant has a value of "OAM"
    IDENTITY_PROVIDER_OAM = "OAM"

    #: A constant which can be used with the identity_provider property of a CreateAuthenticationProviderDetails.
    #: This constant has a value of "GOOGLE"
    IDENTITY_PROVIDER_GOOGLE = "GOOGLE"

    #: A constant which can be used with the identity_provider property of a CreateAuthenticationProviderDetails.
    #: This constant has a value of "MICROSOFT"
    IDENTITY_PROVIDER_MICROSOFT = "MICROSOFT"

    def __init__(self, **kwargs):
        """
        Initializes a new CreateAuthenticationProviderDetails object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param grant_type:
            The value to assign to the grant_type property of this CreateAuthenticationProviderDetails.
            Allowed values for this property are: "CLIENT_CREDENTIALS", "AUTHORIZATION_CODE"
        :type grant_type: str

        :param identity_provider:
            The value to assign to the identity_provider property of this CreateAuthenticationProviderDetails.
            Allowed values for this property are: "GENERIC", "OAM", "GOOGLE", "MICROSOFT"
        :type identity_provider: str

        :param name:
            The value to assign to the name property of this CreateAuthenticationProviderDetails.
        :type name: str

        :param token_endpoint_url:
            The value to assign to the token_endpoint_url property of this CreateAuthenticationProviderDetails.
        :type token_endpoint_url: str

        :param authorization_endpoint_url:
            The value to assign to the authorization_endpoint_url property of this CreateAuthenticationProviderDetails.
        :type authorization_endpoint_url: str

        :param short_authorization_code_request_url:
            The value to assign to the short_authorization_code_request_url property of this CreateAuthenticationProviderDetails.
        :type short_authorization_code_request_url: str

        :param revoke_token_endpoint_url:
            The value to assign to the revoke_token_endpoint_url property of this CreateAuthenticationProviderDetails.
        :type revoke_token_endpoint_url: str

        :param client_id:
            The value to assign to the client_id property of this CreateAuthenticationProviderDetails.
        :type client_id: str

        :param client_secret:
            The value to assign to the client_secret property of this CreateAuthenticationProviderDetails.
        :type client_secret: str

        :param scopes:
            The value to assign to the scopes property of this CreateAuthenticationProviderDetails.
        :type scopes: str

        :param subject_claim:
            The value to assign to the subject_claim property of this CreateAuthenticationProviderDetails.
        :type subject_claim: str

        :param refresh_token_retention_period_in_days:
            The value to assign to the refresh_token_retention_period_in_days property of this CreateAuthenticationProviderDetails.
        :type refresh_token_retention_period_in_days: int

        :param redirect_url:
            The value to assign to the redirect_url property of this CreateAuthenticationProviderDetails.
        :type redirect_url: str

        :param is_visible:
            The value to assign to the is_visible property of this CreateAuthenticationProviderDetails.
        :type is_visible: bool

        :param freeform_tags:
            The value to assign to the freeform_tags property of this CreateAuthenticationProviderDetails.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this CreateAuthenticationProviderDetails.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'grant_type': 'str',
            'identity_provider': 'str',
            'name': 'str',
            'token_endpoint_url': 'str',
            'authorization_endpoint_url': 'str',
            'short_authorization_code_request_url': 'str',
            'revoke_token_endpoint_url': 'str',
            'client_id': 'str',
            'client_secret': 'str',
            'scopes': 'str',
            'subject_claim': 'str',
            'refresh_token_retention_period_in_days': 'int',
            'redirect_url': 'str',
            'is_visible': 'bool',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'grant_type': 'grantType',
            'identity_provider': 'identityProvider',
            'name': 'name',
            'token_endpoint_url': 'tokenEndpointUrl',
            'authorization_endpoint_url': 'authorizationEndpointUrl',
            'short_authorization_code_request_url': 'shortAuthorizationCodeRequestUrl',
            'revoke_token_endpoint_url': 'revokeTokenEndpointUrl',
            'client_id': 'clientId',
            'client_secret': 'clientSecret',
            'scopes': 'scopes',
            'subject_claim': 'subjectClaim',
            'refresh_token_retention_period_in_days': 'refreshTokenRetentionPeriodInDays',
            'redirect_url': 'redirectUrl',
            'is_visible': 'isVisible',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._grant_type = None
        self._identity_provider = None
        self._name = None
        self._token_endpoint_url = None
        self._authorization_endpoint_url = None
        self._short_authorization_code_request_url = None
        self._revoke_token_endpoint_url = None
        self._client_id = None
        self._client_secret = None
        self._scopes = None
        self._subject_claim = None
        self._refresh_token_retention_period_in_days = None
        self._redirect_url = None
        self._is_visible = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def grant_type(self):
        """
        **[Required]** Gets the grant_type of this CreateAuthenticationProviderDetails.
        The grant type for the Authentication Provider.

        Allowed values for this property are: "CLIENT_CREDENTIALS", "AUTHORIZATION_CODE"


        :return: The grant_type of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._grant_type

    @grant_type.setter
    def grant_type(self, grant_type):
        """
        Sets the grant_type of this CreateAuthenticationProviderDetails.
        The grant type for the Authentication Provider.


        :param grant_type: The grant_type of this CreateAuthenticationProviderDetails.
        :type: str
        """
        allowed_values = ["CLIENT_CREDENTIALS", "AUTHORIZATION_CODE"]
        if not value_allowed_none_or_none_sentinel(grant_type, allowed_values):
            raise ValueError(
                "Invalid value for `grant_type`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._grant_type = grant_type

    @property
    def identity_provider(self):
        """
        **[Required]** Gets the identity_provider of this CreateAuthenticationProviderDetails.
        Which type of Identity Provider (IDP) you are using.

        Allowed values for this property are: "GENERIC", "OAM", "GOOGLE", "MICROSOFT"


        :return: The identity_provider of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._identity_provider

    @identity_provider.setter
    def identity_provider(self, identity_provider):
        """
        Sets the identity_provider of this CreateAuthenticationProviderDetails.
        Which type of Identity Provider (IDP) you are using.


        :param identity_provider: The identity_provider of this CreateAuthenticationProviderDetails.
        :type: str
        """
        allowed_values = ["GENERIC", "OAM", "GOOGLE", "MICROSOFT"]
        if not value_allowed_none_or_none_sentinel(identity_provider, allowed_values):
            raise ValueError(
                "Invalid value for `identity_provider`, must be None or one of {0}"
                .format(allowed_values)
            )
        self._identity_provider = identity_provider

    @property
    def name(self):
        """
        **[Required]** Gets the name of this CreateAuthenticationProviderDetails.
        A name to identify the Authentication Provider.


        :return: The name of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this CreateAuthenticationProviderDetails.
        A name to identify the Authentication Provider.


        :param name: The name of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._name = name

    @property
    def token_endpoint_url(self):
        """
        **[Required]** Gets the token_endpoint_url of this CreateAuthenticationProviderDetails.
        The IDPs URL for requesting access tokens.


        :return: The token_endpoint_url of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._token_endpoint_url

    @token_endpoint_url.setter
    def token_endpoint_url(self, token_endpoint_url):
        """
        Sets the token_endpoint_url of this CreateAuthenticationProviderDetails.
        The IDPs URL for requesting access tokens.


        :param token_endpoint_url: The token_endpoint_url of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._token_endpoint_url = token_endpoint_url

    @property
    def authorization_endpoint_url(self):
        """
        Gets the authorization_endpoint_url of this CreateAuthenticationProviderDetails.
        The IDPs URL for the page that users authenticate with by entering the user name and password.


        :return: The authorization_endpoint_url of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._authorization_endpoint_url

    @authorization_endpoint_url.setter
    def authorization_endpoint_url(self, authorization_endpoint_url):
        """
        Sets the authorization_endpoint_url of this CreateAuthenticationProviderDetails.
        The IDPs URL for the page that users authenticate with by entering the user name and password.


        :param authorization_endpoint_url: The authorization_endpoint_url of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._authorization_endpoint_url = authorization_endpoint_url

    @property
    def short_authorization_code_request_url(self):
        """
        Gets the short_authorization_code_request_url of this CreateAuthenticationProviderDetails.
        A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows
        you to send query parameters).  You might need this because the generated authorization-code-request URL
        could be too long for SMS and older smart phones.


        :return: The short_authorization_code_request_url of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._short_authorization_code_request_url

    @short_authorization_code_request_url.setter
    def short_authorization_code_request_url(self, short_authorization_code_request_url):
        """
        Sets the short_authorization_code_request_url of this CreateAuthenticationProviderDetails.
        A shortened version of the authorization URL, which you can get from a URL shortener service (one that allows
        you to send query parameters).  You might need this because the generated authorization-code-request URL
        could be too long for SMS and older smart phones.


        :param short_authorization_code_request_url: The short_authorization_code_request_url of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._short_authorization_code_request_url = short_authorization_code_request_url

    @property
    def revoke_token_endpoint_url(self):
        """
        Gets the revoke_token_endpoint_url of this CreateAuthenticationProviderDetails.
        If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then
        you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens
        component to revoke the user's tokens for this service.


        :return: The revoke_token_endpoint_url of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._revoke_token_endpoint_url

    @revoke_token_endpoint_url.setter
    def revoke_token_endpoint_url(self, revoke_token_endpoint_url):
        """
        Sets the revoke_token_endpoint_url of this CreateAuthenticationProviderDetails.
        If you want to revoke all the refresh tokens and access tokens of the logged-in user from a dialog flow, then
        you need the IDP's revoke refresh token URL. If you provide this URL, then you can use the System.OAuth2ResetTokens
        component to revoke the user's tokens for this service.


        :param revoke_token_endpoint_url: The revoke_token_endpoint_url of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._revoke_token_endpoint_url = revoke_token_endpoint_url

    @property
    def client_id(self):
        """
        **[Required]** Gets the client_id of this CreateAuthenticationProviderDetails.
        The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration.
        With Microsoft identity platform, use the application ID.


        :return: The client_id of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._client_id

    @client_id.setter
    def client_id(self, client_id):
        """
        Sets the client_id of this CreateAuthenticationProviderDetails.
        The client ID for the IDP application (OAuth Client) that was registered as described in Identity Provider Registration.
        With Microsoft identity platform, use the application ID.


        :param client_id: The client_id of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._client_id = client_id

    @property
    def client_secret(self):
        """
        **[Required]** Gets the client_secret of this CreateAuthenticationProviderDetails.
        The client secret for the IDP application (OAuth Client) that was registered as described in Identity Provider
        Registration. With Microsoft identity platform, use the application secret.


        :return: The client_secret of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._client_secret

    @client_secret.setter
    def client_secret(self, client_secret):
        """
        Sets the client_secret of this CreateAuthenticationProviderDetails.
        The client secret for the IDP application (OAuth Client) that was registered as described in Identity Provider
        Registration. With Microsoft identity platform, use the application secret.


        :param client_secret: The client_secret of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._client_secret = client_secret

    @property
    def scopes(self):
        """
        **[Required]** Gets the scopes of this CreateAuthenticationProviderDetails.
        A space-separated list of the scopes that must be included when Digital Assistant requests an access token from
        the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled,
        include the scope that\u2019s necessary to get the refresh token (typically offline_access).


        :return: The scopes of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._scopes

    @scopes.setter
    def scopes(self, scopes):
        """
        Sets the scopes of this CreateAuthenticationProviderDetails.
        A space-separated list of the scopes that must be included when Digital Assistant requests an access token from
        the provider. Include all the scopes that are required to access the resources. If refresh tokens are enabled,
        include the scope that\u2019s necessary to get the refresh token (typically offline_access).


        :param scopes: The scopes of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._scopes = scopes

    @property
    def subject_claim(self):
        """
        Gets the subject_claim of this CreateAuthenticationProviderDetails.
        The access-token profile claim to use to identify the user.


        :return: The subject_claim of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._subject_claim

    @subject_claim.setter
    def subject_claim(self, subject_claim):
        """
        Sets the subject_claim of this CreateAuthenticationProviderDetails.
        The access-token profile claim to use to identify the user.


        :param subject_claim: The subject_claim of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._subject_claim = subject_claim

    @property
    def refresh_token_retention_period_in_days(self):
        """
        Gets the refresh_token_retention_period_in_days of this CreateAuthenticationProviderDetails.
        The number of days to keep the refresh token in the Digital Assistant cache.


        :return: The refresh_token_retention_period_in_days of this CreateAuthenticationProviderDetails.
        :rtype: int
        """
        return self._refresh_token_retention_period_in_days

    @refresh_token_retention_period_in_days.setter
    def refresh_token_retention_period_in_days(self, refresh_token_retention_period_in_days):
        """
        Sets the refresh_token_retention_period_in_days of this CreateAuthenticationProviderDetails.
        The number of days to keep the refresh token in the Digital Assistant cache.


        :param refresh_token_retention_period_in_days: The refresh_token_retention_period_in_days of this CreateAuthenticationProviderDetails.
        :type: int
        """
        self._refresh_token_retention_period_in_days = refresh_token_retention_period_in_days

    @property
    def redirect_url(self):
        """
        Gets the redirect_url of this CreateAuthenticationProviderDetails.
        The OAuth Redirect URL.


        :return: The redirect_url of this CreateAuthenticationProviderDetails.
        :rtype: str
        """
        return self._redirect_url

    @redirect_url.setter
    def redirect_url(self, redirect_url):
        """
        Sets the redirect_url of this CreateAuthenticationProviderDetails.
        The OAuth Redirect URL.


        :param redirect_url: The redirect_url of this CreateAuthenticationProviderDetails.
        :type: str
        """
        self._redirect_url = redirect_url

    @property
    def is_visible(self):
        """
        Gets the is_visible of this CreateAuthenticationProviderDetails.
        Whether this Authentication Provider is visible in the ODA UI.


        :return: The is_visible of this CreateAuthenticationProviderDetails.
        :rtype: bool
        """
        return self._is_visible

    @is_visible.setter
    def is_visible(self, is_visible):
        """
        Sets the is_visible of this CreateAuthenticationProviderDetails.
        Whether this Authentication Provider is visible in the ODA UI.


        :param is_visible: The is_visible of this CreateAuthenticationProviderDetails.
        :type: bool
        """
        self._is_visible = is_visible

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this CreateAuthenticationProviderDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :return: The freeform_tags of this CreateAuthenticationProviderDetails.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this CreateAuthenticationProviderDetails.
        Simple key-value pair that is applied without any predefined name, type, or scope.
        Example: `{\"bar-key\": \"value\"}`


        :param freeform_tags: The freeform_tags of this CreateAuthenticationProviderDetails.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this CreateAuthenticationProviderDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :return: The defined_tags of this CreateAuthenticationProviderDetails.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this CreateAuthenticationProviderDetails.
        Usage of predefined tag keys. These predefined keys are scoped to namespaces.
        Example: `{\"foo-namespace\": {\"bar-key\": \"value\"}}`


        :param defined_tags: The defined_tags of this CreateAuthenticationProviderDetails.
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
