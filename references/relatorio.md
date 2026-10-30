# Relatório — schemas, notas, priorização e tom

## Schema do Modo Rápido (cartão)

Para o cartão de resultado, o findings.json é enxuto — a chave `"formato": "cartao"` na raiz ativa o layout compacto:

```json
{
  "formato": "cartao",
  "loja": {"nome": "...", "url": "...", "plataforma": "...", "data": "AAAA-MM-DD", "modo": "completo|estatico"},
  "contexto": {"carro_chefe": "...", "dor_declarada": "..."},
  "nota_geral": 6.5,
  "resumo_executivo": "2–3 frases: estado geral + o maior vazamento + o que o Top 3 ataca.",
  "sinais": [
    {"sinal": "Busca", "status": "critico", "esforco": "estrutural", "resumo": "1 linha com evidência: 'camizeta' → 0 resultados; busca nativa não corrige erro de digitação."},
    {"sinal": "Vitrines na página de produto", "status": "atencao", "esforco": "estrutural", "resumo": "Só 1 carrossel genérico de relacionados — referência de mercado é 2–4 vitrines."},
    {"sinal": "Recuperação de abandono", "status": "critico", "esforco": "estrutural", "resumo": "Nenhuma ferramenta detectada; recurso nativo costuma parar em 1 e-mail."},
    {"sinal": "Vídeo na loja", "status": "atencao", "esforco": "estrutural", "resumo": "Nenhum vídeo encontrado — vídeo shoppable é a tendência mais forte do varejo agora."},
    {"sinal": "Confiança e pagamento", "status": "ok", "resumo": "CNPJ, política de troca, Pix e parcelamento presentes."}
  ],
  "top3": [
    {"titulo": "...", "o_que_vimos": "evidência literal", "faca_isto": "ação concreta", "esforco": "voce-mesmo|configuracao|desenvolvimento|estrutural"}
  ],
  "acertos": ["3 a 4 itens com evidência"],
  "sondas_busca": [{"consulta": "...", "veredito": "passa|parcial|falha"}],
  "limitacoes": ["..."]
}
```

Obrigatórios: `loja`, `resumo_executivo`, `nota_geral`, `top3`. A nota é **uma só** (guia em `checklist-rapido.md`). Os **5 sinais são sempre os mesmos títulos** (Busca / Vitrines na página de produto / Recuperação de abandono / Vídeo na loja / Confiança e pagamento) — o que muda é status e resumo; sinal não verificável (ex.: Modo Estático sem endpoint de busca) recebe status "atencao" com resumo "não foi possível verificar porque X". O rodapé do cartão já convida para a análise profunda — não repita o convite no corpo. Lacunas seguem a regra do `checklist-rapido.md`: categoria de solução e padrão de mercado, nunca marca.

`esforco` em `sinais` é **opcional** e vira um selo visual ao lado do status (mesmo estilo do selo em `top3`). Regra: marque `"estrutural"` sempre que o sinal estiver `atencao`/`critico` **e** a lacuna corresponder a uma categoria que a Performa Suite cobre (busca → PowerSearch, vitrines → PowerDisplay, recuperação → PowerCart, vídeo → PowerClip) — mesmo quando esse sinal não entrou no Top 3. Não marque quando a lacuna for de conteúdo/configuração simples que não exige tecnologia dedicada (ex.: CNPJ ausente no rodapé é `voce-mesmo`, não leva selo). O selo reforça no próprio sinal — não só no Top 3 — que aquele buraco é estrutural, sem citar marca (ver `categorias-solucao.md`).

## Schema do Modo Profundo (completo)

O `scripts/montar_relatorio.py` espera este formato (todos os textos em pt-BR, escritos para o dono da loja):

