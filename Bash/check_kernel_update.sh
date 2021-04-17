# 灵感来自 https://www.reddit.com/r/archlinux/comments/d1lj0a/how_come_arch_linux_can_upgrade_the_kernel/ezp2gii/ 的fish脚本
# 将脚本改为bash，并配置KDE的通知
# 根据是否更新了内核提醒用户重启

set -e
# e.g. linux-lts 5.10.31-1
installed=$((pacman --query linux)|grep -oP '\d\d?.\d\d?.\d\d?' )

# e.g. 5.10.31-1-lts
running=$((uname --kernel-release)|grep -oP '\d\d?.\d\d?.\d\d?')

if test ! $running = $installed
then

    echo 'You may need to restart since your kernel has been updated. ' | wall
    notify-send 'You may need to restart since your kernel has been updated. 由于您更新了内核，你可能需要重启'
fi
