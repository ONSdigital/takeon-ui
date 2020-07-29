def filter_validations(validations):
    filtered_validations = []
    filtered_validation_outputs = {}
    for validation in validations['validation_outputs']:
        if validation['triggered']:
            filtered_validations.append(validation)
    filtered_validation_outputs['validation_outputs'] = filtered_validations
    return filtered_validation_outputs
