# Checklist — Página de Produto (PDP)

A PDP é onde a decisão acontece. Audite a PDP do **carro-chefe** (informado na entrevista) — a página que mais recebe dinheiro de mídia merece o pente-fino, não uma aleatória. Se der tempo, passe rápido por uma segunda PDP para ver se os achados se repetem (quase sempre são de template, não da página).

## Acima da dobra

- **Nome + preço visíveis sem rolar** — Preço escondido abaixo da dobra adiciona fricção na informação mais buscada.
- **Parcelamento explícito** — "10x de R$ 29,90" muda a percepção de preço no Brasil. Só o valor à vista subaproveita.
- **Desconto legível** — Se há promoção: preço de/por com % clara, ou o desconto exige cálculo mental?
- **Pix com desconto** — Se existe, está anunciado na PDP ou só aparece no checkout? Benefício invisível não influencia decisão.
- **CTA inconfundível** — O botão comprar/adicionar é o elemento mais forte da página? Cor única, texto direto? Botão tímido compete com banners.
- **Disponibilidade honesta** — Estoque claro, "últimas unidades" quando verdadeiro. Descobrir indisponibilidade só ao clicar em comprar é quebra de confiança.

## Mídia

- **Quantidade e ângulos** — Mínimo razoável: 4–5 fotos, produto em uso/escala, detalhe de textura. Uma foto só de catálogo não sustenta decisão.
- **Zoom funcional** — Especialmente mobile (pinça). Foto pequena sem zoom = cliente inseguro.
- **Vídeo** — Existe? Vídeo curto de produto em uso é dos maiores diferenciais de PDP e raríssimo em loja média.
- **Peso das imagens** — Fotos de 2+ MB sem compressão matam o LCP mobile (cruze com dados do coletor/PSI).

## Variações e escolha

- **Seletor de variação claro** — Cor/tamanho/voltagem como botões visíveis (não dropdown escondido), com estado indisponível marcado sem sumir a opção.
- **Guia de tamanhos** — Em moda/calçados: existe tabela de medidas acessível do seletor? Dúvida de tamanho é a maior causa de não-compra e de troca do segmento. Ausência é crítico em moda.
- **Foto muda com a variação** — Selecionar "azul" mostra o produto azul?

## Informação que vende

- **Descrição escaneável** — Bullets de benefício + ficha técnica separada, ou um bloco de texto corrido (ou pior: vazio, ou o texto padrão do fornecedor duplicado em 30 lojas)?
- **Frete e prazo na PDP** — Existe calculadora de CEP na página? Descobrir frete só no checkout é a receita clássica de abandono. Ausência é crítico.
- **Política de troca visível** — Link ou resumo perto do CTA ("troca grátis em 30 dias" reduz medo na hora exata).
- **Avaliações de clientes** — Existem? Com foto? Quantidade razoável? PDP sem nenhuma avaliação em loja estabelecida indica que ninguém pediu (ferramenta de review ausente).
- **Perguntas e respostas** — Espaço para dúvidas respondidas? (forte em eletrônicos/casa)

## Contexto e continuação

- **Cross-sell / "compre junto"** — A PDP sugere complementares ("quem comprou levou também")? PDP sem recomendação é beco sem saída para quem não se convenceu daquele item exato — e ticket médio deixado na mesa para quem se convenceu.
- **Produtos vistos recentemente** — Existe trilha de retorno para comparação?
- **Breadcrumb** — Volta para a categoria sem usar o botão do navegador?

## Dados estruturados (do coletor)

- **JSON-LD `Product`** — Existe? Com `offers` (preço, moeda, disponibilidade), `brand`, `aggregateRating`, GTIN/SKU? Sem isso, Google Shopping, rich results e assistentes de IA enxergam a página como texto solto. Registre os campos ausentes — vai direto pro anexo técnico.
- **Title e meta description** — Título da aba é o nome do produto + loja, ou algo genérico?

## Critérios de nota (camada "Produto")

- Comece de 10; críticos −2 a −3: sem calculadora de frete, sem guia de tamanho (moda), preço/parcelamento invisível, mídia insuficiente no carro-chefe, descrição vazia/duplicada.
- Atenção −0,5 a −1: sem vídeo, sem reviews, sem cross-sell, JSON-LD incompleto, breadcrumb ausente.
- Cross-sell/recomendação ausente: além do desconto, registre como oportunidade de ticket médio (esforço "estrutural/tecnologia" se a plataforma não oferece nativamente).
