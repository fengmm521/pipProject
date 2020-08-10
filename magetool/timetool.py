#!/usr/bin/env python
# -*- coding: utf-8 -*-
import time
import datetime
import sys
# loctim = time.localtime()
# #time.struct_time(tm_year=2015, tm_mon=8, tm_mday=2, tm_hour=12, tm_min=16, tm_sec=47, tm_wday=6, tm_yday=214, tm_isdst=0)
# sendmsg = str(loctim.tm_mon) + '_' +  str(loctim.tm_mday) + '_' + str(loctim.tm_hour) + '_' + str(loctim.tm_min) + '_' + str(loctim.tm_sec)

# print sendmsg


# datex = time.localtime(1459179579)
# sendmsg = str(datex.tm_mon) + '.' +  str(datex.tm_mday) + '_' + str(datex.tm_hour) + ':' + str(datex.tm_min) + ':' + str(datex.tm_sec)
# print sendmsg


# a = [1,2,3,6]
# b = [5,9,10]
# a = a + b
# print a

# print "aa", time.time()
# print time.localtime(time.time() + 60 *3)

import pytz

#iso转时间戳
def iso2timestamp(datestring, format='%Y-%m-%dT%H:%M:%S.%fZ',timespec='seconds'):
    """
    ISO8601时间转换为时间戳

    :param datestring:iso时间字符串 2019-03-25T16:00:00.000Z，2019-03-25T16:00:00.000111Z
    :param format:%Y-%m-%dT%H:%M:%S.%fZ；其中%f 表示毫秒或者微秒
    :param timespec:返回时间戳最小单位 seconds 秒，milliseconds 毫秒,microseconds 微秒
    :return:时间戳 默认单位秒
    """
    tz = pytz.timezone('Asia/Shanghai')
    utc_time = datetime.datetime.strptime(datestring, format)  # 将字符串读取为 时间 class datetime.datetime

    time = utc_time.replace(tzinfo=pytz.utc).astimezone(tz)

    times = {
        'seconds': int(time.timestamp()),
        'milliseconds': round(time.timestamp() * 1000),
        'microseconds': round(time.timestamp() * 1000 * 1000),
    }
    return times[timespec]

#时间戳转iso
def timestamp2iso(timestamp, format='%Y-%m-%dT%H:%M:%S.%fZ'):
    """
    时间戳转换到ISO8601标准时间(支持微秒级输出 YYYY-MM-DD HH:MM:SS.mmmmmm)
    :param timestamp:时间戳，支持 秒，毫秒，微秒级别
    :param format:输出的时间格式  默认 iso=%Y-%m-%dT%H:%M:%S.%fZ；其中%f表示微秒6位长度

    此函数特殊处理，毫秒/微秒部分 让其支持该部分的字符格式输出
    :return:
    """
    format = format.replace('%f','{-FF-}')#订单处理微秒数据 %f
    length = min(16, len(str(timestamp)))#最多去到微秒级

    #获取毫秒/微秒 数据
    sec = '0'
    if length != 10:#非秒级
        sec = str(timestamp)[:16][-(length - 10):]#最长截取16位长度 再取最后毫秒/微秒数据
    sec = '{:0<6}'.format(sec)#长度位6，靠左剩下的用0补齐
    timestamp = float(str(timestamp)[:10])#转换为秒级时间戳
    return datetime.datetime.utcfromtimestamp(timestamp).strftime(format).replace('{-FF-}',sec)



def datetime2timestamp(dt, convert_to_utc=False):
    ''' Converts a datetime object to UNIX timestamp in milliseconds. '''
    if isinstance(dt, datetime.datetime):
        if convert_to_utc: # 是否转化为UTC时间
            dt = dt + datetime.timedelta(hours=-8) # 中国默认时区
        timestamp = datetime.timedelta.total_seconds(dt - datetime.datetime(1970,1,1))
        
        if sys.version_info > (3,1):
            return int(timestamp)
        elif sys.version_info <= (2,7):
            return long(timestamp)
    return dt

def timestamp2datetime(timestamp, convert_to_local=False):
    ''' Converts UNIX timestamp to a datetime object. '''
    if sys.version_info.major >= 3 and sys.version_info.minor >= 1:
        if isinstance(timestamp, (int, int, float)):
            dt = datetime.datetime.utcfromtimestamp(timestamp)
            if convert_to_local: # 是否转化为本地时间
                dt = dt + datetime.timedelta(hours=8) # 中国默认时区
            return dt
        return timestamp
    else:
        if isinstance(timestamp, (int, long, float)):
            dt = datetime.datetime.utcfromtimestamp(timestamp)
            if convert_to_local: # 是否转化为本地时间
                dt = dt + datetime.timedelta(hours=8) # 中国默认时区
            return dt
        return timestamp

def timestamp_utc_now():
    return datetime2timestamp(datetime.datetime.utcnow())

#获取当前时间戳
def getNowDate(ptime = None):
    if ptime:
        return timestamp2datetime(int(ptime),True)
    return timestamp2datetime(int(time.time()),True)

#获取今天的日期
def getDateDay():
    loctim = time.localtime()
    #time.struct_time(tm_year=2015, tm_mon=8, tm_mday=2, tm_hour=12, tm_min=16, tm_sec=47, tm_wday=6, tm_yday=214, tm_isdst=0)
    sendmsg = str(loctim.tm_year) + '_' + str(loctim.tm_mon) + '_' +  str(loctim.tm_mday)
    return sendmsg


#时间戳转为时间结构体
def getDateStructWithSec(t):
    tmp = time.localtime(int(t))
    return tmp

