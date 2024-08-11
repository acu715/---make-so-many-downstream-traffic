"""'''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''
# @Author/作者: acu715
# @LastEditors/最后编辑人: acu715
# @LastEditTime/最后编辑时间: 2024-08-08
# @Description/介绍: This is use for use more download bandwidth when you use PCDN / upload too many things.
                    It is useful to prevent bandwidth from being blocked. [home bandwidth]
                    And consume some CDN traffic of large companies, punish the manufacturers,
                    let the manufacturers understand that download BT and not upload is not right.
                    Anyone can use it, but please do not abuse it, otherwise the consequences are at your own risk.
                    ## ！！The URL inside the URLList are from internet, and NOT related to me ！！##

                    本脚本用于刷下行带宽，在你搭建PCDN或者上传大量文件，有效防止宽带被封禁 [家用宽带]
                    并且消耗一些大厂的CDN流量,惩罚厂商，让厂商明白，吸血BT是不对的
                    任何人都可以使用，但是请勿滥用，否则后果自负
                    ## ！！URLList 内的 URL 皆来自互联网，与本人无关！！##
''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''''"""
import requests
import time
from concurrent.futures import ThreadPoolExecutor
import random
import logging
import sys

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')

urlList = [

# 大善人 Cloudflare (国外)
# Good Man Cloudflare (Overseas)

          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare
          'https://cdn.cloudflare.steamstatic.com/steam/apps/1063730/extras/NW_Sword_Sorcery_2.gif',  # Steam Cloudflare

# 大厂百度 (国内)
# Big Factory Baidu (China)

          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK
          'https://issuecdn.baidupcs.com/issue/netdisk/apk/BaiduNetdiskSetup_wap_share.apk', #百度网盘APK

          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe
          'https://issuepcdn.baidupcs.com/issue/netdisk/yunguanjia/BaiduNetdisk_7.30.5.2.exe', #百度网盘exe

# 大善人Github加速站 (国内)
# Great Good Man GitHub Accelerator (China)

          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站
          'https://gh.con.sh/https://github.com/AaronFeng753/Waifu2x-Extension-GUI/releases/download/v2.21.12/Waifu2x-Extension-GUI-v2.21.12-Portable.7z', #Github文件加速站

          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          'https://gh.con.sh/https://github.com/harry0703/MoneyPrinterTurbo/releases/download/v1.2.1/MoneyPrinterTurbo-Portable-Windows-1.2.1.7z' #Github文件加速站
          
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站
          'https://gh.con.sh/https://github.com/BlinkDL/AI-Writer/releases/download/v2022-02-15-A/A.-.-wangwen-2022-02-15.zip' # Github文件加速站

# 流氓360 (国内)
# Rogue 360 (China)

          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士
          'https://sfdl.360safe.com/inst.exe', #360安全卫士

### ! 以下为破坏BT环境的厂商(BT吸血),建议长期使用以消耗CDN ! ###
### ! The following are vendors that damage the BT environment (BT bloodsuckers). It is recommended to use them for a long time to consume CDN! ###

# 123云盘 (国内)
# 123 Cloud Disk (China)

          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)
          'https://app.123pan.com/app/android/v1/123pan_2.3.12_240327_release.apk', #123云盘apk (破坏BT环境)

          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)
          'https://app.123pan.com/app/pc/windows/132/123pan_2.0.6.exe', #123云盘exe (破坏BT环境)

          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/arm64/132/123pan-2.0.6-arm64.dmg', #123云盘mac (破坏BT环境)

          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)
          'https://app.123pan.com/app/pc/darwin/amd64/132/123pan-2.0.6-x64.dmg', #123云盘mac2 (破坏BT环境)

          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          'https://app.123pan.com/app/tv/pro/v1/123pan_tv1.0.0_240202_release.apk', #123云盘tv (破坏BT环境)
          ]
# thread = 128 # 128 threads
# 线程数量 128足够千兆带宽, 256足够2G带宽, 1024足够10G带宽
# Number of threads 128 is enough for 1G bandwidth, 256 is enough for 2G bandwidth, 1024 is enough for 10G bandwidth

thread = int(input('线程数量（默认128）：'))#128  #线程数量
if thread == '':
    thread = 128
# 预留用于询问
# Reserved for enquiries

# goal = 10240 # 1024 GB
# 消耗的流量，单位GB
# Consumed traffic, unit GB

goal = int(input('消耗流量GB（默认10GB）：'))#1024  #消耗的流量单位GB
if goal == '':
    goal = 10
# 预留用于询问
# Reserved for enquiries

goalGB = goal
# 消耗的流量，单位GB(结果展示用)
# Consumed traffic, unit GB (result display)

if goal > 0:
    goal = goal * 1024 * 1024 * 1024
    # GB转为B
    # GB to B

wasted = 0
# 已消费的流量 B
# Already consumed traffic B
wastedGB = 0
# 已消费的流量 GB
# Already consumed traffic GB
runing = 0
# 正在运行的数量
# Number of running

# 线程池
# Thread pool
executor = ThreadPoolExecutor(max_workers=thread)
# 下载连接池
# Download connection pool
session = requests.Session()
adapter = requests.adapters.HTTPAdapter(pool_connections=thread, pool_maxsize=thread+1, max_retries=1, pool_block=False)
session.mount('http://', adapter)
session.mount('https://', adapter)


# 下载文件
# Download file
def download(url):
    try:
        global runing
        runing += 1
        response = session.get(url, stream=True)
        if response.status_code == 200:
            for chunk in response.iter_content(chunk_size=1020):
                # 按块读取文件内容
                # Read file content in blocks
                if goal > 0:
                    # goal为0时，不记录wasted
                    # When goal is 0, do not record wasted
                    global wasted
                    wasted += 1020
                    # 消耗流量
                    # Consumed traffic
                    if wasted > goal:
                        wastedGB = wasted / 1024 / 1024 / 1024 #GB
                        logging.info("流量已经消耗了"+str(wastedGB)+"B，超过了目标"+str(goalGB)+" GB，终止下载")
                        # logging.info("The traffic has been consumed "+str(wastedGB)+"B, exceeded the goal "+str(goalGB)+" GB, terminate download")
                        sys.exit()
                        return True
    except Exception as e:
        logging.info("下载失败")#, e)
        # logging.info("Download failed")#, e)
    finally:
        runing -= 1
    response.close()
    # 关闭下载连接
    # Close download connection
    return True


def startDownload():
    # time.sleep(random.randint(1, 10))
    time.sleep(random.randint(1, 2))
    global wasted
    wasted = 0
    # 开始下载
    # Start download
    i = thread
    while i > 0:
        executor.submit(download, random.choice(urlList))
        # 休眠0.01秒-0.1秒
        # Sleep 0.01 seconds to 0.1 seconds
        time.sleep(random.randint(1, 10) / 100)
        i -= 1


if __name__ == "__main__":
    startDownload()
    while True:
        if (goal == 0 or wasted < goal) and runing < thread:
            wastedGB = wasted / 1024 / 1024 / 1024  # GB
            logging.info("补充下载链接数/线程：%s , 已下载：%s GB", thread - runing, wastedGB)
            # logging.info("Supplementary download links/threads: %s , downloaded: %s GB", thread - runing, wastedGB)
            i = thread - runing
            while i > 0:
                executor.submit(download, random.choice(urlList))
                time.sleep(random.randint(1, 10) / 100)
                i -= 1
        time.sleep(5)