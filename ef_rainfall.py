import pyodbc, datetime, math, time
from pathlib import Path
from apscheduler.schedulers.blocking import BlockingScheduler

def hourly_rainfall(record,date):
    timedelta = datetime.timedelta(hours = 1)
    h_rainfall = 0
    onehourago = data - timedelta
    for r in record:
        if r.rec_time > onehourago and r.rec_time <= date:
            h_rainfall += r.i_rainfall*0.5
    return h_rainfall

def last_7_days_rain(record, date):
    timedelta = datetime.timedelta(days=7)
    last7 = 0
    sevendaysago = date - timedelta
    for r in record:
        if r.rec_time >= sevendaysago and r.rec_time < date:
            last7 += r.i_rainfall*0.50*0.8      
    return last7

def rain_stop_check(record, date):
    timedelta = datetime.timedelta(hours=1)
    cnt = 0
    for i in range(6):
        accu_rain = 0
        earlytime = date - timedelta
        latetime = date
        for r in record:
            if r.rec_time >= earlytime and r.rec_time <= latetime:
                accu_rain = accu_rain + r.i_rainfall*0.5
        latetime = earlytime
        earlytime = earlytime - timedelta
        if accu_rain > 4:
            cnt += 1
    if cnt > 0:
        return False
    else:
        return True

def effective_rainfall(record,i_r,date,last7,last_rtime):
    i_rain = 0
    if rain_stop_check(record,date) == False:
        for r in record:
            if r.rec_time >= last_rtime and r.rec_time <= date:
                i_rain = r.i_rainfall*0.5
                eff_r = eff_r + i_rain
        eff_r = eff_r + last7
    else:
        eff_r = last_7_days_rain(record,date)
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
    last_rainfall = 0
    last7 = 0
    for r in record:
        hour_rain = hourly_rainfall(record, r.rec_time)
        if hour_rain > 4 and last_rainfall < 4:
            last_raining_time = r.rec_time
            last7 = last_7_days_rain(record, r.rec_time)
        if last_record_time==None or (r.rec_time-last_record_time).seconds>180:
            the_record = str(r.rec_time)+','+\
                         s_id+','+\
                         str(r.i_rainfall*0.5)+','+\
                         str(r.a_rainfall*0.5)+','+\
                         str(effective_rainfall(record, r.i_rainfall*0.5, r.rec_time, last7, last_raining_time))+','+\
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
    filePath = 'C://Inetpub//wwwroot//abri//sensor//taipeicity.csv'
    fout = open(filePath,'wt')
    for i in range(0,len(sensorID)):
        fw_log.write('Get [sid_'+sensorID[i]+'] record...')
        s_id = sensorID[i]
        record_str = ''
        record = cur.execute("select * from "+sensorDataTable[i]+" where s_id like '%"+s_id+"%' and (rec_time between '"+StartTime+"' and '"+EndTime+"') order by rec_time")
        filePath = 'C://Inetpub//wwwroot//abri//sensor//sid_'+str(s_id)+'.csv'
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
            # 
            fout_sid.write('rec_time,s_id,rainfall_10m,rainfall_acc,v\n')
            # 
            [record_str,last_record] = record_CommercialRF(s_id,record)
            
        fout_sid.write(record_str)
        fout.write(last_record)
        fout_sid.close()
    fout.close()
    cur.close()
    conn.close()
    fw_log.write('['+now+'] CSV upload done !!!\n')
    fw_log.close()

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
log_file = 'C://Inetpub//wwwroot//2187//log//abri_get_sql_running.txt'
scheduler = BlockingScheduler()
get_sql()
scheduler.add_job(get_sql, 'cron', minute='5,15,25,35,45,55', end_date='2100-01-01')
scheduler.start()
