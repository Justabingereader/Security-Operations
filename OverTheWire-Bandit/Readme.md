 

### Walkthrough

Level 0: accessed port 2220 on bandit.labs.overthewire.org through a -p flag

Level 0-1: accessed a file called readme present in the home directory

Level 1-2: used the password in the readme file present in level 1 before using the cat command to access the "-" file in level 2 through use of full directory specification.

Level 2-3: Used the password in the "-" file present in level 2 before using the cat command to access the "-- spaces in this filename--"

file in level 3 through the use of single quotes to specify directory.

Level 3-4: Used the password in the "--spaces in this filename--" file in level 3 before using the cat command to access the ".inhere" file in level 4 through the use of a dot in front of the filename to specify hidden directories.

Level 4-5: Used the password present in the ".inhere" file in level 4 before using the the cat command to access the only human readable file through the use of manual inspection.

Level 5-6: Used the password found through manual inspection in level 5 before conducting a manual inspection across all files in the inhere directory, navigating directly from home directory rather than directory specific naviagtion to the files, when that failed, an online research was conducted which revealed the presence of the file as a hidden file in one of the subdirectories present within the inhere directory, using the "find /inhere -type f -size 1033 ! executable" command to satisfy the conditions required to find the specific file in question.

Level 6-7: Used the find command to search the root directory for a file that had user bandit7, group bandit6 and a size of 33 bytes. was initially using plain 33 to search, after revisiting the command that worked in level 5-6, i discovered there was a c omission at the end of the 33 bytes size specification, leading to only processes and runs that i had insufficient privilege to access being displayed.

Level 7-8: After authentication to level 7, used ls in default directory to list set of available files, discovered data.txt. used vim data.txt to open file, then pressed / key to search for the millionth text, screenshoted the text through native window application, pasted on an AI system to generate the text from the image, after pasting, it failed, tried manual translation from image directly to terminal, also failed, used grep -w millionth data.txt, generated the line, copied the generated line and pasted it into level 8's SSH authentication, it worked.

![Level 7-8: grep -w millionth data.txt](screenshots/level7-8_grep_millionth.png)

Level 8-9: After logging in to the 8th level, i ran an ls command to list available files and directories in the default path, through the use of the sort command which arranges and groups all duplicate texts in the document, i then piped the output of the sort command into a uniq command with the -u flag to generate the unique output in the text.

![Level 8-9: sort data.txt | uniq -u](screenshots/level8-9_sort_uniq.png)

Level 9-10: After logging in to the 9th level, i ran an ls command to list the active directories and files present in the server. i found just data.txt. i ran a vim data.txt, then i used the / symbol to manually specify the "=====" that prepended the password string, i found various text that justified this condition, but just one that listed an actual password.

![Level 9-10: vim data.txt attempt with nano fallback](screenshots/level9-10_vim_nano_attempt.png)

![Level 9-10: searching data.txt for the ===== marker](screenshots/level9-10_vim_data_search.png)

Level 10-11: This level required base64 file decoding, making use of the -d flag to decode the data.txt file present in the default directory, leading to knowledge of the next level's password.

![Level 10-11: base64 --help and base64 -d data.txt](screenshots/level10-11_base64_decode.png)

Level 11-12: After gaining access to the 11th level, i made use of a stack overflow guide to identify the translation algorithm for the rot13 cipher, i acquired the relevant command, i then confirmed what the tr command did through the --help flag, then i made use of the cat command to output the data.txt file in the default directory, i piped the output of the cat command to the rot13 cipher translation command found on stack overflow and got the password to the next level, i then ran a cat command on the output of the initial file's contents, confirming it had indeed been encrypted.

![Level 11-12: tr --help and the rot13 translation via tr](screenshots/level11-12_rot13_tr_help.png)

![Level 11-12: cat data.txt confirming the original file is still enciphered](screenshots/level11-12_rot13_confirm_cipher.png)

