import re

tentativas = {} # armazenar tentativas por IP

with open("auth_backup_log.txt", "r") as arquivo:
    linhas = arquivo.readlines()

for linha in linhas:
    if "Failed password" in linha:

        # procura o IP usando regex
        ip_encontrado = re.search(r'from (\d+\.\d+\.\d+\.\d+)', linha)

        if ip_encontrado:
            ip = ip_encontrado.group(1)

            # conta as tentativas do IP usando regex
            if ip in tentativas:
                tentativas[ip] += 1
            else:
                tentativas[ip] = 1

limite = 3 # define limite para o alerta

print("\n===========================================================================\n")

print("RELATÓRIO DE ANÁLISE DE LOGS SSH\n")

for ip, quantidade in tentativas.items():
    print(f"IP: {ip} - Tentativas: {quantidade}")
    if quantidade <= limite:
        print("Comportamento normal — número de tentativas dentro do limite aceitável.")
    else:
        print("Alerta: Possível ataque de força bruta detectado.\n")

print("\n===========================================================================\n")