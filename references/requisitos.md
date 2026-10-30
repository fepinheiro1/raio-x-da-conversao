# Requisitos e pré-check

Leia esta referência antes de iniciar a primeira auditoria em um ambiente novo.

## O que é obrigatório

| Recurso | Como verificar | Se estiver ausente |
|---|---|---|
| Python 3.8+ | `python3 --version` | O coletor e o gerador não funcionam. Peça autorização antes de instalar. |
| Biblioteca padrão do Python | `scripts/preflight.py` | Uma instalação normal do Python já inclui tudo; não instale pacotes com `pip`. |
| Acesso HTTPS à loja | `scripts/preflight.py --url <URL>` | A auditoria não consegue visitar a loja. Verifique permissões de rede ou bloqueio do site. |
| Pasta de saída gravável | `scripts/preflight.py --output-dir <pasta>` | Escolha uma pasta autorizada; não amplie permissões sem consentimento. |

## O que define o modo de auditoria

- **Modo Completo:** requer navegador controlável, screenshots e viewport mobile. Isso é uma capacidade da superfície do Codex ou do ambiente, não um pacote Python desta skill.
- **Modo Estático:** funciona com Python e acesso HTTPS, mas não comprova interações dinâmicas de busca, carrinho, checkout ou mobile. Declare essas limitações.
- **PageSpeed Insights:** opcional. Não requer chave nesta skill, mas é uma chamada externa ao Google e deve ser informada ao usuário antes do uso.

Não são necessários Node.js, npm, banco de dados, credenciais administrativas da loja, login de cliente, CPF, cartão ou chave de API.

## Procedimento obrigatório

1. Verifique as ferramentas disponíveis e confirme se há navegador controlável.
2. Confirme Python com `python3 --version`. Se existir, execute:

   ```bash
   python3 scripts/preflight.py --url <URL_DA_LOJA> --output-dir <PASTA_DE_SAIDA> --json
   ```

3. Antes da auditoria, resuma o resultado ao usuário em três grupos:
   - **Disponível** — pronto para usar.
   - **Ausente ou bloqueado** — o que falta e qual parte da auditoria impede.
   - **Opcional** — recurso que melhora o diagnóstico, mas não bloqueia o modo disponível.
4. Nunca instale software, browser runtime, plugin ou pacote silenciosamente. Se algo essencial estiver ausente, informe:
   - o recurso exato;
   - por que é necessário;
   - o comando ou ação proposta;
   - se haverá download, uso de rede ou alteração fora da pasta do projeto.
5. Só execute a instalação depois de autorização explícita. Se a autorização não vier, ofereça o modo que funciona com os recursos atuais.

Exemplo:

> Pré-check concluído. Python, escrita e acesso à loja estão disponíveis. Não encontrei navegador controlável, então consigo fazer agora o Modo Estático; busca dinâmica, carrinho e mobile ficarão como não verificados. Se você quiser o Modo Completo, posso verificar uma opção de navegador compatível e mostrar exatamente o que seria instalado antes de pedir sua autorização.

Se o ambiente não permitir instalar o recurso, não prometa que a instalação é possível. Explique a limitação e indique uma superfície compatível do Codex ou prossiga no Modo Estático.
