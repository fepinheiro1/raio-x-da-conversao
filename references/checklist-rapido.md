# Checklist Rápido — os 5 sinais (~5 minutos de auditoria)

O cartão de resultado responde **sempre** estas 5 perguntas, cada uma com veredito (ok / atenção / crítico) e evidência literal. Elas são os pontos onde loja média mais perde venda — e onde o diagnóstico tem opinião, não obviedade. Registre tudo com URL, consulta digitada e o que apareceu.

## Preparação (1 minuto)

Abra a home e **anote os nomes reais de 3–4 produtos** do catálogo (da vitrine principal ou da categoria mais destacada). As sondas de busca são construídas a partir deles — nunca de termos genéricos inventados.

Rode o coletor na home + 1 PDP: ele detecta plataforma, stack de ferramentas (recuperação, vídeo, busca, reviews), JSON-LD e peso. Leia a seção da plataforma em `plataformas.md`.

## Sinal 1 — Sua busca encontra?

Pela interface real (campo + Enter). Sondas a partir dos **nomes reais** anotados:

1. **Nome exato** de um produto — e **clique no 1º resultado**: abre página comprável ou erro?
2. **Erro de digitação próximo** — o erro que um cliente real comete no celular: uma letra trocada ("camizeta"), uma omitida ("tenis" sem acento, "relogio"), uma duplicada. **Nada de erros malucos** — o teste é realista ou não vale.
3. **Sinônimo popular** — como o cliente chama, não como o catálogo escreve ("blusa de frio" vs "moletom").
4. **Contraprova** (algo que a loja não vende) — estado vazio digno ou página morta?

**Veredito claro e sem eufemismo**: se a sonda 2 ou 3 falha, o cartão diz *"sua busca está com falha: quem digita '<termo>' recebe <o que apareceu>"*. E contextualize a causa: busca nativa de plataforma é literal — não corrige erro nem entende sinônimo; resolver isso normalmente exige uma ferramenta de busca dedicada (categoria, sem citar marca).

- Zero/baixo resultado exige **segunda confirmação** pela interface antes de virar achado.
- Modo Estático: se o `<form>` de busca for GET simples, execute pelo endpoint do próprio form; se for client-side sem endpoint, declare como não testável.
- **Marque o sinal**: se o status ficou `atencao`/`critico`, coloque `"esforco": "estrutural"` no objeto desse sinal em `findings.json` — vira o selo "Exige tecnologia dedicada" ao lado do veredito no cartão (ver `relatorio.md`).

## Sinal 2 — Sua página de produto vende mais de um produto?

Na PDP do carro-chefe, **conte as vitrines de recomendação e classifique o tipo**: "quem viu também viu", "compre junto", similares/alternativos, "mais vendidos", "vistos recentemente", "combina com". Anote quantas existem e de que tipo.

- **Referência de mercado**: lojas de alta conversão trabalham com 2–4 vitrines na página de produto — é onde nasce boa parte do ticket adicional.
- **0 vitrines ou só 1 carrossel genérico de "relacionados"** = achado relevante: a página que mais recebe visita qualificada está vendendo um produto só. Diga isso com essa clareza.
- **Manual/estática ≠ por comportamento**: vitrine igual para todo mundo vale menos que vitrine que reage ao que o visitante viu/clicou. Se só existe a primeira, registre a distinção — é ela que separa "tem vitrine" de "tem recomendação".
- Olhe a home também: vitrines manuais que nunca mudam e ausência de "vistos recentemente" são o mesmo achado em outra página.
- Aproveite a passada na PDP para os básicos: preço + parcelamento visíveis, frete por CEP, fotos (4+), avaliações, Product JSON-LD (do coletor).
- **Marque o sinal**: se ficou `atencao`/`critico` (0–1 vitrine ou só vitrine manual), coloque `"esforco": "estrutural"` — vira o selo "Exige tecnologia dedicada" no cartão.

## Sinal 3 — Quem abandona, volta?

Pelo coletor (categorias `push_recuperacao`, `suite_performa` e `chat_atendimento`) + navegação. O mercado trabalha **3 níveis de intenção** — quem viu produto, quem encheu carrinho, quem chegou ao checkout — e o veredito deve cobrir os três:

- Alguma **ferramenta de recuperação** detectada (e-mail/push/WhatsApp/overlay de saída)? Qual? Cobre só carrinho ou também produto visitado e checkout incompleto (se der pra saber)?
- O checkout **captura e-mail cedo** (antes da tela de pagamento)? Sem contato capturado, nenhum nível é recuperável.
- Existe **reação à saída** (overlay de exit intent, push opt-in) ou o visitante que vai embora simplesmente vai embora?
- **Nada encontrado?** O cartão diz, nesse tom: *"Não encontrei nenhuma ferramenta de recuperação instalada. Se você usa só o recurso nativo da plataforma, ele costuma parar em um e-mail único de carrinho. O padrão de mercado trabalha três níveis de intenção — produto visitado, carrinho e checkout — com lembretes em sequência por e-mail, push e WhatsApp."* Sem citar marca.
- Contextualize com o benchmark: ~7 a 8 de cada 10 carrinhos são abandonados; sem captura + réguas, essa receita é irrecuperável por definição.
- **Ferramenta detectada?** Reconheça no cartão ("a loja já investe em recuperação") e desloque o olhar: captura antecipada + cobertura dos 3 níveis.
- **Marque o sinal**: se nada foi detectado (status `critico`), coloque `"esforco": "estrutural"` — vira o selo "Exige tecnologia dedicada". Se já tem ferramenta e o achado é só sobre ampliar cobertura, não marque — nesse caso a lacuna não é "não ter tecnologia".

