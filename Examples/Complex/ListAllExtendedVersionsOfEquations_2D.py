import os, sys, inspect

# ensure pyeq2 can be imported
exampleFileDirectory = sys.path[0][:sys.path[0].rfind(os.sep)]
pyeq2IimportDirectory =  os.path.join(os.path.join(exampleFileDirectory, '..'), '..')
if pyeq2IimportDirectory not in sys.path:
    sys.path.append(pyeq2IimportDirectory)
    
    import pyeq2

if __name__ == "__main__":

    for submodule in inspect.getmembers(pyeq2.Models_2D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    for extendedVersionName in pyeq2.ExtendedVersionHandlers.extendedVersionHandlerNameList:
                        try:
                            equation = equationClass[1]('SSQABS', extendedVersionName)
                        except:
                            continue
                        print '2D ' + submodule[0] + ' --- ' + equation.GetDisplayName()
                        
    print 'Done.'