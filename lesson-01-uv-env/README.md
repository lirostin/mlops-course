# Описание проекта 

Предсказать стоимость поездки (fare_amount) в Uber на основе различных параметров.

Используется файл uber.csv с историческими данными поездок, содержащий:

- Координаты посадки (pickup_latitude, pickup_longitude)
- Координаты высадки (dropoff_latitude, dropoff_longitude)
- Количество пассажиров (passenger_count)
- Стоимость поездки (fare_amount) - целевая переменная

# Процесс запуска

Устанавливаем нужные зависимости и запускаем сборку.

```
make install_python310_macos

make install_uv_mac_linux

make init_uv

make run_project
```