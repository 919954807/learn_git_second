

for i in range(0,8):
    for j in range(0,8):
        mystr = "INSERT INTO `basisdata`.`device` (`id`, `create_userid`, `create_time`, `last_update_userid`, `last_update_time`, `name`, `pid`, `sort_number`, `org_id`, `device_address`, `login_user`, `password`, `device_ip`, `port`, `channel_number`, `remark`, `version_number`, `online_status`, `device_brand`, `device_type`, `device_name`, `DeviceMainType`, `cfg_DevBrandConifgId`, `video_port`, `threshold`, `person_threshold`) VALUES ('7fc8519fcf7f4ae38a18631adfaca6"+str(i)+str(j)+"', 'e4bdc27719ae4e87ab9581c3d24c812b', '2020-06-30 12:19:15', 'e4bdc27719ae4e87ab9581c3d24c812b', '2020-06-30 12:19:15', NULL, '956f024fd9c643dbacfd32a0ad7231dd', '2', 'cffeb9506bb8475090c0d0d72ebd4d29', '大门', NULL, NULL, NULL, NULL, '1"+str(i)+str(j)+"', NULL, NULL, '1', '4', '3502', '人脸抓拍枪"+str(i)+str(j)+"', '3500', NULL, NULL, NULL, '85');"
        print(mystr)