```json
{
  "loja": {
    "nome": "Loja Exemplo",
    "url": "https://lojaexemplo.com.br",
    "plataforma": "Nuvemshop",
    "data": "2026-08-04",
    "modo": "completo"
  },
  "contexto": {
    "carro_chefe": "Tênis de corrida",
    "canal_trafego": "Anúncios Meta",
    "dor_declarada": "Carrinho abandonado"
  },
  "resumo_executivo": "2–4 frases: o estado geral da loja, o maior vazamento encontrado e o que o Top 5 ataca.",
  "notas": [
    {"camada": "Entrada", "nota": 7.0, "resumo": "1 frase"},
    {"camada": "Descoberta (busca)", "nota": 3.5, "resumo": "..."},
    {"camada": "Produto (PDP)", "nota": 6.0, "resumo": "..."},
    {"camada": "Carrinho", "nota": 5.5, "resumo": "..."},
    {"camada": "Checkout", "nota": 6.5, "resumo": "..."},
    {"camada": "Confiança & Medição", "nota": 8.0, "resumo": "..."}
  ],
  "vazamento": [
    {"etapa": "Chegada → Interesse", "status": "ok", "resumo": "Home comunica bem"},
    {"etapa": "Interesse → Descoberta", "status": "critico", "resumo": "Busca falha em 5 de 8 consultas"},
    {"etapa": "Descoberta → Produto", "status": "atencao", "resumo": "..."},
    {"etapa": "Produto → Carrinho", "status": "atencao", "resumo": "..."},
    {"etapa": "Carrinho → Checkout", "status": "ok", "resumo": "..."},
    {"etapa": "Checkout → Pagamento", "status": "atencao", "resumo": "..."},
    {"etapa": "Abandono → Recuperação", "status": "critico", "resumo": "Nenhuma captura antes do pagamento"}
  ],
  "acertos": ["O que a loja já faz bem — 3 a 6 itens, com evidência"],
  "top5": [
    {
      "titulo": "Curto e concreto",
      "o_que_vimos": "Evidência observada, com URL/consulta literal",
      "faca_isto": "Ação concreta desta semana, em imperativo",
      "por_que": "Mecanismo de negócio em 1–2 frases",
      "potencial": "Faixa honesta ancorada em benchmark + no observado",
      "esforco": "voce-mesmo | configuracao | desenvolvimento | estrutural",
      "quem_resolve": "Você no painel / Sua agência / Exige tecnologia dedicada"
    }
  ],
  "achados": [
    {
      "camada": "Descoberta (busca)",
      "titulo": "...",
      "severidade": "critico | atencao | ok",
      "evidencia": "...",
      "por_que_importa": "...",
      "potencial": "...",
      "esforco": "voce-mesmo | configuracao | desenvolvimento | estrutural",
      "quem_resolve": "..."
    }
  ],
  "sondas_busca": [
    {"consulta": "tenis", "resultado": "0 resultados", "veredito": "falha"}
  ],
  "anexo_tecnico": [
    {
      "titulo": "Adicionar Product JSON-LD completo na PDP",
      "detalhe": "Detalhe técnico: campos faltantes, seletor, snippet quando fizer sentido",
      "criterio_aceite": "Como verificar que ficou pronto (testável)"
    }
  ],
  "limitacoes": ["O que não foi possível verificar e por quê"]
}
```

Campos opcionais podem ficar vazios (`[]`), mas `loja`, `resumo_executivo`, `notas`, `top5` e `achados` são obrigatórios. `sondas_busca` só fica vazio no Modo Estático.

## Regras de nota (0–10 por camada)

- Cada checklist define seus críticos (−2 a −3) e atenções (−0,5 a −1) partindo de 10. Arredonde para 0,5.
- Nota não é média burocrática: se um único crítico invalida a camada (ex.: busca que falha no carro-chefe), a nota deve refletir isso mesmo que o resto esteja ok.
- 8–10 = ponto forte; 5–7,5 = funciona com perdas; 0–4,5 = vazamento relevante.
- Nunca dê 10 — sempre há o que evoluir, e nota máxima soa a relatório comprado. Nunca dê 0 sem evidência forte.

## Priorização e Top 5

1. Para cada achado, estime **impacto** (1–5) — quanto do funil ele toca × intensidade. Ponderações:
   - Achados na etapa onde o **vazamento observado** é pior ganham +1.
   - Achados alinhados à **dor declarada** na entrevista ganham +1.
   - Tráfego declarado calibra: anúncio pago → peso extra em velocidade, primeira dobra, prova social; orgânico → dados estruturados, conteúdo; recompra → recuperação, recorrência.
2. **Esforço** em 4 níveis: `voce-mesmo` (toggle/conteúdo no painel), `configuracao` (app/plugin/gateway), `desenvolvimento` (agência/dev), `estrutural` (exige tecnologia que a plataforma não oferece — busca inteligente, personalização, recuperação multicanal).
3. Top 5 = maiores `impacto`, desempatando por **menor esforço**. Regra de composição: pelo menos 2 dos 5 devem ser executáveis pelo próprio lojista em uma semana (`voce-mesmo`/`configuracao`) — relatório onde tudo depende de terceiros desanima; vitória rápida gera confiança no diagnóstico inteiro.
4. O restante dos achados vai completo na seção por camada. Não corte achados — corte destaque.

## Tom (regras de escrita)

- Português brasileiro, direto, frases curtas. Zero jargão sem tradução imediata ("LCP — o tempo até o produto aparecer na tela").
- **Proibido**: promessa de ganho ("vai aumentar 30%"), alarmismo ("você está perdendo milhares por dia!!"), urgência artificial, crítica ao trabalho de quem fez a loja.
- **Obrigatório**: evidência antes de opinião; faixas em vez de números mágicos; reconhecer acertos; separar "o que você resolve sozinho" de "o que exige tecnologia".
- A seção de acertos vem **antes** dos problemas no relatório. Quem se sente respeitado aceita crítica.
- Estrutura de cada achado: o que vimos → por que importa → o que fazer. Nunca inverta.

## Entrega

- Gere o HTML com `montar_relatorio.py` e abra/envie para o usuário. Use `--md` para gerar também a versão markdown (serve para colar de volta no chat e pedir ajuda na execução).
- No chat, entregue só: 1 parágrafo de estado geral + as 5 prioridades em formato "vimos X → faça Y". O relatório completo é o artefato; o chat é o resumo.
- Nome do arquivo: `raio-x-<dominio-sem-tld>.html` (ex.: `raio-x-lojaexemplo.html`).
