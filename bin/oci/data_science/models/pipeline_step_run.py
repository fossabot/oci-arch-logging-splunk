# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class PipelineStepRun(object):
    """
    Detail of each StepRun.
    """

    #: A constant which can be used with the step_type property of a PipelineStepRun.
    #: This constant has a value of "ML_JOB"
    STEP_TYPE_ML_JOB = "ML_JOB"

    #: A constant which can be used with the step_type property of a PipelineStepRun.
    #: This constant has a value of "CUSTOM_SCRIPT"
    STEP_TYPE_CUSTOM_SCRIPT = "CUSTOM_SCRIPT"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "WAITING"
    LIFECYCLE_STATE_WAITING = "WAITING"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "CANCELING"
    LIFECYCLE_STATE_CANCELING = "CANCELING"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "DELETED"
    LIFECYCLE_STATE_DELETED = "DELETED"

    #: A constant which can be used with the lifecycle_state property of a PipelineStepRun.
    #: This constant has a value of "SKIPPED"
    LIFECYCLE_STATE_SKIPPED = "SKIPPED"

    def __init__(self, **kwargs):
        """
        Initializes a new PipelineStepRun object with values from keyword arguments. This class has the following subclasses and if you are using this class as input
        to a service operations then you should favor using a subclass over the base class:

        * :class:`~oci.data_science.models.PipelineCustomScriptStepRun`
        * :class:`~oci.data_science.models.PipelineMLJobStepRun`

        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param step_type:
            The value to assign to the step_type property of this PipelineStepRun.
            Allowed values for this property are: "ML_JOB", "CUSTOM_SCRIPT", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type step_type: str

        :param time_started:
            The value to assign to the time_started property of this PipelineStepRun.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this PipelineStepRun.
        :type time_finished: datetime

        :param step_name:
            The value to assign to the step_name property of this PipelineStepRun.
        :type step_name: str

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this PipelineStepRun.
            Allowed values for this property are: "WAITING", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "SKIPPED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this PipelineStepRun.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'step_type': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'step_name': 'str',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'step_type': 'stepType',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'step_name': 'stepName',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._step_type = None
        self._time_started = None
        self._time_finished = None
        self._step_name = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @staticmethod
    def get_subtype(object_dictionary):
        """
        Given the hash representation of a subtype of this class,
        use the info in the hash to return the class of the subtype.
        """
        type = object_dictionary['stepType']

        if type == 'CUSTOM_SCRIPT':
            return 'PipelineCustomScriptStepRun'

        if type == 'ML_JOB':
            return 'PipelineMLJobStepRun'
        else:
            return 'PipelineStepRun'

    @property
    def step_type(self):
        """
        **[Required]** Gets the step_type of this PipelineStepRun.
        The type of step.

        Allowed values for this property are: "ML_JOB", "CUSTOM_SCRIPT", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The step_type of this PipelineStepRun.
        :rtype: str
        """
        return self._step_type

    @step_type.setter
    def step_type(self, step_type):
        """
        Sets the step_type of this PipelineStepRun.
        The type of step.


        :param step_type: The step_type of this PipelineStepRun.
        :type: str
        """
        allowed_values = ["ML_JOB", "CUSTOM_SCRIPT"]
        if not value_allowed_none_or_none_sentinel(step_type, allowed_values):
            step_type = 'UNKNOWN_ENUM_VALUE'
        self._step_type = step_type

    @property
    def time_started(self):
        """
        **[Required]** Gets the time_started of this PipelineStepRun.
        The date and time the pipeline step run was started in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_started of this PipelineStepRun.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this PipelineStepRun.
        The date and time the pipeline step run was started in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_started: The time_started of this PipelineStepRun.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this PipelineStepRun.
        The date and time the pipeline step run finshed executing in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :return: The time_finished of this PipelineStepRun.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this PipelineStepRun.
        The date and time the pipeline step run finshed executing in the timestamp format defined by `RFC3339`__.

        __ https://tools.ietf.org/html/rfc3339


        :param time_finished: The time_finished of this PipelineStepRun.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def step_name(self):
        """
        **[Required]** Gets the step_name of this PipelineStepRun.
        The name of the step.


        :return: The step_name of this PipelineStepRun.
        :rtype: str
        """
        return self._step_name

    @step_name.setter
    def step_name(self, step_name):
        """
        Sets the step_name of this PipelineStepRun.
        The name of the step.


        :param step_name: The step_name of this PipelineStepRun.
        :type: str
        """
        self._step_name = step_name

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this PipelineStepRun.
        The state of the step run.

        Allowed values for this property are: "WAITING", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "SKIPPED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this PipelineStepRun.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this PipelineStepRun.
        The state of the step run.


        :param lifecycle_state: The lifecycle_state of this PipelineStepRun.
        :type: str
        """
        allowed_values = ["WAITING", "ACCEPTED", "IN_PROGRESS", "FAILED", "SUCCEEDED", "CANCELING", "CANCELED", "DELETED", "SKIPPED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this PipelineStepRun.
        Details of the state of the step run.


        :return: The lifecycle_details of this PipelineStepRun.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this PipelineStepRun.
        Details of the state of the step run.


        :param lifecycle_details: The lifecycle_details of this PipelineStepRun.
        :type: str
        """
        self._lifecycle_details = lifecycle_details

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
