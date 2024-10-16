# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Serializer, Deserializer
from msrestazure import AzureConfiguration
from .version import VERSION
from .operations.configuration_operations import ConfigurationOperations
from .operations.statistics_operations import StatisticsOperations
from .operations.devices_operations import DevicesOperations
from .operations.bulk_registry_operations import BulkRegistryOperations
from .operations.query_operations import QueryOperations
from .operations.jobs_operations import JobsOperations
from .operations.cloud_to_device_messages_operations import CloudToDeviceMessagesOperations
from .operations.service_operations import ServiceOperations
from .operations.modules_operations import ModulesOperations
from .operations.digital_twin_operations import DigitalTwinOperations
from . import models


class IotHubGatewayServiceAPIsConfiguration(AzureConfiguration):
    """Configuration for IotHubGatewayServiceAPIs
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        if credentials is None:
            raise ValueError("Parameter 'credentials' must not be None.")
        if not base_url:
            base_url = 'https://fully-qualified-iothubname.azure-devices.net'

        super(IotHubGatewayServiceAPIsConfiguration, self).__init__(base_url)

        self.add_user_agent('iothubgatewayserviceapis/{}'.format(VERSION))
        self.add_user_agent('Azure-SDK-For-Python')

        self.credentials = credentials


class IotHubGatewayServiceAPIs(SDKClient):
    """IotHubGatewayServiceAPIs

    :ivar config: Configuration for client.
    :vartype config: IotHubGatewayServiceAPIsConfiguration

    :ivar configuration: Configuration operations
    :vartype configuration: azure.operations.ConfigurationOperations
    :ivar statistics: Statistics operations
    :vartype statistics: azure.operations.StatisticsOperations
    :ivar devices: Devices operations
    :vartype devices: azure.operations.DevicesOperations
    :ivar bulk_registry: BulkRegistry operations
    :vartype bulk_registry: azure.operations.BulkRegistryOperations
    :ivar query: Query operations
    :vartype query: azure.operations.QueryOperations
    :ivar jobs: Jobs operations
    :vartype jobs: azure.operations.JobsOperations
    :ivar cloud_to_device_messages: CloudToDeviceMessages operations
    :vartype cloud_to_device_messages: azure.operations.CloudToDeviceMessagesOperations
    :ivar service: Service operations
    :vartype service: azure.operations.ServiceOperations
    :ivar modules: Modules operations
    :vartype modules: azure.operations.ModulesOperations
    :ivar digital_twin: DigitalTwin operations
    :vartype digital_twin: azure.operations.DigitalTwinOperations

    :param credentials: Credentials needed for the client to connect to Azure.
    :type credentials: :mod:`A msrestazure Credentials
     object<msrestazure.azure_active_directory>`
    :param str base_url: Service URL
    """

    def __init__(
            self, credentials, base_url=None):

        self.config = IotHubGatewayServiceAPIsConfiguration(credentials, base_url)
        super(IotHubGatewayServiceAPIs, self).__init__(self.config.credentials, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2024-03-31'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.configuration = ConfigurationOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.statistics = StatisticsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.devices = DevicesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.bulk_registry = BulkRegistryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.query = QueryOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.jobs = JobsOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.cloud_to_device_messages = CloudToDeviceMessagesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.service = ServiceOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.modules = ModulesOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.digital_twin = DigitalTwinOperations(
            self._client, self.config, self._serialize, self._deserialize)
