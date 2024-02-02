#
# https://github.com/seout
#

import src.CoreTk
import src.ModeLabel
import src.sortlist

from src.args import getparse, mintosec

def main() -> int:
    rslt = getparse()
    #
    src.sortlist.init(rslt.path);
    #
    core = src.CoreTk.Gpeg(rslt.mode);
    #
    view = src.ModeLabel.ModeLabel(core, mintosec(rslt.time));
    #
    view.create()
    #
    view.appear()
    #
    core.start();
    #

    return 0;

if __name__ == "__main__":
    main()
