import sublime, sublime_plugin

class DummyDebugCommand(sublime_plugin.TextCommand):
    def run(self, edit):
        first_region = self.view.sel()[0]        
        if first_region.empty():
            line = self.view.line(first_region)
            line_contents = self.view.substr(line)
            self.view.insert(edit, line.begin(), line_contents + "console.log('             '); \n")
            self.view.insert(edit, line.begin(), line_contents + "console.log('-------------'); \n")
            self.view.insert(edit, line.begin(), line_contents + "console.log(' ->', ); \n")
            self.view.insert(edit, line.begin(), line_contents + "console.log('-------------'); \n")
            self.view.insert(edit, line.begin(), line_contents + "console.log('             '); \n")
        else:            

            first_line = self.view.line(first_region)
                    
            self.view.insert(edit, first_line.begin(), "console.log('             '); \n")
            self.view.insert(edit, first_line.begin(), "console.log('-------------'); \n")

            variables_to_prompt = []

            for region in self.view.sel():                
                lines = self.view.lines(region)
                for line in lines:
                    line_contents = self.view.substr(line)
                    variables_to_prompt.append(line_contents)
                self.view.erase(edit, region)


            for var in variables_to_prompt:                
                self.view.insert(edit, first_line.begin(), "console.log('" + var + " ->', " + var + " ); \n")                

            self.view.insert(edit, first_line.begin(), "console.log('-------------'); \n")
            self.view.insert(edit, first_line.begin(), "console.log('             '); \n")        
