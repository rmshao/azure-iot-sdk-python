from serviceswagger import DeviceProvisioningServiceServiceRuntimeClient
from serviceswagger.models import IndividualEnrollment, EnrollmentGroup, AttestationMechanism, TpmAttestation, X509Attestation
from connection_string import ConnectionString

cs = ConnectionString("HostName=carter-dps-2.azure-devices-provisioning.net;SharedAccessKeyName=provisioningserviceowner;SharedAccessKey=uNqKlY3IR6fB+p78K9mck9PrDsF2uLYpt0r91Hq2gh0=")
print(cs)
client = DeviceProvisioningServiceServiceRuntimeClient(cs, "https://carter-dps-2.azure-devices-provisioning.net")

ie = client.device_enrollment.get("test")
ie = ie

# tpm = TpmAttestation(endorsement_key="my-ek")
# am = AttestationMechanism(type="tpm", tpm=tpm)
# ie = IndividualEnrollment(registration_id="reg-id", attestation=am)

# #This actually needs another model, not a string, but for ease of example we're just using a string
# x509 = X509Attestation(client_certificates="client-cert")
# am2 = AttestationMechanism(type="x509", x509=x509)
# eg = EnrollmentGroup(enrollment_group_id="group-id", attestation=am2)

# client.device_enrollment.create_or_update(id="reg-id", enrollment=ie)

# client.device_enrollment_group.create_or_update(id="group-id", enrollment_group=eg)


