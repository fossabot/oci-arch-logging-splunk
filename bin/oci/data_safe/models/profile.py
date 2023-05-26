# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class Profile(object):
    """
    The comprehensive information about the user profiles available on a given target.
    It includes details such as profile name, failed login attempts, password reuse time, password verification function,
    password verification function implementation code snippet, sessions per user, connect time inactive account time,
    password lock time, cpu usage per session, target id, and compartment id.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new Profile object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param user_assessment_id:
            The value to assign to the user_assessment_id property of this Profile.
        :type user_assessment_id: str

        :param compartment_id:
            The value to assign to the compartment_id property of this Profile.
        :type compartment_id: str

        :param target_id:
            The value to assign to the target_id property of this Profile.
        :type target_id: str

        :param profile_name:
            The value to assign to the profile_name property of this Profile.
        :type profile_name: str

        :param user_count:
            The value to assign to the user_count property of this Profile.
        :type user_count: int

        :param failed_login_attempts:
            The value to assign to the failed_login_attempts property of this Profile.
        :type failed_login_attempts: str

        :param password_verification_function:
            The value to assign to the password_verification_function property of this Profile.
        :type password_verification_function: str

        :param password_verification_function_details:
            The value to assign to the password_verification_function_details property of this Profile.
        :type password_verification_function_details: str

        :param password_lock_time:
            The value to assign to the password_lock_time property of this Profile.
        :type password_lock_time: str

        :param password_life_time:
            The value to assign to the password_life_time property of this Profile.
        :type password_life_time: str

        :param password_reuse_max:
            The value to assign to the password_reuse_max property of this Profile.
        :type password_reuse_max: str

        :param password_reuse_time:
            The value to assign to the password_reuse_time property of this Profile.
        :type password_reuse_time: str

        :param password_rollover_time:
            The value to assign to the password_rollover_time property of this Profile.
        :type password_rollover_time: str

        :param password_grace_time:
            The value to assign to the password_grace_time property of this Profile.
        :type password_grace_time: str

        :param is_user_created:
            The value to assign to the is_user_created property of this Profile.
        :type is_user_created: bool

        :param sessions_per_user:
            The value to assign to the sessions_per_user property of this Profile.
        :type sessions_per_user: str

        :param inactive_account_time:
            The value to assign to the inactive_account_time property of this Profile.
        :type inactive_account_time: str

        :param connect_time:
            The value to assign to the connect_time property of this Profile.
        :type connect_time: str

        :param idle_time:
            The value to assign to the idle_time property of this Profile.
        :type idle_time: str

        :param composite_limit:
            The value to assign to the composite_limit property of this Profile.
        :type composite_limit: str

        :param cpu_per_call:
            The value to assign to the cpu_per_call property of this Profile.
        :type cpu_per_call: str

        :param cpu_per_session:
            The value to assign to the cpu_per_session property of this Profile.
        :type cpu_per_session: str

        :param logical_reads_per_call:
            The value to assign to the logical_reads_per_call property of this Profile.
        :type logical_reads_per_call: str

        :param logical_reads_per_session:
            The value to assign to the logical_reads_per_session property of this Profile.
        :type logical_reads_per_session: str

        :param private_sga:
            The value to assign to the private_sga property of this Profile.
        :type private_sga: str

        :param freeform_tags:
            The value to assign to the freeform_tags property of this Profile.
        :type freeform_tags: dict(str, str)

        :param defined_tags:
            The value to assign to the defined_tags property of this Profile.
        :type defined_tags: dict(str, dict(str, object))

        """
        self.swagger_types = {
            'user_assessment_id': 'str',
            'compartment_id': 'str',
            'target_id': 'str',
            'profile_name': 'str',
            'user_count': 'int',
            'failed_login_attempts': 'str',
            'password_verification_function': 'str',
            'password_verification_function_details': 'str',
            'password_lock_time': 'str',
            'password_life_time': 'str',
            'password_reuse_max': 'str',
            'password_reuse_time': 'str',
            'password_rollover_time': 'str',
            'password_grace_time': 'str',
            'is_user_created': 'bool',
            'sessions_per_user': 'str',
            'inactive_account_time': 'str',
            'connect_time': 'str',
            'idle_time': 'str',
            'composite_limit': 'str',
            'cpu_per_call': 'str',
            'cpu_per_session': 'str',
            'logical_reads_per_call': 'str',
            'logical_reads_per_session': 'str',
            'private_sga': 'str',
            'freeform_tags': 'dict(str, str)',
            'defined_tags': 'dict(str, dict(str, object))'
        }

        self.attribute_map = {
            'user_assessment_id': 'userAssessmentId',
            'compartment_id': 'compartmentId',
            'target_id': 'targetId',
            'profile_name': 'profileName',
            'user_count': 'userCount',
            'failed_login_attempts': 'failedLoginAttempts',
            'password_verification_function': 'passwordVerificationFunction',
            'password_verification_function_details': 'passwordVerificationFunctionDetails',
            'password_lock_time': 'passwordLockTime',
            'password_life_time': 'passwordLifeTime',
            'password_reuse_max': 'passwordReuseMax',
            'password_reuse_time': 'passwordReuseTime',
            'password_rollover_time': 'passwordRolloverTime',
            'password_grace_time': 'passwordGraceTime',
            'is_user_created': 'isUserCreated',
            'sessions_per_user': 'sessionsPerUser',
            'inactive_account_time': 'inactiveAccountTime',
            'connect_time': 'connectTime',
            'idle_time': 'idleTime',
            'composite_limit': 'compositeLimit',
            'cpu_per_call': 'cpuPerCall',
            'cpu_per_session': 'cpuPerSession',
            'logical_reads_per_call': 'logicalReadsPerCall',
            'logical_reads_per_session': 'logicalReadsPerSession',
            'private_sga': 'privateSga',
            'freeform_tags': 'freeformTags',
            'defined_tags': 'definedTags'
        }

        self._user_assessment_id = None
        self._compartment_id = None
        self._target_id = None
        self._profile_name = None
        self._user_count = None
        self._failed_login_attempts = None
        self._password_verification_function = None
        self._password_verification_function_details = None
        self._password_lock_time = None
        self._password_life_time = None
        self._password_reuse_max = None
        self._password_reuse_time = None
        self._password_rollover_time = None
        self._password_grace_time = None
        self._is_user_created = None
        self._sessions_per_user = None
        self._inactive_account_time = None
        self._connect_time = None
        self._idle_time = None
        self._composite_limit = None
        self._cpu_per_call = None
        self._cpu_per_session = None
        self._logical_reads_per_call = None
        self._logical_reads_per_session = None
        self._private_sga = None
        self._freeform_tags = None
        self._defined_tags = None

    @property
    def user_assessment_id(self):
        """
        **[Required]** Gets the user_assessment_id of this Profile.
        The OCID of the user assessment corresponding to the target under consideration.


        :return: The user_assessment_id of this Profile.
        :rtype: str
        """
        return self._user_assessment_id

    @user_assessment_id.setter
    def user_assessment_id(self, user_assessment_id):
        """
        Sets the user_assessment_id of this Profile.
        The OCID of the user assessment corresponding to the target under consideration.


        :param user_assessment_id: The user_assessment_id of this Profile.
        :type: str
        """
        self._user_assessment_id = user_assessment_id

    @property
    def compartment_id(self):
        """
        Gets the compartment_id of this Profile.
        The OCID of the compartment that contains the user assessment.


        :return: The compartment_id of this Profile.
        :rtype: str
        """
        return self._compartment_id

    @compartment_id.setter
    def compartment_id(self, compartment_id):
        """
        Sets the compartment_id of this Profile.
        The OCID of the compartment that contains the user assessment.


        :param compartment_id: The compartment_id of this Profile.
        :type: str
        """
        self._compartment_id = compartment_id

    @property
    def target_id(self):
        """
        Gets the target_id of this Profile.
        The OCID of the target database.


        :return: The target_id of this Profile.
        :rtype: str
        """
        return self._target_id

    @target_id.setter
    def target_id(self, target_id):
        """
        Sets the target_id of this Profile.
        The OCID of the target database.


        :param target_id: The target_id of this Profile.
        :type: str
        """
        self._target_id = target_id

    @property
    def profile_name(self):
        """
        **[Required]** Gets the profile_name of this Profile.
        The name of the profile.


        :return: The profile_name of this Profile.
        :rtype: str
        """
        return self._profile_name

    @profile_name.setter
    def profile_name(self, profile_name):
        """
        Sets the profile_name of this Profile.
        The name of the profile.


        :param profile_name: The profile_name of this Profile.
        :type: str
        """
        self._profile_name = profile_name

    @property
    def user_count(self):
        """
        Gets the user_count of this Profile.
        The number of users having a given profile.


        :return: The user_count of this Profile.
        :rtype: int
        """
        return self._user_count

    @user_count.setter
    def user_count(self, user_count):
        """
        Sets the user_count of this Profile.
        The number of users having a given profile.


        :param user_count: The user_count of this Profile.
        :type: int
        """
        self._user_count = user_count

    @property
    def failed_login_attempts(self):
        """
        Gets the failed_login_attempts of this Profile.
        Maximum times the user is allowed in fail login before the user account is locked.


        :return: The failed_login_attempts of this Profile.
        :rtype: str
        """
        return self._failed_login_attempts

    @failed_login_attempts.setter
    def failed_login_attempts(self, failed_login_attempts):
        """
        Sets the failed_login_attempts of this Profile.
        Maximum times the user is allowed in fail login before the user account is locked.


        :param failed_login_attempts: The failed_login_attempts of this Profile.
        :type: str
        """
        self._failed_login_attempts = failed_login_attempts

    @property
    def password_verification_function(self):
        """
        Gets the password_verification_function of this Profile.
        Name of the PL/SQL that can be used for password verification.


        :return: The password_verification_function of this Profile.
        :rtype: str
        """
        return self._password_verification_function

    @password_verification_function.setter
    def password_verification_function(self, password_verification_function):
        """
        Sets the password_verification_function of this Profile.
        Name of the PL/SQL that can be used for password verification.


        :param password_verification_function: The password_verification_function of this Profile.
        :type: str
        """
        self._password_verification_function = password_verification_function

    @property
    def password_verification_function_details(self):
        """
        Gets the password_verification_function_details of this Profile.
        Details about the PL/SQL that can be used for password verification.


        :return: The password_verification_function_details of this Profile.
        :rtype: str
        """
        return self._password_verification_function_details

    @password_verification_function_details.setter
    def password_verification_function_details(self, password_verification_function_details):
        """
        Sets the password_verification_function_details of this Profile.
        Details about the PL/SQL that can be used for password verification.


        :param password_verification_function_details: The password_verification_function_details of this Profile.
        :type: str
        """
        self._password_verification_function_details = password_verification_function_details

    @property
    def password_lock_time(self):
        """
        Gets the password_lock_time of this Profile.
        Number of days the user account remains locked after failed login.


        :return: The password_lock_time of this Profile.
        :rtype: str
        """
        return self._password_lock_time

    @password_lock_time.setter
    def password_lock_time(self, password_lock_time):
        """
        Sets the password_lock_time of this Profile.
        Number of days the user account remains locked after failed login.


        :param password_lock_time: The password_lock_time of this Profile.
        :type: str
        """
        self._password_lock_time = password_lock_time

    @property
    def password_life_time(self):
        """
        Gets the password_life_time of this Profile.
        Number of days the password is valid before expiry.


        :return: The password_life_time of this Profile.
        :rtype: str
        """
        return self._password_life_time

    @password_life_time.setter
    def password_life_time(self, password_life_time):
        """
        Sets the password_life_time of this Profile.
        Number of days the password is valid before expiry.


        :param password_life_time: The password_life_time of this Profile.
        :type: str
        """
        self._password_life_time = password_life_time

    @property
    def password_reuse_max(self):
        """
        Gets the password_reuse_max of this Profile.
        Number of day after the user can use the already used password.


        :return: The password_reuse_max of this Profile.
        :rtype: str
        """
        return self._password_reuse_max

    @password_reuse_max.setter
    def password_reuse_max(self, password_reuse_max):
        """
        Sets the password_reuse_max of this Profile.
        Number of day after the user can use the already used password.


        :param password_reuse_max: The password_reuse_max of this Profile.
        :type: str
        """
        self._password_reuse_max = password_reuse_max

    @property
    def password_reuse_time(self):
        """
        Gets the password_reuse_time of this Profile.
        Number of days before which a password cannot be reused.


        :return: The password_reuse_time of this Profile.
        :rtype: str
        """
        return self._password_reuse_time

    @password_reuse_time.setter
    def password_reuse_time(self, password_reuse_time):
        """
        Sets the password_reuse_time of this Profile.
        Number of days before which a password cannot be reused.


        :param password_reuse_time: The password_reuse_time of this Profile.
        :type: str
        """
        self._password_reuse_time = password_reuse_time

    @property
    def password_rollover_time(self):
        """
        Gets the password_rollover_time of this Profile.
        Number of days the password rollover is allowed. Minimum value can be 1/24 day (1 hour) to 60 days.


        :return: The password_rollover_time of this Profile.
        :rtype: str
        """
        return self._password_rollover_time

    @password_rollover_time.setter
    def password_rollover_time(self, password_rollover_time):
        """
        Sets the password_rollover_time of this Profile.
        Number of days the password rollover is allowed. Minimum value can be 1/24 day (1 hour) to 60 days.


        :param password_rollover_time: The password_rollover_time of this Profile.
        :type: str
        """
        self._password_rollover_time = password_rollover_time

    @property
    def password_grace_time(self):
        """
        Gets the password_grace_time of this Profile.
        Number of grace days for user to change password.


        :return: The password_grace_time of this Profile.
        :rtype: str
        """
        return self._password_grace_time

    @password_grace_time.setter
    def password_grace_time(self, password_grace_time):
        """
        Sets the password_grace_time of this Profile.
        Number of grace days for user to change password.


        :param password_grace_time: The password_grace_time of this Profile.
        :type: str
        """
        self._password_grace_time = password_grace_time

    @property
    def is_user_created(self):
        """
        Gets the is_user_created of this Profile.
        Represents if the profile is created by user.


        :return: The is_user_created of this Profile.
        :rtype: bool
        """
        return self._is_user_created

    @is_user_created.setter
    def is_user_created(self, is_user_created):
        """
        Sets the is_user_created of this Profile.
        Represents if the profile is created by user.


        :param is_user_created: The is_user_created of this Profile.
        :type: bool
        """
        self._is_user_created = is_user_created

    @property
    def sessions_per_user(self):
        """
        Gets the sessions_per_user of this Profile.
        Specify the number of concurrent sessions to which you want to limit the user.


        :return: The sessions_per_user of this Profile.
        :rtype: str
        """
        return self._sessions_per_user

    @sessions_per_user.setter
    def sessions_per_user(self, sessions_per_user):
        """
        Sets the sessions_per_user of this Profile.
        Specify the number of concurrent sessions to which you want to limit the user.


        :param sessions_per_user: The sessions_per_user of this Profile.
        :type: str
        """
        self._sessions_per_user = sessions_per_user

    @property
    def inactive_account_time(self):
        """
        Gets the inactive_account_time of this Profile.
        The permitted periods of continuous inactive time during a session, expressed in minutes.
        Long-running queries and other operations are not subject to this limit.


        :return: The inactive_account_time of this Profile.
        :rtype: str
        """
        return self._inactive_account_time

    @inactive_account_time.setter
    def inactive_account_time(self, inactive_account_time):
        """
        Sets the inactive_account_time of this Profile.
        The permitted periods of continuous inactive time during a session, expressed in minutes.
        Long-running queries and other operations are not subject to this limit.


        :param inactive_account_time: The inactive_account_time of this Profile.
        :type: str
        """
        self._inactive_account_time = inactive_account_time

    @property
    def connect_time(self):
        """
        Gets the connect_time of this Profile.
        Specify the total elapsed time limit for a session, expressed in minutes.


        :return: The connect_time of this Profile.
        :rtype: str
        """
        return self._connect_time

    @connect_time.setter
    def connect_time(self, connect_time):
        """
        Sets the connect_time of this Profile.
        Specify the total elapsed time limit for a session, expressed in minutes.


        :param connect_time: The connect_time of this Profile.
        :type: str
        """
        self._connect_time = connect_time

    @property
    def idle_time(self):
        """
        Gets the idle_time of this Profile.
        Specify the permitted periods of continuous inactive time during a  session, expressed in minutes.


        :return: The idle_time of this Profile.
        :rtype: str
        """
        return self._idle_time

    @idle_time.setter
    def idle_time(self, idle_time):
        """
        Sets the idle_time of this Profile.
        Specify the permitted periods of continuous inactive time during a  session, expressed in minutes.


        :param idle_time: The idle_time of this Profile.
        :type: str
        """
        self._idle_time = idle_time

    @property
    def composite_limit(self):
        """
        Gets the composite_limit of this Profile.
        Specify the total resource cost for a session, expressed in service units. Oracle Database calculates the total
        service units as a weighted sum of CPU_PER_SESSION, CONNECT_TIME, LOGICAL_READS_PER_SESSION, and PRIVATE_SGA.


        :return: The composite_limit of this Profile.
        :rtype: str
        """
        return self._composite_limit

    @composite_limit.setter
    def composite_limit(self, composite_limit):
        """
        Sets the composite_limit of this Profile.
        Specify the total resource cost for a session, expressed in service units. Oracle Database calculates the total
        service units as a weighted sum of CPU_PER_SESSION, CONNECT_TIME, LOGICAL_READS_PER_SESSION, and PRIVATE_SGA.


        :param composite_limit: The composite_limit of this Profile.
        :type: str
        """
        self._composite_limit = composite_limit

    @property
    def cpu_per_call(self):
        """
        Gets the cpu_per_call of this Profile.
        Specify the CPU time limit for a call (a parse, execute, or fetch), expressed in hundredths of seconds.


        :return: The cpu_per_call of this Profile.
        :rtype: str
        """
        return self._cpu_per_call

    @cpu_per_call.setter
    def cpu_per_call(self, cpu_per_call):
        """
        Sets the cpu_per_call of this Profile.
        Specify the CPU time limit for a call (a parse, execute, or fetch), expressed in hundredths of seconds.


        :param cpu_per_call: The cpu_per_call of this Profile.
        :type: str
        """
        self._cpu_per_call = cpu_per_call

    @property
    def cpu_per_session(self):
        """
        Gets the cpu_per_session of this Profile.
        Specify the CPU time limit for a session, expressed in hundredth of seconds.


        :return: The cpu_per_session of this Profile.
        :rtype: str
        """
        return self._cpu_per_session

    @cpu_per_session.setter
    def cpu_per_session(self, cpu_per_session):
        """
        Sets the cpu_per_session of this Profile.
        Specify the CPU time limit for a session, expressed in hundredth of seconds.


        :param cpu_per_session: The cpu_per_session of this Profile.
        :type: str
        """
        self._cpu_per_session = cpu_per_session

    @property
    def logical_reads_per_call(self):
        """
        Gets the logical_reads_per_call of this Profile.
        Specify the permitted the number of data blocks read for a call to process a SQL statement (a parse, execute, or fetch).


        :return: The logical_reads_per_call of this Profile.
        :rtype: str
        """
        return self._logical_reads_per_call

    @logical_reads_per_call.setter
    def logical_reads_per_call(self, logical_reads_per_call):
        """
        Sets the logical_reads_per_call of this Profile.
        Specify the permitted the number of data blocks read for a call to process a SQL statement (a parse, execute, or fetch).


        :param logical_reads_per_call: The logical_reads_per_call of this Profile.
        :type: str
        """
        self._logical_reads_per_call = logical_reads_per_call

    @property
    def logical_reads_per_session(self):
        """
        Gets the logical_reads_per_session of this Profile.
        Specify the permitted number of data blocks read in a session, including blocks read from memory and disk.


        :return: The logical_reads_per_session of this Profile.
        :rtype: str
        """
        return self._logical_reads_per_session

    @logical_reads_per_session.setter
    def logical_reads_per_session(self, logical_reads_per_session):
        """
        Sets the logical_reads_per_session of this Profile.
        Specify the permitted number of data blocks read in a session, including blocks read from memory and disk.


        :param logical_reads_per_session: The logical_reads_per_session of this Profile.
        :type: str
        """
        self._logical_reads_per_session = logical_reads_per_session

    @property
    def private_sga(self):
        """
        Gets the private_sga of this Profile.
        Specify the amount of private space a session can allocate in the shared pool of the system global area (SGA),
        expressed in bytes.


        :return: The private_sga of this Profile.
        :rtype: str
        """
        return self._private_sga

    @private_sga.setter
    def private_sga(self, private_sga):
        """
        Sets the private_sga of this Profile.
        Specify the amount of private space a session can allocate in the shared pool of the system global area (SGA),
        expressed in bytes.


        :param private_sga: The private_sga of this Profile.
        :type: str
        """
        self._private_sga = private_sga

    @property
    def freeform_tags(self):
        """
        Gets the freeform_tags of this Profile.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The freeform_tags of this Profile.
        :rtype: dict(str, str)
        """
        return self._freeform_tags

    @freeform_tags.setter
    def freeform_tags(self, freeform_tags):
        """
        Sets the freeform_tags of this Profile.
        Free-form tags for this resource. Each tag is a simple key-value pair with no predefined name, type, or namespace. For more information, see `Resource Tags`__

        Example: `{\"Department\": \"Finance\"}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param freeform_tags: The freeform_tags of this Profile.
        :type: dict(str, str)
        """
        self._freeform_tags = freeform_tags

    @property
    def defined_tags(self):
        """
        Gets the defined_tags of this Profile.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :return: The defined_tags of this Profile.
        :rtype: dict(str, dict(str, object))
        """
        return self._defined_tags

    @defined_tags.setter
    def defined_tags(self, defined_tags):
        """
        Sets the defined_tags of this Profile.
        Defined tags for this resource. Each key is predefined and scoped to a namespace. For more information, see `Resource Tags`__

        Example: `{\"Operations\": {\"CostCenter\": \"42\"}}`

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/resourcetags.htm


        :param defined_tags: The defined_tags of this Profile.
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
