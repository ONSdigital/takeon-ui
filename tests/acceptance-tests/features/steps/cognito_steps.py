import json

from behave import given
from pages.common.login_page import LoginPage

def user_modified(context, username, password, roles):
    if username in context.created_users:
        return not (
            context.created_users[username]["password"] == password
            and context.created_users[username]["roles"].sort() == roles.sort()
        )
    return True

@given(u'"{username}" exists with the password "{password}" and roles {roles}')
def create_user(context, username, password, roles):
    roles = json.loads(roles)
    if context.cognito.user_exists(username):
        if user_modified(context, username, password, roles):
            context.cognito.delete_user(username)
            context.created_users[username] = {"password": password, "roles": roles}
            context.cognito.create_user(username, password, roles)
    else:
        context.created_users[username] = {"password": password, "roles": roles}
        context.cognito.create_user(username, password, roles)

@given(u'"{username}" is logged in')
def login(context, username):
    LoginPage().login(username, context.created_users[username]["password"])
