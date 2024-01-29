# GIT e GITHUB

## Principais Comandos
git config --list \
Para listar as configurações atuais do diretório

git config --global user.name "usuariodogithub" \
Para conectar ao usuário do git hub

git config --global user.email "seuemail" \
Para conectar ao e-mail do github

git remote add origin link_para_o_repositório_do_seu_projeto \
Ligar o seu repositório local ao remoto

git clone \
Para clonar o repositório na sua máquina local

git pull \
Para atualizar o repositório local com a ultima versão do remoto

git push \
Para enviar a versão local do repositório para o remoto

Fork (github) \
Utilizar o fork no Github para salvar uma versão de um repositório no seu repositório

Pull Request (github) \
Quando fazemos uma alteração no repositório forkado e queremos enviar para o original. É uma requisição para o dono do repositório aceitar ou não!

git status \
verificar o sttaus dos arquivos e pastas dentro no nosso repositório local

git add . \
Para adicionar todos os arquivos na esteira do commit

git add "nome do arquivo" \
Para adicionar apenas um arquivo especifico na esteira do commit

git commit -m "comentários" \
Salvar última versão no repositório local com o comentário do que são as modificações deste commit.

git checkout -b nomebranch \
Criar uma nova Branch

git branch \
Verificar quantas e quais branchs temos

git merge nomebranch \
Para unir as branches após feita o Pull Request no Github

git branch -d nome_do_ramo \
Para excluir uma branch local

git push origin --delete nome_do_ramo \
Para excluir uma branch remoto

git log --merges \
Para visualizar os commits de merge

## Navegação Pastas
dir \
Listar as pastas de um diretório

cd \
Entrar em uma pasta

cd ..\ \
Voltar para o nível anterior da pasta

## Branch

Branch \
De maneira simplificada, os ramos (branches) no Git são semelhantes a um ramo de uma árvore, onde o tronco seria a base do código. Desse modo é possível criar diversos ramos e fazer alterações, enquanto a base permanece intacta. Por padrão o ramo principal é denominado de main!

É possível criar e apagar Branchs pelo Github. \

## Colaborando com projetos de outras pessoas

Fork \
Ao entrar no Github e dar um Fork você estará fazendo uma cópia daquele repositório na sua conta.

Atualizar o Fork \
Para manter o seu Fork atualizado é possivel comparar os repositórios no Github e depois solicitar um Pull Request e fazer a mesclagem.

Pull Request \
É a forma de enviar as suas alterações para o repositório original. É recomendado criar uma branch para depois enviar as alterações.