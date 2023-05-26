# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.


from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class TranscriptionTask(object):
    """
    Description of Transcription Task.
    """

    #: A constant which can be used with the lifecycle_state property of a TranscriptionTask.
    #: This constant has a value of "ACCEPTED"
    LIFECYCLE_STATE_ACCEPTED = "ACCEPTED"

    #: A constant which can be used with the lifecycle_state property of a TranscriptionTask.
    #: This constant has a value of "IN_PROGRESS"
    LIFECYCLE_STATE_IN_PROGRESS = "IN_PROGRESS"

    #: A constant which can be used with the lifecycle_state property of a TranscriptionTask.
    #: This constant has a value of "SUCCEEDED"
    LIFECYCLE_STATE_SUCCEEDED = "SUCCEEDED"

    #: A constant which can be used with the lifecycle_state property of a TranscriptionTask.
    #: This constant has a value of "FAILED"
    LIFECYCLE_STATE_FAILED = "FAILED"

    #: A constant which can be used with the lifecycle_state property of a TranscriptionTask.
    #: This constant has a value of "CANCELED"
    LIFECYCLE_STATE_CANCELED = "CANCELED"

    def __init__(self, **kwargs):
        """
        Initializes a new TranscriptionTask object with values from keyword arguments.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param id:
            The value to assign to the id property of this TranscriptionTask.
        :type id: str

        :param display_name:
            The value to assign to the display_name property of this TranscriptionTask.
        :type display_name: str

        :param time_started:
            The value to assign to the time_started property of this TranscriptionTask.
        :type time_started: datetime

        :param time_finished:
            The value to assign to the time_finished property of this TranscriptionTask.
        :type time_finished: datetime

        :param percent_complete:
            The value to assign to the percent_complete property of this TranscriptionTask.
        :type percent_complete: int

        :param ttl_in_days:
            The value to assign to the ttl_in_days property of this TranscriptionTask.
        :type ttl_in_days: int

        :param model_details:
            The value to assign to the model_details property of this TranscriptionTask.
        :type model_details: oci.ai_speech.models.TranscriptionModelDetails

        :param audio_format_details:
            The value to assign to the audio_format_details property of this TranscriptionTask.
        :type audio_format_details: oci.ai_speech.models.AudioFormatDetails

        :param file_size_in_bytes:
            The value to assign to the file_size_in_bytes property of this TranscriptionTask.
        :type file_size_in_bytes: int

        :param file_duration_in_seconds:
            The value to assign to the file_duration_in_seconds property of this TranscriptionTask.
        :type file_duration_in_seconds: int

        :param processing_duration_in_seconds:
            The value to assign to the processing_duration_in_seconds property of this TranscriptionTask.
        :type processing_duration_in_seconds: int

        :param input_location:
            The value to assign to the input_location property of this TranscriptionTask.
        :type input_location: oci.ai_speech.models.ObjectLocation

        :param output_location:
            The value to assign to the output_location property of this TranscriptionTask.
        :type output_location: oci.ai_speech.models.ObjectLocation

        :param lifecycle_state:
            The value to assign to the lifecycle_state property of this TranscriptionTask.
            Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
            Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.
        :type lifecycle_state: str

        :param lifecycle_details:
            The value to assign to the lifecycle_details property of this TranscriptionTask.
        :type lifecycle_details: str

        """
        self.swagger_types = {
            'id': 'str',
            'display_name': 'str',
            'time_started': 'datetime',
            'time_finished': 'datetime',
            'percent_complete': 'int',
            'ttl_in_days': 'int',
            'model_details': 'TranscriptionModelDetails',
            'audio_format_details': 'AudioFormatDetails',
            'file_size_in_bytes': 'int',
            'file_duration_in_seconds': 'int',
            'processing_duration_in_seconds': 'int',
            'input_location': 'ObjectLocation',
            'output_location': 'ObjectLocation',
            'lifecycle_state': 'str',
            'lifecycle_details': 'str'
        }

        self.attribute_map = {
            'id': 'id',
            'display_name': 'displayName',
            'time_started': 'timeStarted',
            'time_finished': 'timeFinished',
            'percent_complete': 'percentComplete',
            'ttl_in_days': 'ttlInDays',
            'model_details': 'modelDetails',
            'audio_format_details': 'audioFormatDetails',
            'file_size_in_bytes': 'fileSizeInBytes',
            'file_duration_in_seconds': 'fileDurationInSeconds',
            'processing_duration_in_seconds': 'processingDurationInSeconds',
            'input_location': 'inputLocation',
            'output_location': 'outputLocation',
            'lifecycle_state': 'lifecycleState',
            'lifecycle_details': 'lifecycleDetails'
        }

        self._id = None
        self._display_name = None
        self._time_started = None
        self._time_finished = None
        self._percent_complete = None
        self._ttl_in_days = None
        self._model_details = None
        self._audio_format_details = None
        self._file_size_in_bytes = None
        self._file_duration_in_seconds = None
        self._processing_duration_in_seconds = None
        self._input_location = None
        self._output_location = None
        self._lifecycle_state = None
        self._lifecycle_details = None

    @property
    def id(self):
        """
        **[Required]** Gets the id of this TranscriptionTask.
        The `OCID`__ of the task.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :return: The id of this TranscriptionTask.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """
        Sets the id of this TranscriptionTask.
        The `OCID`__ of the task.

        __ https://docs.cloud.oracle.com/iaas/Content/General/Concepts/identifiers.htm


        :param id: The id of this TranscriptionTask.
        :type: str
        """
        self._id = id

    @property
    def display_name(self):
        """
        Gets the display_name of this TranscriptionTask.
        A user-friendly display name for the task.


        :return: The display_name of this TranscriptionTask.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """
        Sets the display_name of this TranscriptionTask.
        A user-friendly display name for the task.


        :param display_name: The display_name of this TranscriptionTask.
        :type: str
        """
        self._display_name = display_name

    @property
    def time_started(self):
        """
        Gets the time_started of this TranscriptionTask.
        Task started time.


        :return: The time_started of this TranscriptionTask.
        :rtype: datetime
        """
        return self._time_started

    @time_started.setter
    def time_started(self, time_started):
        """
        Sets the time_started of this TranscriptionTask.
        Task started time.


        :param time_started: The time_started of this TranscriptionTask.
        :type: datetime
        """
        self._time_started = time_started

    @property
    def time_finished(self):
        """
        Gets the time_finished of this TranscriptionTask.
        Task finished time.


        :return: The time_finished of this TranscriptionTask.
        :rtype: datetime
        """
        return self._time_finished

    @time_finished.setter
    def time_finished(self, time_finished):
        """
        Sets the time_finished of this TranscriptionTask.
        Task finished time.


        :param time_finished: The time_finished of this TranscriptionTask.
        :type: datetime
        """
        self._time_finished = time_finished

    @property
    def percent_complete(self):
        """
        Gets the percent_complete of this TranscriptionTask.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :return: The percent_complete of this TranscriptionTask.
        :rtype: int
        """
        return self._percent_complete

    @percent_complete.setter
    def percent_complete(self, percent_complete):
        """
        Sets the percent_complete of this TranscriptionTask.
        How much progress the operation has made, vs the total amount of work that must be performed.


        :param percent_complete: The percent_complete of this TranscriptionTask.
        :type: int
        """
        self._percent_complete = percent_complete

    @property
    def ttl_in_days(self):
        """
        Gets the ttl_in_days of this TranscriptionTask.
        Time to live duration in days for tasks. Task will be available till max 90 days.


        :return: The ttl_in_days of this TranscriptionTask.
        :rtype: int
        """
        return self._ttl_in_days

    @ttl_in_days.setter
    def ttl_in_days(self, ttl_in_days):
        """
        Sets the ttl_in_days of this TranscriptionTask.
        Time to live duration in days for tasks. Task will be available till max 90 days.


        :param ttl_in_days: The ttl_in_days of this TranscriptionTask.
        :type: int
        """
        self._ttl_in_days = ttl_in_days

    @property
    def model_details(self):
        """
        Gets the model_details of this TranscriptionTask.

        :return: The model_details of this TranscriptionTask.
        :rtype: oci.ai_speech.models.TranscriptionModelDetails
        """
        return self._model_details

    @model_details.setter
    def model_details(self, model_details):
        """
        Sets the model_details of this TranscriptionTask.

        :param model_details: The model_details of this TranscriptionTask.
        :type: oci.ai_speech.models.TranscriptionModelDetails
        """
        self._model_details = model_details

    @property
    def audio_format_details(self):
        """
        Gets the audio_format_details of this TranscriptionTask.

        :return: The audio_format_details of this TranscriptionTask.
        :rtype: oci.ai_speech.models.AudioFormatDetails
        """
        return self._audio_format_details

    @audio_format_details.setter
    def audio_format_details(self, audio_format_details):
        """
        Sets the audio_format_details of this TranscriptionTask.

        :param audio_format_details: The audio_format_details of this TranscriptionTask.
        :type: oci.ai_speech.models.AudioFormatDetails
        """
        self._audio_format_details = audio_format_details

    @property
    def file_size_in_bytes(self):
        """
        Gets the file_size_in_bytes of this TranscriptionTask.
        Size of input file in Bytes.


        :return: The file_size_in_bytes of this TranscriptionTask.
        :rtype: int
        """
        return self._file_size_in_bytes

    @file_size_in_bytes.setter
    def file_size_in_bytes(self, file_size_in_bytes):
        """
        Sets the file_size_in_bytes of this TranscriptionTask.
        Size of input file in Bytes.


        :param file_size_in_bytes: The file_size_in_bytes of this TranscriptionTask.
        :type: int
        """
        self._file_size_in_bytes = file_size_in_bytes

    @property
    def file_duration_in_seconds(self):
        """
        Gets the file_duration_in_seconds of this TranscriptionTask.
        Duration of input file in Seconds.


        :return: The file_duration_in_seconds of this TranscriptionTask.
        :rtype: int
        """
        return self._file_duration_in_seconds

    @file_duration_in_seconds.setter
    def file_duration_in_seconds(self, file_duration_in_seconds):
        """
        Sets the file_duration_in_seconds of this TranscriptionTask.
        Duration of input file in Seconds.


        :param file_duration_in_seconds: The file_duration_in_seconds of this TranscriptionTask.
        :type: int
        """
        self._file_duration_in_seconds = file_duration_in_seconds

    @property
    def processing_duration_in_seconds(self):
        """
        Gets the processing_duration_in_seconds of this TranscriptionTask.
        Task proccessing duration, which excludes waiting time in the system.


        :return: The processing_duration_in_seconds of this TranscriptionTask.
        :rtype: int
        """
        return self._processing_duration_in_seconds

    @processing_duration_in_seconds.setter
    def processing_duration_in_seconds(self, processing_duration_in_seconds):
        """
        Sets the processing_duration_in_seconds of this TranscriptionTask.
        Task proccessing duration, which excludes waiting time in the system.


        :param processing_duration_in_seconds: The processing_duration_in_seconds of this TranscriptionTask.
        :type: int
        """
        self._processing_duration_in_seconds = processing_duration_in_seconds

    @property
    def input_location(self):
        """
        Gets the input_location of this TranscriptionTask.

        :return: The input_location of this TranscriptionTask.
        :rtype: oci.ai_speech.models.ObjectLocation
        """
        return self._input_location

    @input_location.setter
    def input_location(self, input_location):
        """
        Sets the input_location of this TranscriptionTask.

        :param input_location: The input_location of this TranscriptionTask.
        :type: oci.ai_speech.models.ObjectLocation
        """
        self._input_location = input_location

    @property
    def output_location(self):
        """
        Gets the output_location of this TranscriptionTask.

        :return: The output_location of this TranscriptionTask.
        :rtype: oci.ai_speech.models.ObjectLocation
        """
        return self._output_location

    @output_location.setter
    def output_location(self, output_location):
        """
        Sets the output_location of this TranscriptionTask.

        :param output_location: The output_location of this TranscriptionTask.
        :type: oci.ai_speech.models.ObjectLocation
        """
        self._output_location = output_location

    @property
    def lifecycle_state(self):
        """
        Gets the lifecycle_state of this TranscriptionTask.
        The current state of the Task.

        Allowed values for this property are: "ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED", 'UNKNOWN_ENUM_VALUE'.
        Any unrecognized values returned by a service will be mapped to 'UNKNOWN_ENUM_VALUE'.


        :return: The lifecycle_state of this TranscriptionTask.
        :rtype: str
        """
        return self._lifecycle_state

    @lifecycle_state.setter
    def lifecycle_state(self, lifecycle_state):
        """
        Sets the lifecycle_state of this TranscriptionTask.
        The current state of the Task.


        :param lifecycle_state: The lifecycle_state of this TranscriptionTask.
        :type: str
        """
        allowed_values = ["ACCEPTED", "IN_PROGRESS", "SUCCEEDED", "FAILED", "CANCELED"]
        if not value_allowed_none_or_none_sentinel(lifecycle_state, allowed_values):
            lifecycle_state = 'UNKNOWN_ENUM_VALUE'
        self._lifecycle_state = lifecycle_state

    @property
    def lifecycle_details(self):
        """
        Gets the lifecycle_details of this TranscriptionTask.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :return: The lifecycle_details of this TranscriptionTask.
        :rtype: str
        """
        return self._lifecycle_details

    @lifecycle_details.setter
    def lifecycle_details(self, lifecycle_details):
        """
        Sets the lifecycle_details of this TranscriptionTask.
        A message describing the current state in more detail. For example, can be used to provide actionable information for a resource in Failed state.


        :param lifecycle_details: The lifecycle_details of this TranscriptionTask.
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
