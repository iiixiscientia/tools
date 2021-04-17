# e.g. linux 4.18.5.arch1-1
set installed (string match --regex '\d\d?.\d\d?.\d\d?' (pacman --query linux))

# e.g. 4.18.4-arch1-1-ARCH
set running (string match --regex '\d\d?.\d\d?.\d\d?' (uname --kernel-release))

if test ! $running = $installed

    printf "restart!"

end