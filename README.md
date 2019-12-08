# Denúncia Fácil - API

## Comandos de acesso
**Cadastrar um usuário:**

http://localhost:5000/user?name=nome&cpf=00000000000&username=username&email=email@gmail.com&senha=senha

**Visualizar usuarios:**

http://localhost:5000/user/select

**Atualizar um usuário:**
É preciso passar o cpf após update/

http://localhost:5000/user/update/00000000000/?name=nome&cpf=00000000000&username=username&email=email@gmail.com&senha=senha

**Deletar um usuário:**
É preciso passar o cpf após delete/

http://localhost:5000/user/delete/00000000000