from selenium.webdriver.support.ui import Select
from locators.quote_page_locators import QuotesPageLocator
from parssers.quote import QuoteParser
class QuotePage:
    def __init__(self,browser):
        self.browser=browser
    @property
    def quotes(self):

        return [QuoteParser(e) for e in self.browser.find_elements_by_css_selector(QuotesPageLocator.QUOTE)]
    @property
    def author_dropdown(self):
        element= self.browser.find_element_by_css_selector(QuotesPageLocator.AUTHOR_DROPDOWN)
        return Select(element)
    def tags_dropdown(self):
        element= self.browser.find_element_by_css_selector(QuotesPageLocator.TAG_DROPDOWN)
        return Select(element)
    def select_author(self,author_name):
        self.author_dropdown.select_by_visible_text(author_name)
    def get_available_tags(self):
        return[option.text.strip() for option in self.tags_dropdown.options]
    def select_tag(self,tag_name):
        self.tags_dropdown.select_by_visible_text(tag_name)