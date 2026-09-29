# ARH -> OPERATOR: GWR-CONTOUR-RETIRE-R01 exact-bytes preservation route

status: BLOCKED_OPERATOR_ASSISTED_PRESERVATION_REQUIRED
entity: ARH / АРХИВАРИУС
project_time: omitted

## Человеческий итог

Exact KOO preservation task принят и проверен.

Текущий ARH writer:
`entities/archivarius/current/ARH__replacement-current-writer-r03.md`
blob `3df64956a5ec4a21e11a4f469abaf91a1e4fd092`
status `WRITER_ESTABLISHED`.

Fresh HQ boundary на входе:
`7467d0eee13ab6a102cbd61bd6de87722b3f053c`.

Три exact legacy objects:
- `/run/wb-shard-gateway/request.json`
- `/var/log/wb-shard-gateway/audit.jsonl`
- `/etc/systemd/system/wellbeing-shard-gateway-verify.service`

Прямое readback:
- request.json: BLOCKED_EACCES
- audit.jsonl: BLOCKED_EACCES
- systemd unit: READABLE

Поэтому ARH не может доказать exact bytes первых двух объектов и не может объявить preservation PASS.

Никакой payload не реконструировался по тексту.

## Authorized operator-assisted route

ОПЕРАТОР должен выполнить один блок на exact host `p552203.kvmvps`.

Блок:
- не удаляет и не меняет source objects;
- копирует bytes в закрытый локальный project preservation contour;
- использует `umask 077`;
- не добавляет remote и не выполняет push;
- создаёт новый локальный Git repository только для immutable version identity;
- фиксирует raw SHA-256 source/destination;
- выполняет `cmp` source/destination;
- фиксирует Git blob identity каждого payload;
- создаёт package manifest и package SHA-256;
- печатает exact locator и commit.

Target:
`/data/wellbeing-lab/private-preservation/gwr-contour-retire-r01/v01`

Если target уже существует, блок fail-closed и ничего не переписывает.

## Exact operator block

