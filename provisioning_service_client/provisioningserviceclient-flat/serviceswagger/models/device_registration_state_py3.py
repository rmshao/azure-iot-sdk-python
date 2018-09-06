# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeviceRegistrationState(Model):
    """Device registration state.

    All required parameters must be populated in order to send to Azure.

    :param registration_id: Required. Registration ID.
    :type registration_id: str
    :param created_date_time_utc: Registration create date time (in UTC).
    :type created_date_time_utc: datetime
    :param assigned_hub: Assigned Azure IoT Hub.
    :type assigned_hub: str
    :param device_id: Device ID.
    :type device_id: str
    :param status: Required. Enrollment status. Possible values include:
     'unassigned', 'assigning', 'assigned', 'failed', 'disabled'
    :type status: str or ~serviceswagger.models.enum
    :param error_code: Error code.
    :type error_code: int
    :param error_message: Error message.
    :type error_message: str
    :param last_updated_date_time_utc: Last updated date time (in UTC).
    :type last_updated_date_time_utc: datetime
    :param etag: The entity tag associated with the resource.
    :type etag: str
    """

    _validation = {
        'registration_id': {'required': True},
        'status': {'required': True},
    }

    _attribute_map = {
        'registration_id': {'key': 'registrationId', 'type': 'str'},
        'created_date_time_utc': {'key': 'createdDateTimeUtc', 'type': 'iso-8601'},
        'assigned_hub': {'key': 'assignedHub', 'type': 'str'},
        'device_id': {'key': 'deviceId', 'type': 'str'},
        'status': {'key': 'status', 'type': 'str'},
        'error_code': {'key': 'errorCode', 'type': 'int'},
        'error_message': {'key': 'errorMessage', 'type': 'str'},
        'last_updated_date_time_utc': {'key': 'lastUpdatedDateTimeUtc', 'type': 'iso-8601'},
        'etag': {'key': 'etag', 'type': 'str'},
    }

    def __init__(self, *, registration_id: str, status, created_date_time_utc=None, assigned_hub: str=None, device_id: str=None, error_code: int=None, error_message: str=None, last_updated_date_time_utc=None, etag: str=None, **kwargs) -> None:
        super(DeviceRegistrationState, self).__init__(**kwargs)
        self.registration_id = registration_id
        self.created_date_time_utc = created_date_time_utc
        self.assigned_hub = assigned_hub
        self.device_id = device_id
        self.status = status
        self.error_code = error_code
        self.error_message = error_message
        self.last_updated_date_time_utc = last_updated_date_time_utc
        self.etag = etag
