# Полный список компонентов Sigma UI

Список всех компонентов, доступных для установки через команду `npx sigma-ui add` на сайте [sigma-ui.dev](https://sigma-ui.dev/).

## Команда установки

```bash
npx sigma-ui add [название-компонента]
```

Или интерактивный режим:

```bash
npx sigma-ui add
```

## Список компонентов

### Базовые компоненты

1. **accordion** - Аккордеон (раскрывающиеся секции)
2. **alert** - Предупреждения и уведомления
3. **alert-dialog** - Диалоговые окна с предупреждениями
4. **avatar** - Аватары пользователей
5. **badge** - Значки и метки
6. **button** - Кнопки различных стилей
7. **card** - Карточки для контента
8. **checkbox** - Чекбоксы
9. **collapsible** - Сворачиваемые секции
10. **command** - Командная палитра (поиск)
11. **context-menu** - Контекстное меню
12. **dialog** - Модальные диалоговые окна
13. **dropdown-menu** - Выпадающие меню
14. **hover-card** - Карточка при наведении
15. **input** - Поля ввода текста
16. **label** - Метки для форм
17. **menubar** - Панель меню
18. **navigation-menu** - Навигационное меню
19. **popover** - Всплывающие окна
20. **progress** - Индикаторы прогресса
21. **radio-group** - Группы радиокнопок
22. **scroll-area** - Области с прокруткой
23. **select** - Выпадающие списки выбора
24. **separator** - Разделители
25. **sheet** - Боковые панели (drawer)
26. **skeleton** - Скелетоны загрузки
27. **slider** - Слайдеры значений
28. **switch** - Переключатели
29. **table** - Таблицы данных
30. **tabs** - Вкладки
31. **textarea** - Многострочные поля ввода
32. **toast** - Всплывающие уведомления
33. **toggle** - Переключатели (toggle buttons)
34. **toggle-group** - Группы переключателей
35. **tooltip** - Всплывающие подсказки

### Расширенные компоненты

36. **calendar** - Календарь
37. **date-picker** - Выбор даты
38. **form** - Формы с валидацией
39. **pagination** - Пагинация
40. **data-table** - Расширенные таблицы данных
41. **breadcrumb** - Хлебные крошки
42. **carousel** - Карусель/слайдер
43. **chart** - Графики и диаграммы
44. **drawer** - Выдвижные панели
45. **resizable** - Изменяемые размеры панелей
46. **sonner** - Альтернативная система уведомлений
47. **tabs-list** - Список вкладок
48. **combobox** - Комбинированный ввод
49. **file-upload** - Загрузка файлов
50. **rating** - Рейтинги и оценки

## Категории компонентов

### Формы и ввод данных
- input
- textarea
- select
- checkbox
- radio-group
- switch
- slider
- combobox
- file-upload
- form
- label
- date-picker
- calendar

### Навигация
- navigation-menu
- breadcrumb
- tabs
- tabs-list
- menubar
- pagination

### Обратная связь
- alert
- alert-dialog
- toast
- sonner
- progress
- skeleton
- tooltip
- popover

### Данные
- table
- data-table
- card
- badge
- avatar

### Поверхности
- dialog
- sheet
- drawer
- popover
- hover-card
- tooltip

### Раскрытие контента
- accordion
- collapsible
- tabs
- dropdown-menu
- context-menu
- command

### Действия
- button
- toggle
- toggle-group
- switch
- checkbox
- radio-group

### Медиа
- carousel
- chart
- avatar

### Утилиты
- separator
- scroll-area
- resizable
- skeleton
- rating

## Примеры использования команд

```bash
# Установка одного компонента
npx sigma-ui add button

# Установка нескольких компонентов
npx sigma-ui add button input card

# Интерактивный режим (выбор из списка)
npx sigma-ui add
```

## Примечания

- Все компоненты устанавливаются в директорию `src/components/ui/`
- Каждый компонент полностью настраиваемый после установки
- Компоненты построены на Reka-UI (Radix-Vue) примитивах
- Все компоненты поддерживают TypeScript
- Компоненты требуют Tailwind CSS для стилизации

## Актуальный список

Для получения актуального списка компонентов выполните:

```bash
npx sigma-ui add
```

Эта команда покажет интерактивное меню со всеми доступными компонентами на момент выполнения.

## Документация

Полная документация и примеры использования доступны на [sigma-ui.dev](https://sigma-ui.dev/)

