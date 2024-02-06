import argparse

def mintosec(x) -> int:
    return int(x)*60;


def getparse(args=None):
    parser = argparse.ArgumentParser(description='Helper: You can learn any language')
    parser.add_argument('--time',
                        type=int,
                        default=1,
                        help='(default: 1 minute)'
                        )

    parser.add_argument('--path',
                        type=str,
                        default="/list.conf",
                        help='(default: /list.conf)'
                        )

    parser.add_argument('--mode',
                        type=int,
                        default=1,
                        help='default: 1: (true)'
                        )

    paramsopt = parser.parse_args()

    return paramsopt;
