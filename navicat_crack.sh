#!/bin/bash
set -xeuo pipefail
echo "Crack Navicat15, works on Arch based Distro....."

echo "安装破解的一切后果请自行承担"
echo "由于版权原因本脚本不再维护，推荐使用DBeaver等开源替代或使用mycli、pgcli等终端工具，或使用教育邮箱或开源贡献认证申请Jetbrains家的DataGrip"

source /etc/os-release
case $ID in
arch)


    ## 安装所需依赖
    sudo pacman -S capstone keystone rapidjson openssl appimagetool-bin

    # 从中文官网下载Navicat
    mkdir ~/Desktop/DoNavicat
    cd ~/Desktop/DoNavicat
    wget "https://download.navicat.com.cn/download/navicat15-premium-cs.AppImage" --no-check-certificate
    mkdir ~/Desktop/DoNavicat/bin
    mkdir ~/Desktop/DoNavicat/navicat15-premium-cs
    mount -o loop ~/Desktop/DoNavicat/navicat15-premium-cs.AppImage ~/Desktop/DoNavicat/navicat15-premium-cs
    cp -r ~/Desktop/DoNavicat/navicat15-premium-cs ~/Desktop/DoNavicat/navicat15-premium-cs-patched
    umount ~/Desktop/DoNavicat/navicat15-premium-cs
    rm -rf ~/Desktop/DoNavicat/navicat15-premium-cs


    # 编译navicat-patcher
    cd ~/Desktop/DoNavicat/bin
    git clone -b linux --single-branch https://github.com/DoubleLabyrinth/navicat-keygen.git
    cd navicat-keygen
    make all

    .navicat-patcher ~/Desktop/DoNavicat/navicat15-premium-cs-patched

    # 编译navicat-keygen
    # git clone -b linux --single-branch https://github.com/DoubleLabyrinth/navicat-keygen.git
    git clone -b linux --single-branch https://gitee.com/andisolo/navicat-keygen.git
    cd navicat-keygen
    make all

    cd ~/Desktop/DoNavicat
    wget 'https://github.com/AppImage/AppImageKit/releases/download/continuous/appimagetool-x86_64.AppImage'
    chmod +x appimagetool-x86_64.AppImage
    ./appimagetool-x86_64.AppImage ~/Desktop/DoNavicat/navicat15-premium-cs-patched ~/Desktop/DoNavicat/navicat15-premium-cs-patched.AppImage
    chmod +x ~/Desktop/DoNavicat/navicat15-premium-cs-patched.AppImage
    ~/Desktop/DoNavicat/navicat15-premium-cs-patched.AppImage


    echo "请断开网络"
    # 开始生成激活码
    ./bin/navicat-keygen --text ./RegPrivateKey.pem

    while true
    do
        read -r -p '是否清理安装文件?（y/n） ' choice
        case "$choice" in
        n|N) break;;
        y|Y)
            rm ~/Desktop/DoNavicat/navicat15-premium-cs.AppImage
            rm -rf ~/Desktop/DoNavicat/navicat15-premium-cs-patched
            mv ~/Desktop/DoNavicat/navicat15-premium-cs-patched.AppImage ~/Desktop/DoNavicat/navicat15-premium-cs.AppImage
            echo "已删除安装文件"
            ;;
        *) echo 'Response not valid';;
        esac
    done

    ;;
*)
    echo "该破解方式只适用于Archlinnux"
    exit 1
    ;;
esac
