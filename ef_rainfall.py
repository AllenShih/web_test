import pyodbc, datetime, math, time
from pathlib import Path
from apscheduler.schedulers.blocking import BlockingScheduler

def hourly_rainfall(one_hour_data, date):
    timedelta = datetime.timedelta(minutes = 57)
    h_rainfall = 0
    onehourago = date - timedelta
    one_hour_data = [x for x in one_hour_data if x[1]>onehourago]
    for item in one_hour_data:
        h_rainfall += item[0]
    # print("hourly_rainfall counting.....")
    return [one_hour_data, h_rainfall]

def last_7_days_rain(seven_days_data, date, raining_check):
    timedelta_p = datetime.timedelta(days = 7, minutes = 3)
    timedelta = datetime.timedelta(days = 6, minutes = 57)
    last7 = 0
    
    if raining_check == "raining":
        sevendaysago = date - timedelta
        seven_days_data = [x for x in seven_days_data if x[1] > sevendaysago]
        seven_days_data_temp = [x for x in seven_days_data if x[1] < date]
        for item in seven_days_data_temp:
            last7 += item[0]
    elif raining_check == "no-raining":
        sevendaysago = date - timedelta_p
        seven_days_data = [x for x in seven_days_data if x[1] > sevendaysago]
        for item in seven_days_data:
            last7 += item[0]
    # print("last_7_day_rain counting.....")  
    return [seven_days_data, last7]

# def raining_check(seven_days_data, date):
#     timedelta = datetime.timedelta(hours=6)
#     timedelta_1 = datetime.timedelta(hours=1)
#     cnt = 0
#     for i in range(6):
#         new_date = date - i*timedelta_1
#         new_date_hourago = new_date - timedelta_1
#         one_hour_data = [x for x in seven_days_data if x[1] > new_date_hourago and x[1] <= new_date]
#         new_date_hourly_rain = hourly_rainfall(one_hour_data,new_date)
#         if new_date_hourly_rain[1] > 4:
#             cnt+=1
#     if cnt>0:
#         return False
#     else:
#         return True


def effective_rainfall(seven_days_data, date, last7, first_raining_time, last_raining_time):
    # print("effective_rainfall counting.....")
    timedelta = datetime.timedelta(hours=6, minutes = 2)
    timedelta_1 = datetime.timedelta(hours=1)
    timedelta_7 = datetime.timedelta(days=7)
    eff_r = 0
    if (date - timedelta) > last_raining_time:
        last7dayrain = last_7_days_rain(seven_days_data, date, "no-raining")
        eff_r = last7dayrain[1]*0.8
    elif (date - timedelta) < last_raining_time:
        seven_days_data = [x for x in seven_days_data if x[1] >= first_raining_time]
        for item in seven_days_data:
            eff_r += item[0]
        eff_r += (last7*0.8)
    return eff_r

# define record format
def record_Commercial(s_id,record):
    record_str = ''
    the_record = ''
    last_record_time = None
    for r in record:
        if last_record_time==None or (r.rec_time-last_record_time).seconds>180:
            the_record = str(r.rec_time)+','+\
                         s_id+','+\
                         str_sw(r.w1)+','+\
                         str_sw(r.w2)+','+\
                         str_sw(r.w3)+','+\
                         str_sw(r.w4)+','+\
                         str_dist(r.dist)+','+\
                         str(r.v)+'\n'
            record_str += the_record
            last_record_time = r.rec_time
    record_list = [record_str,the_record]
    return record_list
