# ОСА. RTV_redactor

## The task
It is necessary to write a program that can translate
hand-drawn bitmap diagrams in vector representation.

## Explanation
1) Translation is carried out in the process of drawing, i.e. algorithm
not only the coordinates of the raster points are available, but also their time
appearance.
2) The resulting vector image can then be edited.
3) In general, the program is a vector editor
schemes with a special mode. In this mode, you can draw
the shape with the mouse and click the "recognize" button. At the recruitment site
points should appear a vector figure, which can now be
edit as vector (resize, add
inscription).
4) Arrows / lines connecting
figures. Simple heuristic formulas may be enough for this.

## Separation of duties

__Azarnikov Ivan__

Development of a graphical interface

__Ogloblin Ivan__

Working with tracing algorithms, writing a classifier. Wrote his own algorithm of recognition with ideas of interpolation angles and point structures 

__Selivanov Makar__

Description of classes of shapes, writing a wrapper for python.

## About interface

The window consists of a black working area and the main menu, on
which contains 6 buttons: `save`, ʻedit`, ʻeraser`,
`color`,` width`, `clean`. `Save` is for saving
thumbnail to the images directory in png format, ʻedit` - to switch
between drawing and editing modes. ʻEraser` - eraser, `color`
for choosing the color of the pen, `width` - the width of the pen,` clear` -
for complete cleaning of the working area.

## Boost installation tutorial

* Download library from [official site] (https://www.boost.org/)
* Unzip wherever convenient
* Next, it will launch bootstrap.sh with this command
>
> ./ bootstrap.sh --with-libraries = python
>
* The project-config.jam file will appear, it will need to be changed a little:
in the using python line, add the path to the includes (21 lines of the file)
* It is necessary to make a line:
>
> using python: 3.6: "/usr/bin/python3.6": "/usr/include/python3.6";
>
__Every space is important here __. Instead of 3.6, write your version of the interpreter.
* If there is nothing in / usr / include / python *, then you need to install python3.6-dev
* Then we write
> ./ b2 install —prefix = "The path where we want to install"
 
--prefix can be omitted if you want to put it in the default place

## Задание 
Необходимо написать программу, которая умеет переводить 
нарисованные от руки растровые схемы в векторное представление.

## Пояснение
1) Перевод осуществляется в процессе рисования, т.е. алгоритму
доступны не только координаты точек растра, но и времена их 
появления. 
2) Получившееся векторное изображение затем можно 
редактировать. 
3) В общем программа представляет из себя векторный редактор 
схем со специальным режимом. В этом режиме можно нарисовать 
фигуру мышкой и нажать кнопку “распознать”. На месте набора 
точек должна появится векторная фигура, которую теперь можно 
редактировать как векторную (менять размеры, добавлять 
надпись). 
4) Так же должны распознаваться стрелки/линии, соединяющие 
фигуры.  Для этого может хватить простых эвристических формул.

## Разделение обязаностей

__Азарников Иван__

Разработка графического интерфейса

__Оглоблин Иван__

Работа с алгоритмами трассировки, написание классификатора

__Селиванов Макар__

Описание классов фигур, написание обертки для питона.

## Про интерфейс

Окно состоит из черного рабочего поля и главного меню, на
котором расположены 6 кнопок: `save`, `edit`, `eraser`, 
`color`, `width`, `clean`. `Save` предназначена для сохранения 
эскиза в директорию images в формате png, `edit` - для переключения
между режимами рисования и редактирования. `Eraser` - ластик, `color` 
предназначени для выбора цвета пера, `width` - ширины пера, `clear` - 
для полного очищения рабочего поля.

## Туториал по установке boost

* Скачать библиотеку с [официального сайта](https://www.boost.org/)
* Разархивировать, куда удобно
* Дальше запустит bootstrap.sh с такой командой
>
>./bootstrap.sh --with-libraries=python
>
* Появиться файл project-config.jam, его надо будет чуть-чуть изменить:
в строчке using python надо дописать путь до инклюдов (21 строчка файла)
* Надо сделать строчку:    
>
>using python : 3.6 : "/usr/bin/python3.6" : "/usr/include/python3.6" ; 
>
__Здесь важен каждый пробел__. Вместо 3.6 пишите свою версию интерпретатора. 
* Если в /usr/include/python* ничего нет, то нужно установить python3.6-dev
* Дальше пишем
>./b2 install —prefix="Путь, куда хотим поставить"
 
--prefix можно не писать, если хотите поставить в место по умолчанию 
