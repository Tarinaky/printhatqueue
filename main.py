import printhatqueue
import argparse

def queue(args):
    print(args)
    with printhatqueue.QueueFile('queue.zip') as queue_file:
        for gcode in args.g:
            queue_file.add_gcode(gcode)

if __name__ == '__main__':
    parser = argparse.ArgumentParser('Manage a queue of gcode files that can be dispatched to octoprint')
    subparsers = parser.add_subparsers()

    scan_parser = subparsers.add_parser('queue', help='add a gcode file to the print queue')
    scan_parser.add_argument('-g', required=True, action='append', type=str, help='a gcode file to add')
    scan_parser.set_defaults(func=queue)

    release_parser = subparsers.add_parser('release', help='release the next job to a printer')
    release_parser.add_argument('-p', required=True, type=str, help='the address of the printer')


    args = parser.parse_args()
    args.func(args)
