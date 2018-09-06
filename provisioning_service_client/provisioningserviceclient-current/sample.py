from serviceswagger import DeviceProvisioningServiceServiceRuntimeClient
from serviceswagger.models import IndividualEnrollment, EnrollmentGroup, AttestationMechanism, TpmAttestation, X509Attestation

#still working on passing through Connection Strings here
client = DeviceProvisioningServiceServiceRuntimeClient()

tpm = TpmAttestation(endorsement_key="my-ek")
am = AttestationMechanism(type="tpm", tpm=tpm)
ie = IndividualEnrollment(registration_id="reg-id", attestation=am)

#This actually needs another model, not a string, but for ease of example we're just using a string
x509 = X509Attestation(client_certificates="client-cert")
am2 = AttestationMechanism(type="x509", x509=x509)
eg = EnrollmentGroup(enrollment_group_id="group-id", attestation=am2)

client.device_enrollment.create_or_update(id="reg-id", enrollment=ie)

client.device_enrollment_group.create_or_update(id="group-id", enrollment_group=eg)


