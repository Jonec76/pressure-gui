# 壓力感測圖形介面

## 執行
1. python3 server.py
2. python3 client.py

## 簡介
原始版本是 server 會每秒傳送訊號到 client，client 收到訊號後隨機產生 56 筆仿壓力資料。

如果要改成接收 Arduino 的真實資料，則將 client.py 裡頭的 `datas` 改掉即可。

## P.S.
onClick 在 demo 應該用不到，只是先留著。