# [Users and groups]
Manage groups and users.

## Key terminology
- sudo

## Exercise
### Sources
- [How to give user sudo authority](https://linuxize.com/post/how-to-add-user-to-sudoers-in-ubuntu/)
- [How to add user to group](https://linuxize.com/post/how-to-add-user-to-group-in-linux/)

### Overcome challanges
[Give a short description of your challanges you encountered, and how you solved them.]

### Results
- Added a new user with 'sudo useradd' and check with 'cat etc/group' or 'cat etc/passwd'
  ![Add a new user](../00_includes/04-LIN_sudoNewUser.png)
- Screenshot of user in *sudo group* and in a new group using the command **cat etc/group**
  ![add new user in map](../00_includes/04-LIN_sudoNewUserInMap.png)
- Proof of sudo new user and in a new group by using command: cat etc/group/ 
  ![proof sudo group](../00_includes/04-LIN_proofSudoGroup.png)