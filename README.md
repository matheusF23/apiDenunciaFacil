# Denúncia Fácil - API

## Comandos de acesso
### Comandos para Usuário
**Cadastrar um usuário:**

[POST] https://api-denuncia-facil.herokuapp.com/user/cpf/arquivo.json

**Visualizar usuarios:**

[GET] https://api-denuncia-facil.herokuapp.com/user/

**Visualizar usuarios por cpf:**

[GET] https://api-denuncia-facil.herokuapp.com/user/cpf/

**Atualizar um usuário:**
É preciso passar o cpf

[PUT] https://api-denuncia-facil.herokuapp.com/user/cpf/


**Deletar um usuário:**
É preciso passar o cpf

[DELETE] https://api-denuncia-facil.herokuapp.com/user/cpf/

### Comandos para Ocorrência
**Cadastrar uma ocorrência:**

[POST] https://api-denuncia-facil.herokuapp.com/ocurrence/arquivo.json

**Visualizar ocorrências:**

[GET] https://api-denuncia-facil.herokuapp.com/ocurrence/

**Visualizar ocorrência por id:**

[GET] https://api-denuncia-facil.herokuapp.com/ocurrence/id/

**Atualizar uma ocorrência:**

É preciso passar o id

[PUT] https://api-denuncia-facil.herokuapp.com/ocurrence/id/

**Deletar uma ocorrência:**

É preciso passar o id

[DELETE] http://localhost:5000/ocorrencia/delete/1