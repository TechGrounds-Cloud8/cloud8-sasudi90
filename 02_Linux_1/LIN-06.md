# Processes
Start, check and end processes.

## Key terminology
- daemon
- sudo apt install telnetd -y: install telnetd and automate with -y
- ps aux | grep inetd: get PID
- sudo systemctl status inetd: shows status (pid, memory) of process 'inetd' in this particular case. 
- sudo systemcl stop inetd

## Exercise
1. Start the telnet daemon.
2. Find out the PID of the telnet daemon.
3. Find out how much memory telnetd is using.
4. Stop or kill the telnetd process.

### Sources
- [How to start and check status telnet daemon](https://www.javatpoint.com/linux-telnet-command)
- [Stop service process](https://youtube.com/clip/UgkxBoKt0so_dD99dDL8_ruDb3C9m1cag6VV)

### Overcome challanges
[Give a short description of your challanges you encountered, and how you solved them.]

### Results
- First update and then install ![install](../00_includes/06-LIN_updateInstall.png)
- ![check status](../00_includes/06-LIN_systemctl.png)
- ![stop1](../00_includes/06-LIN_doubleCheck.png)
- ![stop2](../00_includes/06-LIN_stop1.png)
- ![doublecheck](../00_includes/06-LIN_stop2.png)

