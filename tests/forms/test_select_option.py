"""Выбираем значение из раскрывающегося списка, используя три варианта: value, label и index, выпадающий список создается с помощью тега  <select>,каждый пункт  задается с помощью тега <option>"""
def test_select_by_value(select_page):
    select_page.navigate()
    select_page.select_by_value("3")


def test_select_multiple(select_page):
    select_page.navigate()
    select_page.select_multiple(["playwright", "python"])