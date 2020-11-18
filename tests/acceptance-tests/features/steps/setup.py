from behave import given


@given(u'{name} column is {col}')
def setup_data(context, name, col):
    try:
        context.columns[name] = int(col)
    except AttributeError:
        context.columns = dict()
        context.columns[name] = int(col)


@given(u'I have the "{value_type}" questions to check')
def get_question_codes_as_list(context, value_type):
    context.question_codes = []
    for row in context.table.rows:
        for cell in row.cells:
            context.question_codes.append(cell)
