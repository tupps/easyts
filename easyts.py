#!/usr/bin/env python3

import os
import sys
import argparse
import datetime

import easyts_lib.tasks
import easyts_lib.entries
import easyts_lib.entry


def handle_tasks(task_args):
    easyts_lib.tasks.get_tasks(task_args.api_key)


def handle_list(list_args):
    easyts_lib.entries.send_request(list_args.api_key,
                             list_args.start,
                             list_args.end)


def handle_entry(entry_args):
    easyts_lib.entry.add_time_entries(entry_args.api_key,
                               entry_args.days,
                               entry_args.minutes,
                               entry_args.task,
                               entry_args.comment)


parser = argparse.ArgumentParser()
parser.add_argument("-a", "--api_key",
                    help="Timestamp.io API Key, or set TIMESTAMP_IO_API_KEY environment variable",
                    default=os.getenv('TIMESTAMP_IO_API_KEY'))
parser.add_argument('--version', action='version',
                    version='%(prog)s 0.1')

subparsers = parser.add_subparsers(title="TimeStamp Commands", help="TimeStamp Commands Help")

parser_tasks = subparsers.add_parser("tasks", help="Show all the tasks available")
parser_tasks.set_defaults(func=handle_tasks)

parser_list = subparsers.add_parser("list", help="Show all timesheet entries")
parser_list.add_argument("-s", "--start",
                         help="Filter output to show everything after this date",
                         type=datetime.date.fromisoformat)
parser_list.add_argument("-e", "--end",
                         help="Filter output to show everything before this date",
                         type=datetime.date.fromisoformat)
parser_list.set_defaults(func=handle_list)

parser_entry = subparsers.add_parser("entry", help="Enter a timesheet entry")
parser_entry.add_argument("-d", "--days",
                          help="Days to create a timesheet entry",
                          type=datetime.date.fromisoformat,
                          nargs='*')
parser_entry.add_argument("-c", "--comment",
                          help="Comment for the entry")
parser_entry.add_argument("-m", "--minutes",
                          help="Minutes worked (default 480)./easy",
                          default=480)
parser_entry.add_argument("-t", "--task",
                          help="Task ID for the entry",
                          type=int)
parser_entry.set_defaults(func=handle_entry)

args = parser.parse_args()

if args.api_key is None:
    print("You must specify an api_key (ENV: TIMESTAMP_IO_API_KEY) to access TimeStamp API")
    sys.exit()

try:
    args.func(args)
except AttributeError:
    parser.print_help()
