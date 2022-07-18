# Jokenpo Redes

O projeto é uma aplicação cliente-servidor de um jogo de Jokenpô, popularmente conhecido por “Pedra, Papel e Tesoura”. 

O servidor multi-threading vai receber conexões de clientes, que vão enviar suas jogadas (pedra, papel ou tesoura), e então vai responder com uma ação válida. O cliente vai receber essa resposta e exibir o resultado da partida ao usuário final da aplicação. O usuário poderá escolher novamente entre continuar jogando ou desconectar do servidor, encerrando assim o jogo.


## Instruções de como rodar a aplicação

1. Tenha o Python na versão 3.10.4 e certifique-se de que o comando `python3 --version` retorna `Python 3.10.4`. Caso tenha outras versões do Python em sua máquina e não queira fazer essa atualização, é possível criar um ambiente virtual utilizando *venv*. [Saiba mais](https://docs.python.org/3/library/venv.html).

2. Faça o clone desse git

3. Entre na pasta do projeto

4. Com o terminal aberto na pasta do projeto, execute o arquivo *server.py*:
```shell
python3 src/server.py
```

5. Em uma nova aba, na mesma pasta, execute o arquivo *client.py*: 
```shell
python3 src/client.py
```

6. Vale ressaltar que é possível executar diversos clientes ao mesmo tempo. Basta abrir novas abas e repetir o passo anterior.

7. Ao executar a aplicação cliente você receberá instruções de como jogar e os comandos disponíveis.
