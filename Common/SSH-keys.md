# Public/Private SSH Keys

## Generating Key Pairs

```sh
ssh-keygen -t ed25519 -C "your_email@example.com"
# ed25519 -> modern, secure and recommended over RSA.
# `-C`: is used for creating a label (usually user's email)

# if above command was not supported or RSA generated key pairs were required
ssh-keygen -t rsa -b 4096 -C "your_email@example.com"

    # Select were to store generated key pairs and what to name them
    Enter file in which to save the key (/home/<user>/.ssh/id_ed25519):
    # you can type a custom name, e.g. ~/.ssh/gitlab_ed25519

    Enter passphrase (empty for no passphrase):
    # for extra security set a passphrase
```

## Add Private-Key to SSH-Agent

```sh
# checking generated key pairs
ls -al ~/.ssh

# start the agent
eval "$(ssh-agent -s)"
# `-s`: starts ssh-agent
# `$`: capturing ssh-agent environment variables
# `eval`: set the ssh-agent environments in your current shell

# register your private key to the agent
ssh-add ~/.ssh/id_ed25519

# check currently registered keys
ssh-add -l
# `-L`: listing all public keys

# remove all registered keys
ssh-add -D

# remove specific key
ssh-add -d ~/.ssh/id_ed25519
```

## Add Public-Key to a Service

```sh
cat ~/.ssh/id_ed25519.pub
# copy your public-key
```

- **GitHub** → _Settings > SSH and GPG keys > New SSH key_
  - test: `ssh -T git@github.com`
- **GitLab** → _Preferences > SSH Keys > Add key_
  - test: `ssh -T git@gitlab.com`
- **Server** → paste into `~/.ssh/authorized_keys`
  - test: `ssh -p <port> username@server-IP`

## SSH Key Configuration

```sh
# create configuration file
vim ~/.ssh/config
```

### Permission Configuration

```sh
chmod 600 ~/.ssh/config
chmod 600 ~/.ssh/id_*
chmod 644 ~/.ssh/id_*.pub
```

### Sample Configuration

```text
# Personal server
Host myserver
    HostName <server-IP-address>
    User <server-username>
    Port <server-port>
    IdentityFile ~/.ssh/id_server_ed25519
    IdentitiesOnly yes
```

- **Host** -> alias which can be used with `ssh` command
- **HostName** -> Actual server address
- **User** -> The SSH user to login with
- **Port** -> tells SSH to connect on the given port instead of the default `22` (do not mention if not needed!)
- **IdentityFile** -> Path to your **private key** for this host
- **IdentitiesOnly** -> Forces SSH to use only the specified key, avoiding “too many authentication attempts” errors.

```sh
# now instead of
ssh -i ~/.ssh/id_server_ed25519 -p <port> username@server-ip

# you can connect to your server using
ssh myserver
```
