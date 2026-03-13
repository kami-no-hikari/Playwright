from tabulate import tabulate

def test_get_table(table_page):
    rows_text = table_page.get_all_inner_texts()
    table_headers = rows_text[0].split('\t')
    table_data = [row.split('\t') for row in rows_text[1:]]

    print(tabulate(table_data, headers=table_headers))