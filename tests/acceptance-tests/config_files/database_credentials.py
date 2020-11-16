import json

import boto3


class DatabaseCredentials:
    secret_name = "spp-es-takeon-bdd-rds"
    region_name = "eu-west-2"
    session = boto3.session.Session(profile_name='sandbox')

    def get_secret(self):
        # Create a Secrets Manager client
        client = self.session.client(
            service_name='secretsmanager',
            region_name=self.region_name
        )
        response = client.get_secret_value(
            SecretId=self.secret_name
        )
        return json.loads(response['SecretString'])
