#!/usr/bin/env bash
set -euo pipefail

# sphinx-to-astro.sh
# Post-process Sphinx autodoc2 markdown output for Astro Starlight.
#
# Prerequisites: run `tox -e docs` first (builds Sphinx API docs into
# docs/src/content/docs/api/).  This script only does post-processing:
#   1. Clean up Sphinx build artifacts
#   2. Replace unsupported code block languages
#   3. Add YAML frontmatter required by Starlight
#   4. Remove placeholder .mdx files superseded by generated .md

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
ASTRO_API_DIR="${REPO_ROOT}/docs/src/content/docs/api"

echo "==> Post-processing Sphinx autodoc2 output for Starlight"
echo "    API dir: ${ASTRO_API_DIR}"

# Verify that tox -e docs has been run
if [ ! -d "${ASTRO_API_DIR}/apidocs" ]; then
    echo "ERROR: ${ASTRO_API_DIR}/apidocs not found."
    echo "       Run 'tox -e docs' first to generate the Sphinx API docs."
    exit 1
fi

# Clean up Sphinx build artefacts that Astro does not need
rm -rf "${ASTRO_API_DIR}/.buildinfo" \
       "${ASTRO_API_DIR}/.doctrees" \
       "${ASTRO_API_DIR}/objects.inv"

# Post-process generated markdown files:
# 1. Replace unsupported code block languages with Astro-compatible ones
# 2. Add YAML frontmatter required by Starlight
# 3. Remove placeholder .mdx files that have been superseded
find "${ASTRO_API_DIR}" -name '*.md' -type f | while read -r md_file; do
    # Replace unsupported code block languages (portable: redirect + mv)
    tmp_sed_file=$(mktemp)
    sed -e 's/```pycon/```python/g' -e 's/```default/```text/g' "${md_file}" > "${tmp_sed_file}"
    mv "${tmp_sed_file}" "${md_file}"

    # Extract the first H1 heading as the title (skip if frontmatter already exists)
    if head -1 "${md_file}" | grep -q '^---$'; then
        continue
    fi

    title=$(head -1 "${md_file}" | sed 's/^# //' | sed 's/\[`\(.*\)`\].*/\1/')

    # Prepend YAML frontmatter
    tmpfile=$(mktemp)
    {
        printf '%s\n' '---'
        printf 'title: "%s"\n' "${title}"
        printf 'description: "Auto-generated API reference for %s"\n' "${title}"
        printf '%s\n\n' '---'
        cat "${md_file}"
    } > "${tmpfile}"
    mv "${tmpfile}" "${md_file}"

    # Remove the corresponding placeholder .mdx file if it exists
    base=$(basename "${md_file}" .md)
    dir=$(dirname "${md_file}")
    if [ -f "${dir}/${base}.mdx" ]; then
        rm "${dir}/${base}.mdx"
        echo "    Replaced placeholder: ${base}.mdx -> ${base}.md"
    fi
done

echo "==> Sphinx-to-Astro bridge complete"
echo "    Generated $(find "${ASTRO_API_DIR}" -name '*.md' -type f | wc -l | tr -d ' ') markdown files"
