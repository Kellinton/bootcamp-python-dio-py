contatos = {
    "ace@gmail.com": {"nome": "ace", "telefone": "3333-2221"},
    "luffy@gmail.com": {"nome": "luffy", "telefone": "3443-2121"},
    "zoro@gmail.com": {"nome": "zoro", "telefone": "3344-9871"},
    "sanji@gmail.com": {"nome": "sanji", "telefone": "3333-7766"},
}

resultado = (
    contatos.values()
)  # dict_values([{'nome': 'ace', 'telefone': '3333-2221'}, {'nome': 'luffy', 'telefone': '3443-2121'}, {'nome': 'zoro', 'telefone': '3344-9871'}, {'nome': 'sanji', 'telefone': '3333-7766'}])  # noqa
print(resultado)