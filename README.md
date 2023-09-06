Aproveitando um template criado para um trabalho acadêmico, resolvi implementar e melhorar a plataforma do Heavy Metal Festival, que tem como propósito atrair o maior número de frequentadores possíveis, de todos os Estados brasileiros, oferecendo desconto sobre o valor inteiro do ingresso de acordo com a distância de deslocamento até o local do festival.  Em conjunto com todo o projeto do template, usei o Rasa software, um software de inteligência artificial, para criar um chatbot e auxilar os usuários da melhor forma possível, tirando suas dúvidas, principalmente sobre valores dos ingressos. Tanto o Rasa, quando o código em JavaScript, fazem a leitura dos dados dos Estados através de um arquivo JSON, e retornam seus valores, com os cálculos feitos mostrando o valor do ingresso que o usuário irá pagar, de acordo com seu deslocamento. Para criar a tela de chat, usei a lib Chatroom.js. Basta importar seu CDN e "chamar" sua função principal, onde poderemos configurar e fazer a requisição, via API, dos serviços do Rasa.

Para esse projeto foram usadas as seguintes ferramentas:
- Frontend: HTML, CSS, Bootstrap, Javascript e JQUERY;
- Backend: Python

Observação: Importante, ao iniciar o uso do projeto, criar um ambiente virtual (virtualenv). Após a criação do ambiente virtual, basta instalar as lib's necessárias.
Configurar, personalizar e treinar o Rasa.
