import pexpect

def run_script():
    script_path = 'tg_api.py'  # Укажите путь к вашему скрипту

    # Запуск скрипта
    child = pexpect.spawn(f'python {script_path}')

    # Ожидание запроса телефона
    child.expect_exact('Please enter your phone (or bot token):')
    child.sendline(phone_number)
    
    # Ожидание запроса кода подтверждения
    child.expect('Enter the code you received:')
    child.sendline(code)
    
    # Ожидание запроса пароля
    child.expect('Two-step verification is enabled. Please enter your password:')
    child.sendline(password)
    
    # Вывод результатов
    child.interact()

# Замените эти значения на ваши реальные данные
phone_number = '+380962553957'
code = 'Ваш код подтверждения'
password = 'Ваш пароь'

run_script()