## Sinal 4 — Sua loja tem vídeo?

Pelo coletor (categoria `video_commerce`) + o que você viu na home e na PDP:

- Existe **qualquer vídeo** na loja? (nativo, YouTube/Vimeo embed, ferramenta de vídeo shoppable)
- Vídeo de produto na PDP do carro-chefe? Vídeo comprável (produto clicável no vídeo) ou só player solto?
- **Nada de vídeo?** Registre como oportunidade, nesse tom: *"Não encontrei nenhum vídeo na sua loja. Vídeo shoppable — o formato de Reels/TikTok, mas dentro do e-commerce, com o produto clicável no próprio vídeo — é a tendência mais forte do varejo agora. Se você já produz vídeo para rede social, esse conteúdo pode trabalhar dentro da loja em vez de mandar seu cliente para fora dela."* Sem citar marca.
- Se tem vídeo mas só institucional/embed longe do produto, vale a mesma observação: vídeo que vende fica perto do produto — e o link para a rede social no meio da compra manda o cliente embora.
- **Marque o sinal**: se não há vídeo shoppable nenhum (status `atencao`/`critico`), coloque `"esforco": "estrutural"` — vira o selo "Exige tecnologia dedicada", mesmo quando esse sinal não entrar no Top 3.

## Observações condicionais (não são sinais fixos — levante quando o contexto pedir)

- **Loja de moda/fitness/acessórios** sem guia de tamanhos: além do guia, mencione que provadores virtuais com IA (cliente envia foto, vê o produto aplicado) viraram diferencial real do segmento.
- **Catálogo grande com paginação profunda**: fim de página que vira fim de jornada — mercado usa carrossel de continuação ou vitrine infinita.
- **Nenhum canal de dúvida imediato** (só formulário/WhatsApp mudo) em segmento consultivo: atendimento com IA que conhece o catálogo responde 24h e captura o contato de quem não comprou.
- Redação de todos esses casos: `categorias-solucao.md`.

## Sinal 5 — Dá pra confiar e pagar?

- **CNPJ + endereço** no rodapé (obrigatório no BR; 1º item que comprador novo procura)
- **Política de troca** linkada
- **Pix e parcelamento** anunciados na jornada
- Carrinho→checkout (com navegador): feedback de adição, compra sem cadastro, **pare na última tela antes do pagamento**
- **Analytics** presente (GA4/GTM/Pixel, do coletor)
- Sem navegador: carrinho/checkout = "não verificado", nunca estimado.
- **Este sinal normalmente não leva o selo "estrutural"**: CNPJ, política e Pix são conteúdo/configuração (`voce-mesmo`), não tecnologia dedicada. Exceção: se a lacuna for especificamente ausência de analytics/funil instrumentado, considere `esforco: estrutural` só nesse caso — CNPJ/endereço nunca leva.

## Entrada (transversal, 1 minuto)

Não é um sinal do cartão, mas alimenta a nota: proposta clara em 5s, busca visível no header, pop-up antes do 1º produto, peso da home (>1,5 MB de HTML = achado), categoria coerente (produtos pertencem a ela? filtro do atributo óbvio existe?).

## Nota geral (uma só, 0–10)

Parta de 10; desconte por sinal: crítico −2 a −3, atenção −0,5 a −1. Guia: 8+ = redonda com ajustes finos; 6–7,5 = boa base, 2–3 vazamentos claros; 4–5,5 = perdas em etapa central; <4 = estrutural. Nunca 10, nunca 0 sem evidência forte.

## Top 3

Os 3 achados de maior impacto × menor esforço, **pelo menos 1 executável pelo lojista nesta semana**. Os 5 sinais também entram no cartão como linha própria (schema em `relatorio.md`) — o Top 3 aprofunda os piores; os sinais garantem que nenhum tema estratégico sai sem veredito.

## Como falar de lacuna sem virar propaganda

Regra de ouro: **nomeie a categoria de solução e o padrão de mercado — nunca uma marca.** "Ferramenta dedicada de busca", "recuperação multicanal", "vitrines por comportamento", "vídeo shoppable". A única menção à Performa em todo o entregável é a assinatura discreta que o script já coloca no rodapé. Se o usuário perguntar "e quem faz isso?", aí sim responda naturalmente — foi ele quem pediu.
