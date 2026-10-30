# Raio-X de Conversão 🩻

**Auditoria gratuita de conversão para sua loja virtual — feita por IA, rodando 100% na sua máquina.**

Você dá a URL da sua loja. A IA navega como um cliente de verdade — home, categoria, produto, busca, carrinho e checkout, no computador e no celular — testa sua busca interna com consultas reais, mede velocidade e entrega um cartão com as 3 prioridades para vender mais com o tráfego que você já tem. A análise profunda, quando solicitada, entrega 5 prioridades e anexo técnico.

Uma iniciativa [Performa.AI](https://performa.ai). Sem cadastro, sem coleta de dados, sem pegadinha: seus dados não saem do seu computador.

## O que você recebe (em ~5 minutos)

- ✅ Nota geral da sua loja (0–10) com resumo direto
- ✅ Teste real da sua busca interna (você vai se surpreender)
- ✅ 3 movimentos para esta semana — com "faça isto" concreto
- ✅ Cartão de resultado em HTML: abre no navegador, dá para enviar por e-mail

**Quer mais?** Peça a **análise profunda**: 6 camadas com nota cada, mapa de vazamento do funil, 8 sondas de busca, passada mobile e anexo técnico pronto para repassar à sua agência ou dev.

## Como instalar

### Codex

No Codex, envie esta mensagem:

> **Instale a skill deste repositório: https://github.com/fepinheiro1/raio-x-da-conversao**

Depois que o Codex confirmar a instalação, abra uma nova conversa e envie:

> **Use $raio-x-conversao para fazer o raio-x da minha loja: https://minhaloja.com.br**

Para instalar manualmente como skill global — disponível em qualquer projeto — use:

```bash
mkdir -p ~/.agents/skills
git clone https://github.com/fepinheiro1/raio-x-da-conversao.git ~/.agents/skills/raio-x-conversao
```

Para atualizar uma instalação manual existente:

```bash
git -C ~/.agents/skills/raio-x-conversao pull
```

O Codex também consegue descobrir a skill automaticamente quando o pedido combina com ela. Exemplos:

- `Faça o raio-x da loja https://minhaloja.com.br`
- `Por que meu e-commerce não vende? Analise https://minhaloja.com.br`
- `Faça uma análise profunda da loja https://minhaloja.com.br`

### O que acontece na primeira utilização

A instalação não inicia uma auditoria sozinha. Na primeira vez que a skill for usada, o agente:

1. Explica rapidamente o que será testado, o tempo estimado e o que será entregue.
2. Confirma a URL da loja, caso ela ainda não tenha sido informada.
3. Pergunta qual produto ou categoria é mais importante e qual dor a loja já sente.
4. No modo profundo, pergunta também de onde vem a maior parte do tráfego.
5. Começa a auditoria assim que receber as respostas. Se a pessoa não souber alguma delas, a análise continua mesmo assim.

A primeira mensagem deve ser parecida com esta:

> Vou fazer o Raio-X de Conversão em modo rápido. Em cerca de 5 minutos vou testar entrada, busca, página de produto, carrinho, checkout e confiança — sem finalizar nenhuma compra. No final você recebe uma nota geral e 3 prioridades. Para personalizar: qual produto ou categoria mais importa vender e qual dor você já percebe hoje?

### Claude Code

1. Copie a pasta `raio-x-conversao` para `~/.claude/skills/` (crie a pasta se não existir):
   ```bash
   mkdir -p ~/.claude/skills && cp -r raio-x-conversao ~/.claude/skills/
   ```
2. Abra o Claude Code em qualquer pasta e peça:
   > **"Faz o raio-x da minha loja: minhaloja.com.br"**

### Claude Desktop / claude.ai

Compacte a pasta `raio-x-conversao` em um `.zip`, envie nas configurações de skills (Configurações → Capacidades/Skills) e peça o raio-x da sua loja.

### Cursor e outros agentes

A pasta contém um `AGENTS.md`. Abra a pasta no seu agente e peça:
> **"Siga as instruções do AGENTS.md e faça o raio-x da loja minhaloja.com.br"**

## Requisitos

- Python 3.8+ (já vem no Mac/Linux; no Windows, [python.org](https://python.org)) — os scripts não instalam nada
- Melhor experiência: agente com navegador integrado (percurso completo até o checkout). Sem navegador, a análise roda em modo estático e avisa o que ficou de fora.

## Perguntas frequentes

**É seguro?** Sim. A análise visita sua loja como um visitante comum (8–12 páginas), nunca finaliza compra, nunca preenche dados pessoais e não envia nada para servidor nenhum. A única chamada externa opcional é à API pública do PageSpeed do Google, para medir velocidade.

**Funciona com minha plataforma?** Sim — Nuvemshop, Shopify, VTEX, Tray, Loja Integrada, WooCommerce, Magento, Yampi, Bagy e outras. O raio-x identifica a plataforma e adapta as recomendações ao que ela permite.

**Quanto custa?** Nada. É um presente da [Performa.AI](https://performa.ai) para donos de e-commerce.
