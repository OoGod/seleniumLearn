import unittest
from selenium import webdriver
from bs4 import BeautifulSoup as bs


class douban(unittest.TestCase):
    
    def setUp(self):
        self.driver = webdriver.PhantomJS()
        
    def testDouban(self):
        self.driver.get("https://movie.douban.com/subject/4739952/reviews")
        
        while True:
            soup = bs(self.driver.page_source,"lxml")
            names = soup.find_all("a",{"class":"name"})
            times = soup.find_all("span",{"class":"main-meta"})
            for name,time in zip(names,times):
                print("昵称: ",name.get_text().strip(),"\t时间: ",time.get_text().strip())

            if self.driver.page_source.find("btn-unfold") != -1:
                break
            self.driver.find_element_by_class_name("next").click()
    def tearDown(self):
        self.driver.quit()    


if __name__ == "__main__":
    unittest.main()
