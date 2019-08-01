# SensorFusion
從sensor的陀螺儀、加速度計估算出sensor的傾斜情形。
## Folder
- **\SensorData:** 放一次測試的原始陀螺儀、加速度計數據。(腰部定位點位置數據)  
- **\OrientationOutput:** 輸出的sensor的傾斜情形，以四元數表示；腰部定位點位置數據；每筆資料時間間格(ms)。作為Blender模型的輸入數據。
## Code
- **AlignTime.py:** 對齊\SensorData中的原始數據的時間標記，以第一個檔案的時間為基準，其他檔案的資料用內插法對齊時間標記。輸出SensorData.csv。(無腰部定位點檔案)  
- **AlignTime+pos10.py:** 同AlignTime.py，10個sensor加上腰部定位點檔案。  
- **AlignTime+pos11.py:** 同AlignTime.py，11個sensor加上腰部定位點檔案。  
- **Orientation.m:** 輸入為SensorData.csv，計算sensor的傾斜情形，輸出檔案到\OrientationOutput。
