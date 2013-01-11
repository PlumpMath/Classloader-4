import sublime, sublime_plugin
import os
import fnmatch

class ClassloaderClassCompletion(sublime_plugin.EventListener):
  """Looks through folders starting from a 'com' folder to find namespaces and classes for Classloader code"""
  
  def __init__(self): 
    # get a view from the window
    self.view = sublime.active_window().active_view()

  def needsCompletion(self):
    location = self.view.sel()[0] 

    for region in self.view.sel():
      line = self.view.line(region)
      line_contents = self.view.substr(line)

      # get all the contents of the file
      content = sublime.Region(0,self.view.size())

      # get all the lines
      lines = self.view.split_by_newlines(content)

      # search for package
      completionNeeded = (line_contents.find("Package") != -1);

      # search for Import, Extends, and com. 
      i = 0;
      for line in lines:
        if line.contains(location): # on this line
          for region in [line, lines[i - 1]]: # and the preceding line
            if self.view.substr(region).find("Import") != -1:
              completionNeeded = True
            elif self.view.substr(region).find("Extends") != -1:
              completionNeeded = True  
            elif self.view.substr(region).find("\"com.") != -1:
              completionNeeded = True  
        i = i + 1

      return completionNeeded

  def writingPackage(self):
    for region in self.view.sel():
      line = self.view.line(region)
      line_contents = self.view.substr(line)

      # if 'Package' is on the line
      return (line_contents.find("Package") != -1)

  def getNamespaces(self):
    root = self.getComFolder();

    namespaces = []
    for path in self.getList(root, False):
      path = self.convertPath(path)
      namespaces.append((path, path))

    return namespaces

  def getClasses(self):
    root = self.getComFolder();

    classes = []
    for path in self.getList(root, True):
      path = self.convertPath(path)
      classes.append((path, path))

    return classes

  def getList(self, root, includeFiles):
    matches = []
    if (root):
      # return either a list of files or of folders
      for root, dirnames, filenames in os.walk(root):        
        if (includeFiles):
          for filename in fnmatch.filter(filenames, '*.js'):
            matches.append(os.path.join(root, filename).replace("\\", "/"))
        else:
          for dirname in dirnames:
            matches.append(os.path.join(root, dirname).replace("\\", "/"))

    return matches  

  def convertPath(self, path):
    returnvalue = "";
    # find the path after "/com/"
    if (path.find(".js") != -1):
      returnvalue = path[path.find("/com/")+1:path.find(".js")]
    else:
      returnvalue = path[path.find("/com/")+1:]

    # convert slashes  
    return returnvalue.replace("/", ".")


  def getComFolder(self):
    filename = self.view.file_name()

    # on Windows paths contains backward slashes
    filename = filename.replace("\\", "/")

    # start and end index
    comindex = filename.find('/com/')

    if (comindex == -1):
      return False

    # get folder structure  
    package = filename[0:comindex + 5]

    return package

  def on_query_completions(self, view, prefix, locations):
    # update view
    self.view = view

    # do not run the calculations unless we are on certain lines
    if(not self.needsCompletion()):
      return False

    # package results are namespace, otherwise show complete classes
    if(self.writingPackage()):
      sugs = self.getNamespaces()
    else:
      sugs = self.getClasses()
    
    return sugs
