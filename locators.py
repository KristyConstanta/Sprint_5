from selenium.webdriver.common.by import By


class Locators:
    login_button_main_page = (By.XPATH, './/button[text() = "Войти в аккаунт"]')   # Кнопка "Войти в аккаунт" на главной странице

    register_link = (By.XPATH, '//a[text() = "Зарегистрироваться"]')  # Ссылка "Зарегистрироваться"

    submit_button = (By.XPATH, '//button[text() = "Зарегистрироваться"]') # Кнопка "Зарегистрироваться"
    
    name_field = (By.XPATH, '//label[text()="Имя"]/following-sibling::input')# Поле "Имя"
    
    email_field = (By.XPATH, './/label[text()="Email"]/following-sibling::input')# Поле "Email"
 
    password_field = (By.XPATH, './/input[@name="Пароль"]')   # Поле "Пароль"
    
    login_button = (By.XPATH, './/button[text()="Войти"]')# Кнопка "Войти"
   
    incorrect_password_message = By.XPATH, '//p[text() = "Некорректный пароль"]' # Сообщение об ошибке "Некорректный пароль"
   
    make_an_order_button = By.XPATH, '//button[text()="Оформить заказ"]' # Кнопка "Оформить заказ"
   
    personal_account_button = By.XPATH, '//p[text() = "Личный Кабинет"]' # Кнопка "Личный кабинет"
    
    login_button_in_registration_form = By.XPATH, '//a[text() = "Войти"]'# Кнопка "Войти" на форме регистрации
    
    forgot_password_button = By.XPATH, '//a[text() = "Восстановить пароль"]'# Кнопка "Восстановить пароль"
    
    login_password_recovery_form_button = By.XPATH, '//a[text() = "Войти"]'# Кнопка "Войти" в форме восстановления пароля
   
    profile = By.XPATH, '//a[@href = "/account/profile"]' # Раздел "Профиль"
    
    order_history = By.XPATH, '//a[@href = "/account/order-history"]'# Раздел "История заказов"
    
    constructor_button_in_header = By.XPATH, '//p[text() = "Конструктор"]'# Кнопка "Конструктор" в шапке сайта
    
    logo = By.XPATH, '//div[@class="AppHeader_header__logo__2D0X2"]'# Логотип в шапке сайта

    logout_button = By.XPATH, '//button[@type = "button"]' # Кнопка "Выход"

    buns_section = By.XPATH, '//span[text() = "Булки"]'# Заголовок раздела "Булки"

    sauces_section = By.XPATH, '//span[text() = "Соусы"]'# Заголовок раздела "Соусы"

    fillings_section = By.XPATH, '//span[text() = "Начинки"]'# Заголовок раздела "Начинки"
    
    selected_section = (By.XPATH, '//div[@class="tab_tab__1SPyG tab_tab_type_current__2BEPc pt-4 pr-10 pb-4 pl-10 noselect"]')# Активный раздел конструктора