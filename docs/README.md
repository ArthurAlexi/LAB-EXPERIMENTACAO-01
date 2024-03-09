# Relatório

### Metodologia

Foi realizado requisições para a API do grafhQl do GitHub a fim de obter os dados dos 1000 repositórios necessários para responder as perguntas listadas a baixo, seguido das suas hipóteses informais.

O código utilizado tanto para as requisições quanto para o tratamento dos dados se encontram no diretório scripts.

### Hipóteses informais: 

#### RQ 01: Sistemas populares são maduros/antigos?
Hipótese informal: Sistemas populares tendem a ser mais antigos, uma vez que a maturidade e a popularidade geralmente exigem tempo para se desenvolverem.

#### RQ 02: Sistemas populares recebem muita contribuição externa?
Hipótese informal: Sistemas populares geralmente recebem uma quantidade significativa de contribuições externas, pois a popularidade tende a atrair uma comunidade maior de desenvolvedores interessados em colaborar. Porém, nem todas as contribuições são aceitas.

#### RQ 03: Sistemas populares lançam releases com frequência?
Hipótese informal: Sistemas populares tendem a lançar releases com frequência, já que uma comunidade ativa muitas vezes busca novas funcionalidades e correções de bugs regularmente.

#### RQ 04: Sistemas populares são atualizados com frequência?
Hipótese informal: Sistemas populares são frequentemente atualizados, pois a manutenção contínua é necessária para sustentar sua popularidade e atender às demandas da comunidade.

#### RQ 05: Sistemas populares são escritos nas linguagens mais populares?
Hipótese informal: Sistemas populares têm uma tendência a serem escritos nas linguagens de programação mais populares, uma vez que isso pode aumentar sua acessibilidade e atratividade para uma base de desenvolvedores mais ampla.

#### RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?
Hipótese informal: Sistemas populares tendem a ter um alto percentual de issues fechadas. Por dois fatores: esses sistemas possuem comunidade maior que geralmente implica em uma capacidade maior de resolver problemas e responder às necessidades dos usuários. E o outro fator é devido a complexidade e tamanho do sistema, tornando-se comum ter bugs e issues sendo fechadas.

### Análises: 
<strong>Dia em que os dados foram obtidos:</strong> 09/03/2024
#### RQ 01: Sistemas populares são maduros/antigos?

<strong>Definição:</strong> A base de comparação para saber se um sistema popular é ou não será com a idade do GitHub. Como a a data de criação 2008, teremos como base 16 anos para a análise a seguir.

<strong>Média:</strong> 7.73

<div style="display: flex;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/c0adab42-4f5f-4693-8e99-65b0ce3e3998" alt="violin plot Idades" style="width: 40%; height: auto;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/32242847-8742-47bc-8e60-3a6b7f73a82f" alt="boxplot Idades" style="width: 40%; height: auto;">
</div>

Com o uso de gráficos como o Violin Plot e o Box Plot, podemos analisar a distribuição das idades dos repositórios em relação à média, que é de 7.73. Notavelmente, observamos que não há uma grande dispersão nesses dados. Essa consistência sugere que os repositórios em questão são relativamente novos dentro do ecossistema do GitHub.

No entanto, apesar de sua relativa juventude, esses repositórios demonstram um amadurecimento notável ao longo do tempo. Sua capacidade de atrair uma base sólida de popularidade indica que, embora tenham tido um período relativamente curto de existência, conseguiram aproveitar esse tempo de forma eficiente para estabelecer uma presença significativa e atrair interesse dentro da comunidade do GitHub.

<div style"display: flex; justify-content: center;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/8c097e10-b256-41eb-9a32-c7ac0362092c" alt="" style="width: 80%; height: auto;">
</div>

Ao examinarmos o gráfico de dispersão que relaciona o total de estrelas com a idade dos repositórios, notamos uma grande variedade. Dentro da faixa de 1 a 16 anos, podemos identificar repositórios com popularidade consideráveis, independentemente de sua idade.

Por isso, apesar da idade majoritária dos repositórios ser de 8 anos, não podemos inferir de forma definitiva que a popularidade esteja diretamente ligada à maturidade ou antiguidade dos sistemas.

Essa diversidade sugere que fatores além da  longevidade podem influenciar significamente sua popularidade. Como A qualidade do código, a utilidade do projeto, a relevância para a comunidade e outros aspectos podem desempenhar papéis igualmente importantes na determinação da popularidade e do sucesso de um repositório no GitHub.

#### RQ 02: Sistemas populares recebem muita contribuição externa?

<strong>Média:</strong> 2764.759

<div style="display: flex;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/b315dce8-2261-409c-882a-14ce1141c0b1" alt="" style="width: 60%; height: auto;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/d756364b-9137-4bd6-9d9c-7d421f569142" alt="violin plot Pull Requests" style="width: 30%; height: auto;">
</div>

