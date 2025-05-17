#!/bin/bash

INSTALL_PATH="/usr/local/bin/psw"
SCRIPT_PATH="$(pwd)/main.py"

echo "#!/bin/bash" > psw
echo "python3 \"$SCRIPT_PATH\" \"\$@\"" >> psw
chmod +x psw

sudo mv psw "$INSTALL_PATH"

echo "[✔] Commande 'psw' installée. Vous pouvez maintenant l'utiliser !"

