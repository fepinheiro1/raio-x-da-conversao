# Checklist — Busca Interna (protocolo de sonda)

A busca é onde a intenção de compra se declara: quem digita já sabe o que quer. Cada busca que falha descarta o visitante mais valioso do site. Este protocolo **testa a busca de verdade** — nada de julgar por aparência.

## Antes de começar

Monte as 8 consultas-sonda **adaptadas ao catálogo da loja** (use o carro-chefe informado na entrevista e o que você viu no menu). O padrão abaixo mostra o tipo; troque os exemplos pelo vocabulário do segmento.

> **Regra de ouro do protocolo:** execute cada sonda **pela interface real** — clicar no campo, digitar, apertar Enter. Nunca navegue para URLs de busca construídas à mão: elas podem cair em rotas diferentes das que o usuário vive e produzir falsos "zero resultados". E todo resultado **zero ou suspeitamente baixo** exige segunda confirmação pela interface, com espera generosa, antes de virar achado — páginas client-side às vezes renderizam "0 produtos" como estado intermediário de carregamento. Um falso "busca quebrada" no relatório destrói a credibilidade de todos os outros achados.

## As 8 consultas-sonda

Execute uma a uma na busca da loja (desktop). Para cada uma registre: consulta digitada, nº de resultados, os 3 primeiros itens retornados e veredito.

1. **Termo exato do carro-chefe** — ex.: o nome do produto principal. Se nem isso retorna bem posicionado, a busca está quebrada. *Falha aqui é crítico isolado.*
2. **Erro de digitação comum** — ex.: "tenis" sem acento, "camizeta", "vestido logno". Gente digita errado o tempo todo, especialmente no celular. Busca sem tolerância a erro = zero resultado para intenção real.
3. **Sinônimo popular** — o nome que o cliente usa, não o do catálogo. Ex.: "blusa de frio" (catálogo diz "moletom"), "tênis de corrida" (catálogo diz "running"). Revela se a busca entende gente ou só ficha técnica.
4. **Termo genérico da categoria** — ex.: "presente", "verão", "infantil". Deve retornar uma seleção coerente, não vazio nem caos.
5. **Marca vendida na loja** — se a loja é multimarca. Deve agrupar a marca inteira.
6. **Singular/plural ou variação de gênero** — ex.: "calça" vs "calças", "sandalia feminina". Busca literal quebra com variação mínima.
7. **Termo composto específico** — ex.: "vestido preto festa", "tênis branco 42". Testa se a busca combina atributos ou ignora metade da consulta.
8. **Termo que a loja NÃO vende** (contraprova) — deve dizer "não encontramos" com alternativa digna (categorias, mais vendidos), não uma página morta. O estado de zero resultado é a página mais mal cuidada do e-commerce médio — e é onde o cliente decide entre tentar de novo ou fechar a aba.
9. **Clique no 1º resultado do autocomplete do carro-chefe** — não basta o resultado *aparecer*: clique nele e confirme que a página abre com produto comprável. Lojas desativam produtos de campanha (datas sazonais, edições limitadas) e esquecem o índice de busca — o melhor clique do site passa a terminar em 404. É um achado frequente e devastador, e só aparece clicando.

## O que mais observar durante as sondas

- **Autocomplete** — Sugestões aparecem enquanto digita? Com produto (foto + preço) ou só texto?
- **Velocidade** — Resultado instantâneo ou recarrega a página inteira?
- **Filtros no resultado** — Dá para refinar a busca (preço, tamanho) ou o resultado é uma lista bruta?
- **Relevância do topo** — Nos vereditos, o critério é o top 3: o cliente não rola a página 2 da busca. Resultado "existe mas está na posição 40" conta como falha parcial.
- **Mobile** — Repita 2 sondas (a nº 2 e a nº 3) na viewport mobile. A busca está acessível sem abrir menu?

> **Dropdown ≠ página de resultados.** São frequentemente dois sistemas diferentes (ex.: autocomplete via Algolia, página via rota da plataforma). Teste os dois caminhos: escolher no dropdown E digitar + apertar Enter. Já vimos loja em que o dropdown mostrava 59 produtos de uma marca e o Enter retornava zero — e o Enter é o caminho mais comum.

## Como classificar

- **Falha total**: 0 resultados para termo que a loja claramente atende, top 3 irrelevante, ou resultado que leva a página morta/404.
- **Falha parcial**: encontra, mas mal posicionado, sem foto/preço no resultado, ou ignora parte do termo composto.
- **Passa**: top 3 relevante e rápido.

Calcule a **taxa de falha** (falhas totais + parciais/2, sobre as 7 sondas válidas — a contraprova é avaliada à parte pela qualidade do estado vazio). No relatório, apresente como tabela: consulta → o que voltou → veredito. É a evidência mais visceral do raio-x: o dono da loja reconhece cada termo.

## Critérios de nota (camada "Descoberta")

- Taxa de falha ≤15% e estado vazio digno: 8–10.
- Taxa de falha 15–40%: 5–7.
- Taxa de falha >40% **ou** falha na sonda 1: 0–4 — e o achado entra como candidato natural ao Top 5, porque busca é intenção declarada desperdiçada.
- Some a isso a qualidade de autocomplete, filtros e mobile.

> Contexto para o relatório: em lojas médias brasileiras, 40–60% de falha nas sondas é comum — e cada falha é um visitante de alta intenção dispensado. Busca nativa de plataforma costuma ser literal (sem erro de digitação, sem sinônimo); resolver isso geralmente exige tecnologia de busca dedicada — classifique o esforço como "estrutural/tecnologia" quando for o caso.
