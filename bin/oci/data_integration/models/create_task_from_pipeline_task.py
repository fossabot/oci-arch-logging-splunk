# coding: utf-8
# Copyright (c) 2016, 2023, Oracle and/or its affiliates.  All rights reserved.
# This software is dual-licensed to you under the Universal Permissive License (UPL) 1.0 as shown at https://oss.oracle.com/licenses/upl or Apache License 2.0 as shown at http://www.apache.org/licenses/LICENSE-2.0. You may choose either license.

from .create_task_details import CreateTaskDetails
from oci.util import formatted_flat_dict, NONE_SENTINEL, value_allowed_none_or_none_sentinel  # noqa: F401
from oci.decorators import init_model_state_from_kwargs


@init_model_state_from_kwargs
class CreateTaskFromPipelineTask(CreateTaskDetails):
    """
    The information about the pipeline task.
    """

    def __init__(self, **kwargs):
        """
        Initializes a new CreateTaskFromPipelineTask object with values from keyword arguments. The default value of the :py:attr:`~oci.data_integration.models.CreateTaskFromPipelineTask.model_type` attribute
        of this class is ``PIPELINE_TASK`` and it should not be changed.
        The following keyword arguments are supported (corresponding to the getters/setters of this class):

        :param model_type:
            The value to assign to the model_type property of this CreateTaskFromPipelineTask.
            Allowed values for this property are: "INTEGRATION_TASK", "DATA_LOADER_TASK", "PIPELINE_TASK", "SQL_TASK", "OCI_DATAFLOW_TASK", "REST_TASK"
        :type model_type: str

        :param key:
            The value to assign to the key property of this CreateTaskFromPipelineTask.
        :type key: str

        :param model_version:
            The value to assign to the model_version property of this CreateTaskFromPipelineTask.
        :type model_version: str

        :param parent_ref:
            The value to assign to the parent_ref property of this CreateTaskFromPipelineTask.
        :type parent_ref: oci.data_integration.models.ParentReference

        :param name:
            The value to assign to the name property of this CreateTaskFromPipelineTask.
        :type name: str

        :param description:
            The value to assign to the description property of this CreateTaskFromPipelineTask.
        :type description: str

        :param object_status:
            The value to assign to the object_status property of this CreateTaskFromPipelineTask.
        :type object_status: int

        :param identifier:
            The value to assign to the identifier property of this CreateTaskFromPipelineTask.
        :type identifier: str

        :param input_ports:
            The value to assign to the input_ports property of this CreateTaskFromPipelineTask.
        :type input_ports: list[oci.data_integration.models.InputPort]

        :param output_ports:
            The value to assign to the output_ports property of this CreateTaskFromPipelineTask.
        :type output_ports: list[oci.data_integration.models.OutputPort]

        :param parameters:
            The value to assign to the parameters property of this CreateTaskFromPipelineTask.
        :type parameters: list[oci.data_integration.models.Parameter]

        :param op_config_values:
            The value to assign to the op_config_values property of this CreateTaskFromPipelineTask.
        :type op_config_values: oci.data_integration.models.ConfigValues

        :param config_provider_delegate:
            The value to assign to the config_provider_delegate property of this CreateTaskFromPipelineTask.
        :type config_provider_delegate: oci.data_integration.models.CreateConfigProvider

        :param registry_metadata:
            The value to assign to the registry_metadata property of this CreateTaskFromPipelineTask.
        :type registry_metadata: oci.data_integration.models.RegistryMetadata

        :param pipeline:
            The value to assign to the pipeline property of this CreateTaskFromPipelineTask.
        :type pipeline: oci.data_integration.models.Pipeline

        """
        self.swagger_types = {
            'model_type': 'str',
            'key': 'str',
            'model_version': 'str',
            'parent_ref': 'ParentReference',
            'name': 'str',
            'description': 'str',
            'object_status': 'int',
            'identifier': 'str',
            'input_ports': 'list[InputPort]',
            'output_ports': 'list[OutputPort]',
            'parameters': 'list[Parameter]',
            'op_config_values': 'ConfigValues',
            'config_provider_delegate': 'CreateConfigProvider',
            'registry_metadata': 'RegistryMetadata',
            'pipeline': 'Pipeline'
        }

        self.attribute_map = {
            'model_type': 'modelType',
            'key': 'key',
            'model_version': 'modelVersion',
            'parent_ref': 'parentRef',
            'name': 'name',
            'description': 'description',
            'object_status': 'objectStatus',
            'identifier': 'identifier',
            'input_ports': 'inputPorts',
            'output_ports': 'outputPorts',
            'parameters': 'parameters',
            'op_config_values': 'opConfigValues',
            'config_provider_delegate': 'configProviderDelegate',
            'registry_metadata': 'registryMetadata',
            'pipeline': 'pipeline'
        }

        self._model_type = None
        self._key = None
        self._model_version = None
        self._parent_ref = None
        self._name = None
        self._description = None
        self._object_status = None
        self._identifier = None
        self._input_ports = None
        self._output_ports = None
        self._parameters = None
        self._op_config_values = None
        self._config_provider_delegate = None
        self._registry_metadata = None
        self._pipeline = None
        self._model_type = 'PIPELINE_TASK'

    @property
    def pipeline(self):
        """
        Gets the pipeline of this CreateTaskFromPipelineTask.

        :return: The pipeline of this CreateTaskFromPipelineTask.
        :rtype: oci.data_integration.models.Pipeline
        """
        return self._pipeline

    @pipeline.setter
    def pipeline(self, pipeline):
        """
        Sets the pipeline of this CreateTaskFromPipelineTask.

        :param pipeline: The pipeline of this CreateTaskFromPipelineTask.
        :type: oci.data_integration.models.Pipeline
        """
        self._pipeline = pipeline

    def __repr__(self):
        return formatted_flat_dict(self)

    def __eq__(self, other):
        if other is None:
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
