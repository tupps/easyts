# EasyTS
Command line access to Timestamp.io timesheet data

## Getting Started
EasyTS requires Python3 to be installed on your system. 

To run you will need to get a API_Key from Timestamp.io. To do this, login at timestamp.io and then select your profile (second item on left hand menu). From there select the API tab and copy out the API Key.

It will be in the form: 12345678-9abc-def0-1234-56789abcdef0

From your command line invoke easyts.py:

`./easyts.py --api_key 12345678-9abc-def0-1234-56789abcdef0`

## Useful commands

These examples assume that you have exported the api_key as an environment variable (see Tips and Tricks)

Get a list of tasks available to the user:

`./easyts.py tasks` 

Add a task to the users timesheet, for 450 minutes with the comment Worked Hard:

`./easyts.py entry --task 123456789 -c 'Worked Hard' -m 450 --days 2018-09-03`

Add multiple entries to the users timesheet (default time, 480 minutes, no comment)

`./easyts.py entry --task 123456789 --days 2018-09-03 2018-09-04 2018-09-05`

List all of the work logged for a month

`./easyts.py list --start 2018-08-01 --end 2018-08-31`

## Tips and Tricks
Export your api_key as a variable so you don't have to include it on the command line:

`export TIMESTAMP_IO_API_KEY=12345678-9abc-def0-1234-56789abcdef0`

Automatically add timesheet entries for this week (MacOS example, on linux substitute date for gdate):

``./easyts.py entry --task 123456789 --days `gdate -d'last monday' +%Y-%m-%d` `gdate -d'last tuesday' +%Y-%m-%d` `gdate -d'last wednesday' +%Y-%m-%d` `gdate -d'last thursday' +%Y-%m-%d` `gdate -dfriday +%Y-%m-%d` ``

List all the entries for this month:

``./easyts.py list --start $(gdate -d "`gdate +%Y%m01`" +%Y-%m-%d) --end  $(gdate -d "`gdate +%Y%m01` +1 month -1 day" +%Y-%m-%d) ``