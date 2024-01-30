#!/bin/bash

echo ""
echo 'Cleaning `docs/` sub-directory:'
echo ""

cd docs/
make clean 
cd ..

echo ""
echo 'Generating API (.rst) source files in `docs/source/` sub-directory:'
echo ""

sphinx-apidoc --output-dir "docs/source" -e -f "src/"

echo ""
echo 'Building (.html) API documentation files with sphinx in `docs/build/` sub-directory:'
echo ""

sphinx-build -M html "docs/source" "docs/build" 
