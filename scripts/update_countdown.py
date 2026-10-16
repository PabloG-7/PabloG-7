
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
from html import escape

# Horário de Brasília
TZ = ZoneInfo("America/Sao_Paulo")
now = datetime.now(TZ)

# Primeira atualização: 23/10/2026 às 21h
first_update = datetime(2026, 10, 23, 21, 0, tzinfo=TZ)

# Mantém a primeira data fixa até ela chegar.
# Depois, passa a contar para as próximas sextas-feiras.
next_update = first_update

while next_update <= now:
    next_update += timedelta(days=7)

# Calcula o tempo restante
remaining = next_update - now
total_minutes = max(0, int(remaining.total_seconds() // 60))

days, remainder = divmod(total_minutes, 1440)
hours, minutes = divmod(remainder, 60)

countdown = f"{days:02d}d  {hours:02d}h  {minutes:02d}m"
date_label = next_update.strftime("%d/%m/%Y às %H:%M")

# Cria o SVG
svg = f"""<svg xmlns="http://www.w3.org/2000/svg"
  width="800" height="170" viewBox="0 0 800 170">

  <rect width="800" height="170" rx="16" fill="#0d1117"/>

  <rect x="1" y="1" width="798" height="168" rx="15"
    fill="none" stroke="#30363d" stroke-width="2"/>

  <text x="400" y="37" text-anchor="middle"
    font-family="Arial, sans-serif" font-size="16"
    fill="#8b949e" letter-spacing="2">
    PRÓXIMA ATUALIZAÇÃO EM
  </text>

  <text x="400" y="100" text-anchor="middle"
    font-family="Arial, sans-serif" font-size="44"
    font-weight="bold" fill="#58a6ff">
    {escape(countdown)}
  </text>

  <text x="400" y="140" text-anchor="middle"
    font-family="Arial, sans-serif" font-size="15"
    fill="#8b949e">
    {escape(date_label)} (Brasília)
  </text>

</svg>"""

# Salva o contador
output = Path("assets/project-countdown.svg")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(svg, encoding="utf-8")

print(f"Próxima atualização: {date_label}")
print(f"Tempo restante: {countdown}")
