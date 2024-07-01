import cdsapi
import calendar
import os
#在运行前先安装cdsapi包
'''

'''
c = cdsapi.Client()

dic = {
    'product_type': 'reanalysis-era5-land', #选择数据集
    'format': 'netcdf.zip',  #选择数据格式
    'variable':[
            '2m_dewpoint_temperature', '2m_temperature', 'forecast_albedo',
            'runoff', 'snow_depth_water_equivalent', 'snowmelt',
            'sub_surface_runoff', 'surface_latent_heat_flux', 'surface_net_solar_radiation',
            'surface_runoff', 'surface_sensible_heat_flux', 'total_evaporation',
            'total_precipitation'
        ], #选择要素
    'year': '',  
    'month': '',  
    'day': [],  
    'time': [  
        '00:00', '01:00', '02:00', '03:00', '04:00', '05:00',
        '06:00', '07:00', '08:00', '09:00', '10:00', '11:00',
        '12:00', '13:00', '14:00', '15:00', '16:00', '17:00',
        '18:00', '19:00', '20:00', '21:00', '22:00', '23:00'
    ],
    'area': [
            38.4, 118, 36.9,
            119.5,
        ]
}

def create_folder_if_not_exists(folder_path):
    if not os.path.exists(folder_path):
        os.makedirs(folder_path)
        print(f"文件夹 '{folder_path}' 不存在，已创建。")
    else:
        print(f"文件夹 '{folder_path}' 已存在。")

# 批量下载1979年到2021年所有月份数据
fold='E:/ERA5/'
#create_folder_if_not_exists(fold)
for i in range(2022, 2023): 
    for j in range(6, 13):  
        day_num = calendar.monthrange(i, j)[1]  # 根据年月，获取当月日数
        dic['year'] = str(i) 
        dic['month'] = str(j).zfill(2)
        dic['day'] = [str(d).zfill(2) for d in range(1, day_num + 1)]
        filename = fold+"/Dongying_"+ str(i) +"_"+ str(j).zfill(2) + '.zip'  # 文件存储路径
        c.retrieve('reanalysis-era5-land', dic, filename)  # 下载数据
