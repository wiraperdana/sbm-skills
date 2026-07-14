#!/usr/bin/env bash
# Pasang skill SBM ke direktori skill Claude Code.
#
# Pemakaian:
#   ./install.sh              pasang global, ke ~/.claude/skills
#   ./install.sh --project    pasang ke .claude/skills di direktori kerja saat ini
set -euo pipefail

ASAL="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)/skills"

if [[ "${1:-}" == "--project" ]]; then
  TUJUAN="$(pwd)/.claude/skills"
  RUANG="project ini"
else
  TUJUAN="$HOME/.claude/skills"
  RUANG="semua project (global)"
fi

mkdir -p "$TUJUAN"

for skill in sbm sbm-kemenkeu sbm-ui; do
  if [[ -e "$TUJUAN/$skill" ]]; then
    printf 'Menimpa skill lama: %s\n' "$skill"
    rm -rf "${TUJUAN:?}/$skill"
  fi
  cp -R "$ASAL/$skill" "$TUJUAN/"
  printf 'Terpasang: /%s\n' "$skill"
done

printf '\nSelesai. Dipasang untuk %s, di %s\n' "$RUANG" "$TUJUAN"
printf 'Coba panggil: /sbm berapa honorarium narasumber eselon I?\n'
