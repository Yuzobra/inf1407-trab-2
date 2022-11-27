# inf1407 Trabalho 2

## Aluno: Yuri Zoel Brasil
## Matricula: 1710730

## Relatório

Foi desenvolvido um site para anúncio e compra de jogos de tabuleiro. Na homepage é possivel a ver lista de todos os anúncios disponíveis (que não foram criados pelo usuário). Caso o usuário esteja logado ele é capaz de comprar o jogo.

Usuários logados podem criar anúncios. É também possível editá-los e deletá-los caso outro usuário ainda não tenha comprado o jogo.

Os campos que o usuário deve preencher para inserir o jogo são
 - Nome do jogo
 - Preço do anúncio
 - Data de lançamento do jogo
 - Estado do jogo
 - Link para uma imagem do jogo

Sendo o estado do jogo uma lista com as opções: Novo, Usado e degradado.

O usuário logado também pode ver o histórico das suas compras.

O projeto foi criado usando primáriamente django e HTML. Para o CSS utilizou-se o bootstrap, e o JQuery para adicionar algumas classes dinâmicamente durante a inicialização do projeto.