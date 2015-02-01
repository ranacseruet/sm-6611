# sm-assignment-1

## Part 1
Find and cloe git repositories
test command:
```
$./get_git ./configs/git_conf
```

## Part 2
Find and store raw html on bugs
```
$./get_atlassian_bugs ./configs/bugs_conf
```

## Part 3
Get Contributors list by use of github api.
I have used [pygithub](https://github.com/jacquev6/PyGithub) library as the github api for python. As there is no specific command format given,
I have used a sample format as bellow:

```
$./get_contributor {user|org} {repo}
#example
$./get_contributor poise python
```