Baseado nos gráficos acima, é possível ver que os sistemas populares aceitam um valor considerável de pull requests, na margem de 2500. Em alguns casos, esse valor supera 10000. 

Analisando os gráficos acima, podemos observar que os sistemas populares tendem a aceitar pull requests, com valores geralmente variando em torno de 2500. Em muitos casos, esse número ultrapassam a marca de 10000. 

Esses valores podem indicar a natureza colaborativa e aberta dos projetos populares no GitHub. A aceitação de um grande volume de pull requests sugere uma forte atividade de desenvolvimento nos projetos populares. Isso pode indicar não apenas uma base de usuários ativa, mas também um alto nível de interesse e contribuição por parte da comunidade de desenvolvedores.

#### RQ 03: Sistemas populares lançam releases com frequência?

<strong>Média:</strong> 87.354

<strong>total de releases iguais à 0:</strong> 326 

<div style="display: flex;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/635e9129-5ad3-46b9-8411-81b834452d63" alt="" style="width: 60%; height: auto;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/953d0ce4-523f-4b46-8062-b027eeeab4a5" alt="violin plot" style="width: 30%; height: auto;">
</div>

Ao examinarmos esta seção, é importante observar que os intervalos de lançamento de cada release não foram considerados, o que impede uma avaliação precisa da frequência de lançamento.

Entretanto, ao analisar os gráficos relacionados a essa parte, podemos observar que o total de releases dos sistemas geralmente se concentra em um intervalo entre 0 e 200. Este intervalo indica uma atividade considerável de lançamento de novas versões nos repositórios mais populares.

Outro aspecto que merece destaque é o número considerável de repositórios em que o total de releases é igual a 0. Esta observação levanta duas possíveis interpretações:

- O repositório pode não ter a intenção de liberar releases. Isso pode ocorrer em casos em que o repositório é utilizado apenas para propósitos educativos, experimentais ou para outros fins que não envolvem a distribuição regular de novas versões de software.

- O repositório pode não seguir o padrão comum de lançamentos para indicar suas atualizações. Em alguns casos, os desenvolvedores podem optar por não utilizar o recurso de releases do GitHub para gerenciar suas versões, optando por outras abordagens de versionamento ou métodos alternativos para indicar suas atualizações.


#### RQ 04: Sistemas populares são atualizados com frequência?
<strong>Média:</strong> 0.01

<div style="display: flex;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/7b02e0ac-3dca-4ec6-b366-6125f7f58f3a" alt="violin plot" style="width: 60%; height: auto;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/2ad6e8f1-894a-4058-8484-bcdc50d1a5cf" alt="" style="width: 30%; height: auto;">
</div>

Ao analisarmos os gráficos, observarmos que todos os repositórios receberam atualização no dia que foi construído a base de dados.

O ideal para realizar uma melhor avaliação seria observar o intervalo das alterações.

#### RQ 05: Sistemas populares são escritos nas linguagens mais populares?
<strong>Oberservação:</strong> Durante a análise dos dados, observamos que alguns repositórios não possuíam uma linguagem predominante associada a eles. Ao investigarmos mais de perto esses casos, identificamos que muitos desses repositórios se tratavam de recursos educacionais, tutoriais ou conteúdos similares.

Esses repositórios frequentemente continham uma variedade de tipos de arquivos, como PDFs, vídeos e documentos. Embora esses recursos sejam valiosos e úteis para a comunidade, o GitHub não os considera como uma linguagem de programação específica.

Diante dessa situação, decidimos categorizar esses casos como "outros" para fins de análise. Essa abordagem nos permite agrupar esses repositórios em uma categoria distinta, reconhecendo sua importância enquanto reconhecemos a falta de uma linguagem de programação predominante associada a eles.

![image](https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/816077db-dbb6-4d16-a41f-78cdf03d15c2)

![image](https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/11dffc41-fa76-4181-a195-2d895790a347)

#### RQ 06: Sistemas populares possuem um alto percentual de issues fechadas?

<strong>Definições:</strong> Para essa análise, consideramos o percentual:  Issues fechados / Total de issues

<strong>Média:</strong> 76.05347

<div style="display: flex;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/29077ac5-4dd2-4c13-a253-cba0cb23071b" alt="violin plot" style="width: 60%; height: auto;">
  <img src="https://github.com/ArthurAlexi/LAB-EXPERIMENTACAO-01/assets/90854173/63a6733b-39ea-42ac-8462-8181faf9cb5d" alt="" style="width: 30%; height: auto;">
</div>

Ao examinarmos os gráficos apresentados acima, fica evidente que os repositórios populares exibem uma alta taxa de fechamento de issues. Essa observação está alinhada com as métricas de atualização discutidas anteriormente, que destacaram a frequência de lançamentos, aceitação de pull requests e outras formas de engajamento com a comunidade de desenvolvedores.

A alta taxa de fechamento de issues sugere um compromisso significativo por parte dos responsáveis pelo repositório em resolver problemas relatados pela comunidade de usuários. 
