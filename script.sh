#! /bin/bash

echo "Немного ожидания..."
jupyter nbconvert --execute main.ipynb --to html --no-input
echo "Готово!"