git checkout -b feature/pedido-logica
# Alterações na lógica do pedido, como calcular o preço, armazenar pedidos
git add .
git commit -m "Implementada a lógica de pedidos"
git push origin feature/pedido-logica

git checkout -b feature/listagem-pedidos
# Alterações para exibir os pedidos realizados
git add .
git commit -m "Implementada a funcionalidade de listagem de pedidos"
git push origin feature/listagem-pedidos

git checkout -b feature/testes
# Adicionar testes para a lógica ou a interface
git add .
git commit -m "Adicionados testes para pedidos"
git push origin feature/testes
