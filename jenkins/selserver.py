from selenium import webdriver
from selenium.webdriver.common.keys import Keys


driver = webdriver.Remote(
#    command_executor="http://mr3PE0dGQFKvN5wG9JClpJE9izlW9tDm:Lx2fn6M4BnpfiMLileuBNYAWoMJo5dAG@GIFTSCOMDEMO.gridlastic.com:80/wd/hub",
#    desired_capabilities={
#             "browserName": "firefox",
#             "version": "32",
#             "video": "True",
#             "platform": "LINUX",
#         })
# print ("Video: https://s3.amazonaws.com/4ad4a405-ef2a-b3d3-a629-1ab0a2d338b1/121fce53-381d-da53-ec5e-f0e840017a98/play.html?"+driver.session_id)

	command_executor="http://localhost:4444/wd/hub", 	
	desired_capabilities={
	    'platform': "LINUX",
	    'browserName': "firefox",   
	    # 'version': "34"
	})

try:
    # driver.implicitly_wait(30)
    driver.maximize_window()
    driver.get('http://google.com')
    assert "Google" in driver.title
    print driver.session_id
finally:
    driver.quit()