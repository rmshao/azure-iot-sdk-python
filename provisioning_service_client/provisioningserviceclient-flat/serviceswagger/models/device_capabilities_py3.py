# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class DeviceCapabilities(Model):
    """Device capabilities.

    All required parameters must be populated in order to send to Azure.

    :param iot_edge: Required. IoT Edge capability
    :type iot_edge: bool
    """

    _validation = {
        'iot_edge': {'required': True},
    }

    _attribute_map = {
        'iot_edge': {'key': 'iotEdge', 'type': 'bool'},
    }

    def __init__(self, *, iot_edge: bool, **kwargs) -> None:
        super(DeviceCapabilities, self).__init__(**kwargs)
        self.iot_edge = iot_edge
