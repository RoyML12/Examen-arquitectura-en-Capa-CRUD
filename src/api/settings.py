from pathlib import Path

BASE_DIR = Path(__file__).resolve().parents[2]
DATA_DIR = BASE_DIR / "data"

CLIENTES_FILE = DATA_DIR / "clientes.json"
VEHICULOS_FILE = DATA_DIR / "vehiculos.json"
ORDENES_FILE = DATA_DIR / "ordenes.json"
