import os, sys, inspect

if os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..') not in sys.path:
    sys.path.append(os.path.join(sys.path[0][:sys.path[0].rfind(os.sep)], '../..'))
import pyeq2, pyeq2.ExtendedVersionHandlers


if __name__ == "__main__":

    for submodule in inspect.getmembers(pyeq2.Models_2D):
        if inspect.ismodule(submodule[1]):
            for equationClass in inspect.getmembers(submodule[1]):
                if inspect.isclass(equationClass[1]):
                    for extendedVersionName in pyeq2.ExtendedVersionHandlers.extendedVersionHandlerNameList:
                        
                        if (-1 != extendedVersionName.find('Offset')) and (equationClass[1].autoGenerateOffsetForm == False):
                            continue
                        if (-1 != extendedVersionName.find('Reciprocal')) and (equationClass[1].autoGenerateReciprocalForm == False):
                            continue
                        if (-1 != extendedVersionName.find('Inverse')) and (equationClass[1].autoGenerateInverseForms == False):
                            continue
                        if (-1 != extendedVersionName.find('Growth')) and (equationClass[1].autoGenerateGrowthAndDecayForms == False):
                            continue
                        if (-1 != extendedVersionName.find('Decay')) and (equationClass[1].autoGenerateGrowthAndDecayForms == False):
                            continue
    
                        equation = equationClass[1]('SSQABS', extendedVersionName)
                        print '2D ' + submodule[0] + ' --- ' + equation.GetDisplayName()
                        
    print 'Done.'