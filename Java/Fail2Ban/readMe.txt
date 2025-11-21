According to the instructions, the Fail2Ban program takes two command line arguments. 
To use this Fail2Ban program, we type in “java Fail2Ban logs_processed.txt output.txt” 
into the terminal. The IP addresses of failed login attempts are found in that file. 

We created an arraylist to store string values of the IPs(ips_string), then we also created one to help keep track of failures (ips_track). 
We also import PrintWriter to allow us to create an output file, output.txt, so we can visually see what IP addresses are incorrect. 
The program uses try statements so that it is able to catch exceptions when and if they
occur. We imported and instantiated a scanner so that it is able to read text files. While the scanner is still reading files, 
we set the current line to a temporary value, break the string apart, pass it to an arraylist to make it easier to analyze, 
find the ip value and temporarily set it to x. Then we use an if else loop to check and count the amount of attempts. An output
file (named in the constructor) is then created. Finally, in the second try catch those IPs with more than 3 attempts are added to the output file. 
myWriter.close is used to close the file. If we do not close the file, our output may not be written to the disk file.
