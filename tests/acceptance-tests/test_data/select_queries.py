class SelectQueries:
    def survey_query(self, query_type, survey):
        if query_type.lower() == 'get the survey details with status form sent out':
            return "SELECT reference,period,survey FROM dev01.contributor WHERE survey='" + survey + "' and status='Form sent out' AND formid='100' ORDER BY period ASC LIMIT 1"
