 

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

Level 17-18:  After using key based authentication to gain access to this level, i navigated to the root directory from the home directory and used the cat command to output the password of level 17, for redundancy purposes in case i ever wanted a different method from ssh key based authentication, then i initially try to use the diff command and transfer the output to a new file, when that failed, i tried to pipe it and output it through a cat command, that also failed, so i just reverted to using the diff command, copying the output and gaining access to the next level.

![Level 17-18: reading the current password, then diffing passwords.old against passwords.new (password redacted)](screenshots/level17-18_cat_pass_and_diff.png)

![Level 17-18: diff output - the changed line is the next password (redacted)](screenshots/level17-18_diff_output.png)

Level 18-19: Due to the nature of the level, with the .bashrc file being modified to log the user out upon  connection through an ssh protocol. I had to make use of appending quotes at the end of the ssh command, initially trying to cat the Readme file, when that didn't work, i tried to list the contents of the home directory through the ls command, then got the appropraite capitalisation, which i then used to obtain the password of the next level.

![Level 18-19: running ls as an ssh command argument to dodge the .bashrc logout](screenshots/level18-19_ssh_command_ls.png)

![Level 18-19: cat readme over ssh with correct capitalisation (password redacted)](screenshots/level18-19_ssh_cat_readme.png)

Level 19-20: This level introduced binaries, with a binary on the default directory once access had been granted. I initially tried a setuid --help command to see what this level contained, however that command ended up being irrelevant as it was not installed and required administrator access to install. I then tried a ./ symbol with the binary, which told me what the binary did and essentially gave me the id of the user of the next level, this informed me that i now had access to the password of the next level through this binary, so i ran the binary along with the command needed to output the password of the next level where it was stored and was successfully authorised through the binary.

![Level 19-20: exploring the setuid binary - id shows euid=bandit20](screenshots/level19-20_bandit20-do_attempts.png)

![Level 19-20: using bandit20-do to cat the bandit20 password file (redacted)](screenshots/level19-20_bandit20-do_cat_password.png)

Level 20-21: This level made use of two different terminals. when i authenticated into the level, i ran a ls command and found a binary, when i ran the binary, i saw that it sends back a password on a specific port if the password that was sent to it matches the password in it's storage. this prompted me to make use of netcat to act as a server listening on a specific port, i then used the help command to see the options that were available to me, ran the netcat command with the -l and -p flags to set it to listening mode and set an unused port number, after which, i connected to the level on another  terminal, ran the binary with the port number i specified on netcat, entered the password of the last level on netcat, and got sent the password of the next level by the binary on the listening netcat server.

Level 21-22: This level introduced cron jobs. I had to list out the contents of /etc/cron.d to see what cronjobs were running on the system. after which i used the cat command to output the specific cron job to this level, which showed me the task the cronjob was running, i then used the cat command on the task the chrome job was running, showing me that it was setting permissions and outputting the password of the next level to a temp directory continuously, i then used the cat command on that directory, showing me the password of the next level.

![Level 21-22: the cron script copies the password to a /tmp file, which is then read (redacted)](screenshots/level21-22_cronjob_tmp_file.png)

Level 22-23: This level was similar to the last level, except it contained a bit more scripts, for this level, i had to initially rerun the entire file to see what it did, run each individual line with and without their variable names, and then i found the password of the next level by removing the $mytarget variable and using only the value in the variable, changing the \$myname variable in the value to bandit 23, catting the output of the hash it generated through the combination of a temp directory and the hash to get the password of the next level. 

![Level 22-23: reading cronjob_bandit23 and running the script lines by hand](screenshots/level22-23_cronjob_script.png)

![Level 22-23: substituting bandit23 into the md5 target and reading the /tmp file (password redacted)](screenshots/level22-23_md5_target_password.png)

Level 23-24: For this level i had to create my own script and use the privilege of the next level's user to gain access to the password for the next level. After gaining access to the level, i confirmed what cronjob the level was running, then i catted the outputs of what it was running. This led me to the information that it was running scripts and deleting them as bandit24 in a certain folder. so i wrote a script into the directory and initially used the touch command, i found this didn't work, with my output coming back empty. i then used the redirect flag to create a new file in the tmp directory, i still didn't get access to the password. The solution turned out to be a permissions fix, with me including the executions permissions in the directory through the chmod +x command, to make my created script executable, this seemed to work, giving me the password of the next level.

![Level 23-24: the script written into /var/spool/bandit24/foo](screenshots/level23-24_script_in_vim.png)

![Level 23-24: output file never appearing - the script was not executable](screenshots/level23-24_tmp_file_attempts.png)

![Level 23-24: chmod +x on the script, then the password lands in /tmp (redacted)](screenshots/level23-24_chmod_x_success.png)

Level 24-25: This level involved the use of Brute force to go through 10000 combinations to find the value that combines with the password of the previous level to successfully give the password of the next level. A python script was created which mapped the combinations of the 10000 values to the previous level's password. The file generated by the python script then made use of a python script paired with a pipe flag to netcat that went through all the combinations till it got to the correct value and generated the password of the next level.

![Level 24-25: first brute-force script attempt (nano could not save in the home directory)](screenshots/level24-25_bruteforce_script.png)

![Level 24-25: iterating through Python errors - print syntax and the missing telnetlib module](screenshots/level24-25_python_errors.png)

