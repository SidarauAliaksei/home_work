from selenium.webdriver.common.by import By


class MainPageLoc:
    main_page_url_loc = 'http://automationpractice.com/index.php'

    login_loc = (By.CSS_SELECTOR, ".login")
    basket_empty_loc = (By.XPATH, '//div[@class="shopping_cart"]//span[contains(text(), "(empty)")]')

    faded_short_sleeve_t_shirts_loc = (By.XPATH, "//a[@data-id-product = '1']")
    blouse_add_to_basket_loc = (By.XPATH, "//a[@data-id-product = '2']")

    cross_loc = (By.XPATH, "//*[@class ='cross']")

    basket_loc = (By.XPATH, "//*[@title ='View my shopping cart']")
    go_to_basket_with_blouse_loc = (By.CLASS_NAME, 'icon-chevron-right right')
