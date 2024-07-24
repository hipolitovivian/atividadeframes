def diagnosticar(sintomas):
    diagnosticos = []

    if 'febre' in sintomas and 'tosse' in sintomas:
        diagnosticos.append('gripe')
    if 'febre' in sintomas and 'dor de cabeça' in sintomas:
        diagnosticos.append('gripe')
    if 'tosse' in sintomas and 'dor de cabeça' in sintomas:
        diagnosticos.append('gripe')
    if 'tosse' in sintomas and 'coriza' in sintomas:
        diagnosticos.append('resfriado')
    if 'tosse' in sintomas and 'dor de garganta' in sintomas:
        diagnosticos.append('resfriado')
    if 'coriza' in sintomas and 'espirros' in sintomas:
        diagnosticos.append('resfriado')
    if 'coriza' in sintomas and 'dor de cabeça' in sintomas:
        diagnosticos.append('alergia')
    if 'coriza' in sintomas and 'espirros' in sintomas:
        diagnosticos.append('alergia')
    if 'dor de cabeça' in sintomas and 'espirros' in sintomas:
        diagnosticos.append('alergia')
    if 'fadiga' in sintomas and 'dor de cabeça' in sintomas:
        diagnosticos.append('gripe')

    return diagnosticos

sintomas_paciente = ['tosse', 'coriza', 'espirros']
print(diagnosticar(sintomas_paciente))
