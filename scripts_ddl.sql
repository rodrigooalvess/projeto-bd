create database flowcoffee

create table CLIENTES( 
id_cliente serial primary key, 
nome_cliente varchar(255) not null, 
cpf_cliente char(11) unique not null, 
endereco varchar(255) 
);

create table FUNCIONARIOS( 
id_funcionario serial primary key, 
nome_funcionario varchar(255) not null, 
cpf_funcionario char(11) not null unique, 
cargo char(1) not null check (cargo in ('A', 'C', 'E')),
senha varchar(100) not null,
ativo boolean not null default true
);

create table PRODUTOS( 
id_produto serial primary key, 
nome_produto varchar(255) not null unique,
descricao text, 
valor_produto double precision not null, 
categoria char(1) not null check (categoria in ('C', 'B', 'D', 'S')),
ativo boolean not null default true
);

create table PEDIDOS( 
id_pedido serial primary key, 
id_cliente integer not null, 
constraint fk_cliente foreign key (id_cliente) references CLIENTES (id_cliente), 
id_funcionario integer not null, 
constraint fk_funcionario foreign key (id_funcionario) references FUNCIONARIOS (id_funcionario), 
hora_pedido timestamp not null default CURRENT_TIMESTAMP, 
valor_pedido double precision not null default 0, 
modalidade char(1) not null check (modalidade in ('L', 'E')),
status char(1) not null check (status in ('P', 'C', 'X')) default 'P'
);

create table DELIVERY( 
id_delivery serial primary key, 
id_pedido integer not null, 
constraint fk_pedido foreign key (id_pedido) references PEDIDOS (id_pedido), 
id_funcionario integer not null, 
constraint fk_funcionario foreign key (id_funcionario) references FUNCIONARIOS (id_funcionario) 
);

create table PRODUTOS_PEDIDOS( 
id_pedido integer not null, 
id_produto integer not null, 
primary key (id_pedido, id_produto), 
quantidade integer not null default 1, 
observacao text, 
constraint fk_pedido foreign key (id_pedido) references PEDIDOS (id_pedido), 
constraint fk_produto foreign key (id_produto) references PRODUTOS (id_produto) 
);