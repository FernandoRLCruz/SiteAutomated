
def wait_and_click(self, by, value):
    element = self.is_element_visible(by, value)
    self.click_on_returned_element(element)
