
from datetime import datetime, timedelta
from pathlib import Path
from zoneinfo import ZoneInfo
from html import escape

TZ = ZoneInfo("America/Sao_Paulo")
now = datetime.now(TZ)

# Sexta-feira = 4
days_until_friday = (4 - now.weekday()) % 7

next_update = (now + timedelta(days=days_until_friday)).replace(
    hour=21, minute=0, second=0, microsecond=0
)

if next_update <= now:
    next_update += timedelta(days=7)

remaining = next_update - now
total_minutes = int(remaining.total_seconds() // 60)

days, remainder = divmod(total_minutes, 1440)
hours, minutes = divmod(remainder, 60)

countdown = f"{days:02d}d  {hours:02d}h  {minutes:02d}m"
date_label = next_update.strftime("%d/%m/%Y às 21:00")

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

output = Path("assets/project-countdown.svg")
output.parent.mkdir(parents=True, exist_ok=True)
output.write_text(svg, encoding="utf-8")

print(f"Contador atualizado: {countdown}")
