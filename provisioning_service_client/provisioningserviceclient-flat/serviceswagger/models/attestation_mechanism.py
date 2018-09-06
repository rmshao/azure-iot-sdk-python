# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class AttestationMechanism(Model):
    """Device attestation method.

    All required parameters must be populated in order to send to Azure.

    :param type: Required. Possible values include: 'none', 'tpm', 'x509'
    :type type: str or ~serviceswagger.models.enum
    :param tpm:
    :type tpm: ~serviceswagger.models.TpmAttestation
    :param x509:
    :type x509: ~serviceswagger.models.X509Attestation
    """

    _validation = {
        'type': {'required': True},
    }

    _attribute_map = {
        'type': {'key': 'type', 'type': 'str'},
        'tpm': {'key': 'tpm', 'type': 'TpmAttestation'},
        'x509': {'key': 'x509', 'type': 'X509Attestation'},
    }

    def __init__(self, **kwargs):
        super(AttestationMechanism, self).__init__(**kwargs)
        self.type = kwargs.get('type', None)
        self.tpm = kwargs.get('tpm', None)
        self.x509 = kwargs.get('x509', None)
