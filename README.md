# Raio-X de Conversão 🩻

**Auditoria gratuita de conversão para sua loja virtual — feita por IA, rodando 100% na sua máquina.**

Você dá a URL da sua loja. A IA navega como um cliente de verdade — home, categoria, produto, busca, carrinho e checkout, no computador e no celular — testa sua busca interna com consultas reais, mede velocidade e entrega um relatório com as 5 prioridades para vender mais com o tráfego que você já tem.

Uma iniciativa [Performa.AI](https://performa.ai). Sem cadastro, sem coleta de dados, sem pegadinha: seus dados não saem do seu computador.

## O que você recebe (em ~5 minutos)

- ✅ Nota geral da sua loja (0–10) com resumo direto
- ✅ Teste real da sua busca interna (você vai se surpreender)
- ✅ 3 movimentos para esta semana — com "faça isto" concreto
- ✅ Cartão de resultado em HTML: abre no navegador, dá para enviar por e-mail

**Quer mais?** Peça a **análise profunda**: 6 camadas com nota cada, mapa de vazamento do funil, 8 sondas de busca, passada mobile e anexo técnico pronto para repassar à sua agência ou dev.

## Como instalar

### Claude Code (recomendado)

1. Copie a pasta `raio-x-conversao` para `~/.claude/skills/` (crie a pasta se não existir):
   ```bash
   mkdir -p ~/.claude/skills && cp -r raio-x-conversao ~/.claude/skills/
   ```
2. Abra o Claude Code em qualquer pasta e peça:
   > **"Faz o raio-x da minha loja: minhaloja.com.br"**

### Claude Desktop / claude.ai

Compacte a pasta `raio-x-conversao` em um `.zip`, envie nas configurações de skills (Configurações → Capacidades/Skills) e peça o raio-x da sua loja.

### Codex / Cursor / outros agentes

A pasta contém um `AGENTS.md`. Abra a pasta no seu agente e peça:
> **"Siga as instruções do AGENTS.md e faça o raio-x da loja minhaloja.com.br"**

## Requisitos

- Python 3.8+ (já vem no Mac/Linux; no Windows, [python.org](https://python.org)) — os scripts não instalam nada
- Melhor experiência: agente com navegador integrado (percurso completo até o checkout). Sem navegador, a análise roda em modo estático e avisa o que ficou de fora.

## Perguntas frequentes

**É seguro?** Sim. A análise visita sua loja como um visitante comum (8–12 páginas), nunca finaliza compra, nunca preenche dados pessoais e não envia nada para servidor nenhum. A única chamada externa opcional é à API pública do PageSpeed do Google, para medir velocidade.

**Funciona com minha plataforma?** Sim — Nuvemshop, Shopify, VTEX, Tray, Loja Integrada, WooCommerce, Magento, Yampi, Bagy e outras. O raio-x identifica a plataforma e adapta as recomendações ao que ela permite.

**Quanto custa?** Nada. É um presente da [Performa.AI](https://performa.ai) para donos de e-commerce.
