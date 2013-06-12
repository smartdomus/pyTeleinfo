'''
Created on 9 juin 2013

@author: Hoareau
'''
import tornado

class MenuModule(tornado.web.UIModule):
    

    
    def render(self):
        return """<nav class=\"horizontal-nav full-width\">
   <ul>
      <li><a href=\"/\">Dashboard</a></li>
      <li><a href=\"/live\">Live</a></li>
      <li><a href=\"#\">Historic</a></li>
      <li><a href=\"#\">Cost</a></li>
      <li><a href=\"#\">About</a></li>
      <li><a href=\"#\">Contact</a></li>
   </ul>
</nav>
"""    

    def javascript_files(self):
        return "/static/libs/jquery.horizontalNav.js"
    
    
    def embedded_javascript(self):
        return "$(document).ready(function() {$(\'.full-width\').horizontalNav({});});"