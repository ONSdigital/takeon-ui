from botocore.config import Config
import boto3
import os


class Cognito:
    def __init__(self):
        aws_region = os.getenv("AWS_REGION", "eu-west-2")
        self._user_pool = None
        self._client = boto3.client("cognito-idp", config=Config(region_name=aws_region))

    def user_pool(self):
        if not self._user_pool:
            user_pool_name = os.environ["COGNITO_USER_POOL"]
            user_pools = self._client.list_user_pools(MaxResults=60)
            for user_pool in user_pools["UserPools"]:
                if user_pool["Name"] == user_pool_name:
                    self._user_pool = user_pool
                    break
        return self._user_pool

    def user_exists(self, username):
        users = self._client.list_users(
            UserPoolId=self.user_pool()["Id"]
        )
        return username in [user["Username"] for user in users["Users"]]

    def create_user(self, username, password, roles):
        self._client.admin_create_user(
            UserPoolId=self.user_pool()["Id"],
            Username=username,
        )
        self._client.admin_set_user_password(
            UserPoolId=self.user_pool()["Id"],
            Username=username,
            Password=password,
            Permanent=True,
        )
        for role in roles:
            self._client.admin_add_user_to_group(
                UserPoolId=self.user_pool()["Id"],
                Username=username,
                GroupName=role
            )

    def delete_user(self, username):
        self._client.admin_delete_user(
            UserPoolId=self.user_pool()["Id"],
            Username=username
        )
