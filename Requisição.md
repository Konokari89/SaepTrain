Claro! Com base no exercício que você enviou, preparei um novo estudo de caso com uma estrutura idêntica, mas com um tema diferente, para você praticar.

---

### Exercício de Estudo - Sistema de Gestão de Reservas de Hotel

**Contexto:**
A rede de hotéis "Horizon Hotéis" precisa de um sistema interno para gerenciar as reservas de seus quartos. O objetivo é permitir que recepcionistas e gerentes possam cadastrar hóspedes, verificar a disponibilidade de quartos, criar, alterar e cancelar reservas. O sistema também deve registrar o histórico de estadias de cada hóspede e gerar relatórios de ocupação.

O sistema será acessado por Recepcionistas e Gerentes, cada um com diferentes níveis de permissão. Deve conter controle de login, cadastro de hóspedes, cadastro de tipos de quartos, gerenciamento de reservas e geração de relatórios simples.

**Instruções:**
Cada item é uma entrega obrigatória. Seja objetivo, mas demonstre raciocínio técnico. Linguagem e SGBD de livre escolha.

---

**1. Lista de Requisitos Funcionais**
Liste pelo menos 8 requisitos funcionais que o sistema deve atender (ex: "O sistema deve permitir o cadastro de novos hóspedes", "O sistema deve impedir a reserva de um quarto já ocupado na data solicitada").

**2. DER - Diagrama Entidade-Relacionamento**
Desenhe (ou descreva em texto) o modelo de dados necessário para armazenar informações de `Hóspedes`, `Quartos` (incluindo tipo de quarto, ex: 'Standard', 'Luxo'), `Reservas` e `Usuários` (Recepcionistas, Gerentes).

**3. Script SQL de Criação e População**
Crie o script SQL que:
* Cria o banco `hotel_horizon_db`;
* Cria as tabelas principais (ex: `Usuarios`, `Hospedes`, `Quartos`, `Reservas`);
* Insere ao menos 3 registros por tabela.

**4. Interface de Login**
Descreva os campos, validações (ex: senha com no mínimo 6 caracteres), mensagens de erro e o fluxo completo (login válido e inválido) para um Recepcionista ou Gerente.

**5. Interface Principal (Dashboard)**
Descreva a tela inicial após o login de um Recepcionista. Indique quais menus estariam disponíveis (ex: 'Reservas', 'Hóspedes') e quais informações seriam exibidas (ex: "Check-ins de Hoje", "Check-outs de Hoje", "Quartos Livres").

**6. Interface de Cadastro de Hóspedes**
Descreva os campos obrigatórios (ex: Nome, CPF/Passaporte, Telefone), funcionalidades (Salvar, Editar) e a lógica de validação (ex: impedir a duplicação de CPF).

**7. Interface de Controle de Reservas**
Descreva como será o fluxo para criar uma nova reserva. Como o sistema deve verificar e exibir a disponibilidade de quartos para um período de datas selecionado (Check-in e Check-out)?

**8. Casos de Teste**
Crie 6 casos de teste (sucesso e falha), descrevendo as entradas e saídas esperadas (ex: Teste de login com falha, Teste de criação de reserva com sucesso, Teste de tentativa de reserva em data ocupada).

**9. Requisitos de Infraestrutura**
Liste o sistema operacional, SGBD, linguagem, frameworks e recursos mínimos de hardware (RAM, CPU) que você recomendaria para hospedar esta aplicação.