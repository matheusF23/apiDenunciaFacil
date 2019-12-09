import sqlite3

# conectando...
conn = sqlite3.connect('denunciafacil.db')
# definindo um cursor
cursor = conn.cursor()

# criando as tabelas
usuario = """
            create table usuario(
                cpf varchar(11) primary key,
                email varchar(50) not null,
                username varchar(30) not null,
                nome varchar(50) not null,
                senha varchar(30) not null
            );
        """

motorista = """
            create table motorista(
                cpf varchar(11) primary key,
                nome varchar(50) not null
            );
        """

veiculo = """
            create table veiculo(
                placa varchar(7) primary key,
                modelo varchar(20),
                tipo_veiculo varchar(20),
                cor varchar(10),
                cpf_motorista varchar(11) not null,
                foreign key(cpf_motorista) references motorista(cpf)
            );
        """

ocorrencia = """
            create table ocorrencia(
                id integer primary key autoincrement,
                titulo varchar(100),
                tipo_ocorrencia varchar(100) not null,
                descricao text not null,
                data date not null,
                hora time,
                bairro varchar(60),
                rua varchar(60),
                cidade varchar(60) default 'São Luís',
                estado char(2) default 'MA',
                
                cpf_usuario  varchar(11) not null,
                placa varchar(7) not null,
                foreign key(cpf_usuario) references usuario(cpf),
                foreign key(placa) references veiculo(placa)
            );
        """

# cursor.execute(usuario)
# cursor.execute(motorista)
# cursor.execute(veiculo)
# cursor.execute(ocorrencia)




print('Tabelas criadas com sucesso.')
# desconectando...
conn.close()