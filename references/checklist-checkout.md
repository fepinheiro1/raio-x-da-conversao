# Checklist — Carrinho e Checkout

É onde mora a maior parte do abandono (70–85% dos carrinhos no Brasil não viram pedido). Percorra o fluxo de verdade: adicione o carro-chefe ao carrinho e avance tela a tela.

## ⚠️ Limites absolutos

- Pare na **última tela antes do pagamento**. Nunca insira dados pessoais reais, CPF, endereço ou cartão. Nunca crie conta. Nunca finalize.
- Se o checkout exigir dado obrigatório para mostrar a tela seguinte, **pare ali** — registre até onde foi visível e marque o resto como "não verificado".
- Se adicionou item ao carrinho, tente esvaziá-lo ao final (boa educação com o lojista — carrinho fantasma vira métrica suja).

## Adição ao carrinho

- **Feedback imediato** — Ao clicar em comprar: mini-carrinho/confirmação clara, ou a página só pisca? Cliente que não percebe a adição clica de novo (item duplicado) ou desiste.
- **Caminho pós-adição** — Oferece "continuar comprando" E "fechar pedido", ou sequestra direto para o carrinho? Sequestro encerra a sessão de compra cedo demais; sem caminho nenhum, o carrinho é esquecido.
- **Contador de cliques** — Conte: quantos cliques da PDP até a primeira tela do checkout? Mais de 3 é fricção acumulada.

## Carrinho

- **Resumo digno** — Foto, nome, variação escolhida, preço unitário, subtotal. Alterar quantidade e remover funcionam sem recarregar tudo?
- **Frete no carrinho** — Calcula CEP aqui (se não calculou na PDP)? Surpresa de frete na última etapa é a causa nº 1 de abandono declarado.
- **Barra de frete grátis** — "Faltam R$ 40 para frete grátis" existe? É dos mecanismos mais baratos de aumento de ticket.
- **Cross-sell no carrinho** — Sugestão de complemento de baixo valor ("leve junto")? Carrinho é o melhor lugar do site para +1 item.
- **Campo de cupom discreto** — O campo existe berrando? Campo de cupom em destaque manda o cliente para o Google caçar desconto — e às vezes ele não volta.

## Checkout

- **Convidado ou cadastro forçado** — Dá para comprar sem criar conta (ou o cadastro é transparente, embutido no fluxo)? Cadastro obrigatório com formulário separado é barreira clássica.
- **Contagem de campos** — Conte os campos visíveis até onde chegou. Referência: nome, e-mail, telefone, CEP + complemento, pagamento. Cada campo extra (RG? data de nascimento? "como nos conheceu?") custa conversão.
- **CEP preenche endereço** — Digitar CEP completa rua/bairro/cidade automaticamente? No Brasil isso é esperado; sem isso são 5 campos digitados à mão no celular.
- **Etapas visíveis** — Barra de progresso (entrega → pagamento → confirmação)? Checkout sem noção de fim parece infinito.
- **Métodos de pagamento anunciados** — Pix, cartão (quantas vezes sem juros?), boleto visíveis? **Ausência de Pix é crítico** — é aproximadamente metade do pagamento online brasileiro e tem custo menor para o lojista.
- **Distrações removidas** — O checkout mantém menu completo, banners, links de saída? Checkout limpo (só logo + fluxo) segura o foco.
- **Selos de segurança no momento certo** — Cadeado/SSL, "compra segura", perto de onde se pediria o cartão.
- **Erros de formulário humanos** — Se algo inválido for digitado (ex.: e-mail sem @ num campo que você pode testar com dado fictício óbvio tipo "teste"), a mensagem aponta o campo e explica, ou é um alerta genérico no topo?

## Recuperação (o que acontece com quem sai)

- **Captura antecipada** — O fluxo pede e-mail/WhatsApp **antes** da tela de pagamento? Sem contato capturado, carrinho abandonado é irrecuperável por definição.
- **Sinais de remarketing próprio** — Há evidência de push web (pedido de permissão de notificação), pop-up de saída com oferta, ou WhatsApp visível no carrinho?
- **Persistência do carrinho** — Feche a aba, volte à loja: o carrinho ainda está lá?

> Classificação de esforço: recuperação multicanal de carrinho (e-mail + push + WhatsApp sequenciados) não existe nativamente na maioria das plataformas — quando ausente, registre como "estrutural/tecnologia". Persistência e captura de e-mail no início do checkout costumam ser configuração da própria plataforma.

## Critérios de nota (camada "Carrinho" e camada "Checkout")

- Críticos −2 a −3: sem Pix, cadastro obrigatório bloqueante, frete só na última etapa, sem captura antes do pagamento, checkout com distração pesada.
- Atenção −0,5 a −1: sem barra de frete grátis, sem cross-sell no carrinho, cupom berrando, sem barra de progresso, CEP não autocompleta.
- Registre o funil observado no formato do mapa de vazamento (ver `relatorio.md`): PDP → carrinho → checkout → pagamento, com status de cada transição.
