# Checklist — Mobile, Velocidade, Confiança e Mensuração

## Mobile (viewport 375×812)

A maioria das lojas brasileiras recebe 60–80% do tráfego no celular — o mobile **é** a loja; o desktop é a exceção. Redimensione a viewport (ou use device emulation) e repita os pontos críticos. Se a ferramenta não aceitar 375px (janelas reais de navegador têm mínimo de ~500px), use a menor largura possível — abaixo de ~768px o layout mobile já é acionado — e registre em Limitações que foi emulação por janela estreita, não aparelho.

> Compare templates entre si: é comum a home mobile esconder a busca no menu enquanto a PDP mobile a mostra no header (ou vice-versa). Inconsistência entre templates é achado, não detalhe.

- **Busca a um toque** — O campo/ícone de busca está no header mobile, ou enterrado dentro do menu hambúrguer? Busca a dois toques de distância perde o comprador apressado.
- **Primeira dobra mobile** — O que aparece sem rolar? Muitas lojas gastam a dobra inteira com logo + menu + banner cortado.
- **CTA fixo na PDP** — O botão comprar acompanha a rolagem (sticky) ou some quando o cliente lê a descrição?
- **Alvos de toque** — Botões e links com área digna (~44px) ou linkzinhos apertados? Seletor de variação utilizável com dedo?
- **Imagens com pinça** — Zoom por gesto funciona na foto do produto?
- **Teclado correto** — Campo de CEP/telefone abre teclado numérico? (`inputmode`/`type` corretos — verificável no HTML)
- **Pop-up no mobile** — O pop-up de entrada cobre a tela inteira e o X é encontrável?
- **Repita 2 sondas de busca** no mobile (ver checklist-busca).

## Velocidade (Core Web Vitals)

Use o coletor com `--psi` (estratégia mobile). Limiares do Google:

| Métrica | Bom | Precisa melhorar | Ruim |
|---|---|---|---|
| LCP (maior elemento visível) | ≤2,5s | 2,5–4s | >4s |
| INP (resposta à interação) | ≤200ms | 200–500ms | >500ms |
| CLS (estabilidade visual) | ≤0,1 | 0,1–0,25 | >0,25 |

- Priorize **dados de campo** (usuários reais, quando o PSI retornar `loadingExperience`) sobre o lab score.
- Traduza sempre para negócio: "a página principal demora Xs para mostrar o produto no celular — parte dos visitantes desiste antes disso".
- Causas comuns visíveis no coletor: imagens gigantes sem compressão, dezenas de scripts de terceiros, fontes bloqueantes. Aponte a causa provável, não só o número.
- LCP ruim na home/PDP com tráfego pago = dinheiro de anúncio pago por visita que não chega a ver a página. É argumento de primeira ordem no relatório.

## Confiança

O visitante decide em segundos se o site parece confiável — e loja desconhecida começa devendo:

- **HTTPS sem aviso** — Cadeado limpo, sem conteúdo misto.
- **Identidade real no rodapé** — CNPJ, razão social, endereço. Ausência é crítico: é requisito legal (e-commerce BR) e a primeira coisa que comprador desconfiado procura.
- **Canais de contato reais** — WhatsApp, telefone, e-mail, horário de atendimento. Só um formulário mudo é sinal fraco.
- **Políticas encontráveis** — Troca/devolução, privacidade, frete: linkadas no rodapé e escritas em gente (não juridiquês copiado)? A política de troca é lida **antes** da primeira compra em loja nova.
- **Prova social externa** — Nota no Google/Reclame Aqui linkada? Instagram ativo linkado (última postagem recente)? Rede social abandonada há 8 meses levanta suspeita de loja morta.
- **Atendimento visível** — Chat/WhatsApp flutuante existe? Responde algo ou é decorativo? (registre se há indício de automação/bot)

## Mensuração

Loja que não mede decide no escuro. Pelo coletor (scripts detectados) e pela navegação (requisições de rede, se o navegador permitir observar):

- **GA4 / GTM presentes** — Existe `gtag`/GTM na página?
- **Meta Pixel** — Presente? (essencial se o tráfego declarado na entrevista é anúncio Meta)
- **Eventos de e-commerce disparam** — Se conseguir observar rede: `view_item` ao abrir PDP, `add_to_cart` ao adicionar? Pixel instalado sem eventos de funil = mídia otimizando às cegas.
- **Duplicidade** — Dois GA/GTM/Pixels na mesma página (agência antiga + atual) infla métrica e confunde otimização.
- **Ferramenta de comportamento** — Clarity/Hotjar presente? (não é obrigatório; é bônus de maturidade)

> No Modo Estático, a presença dos scripts é verificável; o disparo de eventos não — marque como "não verificado" em vez de supor.

## Critérios de nota

- **Mobile** entra distribuído nas camadas correspondentes (uma busca ruim no mobile piora "Descoberta"; CTA não-fixo piora "Produto"). Não é camada separada.
- **Confiança + Mensuração** formam a camada "Confiança & Medição": críticos −2 a −3 (sem CNPJ, sem HTTPS limpo, sem nenhum analytics, sem política de troca); atenção −0,5 a −1 (sem prova externa, canais fracos, sem eventos de funil, duplicidade).
- **Velocidade** entra na camada "Entrada" (home) e "Produto" (PDP) conforme a página medida.
