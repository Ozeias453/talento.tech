# Lanchonete OSP - Sistema de Pedidos

## Descrição

O projeto **Lanchonete OSP** é um sistema simples desenvolvido em Python, utilizando a biblioteca **Tkinter** para interface gráfica, que permite registrar pedidos de clientes em uma lanchonete. A aplicação permite que o atendente insira o nome do cliente, escolha o lanche desejado, defina se será incluído refrigerante e escolha entre **entrega** ou **retirada no local**. O sistema calcula automaticamente o valor total do pedido com base nas opções selecionadas.

### Funcionalidades

- **Cadastro de cliente**: Registra o nome do cliente para cada pedido.
- **Escolha de lanche**: O atendente pode escolher entre os seguintes lanches:
  - Hambúrguer - R$ 10
  - X-Burguer - R$ 9
  - X-Salada - R$ 11
  - X-Bacon - R$ 14
  - Vegano - R$ 13
- **Opção de refrigerante**: Adiciona um refrigerante por R$ 4, caso o cliente deseje.
- **Forma de entrega**: O cliente pode escolher entre **entrega** ou **retirada no local**.
- **Cálculo automático**: O sistema calcula automaticamente o total do pedido com base no lanche e no refrigerante (se houver).
- **Exibição dos pedidos**: Uma lista de todos os pedidos feitos é exibida na interface, incluindo o nome do cliente, lanche escolhido, refrigerante e forma de entrega.

### Objetivo

O objetivo deste sistema é facilitar o processo de registro de pedidos na lanchonete, proporcionando uma interface simples e intuitiva para os atendentes. O sistema automatiza o cálculo do valor total e organiza os pedidos de maneira eficiente, ajudando a otimizar o atendimento e reduzir erros no registro de pedidos.

---

## Como Usar

### Requisitos

- **Python 3.x** ou superior
- **Tkinter** (já incluído na instalação padrão do Python)

### Passos para rodar o projeto

1. **Baixe o repositório**:
   - Clone o repositório ou baixe o código-fonte diretamente em sua máquina.

2. **Instale o Python**:
   - Certifique-se de que o Python está instalado. Você pode verificar isso com o comando:
     ```bash
     python --version
     ```

   Caso o Python não esteja instalado, baixe a versão mais recente em [python.org](https://www.python.org/downloads/).

3. **Execute o código**:
   - Abra o terminal ou prompt de comando, navegue até o diretório onde o arquivo Python está localizado e execute o script:
     ```bash
     python nome_do_arquivo.py
     ```
   - A interface gráfica será aberta, permitindo registrar pedidos e visualizar a lista de pedidos realizados.

---

## Funcionalidades do Código

1. **Interface gráfica com Tkinter**:
   - A interface permite ao atendente registrar o nome do cliente, escolher o lanche, adicionar refrigerante e decidir entre **entrega** ou **retirada**.
   
2. **Cálculo de preço**:
   - O sistema calcula automaticamente o valor total do pedido considerando o lanche escolhido e se o refrigerante foi adicionado.

3. **Exibição de pedidos**:
   - Todos os pedidos realizados são exibidos em uma lista, com o nome do cliente, o lanche escolhido, refrigerante (se incluído) e a forma de entrega (entrega ou retirada).

---

## Exemplo de Uso

- Ao iniciar o programa, a interface gráfica permitirá ao atendente preencher o **nome do cliente**, selecionar o **lanche** desejado, indicar se o pedido terá **refrigerante** e escolher entre **entrega** ou **retirada**.
- Depois de preencher as informações, o atendente clica em **Registrar Pedido**, e o valor total é calculado automaticamente.
- O pedido é adicionado à lista de pedidos realizados, que será exibida na interface.

---

## Estrutura do Código

O código é dividido em funções responsáveis por cada tarefa:

1. **Função `registrar_pedido()`**:
   - Registra o pedido, calcula o valor total e exibe o pedido na lista de pedidos.

2. **Função `calcular_total()`**:
   - Calcula o valor total com base no lanche e no refrigerante (se aplicável).

3. **Função `adicionar_na_lista()`**:
   - Adiciona o pedido à lista de pedidos realizados.

---

## Contribuição

Sinta-se à vontade para contribuir com o projeto. Para isso, siga os passos abaixo:

1. Faça um fork do repositório.
2. Crie uma branch para a funcionalidade ou correção que deseja implementar.
3. Envie um pull request com suas alterações.

---

## Licença

Este projeto está licenciado sob a **MIT License** - consulte o arquivo [LICENSE](LICENSE) para mais detalhes.

---

### Agradecimentos

Obrigado por utilizar o sistema de pedidos da **Lanchonete OSP**! Se tiver dúvidas ou sugestões, fique à vontade para entrar em contato.

