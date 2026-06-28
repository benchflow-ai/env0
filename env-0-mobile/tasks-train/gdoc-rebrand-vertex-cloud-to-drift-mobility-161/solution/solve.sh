#!/usr/bin/env bash
set -euo pipefail

OLD="Vertex Cloud"
NEW="Drift Mobility"

DOC_IDS=$(gws drive files list --params "{\"q\": \"fullText contains '$OLD'\", \"pageSize\": 100}" | python3 -c "
import sys, json
data = json.load(sys.stdin)
for f in data.get('files', []):
    print(f['id'])
")

for DOC_ID in $DOC_IDS; do
    gws docs documents batchUpdate \
      --params "{\"documentId\": \"$DOC_ID\"}" \
      --json "{
        \"requests\": [{
          \"replaceAllText\": {
            \"containsText\": {\"text\": \"$OLD\", \"matchCase\": true},
            \"replaceText\": \"$NEW\"
          }
        }]
      }"
    echo "Replaced in doc: $DOC_ID"
done

echo "Done. Replaced all occurrences of $OLD with $NEW."