```bash
set -euo pipefail
umask 077

SRC_REQUEST='/run/wb-shard-gateway/request.json'
SRC_AUDIT='/var/log/wb-shard-gateway/audit.jsonl'
SRC_UNIT='/etc/systemd/system/wellbeing-shard-gateway-verify.service'

ROOT='/data/wellbeing-lab/private-preservation/gwr-contour-retire-r01'
DST="$ROOT/v01"

if [ -e "$DST" ]; then
  echo "BLOCKED: preservation target already exists: $DST" >&2
  exit 40
fi

sudo install -d -m 0700 -o shd -g shd "$ROOT"
sudo install -d -m 0700 -o shd -g shd "$DST"

sudo test -f "$SRC_REQUEST"
sudo test -f "$SRC_AUDIT"
sudo test -f "$SRC_UNIT"

sudo cp --reflink=auto --sparse=never -- "$SRC_REQUEST" "$DST/request.json"
sudo cp --reflink=auto --sparse=never -- "$SRC_AUDIT" "$DST/audit.jsonl"
sudo cp --reflink=auto --sparse=never -- "$SRC_UNIT" "$DST/wellbeing-shard-gateway-verify.service"

sudo chown shd:shd "$DST/request.json" "$DST/audit.jsonl" "$DST/wellbeing-shard-gateway-verify.service"
chmod 0600 "$DST/request.json" "$DST/audit.jsonl" "$DST/wellbeing-shard-gateway-verify.service"

SRC_REQUEST_SHA256="$(sudo sha256sum "$SRC_REQUEST" | awk '{print $1}')"
SRC_AUDIT_SHA256="$(sudo sha256sum "$SRC_AUDIT" | awk '{print $1}')"
SRC_UNIT_SHA256="$(sudo sha256sum "$SRC_UNIT" | awk '{print $1}')"

DST_REQUEST_SHA256="$(sha256sum "$DST/request.json" | awk '{print $1}')"
DST_AUDIT_SHA256="$(sha256sum "$DST/audit.jsonl" | awk '{print $1}')"
DST_UNIT_SHA256="$(sha256sum "$DST/wellbeing-shard-gateway-verify.service" | awk '{print $1}')"

test "$SRC_REQUEST_SHA256" = "$DST_REQUEST_SHA256"
test "$SRC_AUDIT_SHA256" = "$DST_AUDIT_SHA256"
test "$SRC_UNIT_SHA256" = "$DST_UNIT_SHA256"

sudo cmp -s -- "$SRC_REQUEST" "$DST/request.json"
sudo cmp -s -- "$SRC_AUDIT" "$DST/audit.jsonl"
sudo cmp -s -- "$SRC_UNIT" "$DST/wellbeing-shard-gateway-verify.service"

cat > "$DST/OBJECTS.sha256" <<EOF
$DST_REQUEST_SHA256  request.json
$DST_AUDIT_SHA256  audit.jsonl
$DST_UNIT_SHA256  wellbeing-shard-gateway-verify.service
EOF

cat > "$DST/LINEAGE.txt" <<'EOF'
legacy_contour=wellbeing-shard-gateway
host=p552203.kvmvps
request_source=/run/wb-shard-gateway/request.json
audit_source=/var/log/wb-shard-gateway/audit.jsonl
unit_source=/etc/systemd/system/wellbeing-shard-gateway-verify.service
purpose=GWR-CONTOUR-RETIRE-R01 exact-bytes preservation before any retirement
retirement_performed=no
EOF

cd "$DST"
git init -q
git config user.name 'Wellbeing ARH Preservation'
git config user.email 'arh-preservation@local.invalid'
printf '* -text\n' > .gitattributes

git add -- request.json audit.jsonl wellbeing-shard-gateway-verify.service OBJECTS.sha256 LINEAGE.txt .gitattributes
git commit -q -m 'Preserve exact GWR-CONTOUR-RETIRE-R01 bytes'

COMMIT="$(git rev-parse HEAD)"
TREE="$(git rev-parse HEAD^{tree})"
REQUEST_BLOB="$(git hash-object request.json)"
AUDIT_BLOB="$(git hash-object audit.jsonl)"
UNIT_BLOB="$(git hash-object wellbeing-shard-gateway-verify.service)"
MANIFEST_BLOB="$(git hash-object OBJECTS.sha256)"
LINEAGE_BLOB="$(git hash-object LINEAGE.txt)"
PACKAGE_SHA256="$(sha256sum OBJECTS.sha256 | awk '{print $1}')"

git fsck --no-dangling --strict >/dev/null
git diff --exit-code
git diff --cached --exit-code

echo "PRESERVATION_LOCATOR=$DST"
echo "GIT_COMMIT=$COMMIT"
echo "GIT_TREE=$TREE"
echo "REQUEST_SHA256=$DST_REQUEST_SHA256"
echo "REQUEST_GIT_BLOB=$REQUEST_BLOB"
echo "AUDIT_SHA256=$DST_AUDIT_SHA256"
echo "AUDIT_GIT_BLOB=$AUDIT_BLOB"
echo "UNIT_SHA256=$DST_UNIT_SHA256"
echo "UNIT_GIT_BLOB=$UNIT_BLOB"
echo "OBJECTS_MANIFEST_GIT_BLOB=$MANIFEST_BLOB"
echo "LINEAGE_GIT_BLOB=$LINEAGE_BLOB"
echo "PACKAGE_SHA256=$PACKAGE_SHA256"
echo "BYTE_IDENTITY=request:PASS audit:PASS unit:PASS"
echo "GIT_FSCK=PASS"
echo "RETIREMENT_PERFORMED=NO"
```

## Boundary

До выполнения блока:
`PRESERVATION_PASS = NOT_ESTABLISHED`.

Gateway retirement:
`NOT_PERFORMED`.

NEW SIS retirement task:
`NOT_YET_ADMISSIBLE`.

После получения exact stdout ОПЕРАТОРА ARH должен:
1. прочитать exact local locator;
2. independently recompute three payload SHA-256;
3. verify Git commit/tree/blob identities;
4. verify OBJECTS.sha256 and LINEAGE.txt;
5. compare evidence with operator stdout;
6. only then return PASS/FAIL to KOO.

---
КТО: ARH / АРХИВАРИУС
СТАТУС: BLOCKED_OPERATOR_ASSISTED_PRESERVATION_REQUIRED
