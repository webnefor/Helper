#
# https://github.com/seout
#

import src.CoreTk
import src.ModeLabel
import src.sortlist

from src.args import getparse, mintosec

def main() -> int:
    
    rslt = getparse() # Get args 
    
    src.sortlist.init(rslt.path); # init();
    
    core = src.CoreTk.Gpeg(rslt.mode); # Create a window
    
    view = src.ModeLabel.ModeLabel(core, mintosec(rslt.time)); # Create label's element
    
    view.appear()
    core.start();
    

    return 0;

if __name__ == "__main__":
    main()
