from bs4 import BeautifulSoup
from pyquery import PyQuery
data = """
    <ul>
        <li class="item">item1</li>
        <li class="item">item2</li>
        <li class="item">item3</li>
    </ul>
"""
soup = BeautifulSoup(data, 'html.parser')
for item in soup.select('li.item'):
    print(item.get_text())
# PyQuery
html = """
    <h1>Sales</h1>
    <table id="table">
    <tr>
        <td>Lorem</td>
        <td>46</td>
        </tr>
    <tr>
        <td>Ipsum</td>
        <td>12</td>
        </tr>
        <tr>
        <td>Dolor</td>
        <td>27</td>
    </tr>
    <tr>
        <td>Sit</td>
        <td>90</td>
    </tr>
    </table>
    """
doc = PyQuery(html)
title = doc('h1').text()
print(title)
table_data = []
rows = doc('#table >tr')
for row in rows:
    name = PyQuery(row).find('td').eq(0).text()
    value = PyQuery(row).find('td').eq(1).text()
    print("({},{})".format(name, value))