clear;
close all;
samplePeriod = 1/100;
P = csvread('SensorData.csv', 2, 1);
[datanum, dia] = size(P);

if dia == 65 %10+pos
    sensorNum = 10;
    PosCol = 61;
    TimeCol = 64;
elseif dia == 71 %11+pos
    sensorNum = 11;
    PosCol = 67;
    TimeCol = 70;
elseif dia == 68 %10 or 11
    if P(1,61) == 0 %10
        sensorNum = 10;
        PosCol = -1;
        TimeCol = 61;
    elseif P(1,61) ~= 0 %11
        sensorNum = 11;
        PosCol = -1;
        TimeCol = 67;
    end
end
fid = fopen('SensorData.csv');
FirstLine = textscan(fid,'%s',1);
FirstLine = string(FirstLine);
SensorPos0 = split(FirstLine, ',')';

for i = 1:sensorNum
    gyrX = csvread('SensorData.csv',2,(i-1)*6+1,[2,(i-1)*6+1,datanum,(i-1)*6+1]);
    gyrY = csvread('SensorData.csv',2,(i-1)*6+2,[2,(i-1)*6+2,datanum,(i-1)*6+2]);
    gyrZ = csvread('SensorData.csv',2,(i-1)*6+3,[2,(i-1)*6+3,datanum,(i-1)*6+3]);
    accX = csvread('SensorData.csv',2,(i-1)*6+4,[2,(i-1)*6+4,datanum,(i-1)*6+4]);
    accY = csvread('SensorData.csv',2,(i-1)*6+5,[2,(i-1)*6+5,datanum,(i-1)*6+5]);
    accZ = csvread('SensorData.csv',2,(i-1)*6+6,[2,(i-1)*6+6,datanum,(i-1)*6+6]);
    if gyrX == 0
       break; 
    end
    Accelerometer = [accX accY accZ]*9.8;
    Gyroscope = [gyrX gyrY gyrZ]*pi/180;
    
    ifilt = imufilter();
    for ii=1:size(Accelerometer,1)
        qimu(ii) = ifilt(Accelerometer(ii,:), Gyroscope(ii,:));
    end
    [a,b,c,d] = parts(qimu);
    quat = [a' b' c' d'];
    csvwrite(strcat('OrientationOutput\', strcat(SensorPos0(i), 'quaternions.csv')), quat);
end
if PosCol ~= -1
    PosX = csvread('SensorData.csv',2,PosCol,[2,PosCol,datanum,PosCol]);
    PosY = csvread('SensorData.csv',2,PosCol+1,[2,PosCol+1,datanum,PosCol+1]);
    PosZ = csvread('SensorData.csv',2,PosCol+2,[2,PosCol+2,datanum,PosCol+2]);
    Pos = [PosX PosY PosZ];
    csvwrite('OrientationOutput\Position.csv', Pos);
end
%----------------------------TimeStamp-------------------------------------
TimeStamp = csvread('SensorData.csv',2,TimeCol,[2,TimeCol,datanum,TimeCol]);
TimeStampDiff = diff(TimeStamp);
csvwrite('OrientationOutput\TimeStampDiff.csv', TimeStampDiff);
%-------------------------------------------------------------------------
