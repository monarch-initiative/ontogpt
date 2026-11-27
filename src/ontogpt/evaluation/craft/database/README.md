# CRAFT corpus

The CRAFT corpus is available at its own repository, at <https://github.com/UCDenver-ccp/CRAFT>.

The version used in this evaluation is v5.0.2.

To prepare the version used here, do the following. This process ensures the compatible Java version is available.

## Get Clojure Boot in a Docker container

```bash
$ docker pull clojure:openjdk-8-boot-2.8.1
...
$ docker run clojure:boot
SLF4J: Failed to load class "org.slf4j.impl.StaticLoggerBinder".
SLF4J: Defaulting to no-operation (NOP) logger implementation
SLF4J: See http://www.slf4j.org/codes.html#StaticLoggerBinder for further details.
Retrieving tools.nrepl-0.2.13.pom from https://repo1.maven.org/maven2/ (3k)
Retrieving pom.contrib-0.2.2.pom from https://repo1.maven.org/maven2/ (7k)
Retrieving tools.nrepl-0.2.13.jar from https://repo1.maven.org/maven2/ (40k)
nREPL server started on port 42403 on host 127.0.0.1 - nrepl://127.0.0.1:42403
REPL-y 0.3.7, nREPL 0.2.13
Clojure 1.8.0
OpenJDK 64-Bit Server VM 1.8.0_181-8u181-b13-2~deb9u1-b13
        Exit: Control+D or (exit) or (quit)
    Commands: (user/help)
        Docs: (doc function-name-here)
              (find-doc "part-of-name-here")
Find by Name: (find-name "part-of-name-here")
      Source: (source function-name-here)
     Javadoc: (javadoc java-object-or-class-here)
    Examples from clojuredocs.org: [clojuredocs or cdoc]
              (user/clojuredocs name-here)
              (user/clojuredocs "ns-here" "name-here")
boot.user=> Bye for now!
$ docker ps -a
CONTAINER ID   IMAGE                                                COMMAND                  CREATED             STATUS                          PORTS     NAMES
54d94e154884   clojure:openjdk-8-boot-2.8.1                         "boot repl"              28 seconds ago      Exited (0) 18 seconds ago                 crazy_stonebraker
```

## Enter the containter and retrieve the CRAFT corpus

```bash
$ docker run -ti clojure:boot /bin/bash
root@cdd32ade99bd:/tmp# 
root@cdd32ade99bd:/tmp# curl -OL https://github.com/UCDenver-ccp/CRAFT/archive/refs/tags/v5.0.2.tar.gz
  % Total    % Received % Xferd  Average Speed   Time    Time     Time  Current
                                 Dload  Upload   Total   Spent    Left  Speed
  0     0    0     0    0     0      0      0 --:--:-- --:--:-- --:--:--     0
100  165M    0  165M    0     0  16.7M      0 --:--:--  0:00:09 --:--:-- 10.6M
root@cdd32ade99bd:/tmp# ls -lh
total 166M
drwxr-xr-x 1 root root 4.0K Nov 17  2018 hsperfdata_root
-rw-r--r-- 1 root root 166M Nov 28 22:53 v5.0.2.tar.gz
root@cdd32ade99bd:/tmp# tar -xvzf v5.0.2.tar.gz
... decompress everything ...
root@cdd32ade99bd:/tmp# cd CRAFT-5.0.2/
root@cdd32ade99bd:/tmp/CRAFT-5.0.2# export BOOT_JVM_OPTIONS='-Xmx5g -client'
```

## Convert to BRAT standoff format

This format is most compatible with OntoGPT evaluations because it includes full input text (in each txt file) and one entity annotation per line (in each ann file).

Note this command will not include the extension classes - this is intentional.

```bash
root@cdd32ade99bd:/tmp/CRAFT-5.0.2# boot all-concepts convert -o ./converted/all --brat
```

## Copy over the converted files

Back on the host machine, copy the full directory of converted annotations to the `/ontogpt/src/ontogpt/evaluation/craft/database/` directory.

```bash
$ docker cp stoic_allen:/tmp/CRAFT-5.0.2/converted/all .
Successfully copied 8.58MB to /home/harry/ontogpt/src/ontogpt/evaluation/craft/database/.
```
