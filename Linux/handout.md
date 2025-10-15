# Linux

- [Linux](#linux)
  - [General Useful Points](#general-useful-points)
    - [Using `sudo tee` instead of `>` \& `>>`](#using-sudo-tee-instead-of---)

## General Useful Points

### Using `sudo tee` instead of `>` & `>>`

- `tee` reads from standard input (`stdin`) and writes it both to a file and to standard output (`stdout`).
- By default, `sudo tee` **overwrites** the file — just like normal redirection (`>`).

```sh
# if you need root permissions below command won’t work properly, because sudo only applies to echo, not to the redirection (>).
# The redirection is handled by your regular user shell, which likely doesn’t have permission to write to /etc.
sudo echo "text" > /etc/file

# you can solve this issue by using
echo "text" | sudo tee /etc/file

# if you don't want tee to print to terminal
echo "text" | sudo tee /etc/file > /dev/null

# if you want to append to a file
echo "new line" | sudo tee -a /etc/file

# above command behaves like this (but with root permissions)
echo "new line" >> /etc/file

# you can also pipe multi-line text to sudo tee
cat <<EOF | sudo tee /etc/file >/dev/null
...
EOF
```
