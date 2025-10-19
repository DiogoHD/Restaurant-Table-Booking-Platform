# Sistema de Reservas Couraça
Sistema de reservas online para o Café-Restaurante Couraça, feito com Django.

## Configurações
### Pré-Requisitos
- Python
- pip
- Git

### Clonar o Projeto
```bash
git clone https://github.com/DiogoHD/Restaurant-Table-Booking-Platform.git
```

### Criar e Ativar o Ambiente Virtual
```bash
python -m venv .venv
.\.venv\Scripts\Activate.ps1
cd restaurant_table_booking_platform
```

### Instalar dependências
```bash
pip install -r requirements.txt
```

### Migrar a base de dados
```bash
python manage.py makemigrations
python manage.py migrate
```

### Criar superuser (Opcional, mas serve para aceder às opções admin)
```bash
python manage.py createsuperuser
```

### Executar o servidor
```bash
python manage.py runserver
```
Num browser web (chrome, brave, firefox,...), aceder a [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

## Funcionalidades
### Home ([http://127.0.0.1:8000/](http://127.0.0.1:8000/))
- Logo clicável (que redireciona para a página principal)
- Carrousel de imagens
- Redes Sociais clicáveis
- Botão para efetuar uma reserva

### Reservar ([http://127.0.0.1:8000/reserva/](http://127.0.0.1:8000/reserva/))
- Forms com validação de dados para:
    - Número de telemóvel (Verifica se contém 9 digitos e se começa por 9 (número português))
    - Pessoas por Mesa (Verifica se o número de pessoas cabe na mesa escolhida)
    - Double-booking (Verifica se a mesa está livre à hora pretendida)
    - Mesa Opcional (O cliente pode escolher a mesa ou não, sendo-lhe atribuída uma mesa caso não escolha)

### Admin ([http://127.0.0.1:8000/admin/](http://127.0.0.1:8000/admin/))
Nota: Necessário fazer login com o superuser
- Adicionar mesas ao restaurante 
    - número/nome da mesa 
    - número de lugares
- Adicionar reservas nas mesmas condições dos convidados
- Gerir mesas e reservas
    - Adicionar
    - Eliminar
- Filtrar e procurar reservas
    - Filtrar por data e/ou mesa
    - Procurar por nome
- Mostrar estatisticas de reservas diárias
    - Em "Action" selecionar "Daily summary"
    - Escolher a caixa que seleciona todas as reservas, que se encontra no cabeçalho das reservas
    - Clicar em "Go"