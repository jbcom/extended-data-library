#!/usr/bin/env bash
set -euo pipefail

# sphinx-to-astro.sh
# Build Sphinx API docs (via autodoc2) as markdown and place them into the
# Astro Starlight content directory so that the static site generator can
# pick them up.

REPO_ROOT="$(cd "$(dirname "$0")/.." && pwd)"
SPHINX_SRC="${REPO_ROOT}/docs/sphinx"
ASTRO_API_DIR="${REPO_ROOT}/docs/src/content/docs/api"

echo "==> Building Sphinx autodoc2 API docs (markdown output)"
echo "    Source:  ${SPHINX_SRC}"
echo "    Output:  ${ASTRO_API_DIR}"

# Ensure output directory exists
mkdir -p "${ASTRO_API_DIR}"

# Build Sphinx docs as markdown into the Astro content directory
sphinx-build -E -b markdown "${SPHINX_SRC}" "${ASTRO_API_DIR}"

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
