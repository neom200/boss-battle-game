# 🗡️ The Guardians of Habnamia: Terminal Boss Battle

Bem-vindo às terras distantes de **Habnamia**. Após a morte do Rei Absalom III, o reino mergulhou no caos com o surgimento de 12 criaturas monstruosas. Como um aventureiro humilde, sua missão — dada pela Rainha Rasphelia — é derrotar esses monstros para conquistar fama, glória e a mão da Princesa Myrian.

Este é um RPG de combate por turnos focado em estratégia e reflexos, rodando inteiramente no seu terminal.

---

## 🎮 Como Jogar

Para iniciar sua jornada, execute o script principal:

```bash
python3 main.py
```

### Comandos de Menu
No menu principal, você pode navegar usando números:
- `0`: Sair do jogo.
- `1`: Ver perfil (Status, Equipamento, Ouro).
- `2`: Visitar a Loja (Comprar armas, armaduras e poções).
- `3`: Lista de Bosses (Escolha seu próximo desafio pelo nome).
- `4`: Salvar progresso.

---

## 🔥 Sistema de Combate

O combate é dinâmico e exige atenção à sua **Posição** e **Stamina**.

### Comandos de Batalha:
- `a`: **Atacar** - Gasta 1 stamina. Causa dano baseado em sua força e arma.
- `d`: **Defender** - Aumenta sua defesa para o próximo turno e recupera 1 stamina.
- `h`: **Curar** - Bebe uma poção para recuperar vida. Recupera 1 stamina.
- `l` / `r`: **Mover (Esquerda/Direita)** - Muda sua posição no campo de batalha para desviar de ataques. Recupera 1 stamina.

> [!IMPORTANT]
> **Posicionamento**: Muitos ataques de bosses são direcionais. Se o boss atacar para a direita (`r`) e você estiver na direita, você receberá dano. Mova-se no momento certo!

### Sistema de Combos
Realizar sequências específicas de movimentos libera bônus:
- **Combo de Ataque**: Sequências de ataques (`a, a, a`) podem causar dano extra.
- **Combo de Defesa**: Defender repetidamente (`d, d, d`) garante uma proteção massiva.
- **Evasão**: Mover-se estrategicamente (`r, l, r`) pode aumentar sua defesa temporariamente.

---

## 🛡️ Atributos e Itens

### Classes de Personagem
- **Fighter**: Equilibrado, com foco em força e combate direto.
- **Priest**: Alta defesa e maior capacidade de cura.
- **Elf**: Ágil, focado em velocidade para desviar de ataques.
- **Orc**: Grande resistência e stamina para lutas prolongadas.

### Atributos:
- **Strength (Att)**: Define seu dano básico.
- **Defence (Def)**: Reduz o dano recebido.
- **Speed (Spd)**: Aumenta chances de acerto crítico e esquiva.
- **Stamina (Stm)**: Necessária para atacar. Se chegar a 0, você não poderá golpear!

### A Loja
Use o ouro obtido ao derrotar monstros para evoluir:
- **Armas**: De Adagas a Lâminas Gigantes, cada uma aumenta seu dano.
- **Armaduras**: Do Couro ao Obsidiana, aumentam sua mitigação de dano.
- **Poções**: Essenciais para sobreviver a batalhas longas.

---

## 👹 Os 12 Desafios

Sua jornada o levará a enfrentar desde criaturas trapaceiras até dragões ancestrais. Alguns dos nomes que ecoam nos pesadelos de Habnamia são:
- *Pupu, o Tolo*
- *Nemus, o Dragão de Água*
- *Shamack, o Abismo Eterno*

Cada boss possui um padrão de ataque único. Observe, aprenda e adapte sua estratégia!

---

## ⚙️ Instalação e Requisitos

- **Linguagem**: Python 3.x
- **Dependências**: Nenhuma (usa apenas bibliotecas padrão como `random` e `json`).

Para rodar, basta clonar o repositório e executar:
```bash
python main.py
```

*Boa sorte, herói. Habnamia conta com você!*
