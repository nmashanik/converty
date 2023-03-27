# Converty

## Постановка решаемой задачи

Разработать Telegram бота, который позволит конвертировать файлы, присланные пользователем в определенные форматы.

## Описание предполагаемых инструментов решения

Библиотека `telebot` для создания Telegram бота
Библиотека `zipfile` для работы с архивами
Пакеты `img2pdf`, `pdf2image`, `fpdf`, etc.

## Интерфейс

Бот взаимодействует с пользователем через Telegram.
Пользователь отправляет файлы, которые хочет конвертировать и задает желаемый формат.

Примеры команд для бота:

1. `/start`: начало работы, инициализация бота;

2. `/help`: отображение списка доступных команд и их описание;

3. `/make <формат>`: создает файл указанного формата из загруженных файлов;

4. `/reset`: бот забывает загруженные ранее файлы;

5. `/stop`: завершение сеанса;

...
