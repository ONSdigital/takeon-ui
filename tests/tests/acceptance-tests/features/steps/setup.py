from behave import given

@given(u'{name} column is {col}')
def step_impl(context, name, col):
    try:
        context.columns[name] = int(col)
    except AttributeError:
        context.columns = dict()
        context.columns[name] = int(col)

