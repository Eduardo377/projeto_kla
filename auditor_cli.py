import os
import sys
from dotenv import load_dotenv
from groq import Groq

# Cores ANSI para o terminal Linux
RED = "\033[91m"
GREEN = "\033[92m"
YELLOW = "\033[93m"
CYAN = "\033[96m"
RESET = "\033[0m"

# --- CONFIGURAÇÃO ---
load_dotenv()
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    print("\033[91m[✗] Erro: GROQ_API_KEY não encontrada no .env\033[0m")
    sys.exit(1)

# Inicializa o cliente Groq
client = Groq(api_key=API_KEY)


def print_banner():
    banner = f"""{CYAN}
    =========================================
      🛡️  KENSEI LOG AUDITOR (KLA) - CLI
    ========================================={RESET}
    """
    print(banner)


def analyze_log(log_content):
    prompt = f"""
    Você é um Engenheiro de Segurança SOC especialista em ambientes Linux.
    Analise o log abaixo. Identifique:
    1. Anomalias críticas.
    2. Tentativas de intrusão.
    Forneça 2 ações imediatas de mitigação. Seja técnico e direto.
    
    LOG:
    {log_content}
    """

    try:
        print(f"{YELLOW}[⏳] Consultando Llama 3 via Groq...{RESET}")

        # Chamada ultra-rápida do modelo Llama 3
        response = client.chat.completions.create(
            messages=[{"role": "user", "content": prompt}],
            model="llama-3.1-8b-instant",
            temperature=0.2,
        )

        print(f"\n{GREEN}[✓] RELATÓRIO DA AUDITORIA:{RESET}")
        print("-" * 60)
        print(response.choices[0].message.content)
        print("-" * 60)

    except Exception as e:
        print(f"{RED}[✗] Falha na comunicação: {e}{RESET}")


if __name__ == "__main__":
    print(f"{CYAN}=========================================")
    print("  🛡️  KENSEI LOG AUDITOR (KLA) - CLI")
    print(f"========================================={RESET}")

    if len(sys.argv) < 2:
        print("Uso: python3 auditor_cli.py <arquivo>")
        sys.exit(1)

    try:
        # Lê apenas as últimas 50 linhas para otimização
        with open(sys.argv[1], "r", errors="ignore") as f:
            lines = f.readlines()
            log_data = "".join(lines[-50:])

        if log_data.strip():
            analyze_log(log_data)
        else:
            print(f"{YELLOW}[!] O arquivo de log está vazio.{RESET}")

    except Exception as e:
        print(f"{RED}[✗] Erro ao ler arquivo: {e}{RESET}")
