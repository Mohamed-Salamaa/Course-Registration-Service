#!/bin/bash
set -e

# System dependencies (Python, PostgreSQL, Adminer optional)
sudo apt update
sudo apt install -y python3.10 python3.10-venv python3-pip postgresql postgresql-client

# Optional: Adminer (web DB UI) and Apache integration
if ! dpkg -s adminer >/dev/null 2>&1; then
  sudo apt install -y adminer
  sudo a2enconf adminer || true
  sudo systemctl reload apache2 || true
fi

# Project root
home="$(pwd)"

# Create fresh virtual environment
rm -rf "$home/env"
python3 -m venv "$home/env"
echo "export PYTHONPATH='$home'" >> "$home/env/bin/activate"

# Activate venv and install Python dependencies
echo "Entering the env"
source "$home/env/bin/activate"
pip install --upgrade pip
pip install -r "$home/requirements.txt"

# Ensure JWT and related libs are compatible with Python 3.10
pip install --upgrade PyJWT Flask-JWT-Extended attrs

# Export helpful env var for running the app
echo "export FLASK_APP=run.py" >> "$home/env/bin/activate"

echo "Setup complete. Next steps:"
echo "1) source env/bin/activate"
echo "2) Ensure PostgreSQL user/db exist (see README)."
echo "3) flask run"
