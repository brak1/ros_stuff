clear all; close all; clc; 

y = [0:0.1:100]; 
z = 50 + sin(y) + rand; 

clock_now = fix(clock());

S = strsplit(num2str(clock_now));

filename = ['./data/temp_' date '_' num2str(clock_now(4)) '-' num2str(clock_now(5)) '-' num2str(clock_now(6)) '.csv'];

Y = [ -1 y]; % add a first index to fill
Z = [ clock_now(6) z]; % add the "X" value for this file, using the current seconds
csvwrite(filename, [Y' Z']); 

figure; 
plot(y,z); 
