# Denúncia Fácil - API

## Comandos de acesso
### Comandos para Usuário
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

### Comandos para Ocorrência
**Cadastrar uma ocorrência:**

Aqui não foi passado alguns campos, como os de localização da denuncia e hora. Mas pode ser passado colocando &nomeDoParametro .. Ex: ...&hora=hh:mm:ss

http://localhost:5000/ocorrencia?cpf_usuario=88888888888&placa=ABC0000&tipo_ocorrencia=Estacionamento+proibido&descricao=Motorista+estacionou+na+frente+da+minha+garagem&data=2019-12-07

**Visualizar ocorrências:**

http://localhost:5000/ocorrencia/select

**Atualizar uma ocorrência:**

É preciso passar o id após update/

http://localhost:5000/ocorrencia/update/1/?parametros...

**Deletar uma ocorrência:**

É preciso passar o id após delete/

http://localhost:5000/ocorrencia/delete/1