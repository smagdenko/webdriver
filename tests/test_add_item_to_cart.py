def test_add_item_to_cart(app):
    for i in range(3):
        app.base_page.add_item()
        app.item_page.add_to_cart()
        app.item_page.get_text_element()
        app.base_page.back_driver()
    app.base_page.checkout()
    app.basket_page.remove_items_from_table()
    app.basket_page.check_message()
