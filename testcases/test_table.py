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

    #Specific Cell
    fifth_row_first_column = static_table.locator("tbody tr").nth(4).locator("td").nth(0).inner_text()
    print("Fifth row, first column:", fifth_row_first_column)
    
    #Dynamic Web table
    print("====================Dynamic web Table====================")
    dynamic_table = page.locator("h2", has_text="Dynamic Web Table").locator("xpath=following::table[1]")

    dynamic_row = dynamic_table.locator("tbody tr")
    print("Dynamic table row count:", dynamic_row.count())

    dynamic_data = []
    for i in range(dynamic_row.count()):
        cells = dynamic_row.nth(i).locator("td")
        cell_count = cells.count()
        row_data = []
        for j in range(cell_count):
            row_data.append(cells.nth(j).inner_text())
        dynamic_data.append(row_data)
    print("Dynamic table data:", dynamic_data)

    #Find the chrome row
    chrome_row = dynamic_row.filter(has_text="Chrome")
    if chrome_row.count() > 0:
        print("Chrome row:", chrome_row.inner_text())
        chrome_cells = chrome_row.locator("td")
        chrome_data = [chrome_cells.nth(j).inner_text() for j in range(chrome_cells.count())]
        print("Chrome row data:", chrome_data)
        for i in range(len(chrome_data)):
            if chrome_data[i] == "Chrome":
                print("Chrome row, first column:", chrome_data[0])
                print("Chrome row, second column:", chrome_data[1])
                print("Chrome row, third column:", chrome_data[2])
                print("Chrome row, fourth column:", chrome_data[3])
                
    #CPU Value
    print("====================CPU Value====================")
    if chrome_row.count() > 0:
        chrome_cells = chrome_row.locator("td")
        headers = dynamic_table.locator("thead th")
        cpu_index = -1
        for i in range(headers.count()):
            header_text = headers.nth(i).inner_text()
            if "CPU" in header_text:
                cpu_index = i
                break

    if cpu_index != -1:
        cpu_value = chrome_cells.nth(cpu_index).inner_text()
        print("CPU Value:", cpu_value)
        
#     Task:
#     Memory Size of Firefox process: 89.9 MB

# Network speed of Chrome process: 6.0 Mbps

# Disk space of Firefox process: 0.36 MB/s    
    #Pagination Table
    print("====================Pagination Table====================")
    pagination_table = page.locator("h2",has_text = "Pagination Web Table").locator("xpath=following::table[1]")
    pagination_rows = pagination_table.locator("tbody tr")
    pagination_links = page.locator("#pagination li a") 
    print("Pagination row count:", pagination_rows.count())
    print("Pagination pages:", pagination_links.count()) 
    for page_number in range(pagination_links.count()):
        if page_number >0:
            pagination_links.nth(page_number).click() 
            page.wait_for_timeout(1000)
    print("\nPage numbers:",page_number + 1)
    pagination_rows = pagination_table.locator("tbody tr")
    for i in range(pagination_rows.count()): 
        cells = pagination_rows.nth(i).locator("td")
        row_data = []
        for j in range(cells.count()):
            row_data.append(cells.nth(j).inner_text())
        print("Row", i + 1, "data:", row_data)   
        
    # Task: Select the product from the pagination table     