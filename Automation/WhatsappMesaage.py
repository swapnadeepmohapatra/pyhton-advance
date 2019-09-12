# _19RFN  -> GroupName Class
# _3u328   -> Input Field
# _3M-N-   -> send button

from selenium import webdriver

driver = webdriver.Chrome(
    'C:/Users/Home PC/Downloads/Compressed/chromedriver_win32/chromedriver.exe')
driver.get('https://web.whatsapp.com/')

while True:

    name = input('Enter the name of user or group : ')
    msg = input('Enter your message : ')
    count = int(input('Enter the count : '))

    input('Enter anything if you want to send message to ')

    user = driver.find_element_by_xpath('//span[@title = "{}"]'.format(name))
    user.click()

    msg_box = driver.find_element_by_class_name('_3u328')

    for i in range(count):
        msg_box.send_keys(msg)
        button = driver.find_element_by_class_name('_3M-N-')
        button.click()
