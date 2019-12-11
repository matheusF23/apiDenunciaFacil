# Denúncia Fácil - API

## Comandos de acesso
### Comandos para Usuário
**Cadastrar um usuário:**

[POST] https://api-denuncia-facil.herokuapp.com/user/email/arquivo.json

**Visualizar usuarios:**

[GET] https://api-denuncia-facil.herokuapp.com/user

**Visualizar usuarios por cpf:**

[GET] https://api-denuncia-facil.herokuapp.com/user/email

**Validar login**

[GET] https://api-denuncia-facil.herokuapp.com/user/email/senha

**Atualizar um usuário:**
É preciso passar o email

[PUT] https://api-denuncia-facil.herokuapp.com/user/email


**Deletar um usuário:**
É preciso passar o email

[DELETE] https://api-denuncia-facil.herokuapp.com/user/email

### Comandos para Ocorrência
**Cadastrar uma ocorrência:**

É preciso passar o cpf de quem fará a ocorrência

[POST] https://api-denuncia-facil.herokuapp.com/occurrence/email/arquivo.json

**Visualizar ocorrências:**

[GET] https://api-denuncia-facil.herokuapp.com/occurrence

**Visualizar ocorrência por id:**

[GET] https://api-denuncia-facil.herokuapp.com/occurrence/id

**Visualizar ocorrência por usuário:**

[GET] https://api-denuncia-facil.herokuapp.com/occurrence/user/cpf

**Atualizar uma ocorrência:**

É preciso passar o id

[PUT] https://api-denuncia-facil.herokuapp.com/occurrence/id

**Deletar uma ocorrência:**

É preciso passar o id

[DELETE] http://localhost:5000/ocorrencia/delete/id