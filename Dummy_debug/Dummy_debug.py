import sublime, sublime_plugin

class DummyDebugCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        region = self.view.sel()[0]
        
        if region.empty():
            line = self.view.line(region)
            line_contents = self.view.substr(line)
            self.view.insert(edit, line.begin(), line_contents + "console.log('             '); \n")
            self.view.insert(edit, line.begin(), line_contents + "console.log('-------------'); \n")
            self.view.insert(edit, line.begin(), line_contents + "\n\n")
            self.view.insert(edit, line.begin(), line_contents + "console.log('-------------'); \n")
            self.view.insert(edit, line.begin(), line_contents + "console.log('             '); \n")
        else:
            selection_content = self.view.substr(region)                        
            self.view.erase(edit, region)
            line = self.view.line(region)
            line_contents = self.view.substr(line)
            self.view.insert(edit, region.begin(), line_contents + "console.log('             '); \n")
            self.view.insert(edit, region.begin(), line_contents + "console.log('-------------'); \n")
            self.view.insert(edit, region.begin(), line_contents + "console.log('" + selection_content + " -> '," + selection_content + "); \n\n")
            self.view.insert(edit, region.begin(), line_contents + "console.log('-------------'); \n")
            self.view.insert(edit, region.begin(), line_contents + "console.log('             '); \n")                            