Level 25-26/26-27: This level made use of a different login terminal than bash, closing my connections when i didn't specify any commands and leading me to a zone where no text was parsed when i specified some commands. I gained access to this level through ssh key authentication. This level saw me start with the getent, more and vi command on my bandit25 terminal. i successfully gained access to the login terminal through a cat etc/passwd command, however use of the getent passwd bandit26 command highlighted a faster way to get the same result. i then navigated to the contents of the fle i was shown, leading me to see a more ~/text.txt as the login script for bandit 26 in bandit 25's terminal. I discovered a quirk in the more functionality that pauses if the terminal is small enough and lets me use the vi command to navigate to a text editor that could parse commands. i then created a new shell using the vi editor and listed the contents of the bandit 26 terminal. after this i copied the password of level 26 to give me another means of access which i didn't previously have due to my key based authentication. i saw a binary file in the list of contents and tried to run it through bash, this however didn't worked and left me with jumbled text which i tried to make sense of with strings and file commands to understand what i was working with, this led to some very useful hints about what type of file i was dealing with, and when i specified the exact directory with the id command, i was shown the purpose of the binary file as a means to grant me access as bandit27 on the terminal, which i then used to display the outputs of bandit 27's password. 

![Level 25-26: logging in to bandit26 with the private key](screenshots/level25-26_ssh_key_login.png)

![Level 25-26: getent passwd reveals /usr/bin/showtext as the login shell, which runs more](screenshots/level25-26_getent_showtext.png)

![Level 25-26: escaping more -> vi -> :shell and inspecting the bandit27-do binary](screenshots/level25-26_vi_shell_escape.png)

![Level 25-26: listing the bandit26 home directory (bandit26 password redacted)](screenshots/level26-27_bandit26_home.png)

![Level 25-26: file and id on bandit27-do, then reading the bandit27 password (redacted)](screenshots/level26-27_bandit27-do.png)

Level 27-28: This level was an introduction to git, it involved me cloning a git repo to my local machine, making use of the git clone command, once i successfully cloned the repo, i checked my local device using pwd command to check where the file landed, checked the directory, opened the readme, and saw the password to the next level.

![Level 27-28: cloning without the 2220 port - the server rejects port 22](screenshots/level27-28_clone_wrong_port.png)

![Level 27-28: the cloned README contains the next password (redacted)](screenshots/level27-28_readme_password.png)

Level 28-29: This level initially looked similar to the last one, however, upon a review of the readme, it was found that the password credential had been redacted. The log of the local copy was then investigated, revealing three previous commits, and through their messages, the old commit that had the password and the new commit that had its password redacted were displayed. a git diff command with the comparison of the old and new commit displayed the difference between the two commits, revealing the redacted password.

![Level 28-29: git log - the "fix info leak" commit is the clue](screenshots/level28-29_git_log.png)

![Level 28-29: git diff between the two commits reveals the removed password (redacted)](screenshots/level28-29_git_diff.png)

Level 29-30: Rather than dealing with history of commits, this level instead dealt with the different environment types in git. upon cloning the repo, i got access to the readme, which read that there were no keys in production, leading me to understand i was in the production branch. After using the git switch command to switch to a different branch, i made use of the git log command to show all past commits in the new test environment, then i used the git show command to show the contents of the last commit file for the environment i had switched to, giving me access to the password for the next level.

![Level 29-30: "no passwords in production!" on master](screenshots/level29-30_production_readme.png)

![Level 29-30: git show on the dev branch commit reveals the password (redacted)](screenshots/level29-30_dev_branch_show.png)

Level 30-31: This level involved the use of git tags. Through the refs directory oresent in the .git directory, branches, environment types and tags were found, since the previous two levels were focused on both branches and environment types, i reasoned that this level must be focused on tags, leaving me to research on what tags were and how to display the contents of a git tag, leading to the password for the next level.

![Level 30-31: .git/refs leads to a tag named secret; git show secret (output redacted)](screenshots/level30-31_git_tag_secret.png)

Level 31-32: Upon cloning the repo for this level, The readme informed me i was to push contents to the remote repo in this round. After initially creating the file, adding it, commiting it, and pushing it, i was told everything was up to date, even though my file was successfully created and reflected when i ran the ls -a flag, leading me to the belief that something was suppressing my file, i included it either way the force flag in the git add flag, successfully adding and pushing the file, however it still failed to give me the password of the next level. I realised the error was in the capitalisation in the naming of the file, prompting me to rename and repush the file, successfully getting the password for the next level.

![Level 31-32: "nothing to commit" - .gitignore was silently excluding the file (local notes and email redacted)](screenshots/level31-32_nothing_to_commit.png)

![Level 31-32: pushing Key.txt - rejected by the pre-receive hook because of the capital K](screenshots/level31-32_push_rejected.png)

![Level 31-32: after renaming to key.txt the hook returns the password (redacted)](screenshots/level31-32_password_returned.png)

Level 32-33: Upon successful authentication to this level, i came upon an uppershell, which wrapped all of my flags in upper cases and sent it out for execution, leaving them nonfunctional due to linux's case sensitivity. To get around this, i had to look outside of just letters, for values that remained the same even after they had been wrapped, that led me to shell special characters, and after reading what each did, i surmised that the $0 flag might be able to get me out of the uppershell, i noticed the terminal had changed and i could run commands now, i ran an ls and a whoami command which gave me information about the system, but temporarily not knowing what to do, i ran the binary file that was in the default directory, which brought me back to the uppershell, after further research, i found out i had already mistakenly broken out of the shell, and a whoami command revealed that i had the privileges of the next level, leading me to cat out the contents of the password of the next level and gaining access to the password.

![Level 32-33: $0 survives uppercasing and spawns a shell as bandit33 (password redacted)](screenshots/level32-33_uppershell_escape.png)
