===
cli_py
===

This is a client-server command line interface that can be used with your python applications and communicate with them via commands entered in cli_client.

cli_server stars a python socket server that listens on a given port. By starting the cli_client, you are able to send commands to the server. Currently server only responds with "command + OK", but this is meant to be replaced with your own application logic (probably calling your application methods and get your data back).

This was originally made for the kalashnikovdb open source database management system that is being built on sourceforge. You can see it here:

http://sourceforge.net/projects/kalashnikovdb/

For any other quiestions, you can contact me via e-mail.