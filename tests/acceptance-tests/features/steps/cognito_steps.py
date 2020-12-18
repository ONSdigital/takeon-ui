import json

from behave import given
from pages.common.login_page import LoginPage


@given(u'"{username}" exists with the password "{password}" and roles {roles}')
def create_user(context, username, password, roles):
    if context.cognito.user_exists(username):
        context.cognito.delete_user(username)
    context.created_users[username] = password
    context.cognito.create_user(username, password, json.loads(roles))

@given(u'"{username}" is logged in')
def login(context, username):
    LoginPage().login(username, context.created_users[username])
