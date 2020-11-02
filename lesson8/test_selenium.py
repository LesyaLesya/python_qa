from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


def test_assert_main_page(browser, url):
    """Test main page title"""
    browser.get(url)
    assert browser.title == "Your Store", "Wrong title"


def test_main_page_elements_is_displayed(browser, url):
    """Test elements on main page"""
    browser.get(url)
    # banner
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 "#content .swiper-viewport:nth-child(1)")))
    except TimeoutException:
        assert False, "Banner is not displayed"

    # banner pagination bullets
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 ".swiper-pagination.slideshow0.swiper-pagination-clickable.swiper-pagination-bullets"
                 )))
    except TimeoutException:
        assert False, "Slideshow pagination bullets are not displayed"

    # header Featured
    try:
        header = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h3")))
    except TimeoutException:
        assert False, "Header is not displayed"
    assert header.text == "Featured", "Wrong header text"

    # carousel brand
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#carousel0.swiper-container-horizontal")))
    except TimeoutException:
        assert False, "Carousel brand is not displayed"

    # carousel pagination bullets
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located(
                (By.CSS_SELECTOR,
                 ".swiper-pagination.carousel0.swiper-pagination-clickable.swiper-pagination-bullets"
                 )))
    except TimeoutException:
        assert False, "Carousel pagination bullets are not displayed"


def test_catalogue_page_elements_is_displayed(browser, url):
    """Test elements on catalogue page"""
    browser.get(f'{url}index.php?route=product/category&path=18')
    # bread_crump
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "breadcrumb")))
    except TimeoutException:
        assert False, "Breadcrump is not displayed"

    # header
    try:
        header = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.TAG_NAME, "h2")))
    except TimeoutException:
        assert False, "Header of catalogue is not displayed"
    assert header.text == "Laptops & Notebooks", "Wrong header"

    # catalogue img
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "img-thumbnail")))
    except TimeoutException:
        assert False, "Image of catalogue is not displayed"

    # left menu
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "column-left")))
    except TimeoutException:
        assert False, "Left menu is not displayed"

    # banner under left menu
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "banner0")))
    except TimeoutException:
        assert False, "Banner is not displayed"


def test_product_page_elements_is_displayed(browser, url):
    """Test elements on product page"""
    browser.get(f'{url}index.php?route=product/product&path=18&product_id=47')
    # product header
    try:
        product_header = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".btn-group + h1")))
    except TimeoutException:
        assert False, "Header is not displayed"
    assert product_header.text == "HP LP3065", "Wrong header text"

    # button cart
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "button-cart")))
    except TimeoutException:
        assert False, "Button cart is not displayed"

    # images block
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "thumbnails")))
    except TimeoutException:
        assert False, "Block of images is not displayed"

    # rating block
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "rating")))
    except TimeoutException:
        assert False, "Rating block is not displayed"

    # product description
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#tab-description > p")))
    except TimeoutException:
        assert False, "Product description is not displayed"


def test_user_login_page_elements_is_displayed(browser, url):
    """Test elements on user login page"""
    browser.get(f'{url}index.php?route=account/login')
    # new customer form
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#content > .row > .col-sm-6:first-child >.well")))
    except TimeoutException:
        assert False, "Form for new customer is not displayed"

    # old customer form
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR,
                                              "#content > .row > .col-sm-6:last-child >.well")))
    except TimeoutException:
        assert False, "Form for old customer is not displayed"

    # right list menu
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "list-group")))
    except TimeoutException:
        assert False, "Right menu list is not displayed"

    # button for new customer form
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "a.btn.btn-primary")))
    except TimeoutException:
        assert False, "Button in new customer form is not displayed"

    # button for old customer form
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "input.btn.btn-primary")))
    except TimeoutException:
        assert False, "Button in old customer form is not displayed"


def test_admin_login_page_elements_is_displayed(browser, url):
    """Test elements on admin login page"""
    browser.get(f'{url}admin/')
    # panel heading
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "panel-heading")))
    except TimeoutException:
        assert False, "Panel heading is not displayed"

    # username input
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-username")))
    except TimeoutException:
        assert False, "Username input is not displayed"

    # password input
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-password")))
    except TimeoutException:
        assert False, "Password input is not displayed"

    # login button
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    except TimeoutException:
        assert False, "Login button is not displayed"

    # help block
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CLASS_NAME, "help-block")))
    except TimeoutException:
        assert False, "Help block is not displayed"


def test_login_action(browser, url):
    """Test login to admin panel"""
    browser.get(f'{url}admin/')
    try:
        username_input = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-username")))
    except TimeoutException:
        assert False, "Username input is not displayed"

    try:
        password_input = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-password")))
    except TimeoutException:
        assert False, "Password input is not displayed"

    try:
        login_button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    except TimeoutException:
        assert False, "Login button is not displayed"
    username_input.clear()
    username_input.send_keys("demo")
    password_input.clear()
    password_input.send_keys("demo")
    login_button.click()
    try:
        WebDriverWait(browser, 5).until(EC.title_is("Dashboard"))
    except TimeoutException:
        assert False, "Title is wrong"


def test_logout_action(browser, url):
    """Test logout from admin panel"""
    browser.get(f'{url}admin/')
    try:
        username_input = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-username")))
    except TimeoutException:
        assert False, "Username input is not displayed"

    try:
        password_input = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-password")))
    except TimeoutException:
        assert False, "Password input is not displayed"

    try:
        login_button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    except TimeoutException:
        assert False, "Login button is not displayed"
    username_input.clear()
    username_input.send_keys("demo")
    password_input.clear()
    password_input.send_keys("demo")
    login_button.click()
    try:
        logout_button = WebDriverWait(browser, 5).until(
            EC.element_to_be_clickable((By.CSS_SELECTOR, ".nav > li:nth-child(2) > a")))
    except TimeoutException:
        assert False, "Logout button is not displayed and not clickable"
    logout_button.click()
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.XPATH,
                                              "//h1[contains(text(), 'enter your login')]")))
    except TimeoutException:
        assert False, "Fail logout"


def test_go_to_products_table(browser, url):
    """Test go to prodcts table in admin panel"""
    browser.get(f'{url}admin/')
    try:
        username_input = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-username")))
    except TimeoutException:
        assert False, "Username input is not displayed"

    try:
        password_input = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.ID, "input-password")))
    except TimeoutException:
        assert False, "Password input is not displayed"

    try:
        login_button = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "button.btn.btn-primary")))
    except TimeoutException:
        assert False, "Login button is not displayed"
    username_input.clear()
    username_input.send_keys("demo")
    password_input.clear()
    password_input.send_keys("demo")
    login_button.click()
    try:
        catalog = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#menu-catalog > a")))
    except TimeoutException:
        assert False, "Catalogue is not displayed in menu"
    catalog.click()
    try:
        categories = WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, "#collapse1 > li:nth-child(1) > a")))
    except TimeoutException:
        assert False, "Categories is not displayed in menu"
    categories.click()
    try:
        WebDriverWait(browser, 5).until(
            EC.visibility_of_element_located((By.CSS_SELECTOR, ".table-responsive")))
    except TimeoutException:
        assert False, "Table with products is not displayed"
