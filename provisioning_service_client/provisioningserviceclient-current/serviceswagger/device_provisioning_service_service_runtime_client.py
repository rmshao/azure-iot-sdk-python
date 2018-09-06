# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.service_client import SDKClient
from msrest import Configuration, Serializer, Deserializer
from .version import VERSION
from .operations.device_enrollment_operations import DeviceEnrollmentOperations
from .operations.device_enrollment_group_operations import DeviceEnrollmentGroupOperations
from .operations.registration_state_operations import RegistrationStateOperations
from . import models


class DeviceProvisioningServiceServiceRuntimeClientConfiguration(Configuration):
    """Configuration for DeviceProvisioningServiceServiceRuntimeClient
    Note that all parameters used to create this instance are saved as instance
    attributes.

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        if not base_url:
            base_url = 'https://localhost'

        super(DeviceProvisioningServiceServiceRuntimeClientConfiguration, self).__init__(base_url)

        self.add_user_agent('deviceprovisioningserviceserviceruntimeclient/{}'.format(VERSION))


class DeviceProvisioningServiceServiceRuntimeClient(SDKClient):
    """API for service operations with the Azure IotHub Device Provisioning Service

    :ivar config: Configuration for client.
    :vartype config: DeviceProvisioningServiceServiceRuntimeClientConfiguration

    :ivar device_enrollment: DeviceEnrollment operations
    :vartype device_enrollment: serviceswagger.operations.DeviceEnrollmentOperations
    :ivar device_enrollment_group: DeviceEnrollmentGroup operations
    :vartype device_enrollment_group: serviceswagger.operations.DeviceEnrollmentGroupOperations
    :ivar registration_state: RegistrationState operations
    :vartype registration_state: serviceswagger.operations.RegistrationStateOperations

    :param str base_url: Service URL
    """

    def __init__(
            self, base_url=None):

        self.config = DeviceProvisioningServiceServiceRuntimeClientConfiguration(base_url)
        super(DeviceProvisioningServiceServiceRuntimeClient, self).__init__(None, self.config)

        client_models = {k: v for k, v in models.__dict__.items() if isinstance(v, type)}
        self.api_version = '2018-04-01'
        self._serialize = Serializer(client_models)
        self._deserialize = Deserializer(client_models)

        self.device_enrollment = DeviceEnrollmentOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.device_enrollment_group = DeviceEnrollmentGroupOperations(
            self._client, self.config, self._serialize, self._deserialize)
        self.registration_state = RegistrationStateOperations(
            self._client, self.config, self._serialize, self._deserialize)
