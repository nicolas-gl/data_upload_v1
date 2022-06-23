import openpyxl
import image_URL

my_file = 'committent_catalog_items.xlsx'

def reporter(file) -> None:

    book = openpyxl.open(file, read_only=True)
    sheet = book.active
    n = 0

    for row in sheet:
        if n == 0:
            n = 1
            continue
        a = '{}\n{}, {}\n\n'.format(
            row[2].value,           # статус
            row[0].value,           # артикул
            row[1].value,           # название
            )
        url = image_URL.make(row[0].value)
        print(url)
        print(a)

# reporter(my_file)

from IPython.display import Image

url= 'https://bersoantik.com/media/_versions/catalog/2022/5/antikvarnaya-pech_02_0843_1_object_big.jpg'

Image(
    url=url,
    width=400,
    # unconfined=True,      non-understood parameter
)