def record_CommercialRF(s_id,record):
    record_str = ''
    the_record = ''
    last_record_time = None
    last_raining_time = datetime.datetime(2010, 12, 18, 12, 30, 59, 0)
    first_raining_time = last_raining_time
    last7 = 0
    one_hour_data = []
    seven_days_data = []
    for r in record:
        # data adding
        rain_time = [r.i_rainfall*0.5, r.rec_time]
        one_hour_data.append(rain_time)
        seven_days_data.append(rain_time)
        # counting start
        hourly_rain = hourly_rainfall(one_hour_data, r.rec_time)
        hour_rain = hourly_rain[1]
        one_hour_data = hourly_rain[0]

        if hour_rain > 4 and last_rainfall < 4:
            first_raining_time = r.rec_time
            last7daysrain = last_7_days_rain(seven_days_data, r.rec_time, "raining")
            last7 = last7daysrain[1]
            seven_days_data = last7daysrain[0]
        if hour_rain > 4:
            last_raining_time = r.rec_time
        if r.rec_time<datetime.datetime(2017, 9, 30, 12, 30, 59, 0):
            print(last_raining_time)
        if last_record_time==None or (r.rec_time-last_record_time).seconds>180:
            the_record = str(r.rec_time)+','+\
                         s_id+','+\
                         str(r.i_rainfall*0.5)+','+\
                         str(r.a_rainfall*0.5)+','+\
                         str(round(effective_rainfall(seven_days_data, r.rec_time, last7, first_raining_time, last_raining_time),2))+','+\
                         str(r.v)+'\n'
            record_str += the_record
            last_record_time = r.rec_time
        last_rainfall = hour_rain
    record_list = [record_str,the_record]
    return record_list
def record_SmartStick(s_id,record):
    record_str = ''
    the_record = ''
    last_record_time = None
    for r in record:
        if last_record_time==None or (r.rec_time-last_record_time).seconds>180:
            the_record = str(r.rec_time)+','+\
                         s_id+','+\
                         str_sticksw(r.w1)+','+\
                         str_sticksw(r.w2)+','+\
                         str_sticksw(r.w3)+','+\
                         str_sticksw(r.w4)+','+\
                         str_stickst(r.st1)+','+\
                         str_stickst(r.st2)+','+\
                         str_stickst(r.st3)+','+\
                         str_stickst(r.st4)+','+\
                         str_at(r.at)+','+\
                         str_rh(r.rh)+','+\
                         str_ap(r.ap)+','+\
                         str_rf(r.rf)+','+\
                         str_stickxy(r.ax)+','+\
                         str_stickxy(r.ay)+','+\
                         str_ax(r.az)+','+\
                         str_ay(r.gx)+','+\
                         str_az(r.gy)+','+\
                         str_gx(r.gz)+','+\
                         str_gy(r.inx)+','+\
                         str_gz(r.iny)+'\n'                        
            record_str += the_record
            last_record_time = r.rec_time
    record_list = [record_str,the_record]
    return record_list
def record_TiltStick(s_id,record):
    record_str = ''
    the_record = ''
    last_record_time = None
    for r in record:
        if last_record_time==None or (r.rec_time-last_record_time).seconds>180:
            the_record = str(r.rec_time)+','+\
                         s_id+','+\
                         str_tiltxy(r.inx)+','+\
                         str_tiltxy(r.iny)+'\n'
            record_str += the_record
            last_record_time = r.rec_time
    record_list = [record_str,the_record]
    return record_list
def str_sw(w):
    if w<0:
        return 'null'
    else:
        return str(w)
def str_dist(dist):
    if dist<0 or dist>206:
        return 'null'
    else:
        return str(dist)
def str_sticksw(w):
    if w == 65535 or w<=289:
        return 'null'
    else:
        return str(w*0.3226-93.548)
def str_sticksw2(w):
    if w == 65535 or w<=329:
        return 'null'
    else:
        return str(w*0.3704-122.22)
def str_stickst(st):
    if st == 65535 or st==0:
        return 'null'
    else:
        return str(st*0.1001-1.3028)
def str_at(at):
    if at < -20 or at > 70:
        return 'null'
    else:
        return str(at)
def str_rh(rh):
    if rh < 0 or rh > 100:
        return 'null'
    else:
        return str(rh)
