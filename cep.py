import brazilcep as bc

def consultar_cep(cep=''):

    try:
        endereco = bc.get_address_from_cep(cep)

    except bc.exceptions.InvalidCEP as endereco:
        print('CEP Inválido.')
        exit()

    except bc.exceptions.CEPNotFound as endereco:
        print('CEP não encontrado.')
        exit()

    except bc.exceptions.ConnectionError as endereco:
        print('Erro de Conexão.')
        exit()

    except bc.exceptions.Timeout as endereco:
        print('Tempo excedido.')
        exit()

    except bc.exceptions.HTTPError as endereco:
        print('Erro HTTP.')
        exit()

    except bc.exceptions.BaseException as endereco:
        print('Erro Desconhecido.')
        exit()

    return endereco


print('-' * 40)
print(f'|{"Consultar CEP | Correios":^38}|')

cep_para_consultar = ''
cep_consultado = ''
user_resp = ''

while user_resp != 'N':
    print('-' * 40)
    cep_para_consultar = input('CEP: ').strip()
    cep_consultado = consultar_cep(cep_para_consultar)

    print('Estado:', cep_consultado['uf'])
    print('Cidade:', cep_consultado['city'])
    print('Bairro:', cep_consultado['district'])
    print('Logradouro:', cep_consultado['street'])
    print('CEP:', cep_consultado['cep'])

    user_resp = input('Deseja consultar outro CEP [S/N]? ').upper().strip()

    if user_resp != 'S' and user_resp != 'N':
        print('Por favor faça uma escolha válida.')
        user_resp = input('Deseja consultar outro CEP [S/N]? ').upper().strip()
