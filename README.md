## SavingStuffBot

This is the code for the Telegram bot that was given as a test assignment. (Not writing the task here as its is a public repo.)

The local disk is used as the database. The bot deals with both audio and voice messages as audio messages.

For launching the bot with docker:\
`sudo docker build -t test_bot .`\
`sudo docker run -it -e TOKEN=<token here> test_bot`