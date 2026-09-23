from playwright.sync_api import sync_playwright, Page

def test_static_web_table(page: Page):
    page.goto("https://testautomationpractice.blogspot.com/", wait_until="domcontentloaded")

    static_table = page.locator("table[name='BookTable']")
    rows = static_table.locator("tbody tr")

    row_count = rows.count()
    assert row_count > 0, "Static web table is empty or not found"

    table_data = []
    mukesh_books = []
    total_price = 0

    for i in range(row_count):
        cells = rows.nth(i).locator("td")
        cell_count = cells.count()
        row_data = []

        for j in range(cell_count):
            row_data.append(cells.nth(j).inner_text().strip())

        table_data.append(row_data)

        if cell_count >= 2:
            book_name = cells.nth(0).inner_text().strip()
            author = cells.nth(1).inner_text().strip()
            if author == "Mukesh":
                mukesh_books.append(book_name)

        if cell_count >= 4:
            price_text = cells.nth(3).inner_text().strip().replace(",", "")
            if price_text.isdigit():
                total_price += int(price_text)

    print("Table Data:", table_data)
    print("Books written by Mr. Mukesh:", mukesh_books)
    print("Total price:", total_price)

    assert any(row[1] == "Mukesh" for row in table_data), "Mukesh was not found in the table"
    assert total_price > 0, "No valid numeric prices were found in the table"
    