# 🐱 DumbGame
 
> *Just one silly game for uni project*
 
---
 
## 🇷🇺 Русский
 
### О игре
 
Маленькая аркада на Python + Pygame, сделанная как учебный проект. Играешь за кота, который ловит рыбу и уворачивается от кокосов. Чем больше рыбы поймаешь — тем выше уровень и тем быстрее всё падает. Не дай кокосам тебя доконать!
 
### Управление
 
- `←` / `A` — двигаться влево
- `→` / `D` — двигаться вправо
### Что падает
 
| Объект | Очки | Здоровье |
|--------|------|----------|
| 🐟 Обычная рыба | +1 | 0 |
| 🌟 Золотая рыба | +5 | +5 |
| 🥥 Кокос | -2 | -2 |
 
### Как запустить
 
**Вариант 1 — готовый `.exe`** (только Windows):
```
dist/main.exe
```
 
**Вариант 2 — из исходников:**
```bash
pip install pygame
python main.py
```
 
### Сборка `.exe` самостоятельно
 
```bash
pip install pyinstaller
pyinstaller main.spec
```
 
Готовый файл появится в папке `dist/`.
 
### Технологии
 
- Python 3
- Pygame
---
 
## 🇬🇧 English
 
### About
 
A small arcade game built with Python + Pygame as a university project. You play as a cat catching fish and dodging coconuts. The more fish you catch, the higher the level — and the faster everything falls. Don't let the coconuts get you!
 
### Controls
 
- `←` / `A` — move left
- `→` / `D` — move right
### What's falling
 
| Object | Score | Health |
|--------|-------|--------|
| 🐟 Regular fish | +1 | 0 |
| 🌟 Golden fish | +5 | +5 |
| 🥥 Coconut | -2 | -2 |
 
### How to run
 
**Option 1 — prebuilt `.exe`** (Windows only):
```
dist/main.exe
```
 
**Option 2 — from source:**
```bash
pip install pygame
python main.py
```
 
### Building `.exe` yourself
 
```bash
pip install pyinstaller
pyinstaller main.spec
```
 
The output will appear in the `dist/` folder.
 
### Tech stack
 
- Python 3
- Pygame
