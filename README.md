# Simple-SSH-Logs-Analyzer
Script em Python dentifica IPs com múltiplas falhas de login em arquivo de logs SSH e gera alerta.

Processos:
- Abrir o arquivo
- Procurar linhas com “Failed password”
- Extrair o IP
- Contar quantas vezes apareceu
- Se IP > 3 tentativas = alerta ao usuário

Tecnologias
- Python
- Linux (conceito)
- Logs SSH

Conceitos Aplicados
- Monitoramento de eventos
- Detecção de comportamento anômalo
- Segurança defensiva (Blue Team)
- Brute force
- Analise de logs (atividade real de SOC)

