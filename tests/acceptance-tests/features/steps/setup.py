from behave import given, when, then


@given(u'the url is {location}')
def step_impl(context, location):
    context.driver.get(location)

@given(u'{name} column is {col}')
def step_impl(context, name, col):
    try:
        context.columns[name] = int(col)
    except AttributeError:
        context.columns = dict()
        context.columns[name] = int(col)

