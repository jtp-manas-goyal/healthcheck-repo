from playwright.sync_api import sync_playwright
import json
import datetime
import time
import os
import base64
from action import listOfAllActions , listOfWebsites

class PlaywrightActions:
    linkofwebsite = ""
    
    def initialize(self):
        self.playwright = sync_playwright().start()
        self.browser = self.playwright.chromium.launch(args=["--disable-gpu", "--single-process", "--headless=new"], headless=True)
        self.page = self.browser.new_page()

    def teardown(self):
        """Close the page and the browser, stop Playwright"""
        # self.page.close()
        self.browser.close()
        # self.playwright.stop()

    # goto function - will redirect to the provided url.
    def goto(self, url, errorval):
        try:
            self.page.goto(url , timeout = 10000)
            return "Navigated to " + url 
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"
    # click funciton - it will click on the given selector.
    def click(self, selector, errorval):
        try:
            self.page.click(selector , timeout = 20000)
            return f"Clicked on {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def fill(self, selector, value, errorval):
        try:
            self.page.fill(selector, value ,timeout = 10000)
            return f"Filled {selector} with value '{value}'"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def type(self, selector, value, errorval):
        try:
            self.page.type(selector, value , timeout = 10000)
            return f"Typed '{value}' into {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def hover(self, selector, errorval):
        try:
            self.page.hover(selector ,timeout = 10000)
            return f"H hovered over {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def wait_for_selector(self, selector, errorval , timeout=10000):
        try:
            self.page.wait_for_selector(selector, timeout=timeout)
            return f"Waited for {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def wait_for_navigation(self, errorval):
        try:
            self.page.wait_for_navigation()
            return "Waited for navigation"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def select(self, selector, value, errorval):
        try:
            self.page.select_option(selector, value,timeout = 10000)
            return f"Selected '{value}' in {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def select_opt(self, selector, option_xpath, errorval):
        try:
            self.page.click(selector,timeout = 10000)
            option_value = self.page.query_selector(option_xpath).inner_text()
            if option_value:
                self.page.select_option(selector, option_value,timeout = 10000)
                return f"Selected '{option_value}' in {selector}"
            else:
                return f"Error in {errorval} step,Option not found in {selector}."

        except Exception as e:
            return f"Error in {errorval} step. \nError: {str(e)}"
        
    def check(self, selector, errorval):
        try:
            self.page.check(selector,timeout = 10000)
            return f"Checked {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def uncheck(self, selector, errorval):
        try:
            self.page.uncheck(selector,timeout = 10000)
            return f"Unchecked {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def press(self, selector, key, errorval):
        try:
            self.page.press(selector, key,timeout = 10000)
            return f"Pressed '{key}' on {selector}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def check_text(self, selector, expected_text, errorval):
        try:
            text = self.page.locator(selector).text_content( timeout =  10000)
            if text == expected_text:
                return f"Text matches: '{expected_text}'"
            else:
                return f"Error in {errorval} step, Text does not match. Found: '{text}', Expected: '{expected_text}'"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def screenshot(self, path, errorval):
        try:
            self.page.screenshot(path=path , timeout =  10000)
            return f"Screenshot saved to {path}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"
    
    def full_screenshot(self , imgpath ):
        try:
            self.page.screenshot(path = imgpath , full_page = True)
            return f"screenshot is saved on this path  {imgpath}. "
        except Exception as e:
            return f"Error in the screenshot step. \n error : {str(e)}"
            

    def evaluate(self, script, errorval):
        try:
            result = self.page.evaluate(script , timeout =  10000 )
            return f"Script evaluated, result: {result}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def navigate_back(self, errorval):
        try:
            self.page.go_back( timeout =  10000)
            return "Navigated back"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def navigate_forward(self, errorval):
        try:
            self.page.go_forward( timeout =  10000)
            return "Navigated forward"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def wait_for_timeout(self, ms, errorval):
        try:
            self.page.wait_for_timeout(ms, timeout =  10000)
            return f"Waited for {ms} milliseconds"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def set_viewport(self, width, height, errorval):
        try:
            self.page.set_viewport_size({"width": width, "height": height}, timeout =  10000)
            return f"Viewport set to {width}x{height}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"

    def scroll_to(self, x, y, errorval):
        try:
            self.page.evaluate(f"window.scrollTo({x}, {y})" , timeout =  10000)
            return f"Scrolled to ({x}, {y})"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"
        
    def close(self, errorval):
        try:
            self.teardown( timeout =  10000)
            return "Closed the browser session"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"
    
    def fill_date(self, selector, errorval , date):
        try:
            input_element = self.page.query_selector(selector)
            input_element.fill(date)
            return f"Filled the date {date}"
        except Exception as e:
            return f"Error in {errorval} step. \n error : {str(e)}"
    
    def file_upload(self , selector , type, errorval):
        pass
    
    def perform_actions(self, website_index):
        actions = listOfAllActions[website_index]["actions"]["actions"]
        results = []
        for action in actions:
            
            action_type = action.get("action")
            errorval = action.get("errorval")
            
            if action_type not in [
                "goto", "click", "fill", "type", "hover",
                "wait_for_selector", "wait_for_navigation", "select",
                "check", "uncheck", "press", "check_text",
                "screenshot", "evaluate", "navigate_back",
                "navigate_forward", "wait_for_timeout", "set_viewport",
                "scroll_to", "close" , "select_opt" , "fill_date" ,
                "full_screenshot"
            ]:
                results.append(f"Error: Unknown action '{action_type}'")
                break

            if action_type == "goto":
                url = action.get("url")
                self.linkofwebsite =  url
                result = self.goto(url, errorval)
            elif action_type == "click":
                selector = action.get("selector")
                result = self.click(selector, errorval)
            elif action_type == "fill":
                selector = action.get("selector")
                value = action.get("value")
                result = self.fill(selector, value, errorval)
            elif action_type == "type":
                selector = action.get("selector")
                value = action.get("value")
                result = self.type(selector, value, errorval)
            elif action_type == "hover":
                selector = action.get("selector")
                result = self.hover(selector, errorval)
            elif action_type == "wait_for_selector":
                selector = action.get("selector")
                timeout = action.get("timeout", 10000)
                result = self.wait_for_selector(selector, timeout, errorval)
            elif action_type == "wait_for_navigation":
                result = self.wait_for_navigation(errorval)
            elif action_type == "select":
                selector = action.get("selector")
                value = action.get("value")
                result = self.select(selector, value, errorval)
            elif action_type == "check":
                selector = action.get("selector")
                result = self.check(selector, errorval)
            elif action_type == "uncheck":
                selector = action.get("selector")
                result = self.uncheck(selector, errorval)
            elif action_type == "press":
                selector = action.get("selector")
                key = action.get("key")
                result = self.press(selector, key, errorval)
            elif action_type == "check_text":
                selector = action.get("selector")
                expected_text = action.get("expected_text")
                result = self.check_text(selector, expected_text, errorval)
            elif action_type == "screenshot":
                path = action.get("path")
                result = self.screenshot(path, errorval)
            elif action_type == "evaluate":
                script = action.get("script")
                result = self.evaluate(script, errorval)
            elif action_type == "navigate_back":
                result = self.navigate_back(errorval)
            elif action_type == "navigate_forward":
                result = self.navigate_forward(errorval)
            elif action_type == "wait_for_timeout":
                ms = action.get("ms")
                result = self.wait_for_timeout(ms, errorval)
            elif action_type == "set_viewport":
                width = action.get("width")
                height = action.get("height")
                result = self.set_viewport(width, height, errorval)
            elif action_type == "scroll_to":
                x = action.get("x")
                y = action.get("y")
                result = self.scroll_to(x, y, errorval)
            elif action_type == "close":
                result = self.close(errorval)
            elif action_type == "select_opt":
                selector = action.get("selector")
                option_xpath = action.get("option_xpath")
                result = self.select_opt(selector , option_xpath , errorval)
            elif action_type == "fill_date":
                selector = action.get("selector")
                if not action.get("date"):
                    todayDate = str(datetime.datetime.now().date())
                else:
                    todayDate = action.get("date")
                result = self.fill_date(selector= selector , date=todayDate ,errorval= errorval )
                
            
            if "Error in" in result:
                results.append({"step" :errorval , "result" : result}) 
                break 
            else:
                results.append({"step" :errorval , "result" : result}) 
        
        res = self.stringfyRes(results)
        
        # self.linkofwebsite = (self.linkofwebsite[7:])
        # imgpath = f"image/{self.linkofwebsite}/test.jpg"
        
        # time.sleep(2)
        
        # self.full_screenshot(imgpath=imgpath)
        
        # with open(imgpath, "rb") as image_file:
        #  encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
        
        return ({"result" : res })
    
    def stringfyRes( self , results ):
        logs = [] 
        result = "" #this is to store the end result
        ifsuccessfull = "Successfull"
        for item in results:
            str = " {step} :- {res}  \n ".format(step = item["step"] , res = item["result"])
            logs.append(str)
    
            if "Error" in item["result"]:
                ifsuccessfull = "Un-Successfull"
                result = "There is an error , please check your Webite. !!"
        
        
        log = ' '.join(logs) 

        if result == "":
            result = "Webite is working properly!"


        mainstr = '''\
            
        ------------------------{isnot} !----------------------
        *************************************************
        -------------------------------------------------------
                            -:LOGS:-
                        ---------------
        {log}
        -------------------------------------------------------
        *************************************************
        -------------------------------------------------------
        Result : {msg}\
        
        -------------------------------------------------------
                            '''.format(isnot = ifsuccessfull , log = log , msg = result )              
        return mainstr

# Test the PlaywrightActions with a set of actions
def handler(event, context):
    searchedWebsite = listOfWebsites.index(event["website"])
    
   
    object = PlaywrightActions()
    object.initialize()
    try:
        res = object.perform_actions(searchedWebsite)
    finally:
        object.teardown()  
        
    return res
