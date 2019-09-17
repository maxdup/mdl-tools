sphinx-autobuild \
    -z ../mdltools \
    --ignore "*~" \
    --ignore "*/#*#*" \
    --ignore "*.#*" \
    --ignore "*.swp" \
    --ignore "*.pdf" \
    --ignore "*.log" \
    --ignore "*.out" \
    --ignore "*.toc" \
    --ignore "*.aux" \
    --ignore "*.idx" \
    --ignore "*.ind" \
    --ignore "*.ilg" \
    --ignore "*.tex" \
    --ignore "*.tex" \
    source build