def str_ap(ap):
    if ap < 800 or ap > 1100:
        return 'null'
    else:
        return str(ap)
def str_rf(rf):
    return str(rf*0.38)
def str_stickxy(inxy):
    if inxy >= -614 and inxy <= 2662:
        return str(math.asin((inxy-1024)/1638)*180/math.pi)
    else:
        return 'null'
def str_tiltxy(inxy):
    if inxy >= 205 and inxy <= 1843:
        return str(math.asin((inxy-1024)/819)*180/math.pi)
    else:
        return 'null'
def str_ax(ax):
    return str(ax)
def str_ay(ay):
    return str(ay)
def str_az(az):
    return str(az)
def str_gx(gx):
    return str(gx)
def str_gy(gy):
    return str(gy)
def str_gz(gz):
    return str(gz)
	
def get_sql():
    fw_log = open(log_file,'a')
    now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    fw_log.write('now = '+now)
    # Connect MSSQL
    fw_log.write('MSSQL connect...')
    conn = pyodbc.connect(connStr)
    cur = conn.cursor()
    # Get record    
    filePath = 'C://test//taipeicity.csv'
    fout = open(filePath,'wt')
    for i in range(0,len(sensorID)):
        fw_log.write('Get [sid_'+sensorID[i]+'] record...')
        s_id = sensorID[i]
        record_str = ''
        record = cur.execute("select * from "+sensorDataTable[i]+" where s_id like '%"+s_id+"%' and (rec_time between '"+StartTime+"' and '"+EndTime+"') order by rec_time")
        filePath = 'C://test//sid_'+str(s_id)+'.csv'
        fout_sid = open(filePath,'wt')
        if sensorType[i]==1:
            fout_sid.write('rec_time,s_id,w1,w2,w3,w4,dist,v\n')
            [record_str,last_record] = record_Commercial(s_id,record)
        elif sensorType[i]==2:
            fout_sid.write('rec_time,s_id,w1,w2,w3,w4,st1,st2,st3,st4,at,rh,ap,rf,inx,iny,ax,ay,az,gx,gy,gz\n')
            [record_str,last_record] = record_SmartStick(s_id,record)
        elif sensorType[i]==3:
            fout_sid.write('rec_time,s_id,inx,iny\n')
            [record_str,last_record] = record_TiltStick(s_id,record)
        elif sensorType[i]==4:
            fout_sid.write('rec_time,s_id,rainfall_10m,rainfall_acc,rainfall_eff,v\n')
            [record_str,last_record] = record_CommercialRF(s_id,record)
        fout_sid.write(record_str)
        fout.write(last_record)
        fout_sid.close()
    fout.close()
    cur.close()
    conn.close()
    fw_log.write('['+now+'] CSV upload done !!!\n')
    fw_log.close()
    print("get sql done")

# Record Time range
StartTime = '2017/08/04 12:00:00'
EndTime = '2100/01/1 00:00:00'

# Connect MS SQL
MSSQL_serverName = 'GERCNETV'
MSSQL_database = 'Sinogerc'
MSSQL_userID = 'Sinotech'
MSSQL_password = '11569326'
connStr = 'DRIVER={SQL Server};SERVER='+MSSQL_serverName+';DATABASE='+MSSQL_database+';UID='+MSSQL_userID+';PWD='+MSSQL_password

# read sensor
sensorID = ['78','1','2','89']
sensorType = [1,2,2,4]#Type1=commercial; Type2=SmartStick; Type3=TiltStick; Type4=commercial_rainfall
sensorDataTable = ['taipeicity1','taipeicity2','taipeicity2','taipeicity3']

# Start every 10 minutes
log_file = 'C://test//abri_get_sql_running.txt'
scheduler = BlockingScheduler()
get_sql()
scheduler.add_job(get_sql, 'cron', minute='5,15,25,35,45,55', end_date='2100-01-01')
scheduler.start()