Level 12-13: I spent about 5 hours and 2 different sessions on this level, upon creating a temporary directory with the mktemp command, i copied the file in the default directory to the temporary directory. I initially used the file command which showed me i was dealing with an ascii text, then i used the xxd command to rename the file to a .bin extension format, and used a strings command to extract the text out of the encoded .bin file. i couldn't make sense of what i was looking at, and upon research, i found out the string inside the extracted file using the strings command was a magic number for the bzip extension file, this still made no sense to me and concluded the end of the first session. I started the second session and tried to get back to my old temporary directory but found out it was deleted, i then created a new temporary directory, and experienced directory navigation errors when trying to move the file in the default directory to the temporary directory, this was because the data.txt file was in the home directory and the tmp directory was on the same level as the home directory, so i navigated to their parent directory, used the mv command, specified exact directories from the parent directories and that led to the successful transferance of the file. i then changed the file gotten from the default directory to a .bz2 extension to try to use bunzip2 command to unpack it, after it failed, i tried a file command on the file with the .bz2 extension, and i got some information indicating it was a gz extension file instead, this led to a gradual unpacking of several layers of gzip, bz2, and Posix layers till i got to a layer with an ASCII text format, which i converted to a .txt with the mv command and opened with the vim command, getting the password for the next level.

![Level 12-13: renaming to .bz2, file identifying gzip, then gunzip](screenshots/level12-13_bz2_gzip_layers.png)

![Level 12-13: file identifying a POSIX tar archive layer](screenshots/level12-13_gzip_to_tar_layers.png)

![Level 12-13: extracting the tar layer and reaching an ASCII text layer](screenshots/level12-13_tar_to_ascii_vim.png)

![Level 12-13: opening the final ASCII layer in vim](screenshots/level12-13_final_layer_vim.png)

Level 13-14: This level required using key based authentication, after successfully gaining access to level 13, the password for level 14 was a private ssh key file present on the default directory, i copied this file to my local machine through the scp command, specifying my documents directory as the destination path. after doing this, i tried to authenticate to the next level using the copied file by specifying an identity file tag and the file in an ssh command, this failed as permissions were deemed to be too open, prompting me to make use of a chmod command to restrict permissions to only the owner, after this, i managed to successfully authenticate to the next level.

![Level 13-14: failed scp attempts pushing from the bandit13 session](screenshots/level13-14_scp_connection_refused.png)

![Level 13-14: scp of sshkey.private to the local Documents directory](screenshots/level13-14_scp_key_to_local.png)

![Level 13-14: too-open key permissions warning fixed with chmod 600](screenshots/level13-14_key_permissions_chmod600.png)

Level 14-15: This level was quite simple once i figured it out, my problem was not successfully connecting to the server through netcat or telnet, but what password to enter once i gained access to the server, there was some confusion on my end as the level specified the current level password, which i kept mistaking to be my ssh private key, but after some research online, i found out it was in a different directory and it was straightforward from there

![Level 14-15: nc localhost 30000 after locating the password in /etc/bandit_pass](screenshots/level14-15_nc_localhost_30000.png)

Level 15-16: This level was quite similar to the last one, requiring a localhost connection to a specified port on the target device, except this time it made use of SSL/TLS encryption through the openssl s_client command, giving the output of the next level once the passoword of the current level was submitted.

![Level 15-16: openssl s_client submission to the SSL/TLS port](screenshots/level15-16_openssl_s_client.png)

Level 16-17: This level was similar to previous levels, except for the range of ports provided and active open servers that both supported and did not support openssl. after gaining the password of the current level through the cat command, the nmap command was used, with the -Pn, -T4, and -p commands to treat all ports as open, increase the navigation rate of nmap and specify the range of ports on the localhost. this returned a total of 5 active servers, with the openssl s_client command used for each of the five servers to test which supported ssl and which ones did not support ssl, after the initial round,a keyupdate message was continuously showing on the screen for those servers that supported ssl, leading to the use of the -ign_eof command, which eventually gave the password for the next level as a private key based authentication.

![Level 16-17: nmap scan of ports 31000-32000 on localhost](screenshots/level16-17_nmap_port_scan.png)

![Level 16-17: KEYUPDATE messages repeating on SSL-enabled ports](screenshots/level16-17_keyupdate_loop.png)

![Level 16-17: -ign_eof against ports that did not accept the handshake](screenshots/level16-17_ign_eof_non_ssl_ports.png)

![Level 16-17: wrong password response and the self-signed SnakeOil server](screenshots/level16-17_snakeoil_wrong_password.png)

![Level 16-17: private key returned by the correct port (contents redacted)](screenshots/level16-17_private_key_received.png)

![Level 16-17: key saved as a file on the local machine](screenshots/level16-17_saved_key_file.png)
