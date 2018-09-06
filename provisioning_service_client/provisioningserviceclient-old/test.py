from generatedclient.models import IndividualEnrollment, TpmAttestation, AttestationMechanism
#import logging

#logging.basicConfig()

#PyLong_Check(2)


def test_method():
    print("method called")


class TestClass:
    def __init__(self):
        self.method = test_method
    
    def natural_method(self):
        print("natural method called")

a = TestClass()
a.method()


# kwargs = {"endorsement_key": "ek"}
# tpm = TpmAttestation(**kwargs)
# am = AttestationMechanism(type="tpm", tpm=tpm)

# kwargs2 = {"registration_id": "reg_id", "attestation": am, "created_date_time_utc": "test"}
# ie = IndividualEnrollment(**kwargs2)
# #ie = IndividualEnrollment(registration_id="reg_id", attestation=am, created_date_time_utc="test")
# ie = ie