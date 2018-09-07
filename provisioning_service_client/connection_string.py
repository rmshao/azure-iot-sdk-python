from msrest.authentication import Authentication
from sastoken import SasToken

CS_DELIMITER = ";"
CS_VAL_SEPARATOR = "="
HOST_NAME_LABEL = "HostName"
SHARED_ACCESS_KEY_NAME_LABEL = "SharedAccessKeyName"
SHARED_ACCESS_KEY_LABEL = "SharedAccessKey"

class ConnectionString(Authentication):

    def __init__(self, connection_string):
        super(ConnectionString, self).__init__()
        cs_args = connection_string.split(CS_DELIMITER)

        if len(cs_args) != 3:
            raise ValueError("Too many or too few values in the connection string")
        if len(cs_args) > len(set(cs_args)):
            raise ValueError("Duplicate item in connection string")

        for arg in cs_args:
            tokens = arg.split(CS_VAL_SEPARATOR, 1)

            if tokens[0] == HOST_NAME_LABEL:
                self.host_name = tokens[1]
            elif tokens[0] == SHARED_ACCESS_KEY_NAME_LABEL:
                self.shared_access_key_name = tokens[1]
            elif tokens[0] == SHARED_ACCESS_KEY_LABEL:
                self.shared_access_key = tokens[1]
            else:
                raise ValueError("Connection string contains incorrect values")

    def __repr__(self):
        return HOST_NAME_LABEL + CS_VAL_SEPARATOR + self.host_name + CS_DELIMITER + \
            SHARED_ACCESS_KEY_NAME_LABEL + CS_VAL_SEPARATOR + self.shared_access_key_name + CS_DELIMITER + \
            SHARED_ACCESS_KEY_LABEL + CS_VAL_SEPARATOR + self.shared_access_key

    def signed_session(self, session=None):
        session = super(ConnectionString, self).signed_session(session)

        #Authorization header 
        sastoken = SasToken(self.host_name, self.shared_access_key_name, self.shared_access_key)
        session.headers[self.header] = str(sastoken)

        return session

