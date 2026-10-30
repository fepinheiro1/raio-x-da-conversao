# Plataformas — o que cada uma resolve, onde o lojista mexe, o que é estrutural

Leia **apenas a seção da plataforma detectada** pelo coletor. O objetivo: classificar corretamente o "quem resolve" de cada achado — painel da própria plataforma, app/configuração, ou tecnologia externa. Errar essa classificação mina a credibilidade do relatório (dizer "peça ao dev" para algo que é um toggle no painel, ou "é só configurar" para algo que a plataforma não faz).

Regra geral para todas: **busca nativa é literal** (sem tolerância a erro de digitação, sem sinônimos, sem ranking comportamental) e **recomendação nativa é estática** (manual ou "relacionados por categoria"). Personalização real, busca inteligente e recuperação multicanal são camada de tecnologia externa em praticamente todas — classifique como "estrutural/tecnologia".

## Nuvemshop (Tiendanube)

- **Painel resolve**: barra de anúncio, banner, menu, frete grátis condicional, cupons, checkout nativo (já é limpo, com Pix via gateways), guia de tamanhos por descrição, SEO básico por produto.
- **Apps resolvem**: reviews, pop-up, pixel extra.
- **Limites estruturais**: busca nativa simples; vitrines estáticas por seção; recuperação nativa = e-mail básico de carrinho (sem sequência multicanal); pouca flexibilidade no checkout (que é padronizado — bom para conversão, ruim para customizar).
- Temas variam muito: parte dos achados de PDP pode ser limitação do tema, não da plataforma.

## Shopify

- **Painel/tema resolve**: praticamente todo layout (Theme Editor), barra de frete grátis via tema, metafields para guia de tamanho, Shop Pay.
- **Apps resolvem quase tudo** — reviews, busca melhorada, upsell, recuperação. Cuidado: excesso de apps é a causa nº 1 de LCP ruim em Shopify; se o coletor mostrar dezenas de scripts, registre.
- **Limites estruturais**: checkout fechado (fora do Plus) — campos e etapas não mudam; Pix depende do gateway BR configurado (verificar presença!); apps em inglês/dólar pesam o custo mensal.

## VTEX

- **Painel resolve**: promoções complexas, frete, políticas comerciais. Plataforma robusta — quase tudo é *possível*.
- **Limites práticos**: quase nada é *simples* — mudanças de vitrine, PDP e checkout normalmente passam pela agência/dev que mantém a loja. Classifique achados de layout como "desenvolvimento" mesmo quando pareçam triviais.
- VTEX tem busca inteligente própria (Intelligent Search) — se a busca falhar nas sondas, pode ser má configuração dela, não ausência; registre a nuance.

## Tray

- **Painel resolve**: layout por temas, promoções, frete, integrações com marketplaces (foco da plataforma).
- **Limites estruturais**: busca literal; recomendação básica; checkout com customização limitada; qualidade final depende muito do tema aplicado.

## Loja Integrada

- Público de entrada; planos gratuitos têm limitações visíveis (inclusive selo da plataforma).
- **Painel resolve**: básico de banners, categorias, frete, cupom.
- **Limites estruturais**: quase tudo além do básico — busca, recomendação, recuperação sofisticada. Se a loja cresceu, parte dos achados pode apontar para "a operação superou a ferramenta"; diga isso com respeito.

## WooCommerce (WordPress)

- **Tudo é plugin**: cada achado vira "instalar/configurar plugin X ou pedir ao dev". Não há "painel oficial" que garanta qualidade — a loja é tão boa quanto quem a mantém.
- **Riscos típicos a checar no coletor**: excesso de plugins (dezenas de scripts), tema pesado, HTTPS/manutenção irregular. Performance ruim aqui é padrão, não exceção.
- Classificação de esforço: quase tudo "configuração/app" ou "desenvolvimento"; pouca coisa é toggle simples.

## Magento / Adobe Commerce

- Semelhante à VTEX: poderosa, dependente de agência. Classifique mudanças como "desenvolvimento".
- Verificar versão/manutenção — Magento desatualizado é risco de segurança e performance.

## Wake / Linx / Fbits

- Plataformas corporativas BR; operação via agência na maioria dos casos → esforço "desenvolvimento".
- Costumam ter módulos próprios de busca/recomendação (Linx Impulse) — se detectados pelo coletor mas falhando nas sondas, o achado é de configuração, não de ausência.

## Bagy / Yampi / Shoppub e similares

- Plataformas enxutas: checkout costuma ser o ponto forte (Yampi nasceu de checkout). Limitações ficam em busca, vitrine e conteúdo.
- Painel simples: maioria dos ajustes de conteúdo é "você mesmo".

## Plataforma não identificada / própria

- Não assuma nada: teste tudo e classifique esforço como "desenvolvimento" por padrão, anotando no relatório que a loja usa plataforma própria/não identificada (o que por si só significa que toda melhoria depende do time técnico dela).
