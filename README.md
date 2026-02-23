# Simple-SSH-Logs-Analyzer
Script em Python dentifica IPs com múltiplas falhas de login em arquivo de logs SSH e gera alerta.

<img width="1197" height="176" alt="image" src="https://github.com/user-attachments/assets/9000e2ab-dd5e-49bc-b825-554fa25a5b77" /> <br>

<img width="727" height="260" alt="image" src="https://github.com/user-attachments/assets/0ffc790c-8238-4e00-9171-d77d394ff3d0" /> <br>

Processos:
- Abrir o arquivo
- Procurar linhas com “Failed password”
- Extrair o IP
- Contar quantas vezes apareceu
- Se IP > 3 tentativas = alerta ao usuário

<br>

Tecnologias
- Python
- Linux (conceito)
- Logs SSH

<br>

Conceitos Aplicados
- Monitoramento de eventos
- Detecção de comportamento anômalo
- Segurança defensiva (Blue Team)
- Brute force
- Analise de logs (atividade real de SOC)

