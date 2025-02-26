# 進入Caldera容器
docker exec -it caldera-1 bash

# 在容器內執行
python3 -c "import pyrdp; print(pyrdp.__version__)"
# 應輸出：2.1.0