#时间戳转为字符串时间
def conventTimesampToDate(ptime):
    loctim = getDateStructWithSec(ptime)
    outstr = str(loctim.tm_year) + '.' + str(loctim.tm_mon) + '.' +  str(loctim.tm_mday)+ ' ' +  str(loctim.tm_hour)+ ':' +  str(loctim.tm_min)+ ':' +  str(loctim.tm_sec)
    return outstr

#结构体转为时间戳
def makeSecTimeWithStructTime(structtime):
    timetmp = time.mktime(structtime)
    return timetmp

#年_月_日转为时间结构体
def getStruceTimeWithStrDate(strdate):
    timex = time.strptime(strdate, '%Y_%m_%d')
    return timex


#获取date的下一天日期,date格式:年_月_日
def getNextDayDate(date):
    structtime = getStruceTimeWithStrDate(date)
    sectime = makeSecTimeWithStructTime(structtime)
    onedaysec = 24*60*60
    sectime += onedaysec
    nextstruct = getDateStructWithSec(sectime)
    nextday = str(nextstruct.tm_year) + '_' + str(nextstruct.tm_mon) + '_' +  str(nextstruct.tm_mday)
    return nextday

def conventDayStrAdd_(pday,pjoin = '_'):
    ymds = pday.split(pjoin)
    y = ymds[0]
    m = ymds[1]
    d = ymds[2]
    if len(m) == 1:
        m = '0' + m
    if len(d) == 1:
        d = '0' + d
    out = y + pjoin + m + pjoin + d
    return out

def conventDayStrSub_(pday,pjoin = '_'):
    ymds = pday.split(pjoin)
    y = str(int(ymds[0]))
    m = str(int(ymds[1]))
    d = str(int(ymds[2]))
    out = y + pjoin + m + pjoin + d
    return out

#获取从某一天一直到今天的所有以天计算日期,年_月_日
def getDateDaysFromOneDate(startDate):
    startday = startDate
    today = getDateDay()
    startsec = getStruceTimeWithStrDate(startday)
    todaysec = getStruceTimeWithStrDate(today)
    if startsec >= todaysec:
        return []
    nextday = startday
    outdays =[]
    while today != nextday:
        nextday = getNextDayDate(nextday)
        outdays.append(nextday)
    return outdays
    # timetmp = time.struct_time(tm_year=toyear, tm_mon=tomon, tm_mday=today, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=0, tm_yday=0, tm_isdst=0)
    # print timetmp



#UTC时间转本地时间
def utc2local(utc_st):
    '''UTC时间转本地时间（+8:00）'''
    now_stamp = time.time()
    local_time = datetime.datetime.fromtimestamp(now_stamp)
    utc_time = datetime.datetime.utcfromtimestamp(now_stamp)
    offset = local_time - utc_time
    local_st = utc_st + offset
    return local_st


#本地时间转UTC时间
def local2utc(local_st):
    '''本地时间转UTC时间（-8:00）'''
    time_struct = time.mktime(local_st.timetuple())
    utc_st = datetime.datetime.utcfromtimestamp(time_struct)
    return utc_st

#UTC格式的时间转换为本地时间
def utcStrToLocalTimeStr(tstr,UTC_FORMAT='%Y-%m-%dT%H:%M:%S.%fZ'):
    t1 = datetime.datetime.strptime(tstr, UTC_FORMAT)
    lt1 = utc2local(t1)
    return lt1.strftime("%Y-%m-%d %H:%M:%S")

def utcStrTimeToTime(tstr,UTC_FORMAT='%Y-%m-%dT%H:%M:%S.%fZ'):
    ldate = utcStrToLocalTimeStr(tstr,UTC_FORMAT)
    timeArray = time.strptime(ldate, "%Y-%m-%d %H:%M:%S")
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp
    
def strTimeToTime(tstr,FORMAT='%Y%m%d%H%M%S'):
    timeArray = time.strptime(tstr, FORMAT)
    #转换成时间戳
    timestamp = time.mktime(timeArray)
    return timestamp

#时间戳转utc时间结构体
def utcSructTimeWithTime(dt):
    return time.gmtime(dt)

def conventTimeFromStrConfig(pstr):
    dats = pstr.split("|")
    if len(dats) == 1:#说明是时间定义的是今天的这个时间
        today = getDateDay() + '|' + dats[0]
        times = today.split('!')
        ptime = strTimeToTime(times[0],FORMAT = '%Y_%m_%d|%H:%M:%S')#2020-01-13|12:03:25
        outtime = ptime + float(times[1])/1000.0
        return outtime

    elif len(dats) != 2:
        print("时间格式错误")
    else:
        #定义是某一天的时间，在这里返回时间戳
        times = pstr.split('!')
        ptime = strTimeToTime(times[0],FORMAT = '%Y-%m-%d|%H:%M:%S')#2020-01-13|12:03:25
        outtime = ptime + float(times[1])/1000.0
        return outtime


if __name__ == '__main__':
    # print datetime.datetime.utcnow()
    # print timestamp_utc_now()
    print(timestamp2datetime(int(time.time()),False))

    dx = getNowDate()
    print(dx,type(dx))
    print(time.gmtime())
    print(time.localtime())

    x = conventTimeFromStrConfig('2020-01-13|12:03:25!000')
    print(x)
    print(time.localtime(int(x)))
    print(time.time())
    iostime = timestamp2iso(int(time.time()))
    print(iostime)

    testdat = '2020-08-10 22:18:59'
    t = strTimeToTime(str(dx),FORMAT='%Y-%m-%d %H:%M:%S')
    print(t)
    # tmpdat = '2017_7_17'
    # print(getDateDaysFromOneDate(tmpdat))
    # outstr = timestamp2datetime(int(time.time() + 60 * 5),True)
    # print outstr