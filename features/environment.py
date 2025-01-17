from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from app.application import Application
from selenium.webdriver.edge.options import Options
from webdriver_manager.firefox import GeckoDriverManager


def browser_init(context):
    """
    :param context: Behave context
    """

    context.platform = ""
    #Mobile_web Chrome device
    # mobile_emulation = {"deviceName": "Nexus 5"}
    # chrome_options = webdriver.ChromeOptions()
    # chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
    #
    # service = Service(ChromeDriverManager().install())
    # driver = webdriver.Chrome(service=service, options=chrome_options)
    #
    # context.driver = driver
    # context.platform = "Mobile_web"

    # BrowserStack configuration for mobile
    BROWSERSTACK_CONFIG = {
        'bstack:options': {
            'os': 'Android',
            'osVersion': '10.0',
            'deviceName': 'Samsung Galaxy S20',
            'realMobile': 'true',
            'userName': 'mary_bCHue6',
            'accessKey': 'UphCy53ptH9UisefSaqN',
            'sessionName': 'Internship_Project_Mobile',
            'buildName': 'Internship_Project_Build',
        },
        'browserName': 'Chrome',
        'browserVersion': 'latest',
    }

    # Initialize WebDriver with BrowserStack capabilities
    options = Options()
    options.set_capability('bstack:options', BROWSERSTACK_CONFIG['bstack:options'])
    options.set_capability('browserName', BROWSERSTACK_CONFIG['browserName'])
    options.set_capability('browserVersion', BROWSERSTACK_CONFIG['browserVersion'])

    context.driver = webdriver.Remote(
        command_executor='https://hub-cloud.browserstack.com/wd/hub',
        options=options
    )
    context.platform = "Mobile_web"
    # # BrowserStack configuration for web
    # BROWSERSTACK_CONFIG = {
    #     'bstack:options': {
    #         'os': 'Windows',
    #         'osVersion': '10',
    #         'resolution': '1920x1080',
    #         'sessionName': 'Internship_Project',
    #         'buildName': 'Internship_Project_Build',
    #         'userName': 'mary_bCHue6',
    #         'accessKey': 'UphCy53ptH9UisefSaqN',
    #     },
    #     'browserName': 'Chrome',
    #     'browserVersion': 'latest',
    # }
    #
    # # Initialize WebDriver with capabilities
    # options = webdriver.ChromeOptions()
    # options.set_capability('bstack:options', BROWSERSTACK_CONFIG['bstack:options'])
    # options.set_capability('browserName', BROWSERSTACK_CONFIG['browserName'])
    # options.set_capability('browserVersion', BROWSERSTACK_CONFIG['browserVersion'])
    #
    # context.driver = webdriver.Remote(
    #     command_executor='https://hub-cloud.browserstack.com/wd/hub',
    #     options=options
    # )

    #Chrome
    # driver_path = ChromeDriverManager().install()
    # service = Service(driver_path)
    # context.driver = webdriver.Chrome(service=service)


    #Allure_report_Commands
    # pip install allure_behave
    # behave - f allure_behave.formatter: AllureFormatter - o Test_Results
    # brew install allure
    # allure serve Test_Results

    # context.driver.maximize_window()
    context.driver.implicitly_wait(4)

    context.app = Application(context.driver)


def before_scenario(context, scenario):
    print('\nStarted scenario: ', scenario.name)
    browser_init(context)


def before_step(context, step):
    print('\nStarted step: ', step)


def after_step(context, step):
    if step.status == 'failed':
        print('\nStep failed: ', step)


def after_scenario(context, feature):
    context.driver.quit()


