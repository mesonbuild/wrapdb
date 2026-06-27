@echo off

chdir /d %1
go run %3 -in-executable %2
