# Гайд по использованию Sigma UI

## Что такое Sigma UI?

Sigma UI - это коллекция полностью настраиваемых компонентов для Vue 3, построенных на основе Reka-UI (Radix) примитивов. Компоненты копируются напрямую в ваш проект через GOAT (Git Obtained As Template) метод, что дает полный контроль над кодом.

## Установка и настройка

### Шаг 1: Инициализация конфигурации

Выполните в терминале в директории `frontend`:

```bash
npx sigma-ui init
```

Эта команда создаст файл `.sigma-ui.json` с настройками проекта.

### Шаг 2: Установка зависимостей

Sigma UI требует следующие зависимости:

**Уже установлены в проекте:**

- Vue 3+
- TypeScript
- Tailwind CSS

**Необходимо установить дополнительно:**

```bash
npm install reka-ui clsx tailwind-merge
```

Где:

- `reka-ui` - примитивы для компонентов (основа Sigma UI)
- `clsx` - утилита для условных классов
- `tailwind-merge` - утилита для объединения классов Tailwind без конфликтов

**Примечание:** Утилита `cn()` уже создана в `src/lib/utils.ts` и используется компонентами для объединения классов.

### Шаг 3: Добавление компонентов

Для добавления компонентов используйте:

```bash
npx sigma-ui add
```

Эта команда откроет интерактивное меню, где вы можете выбрать нужные компоненты. Компоненты будут скопированы в директорию `src/components/ui/`.

## Структура после установки

После добавления компонентов структура будет выглядеть так:

```text
frontend/src/
  components/
    ui/
      button/
        Button.vue
        index.ts
      input/
        Input.vue
        index.ts
      ...
```

## Использование компонентов

### Пример 1: Кнопка (Button)

```vue
<template>
  <Button variant="default" size="md">
    Нажми меня
  </Button>
</template>

<script setup lang="ts">
import { Button } from '@/components/ui/button'
</script>
```

### Пример 2: Поле ввода (Input)

```vue
<template>
  <div>
    <label>Email</label>
    <Input 
      v-model="email" 
      type="email" 
      placeholder="Введите email"
    />
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Input } from '@/components/ui/input'

const email = ref('')
</script>
```

### Пример 3: Диалог (Dialog)

```vue
<template>
  <div>
    <Button @click="open = true">Открыть диалог</Button>
    <Dialog v-model:open="open">
      <DialogContent>
        <DialogHeader>
          <DialogTitle>Заголовок</DialogTitle>
          <DialogDescription>Описание диалога</DialogDescription>
        </DialogHeader>
        <p>Содержимое диалога</p>
        <DialogFooter>
          <Button @click="open = false">Закрыть</Button>
        </DialogFooter>
      </DialogContent>
    </Dialog>
  </div>
</template>

<script setup lang="ts">
import { ref } from 'vue'
import { Button } from '@/components/ui/button'
import { 
  Dialog, 
  DialogContent, 
  DialogHeader, 
  DialogTitle, 
  DialogDescription,
  DialogFooter 
} from '@/components/ui/dialog'

const open = ref(false)
</script>
```

## Кастомизация компонентов

Поскольку компоненты копируются в ваш проект, вы можете:

1. **Изменять стили напрямую** - редактируйте классы Tailwind в компонентах
2. **Модифицировать логику** - изменяйте props, события, методы компонентов
3. **Добавлять функциональность** - расширяйте компоненты под свои нужды

### Пример кастомизации кнопки

```vue
<!-- src/components/ui/button/Button.vue -->
<template>
  <button
    :class="cn(
      'inline-flex items-center justify-center rounded-md font-medium transition-colors',
      'focus-visible:outline-none focus-visible:ring-2 focus-visible:ring-offset-2',
      'disabled:pointer-events-none disabled:opacity-50',
      variants[variant],
      sizes[size]
    )"
    :disabled="disabled"
    @click="$emit('click', $event)"
  >
    <slot />
  </button>
</template>

<script setup lang="ts">
// Ваша кастомная логика
</script>
```

## Популярные компоненты

- **Button** - кнопки различных вариантов
- **Input** - поля ввода
- **Dialog** - модальные окна
- **Select** - выпадающие списки
- **Checkbox** - чекбоксы
- **Radio** - радиокнопки
- **Card** - карточки
- **Table** - таблицы
- **Form** - формы с валидацией
- **Toast** - уведомления
- **Dropdown Menu** - выпадающие меню
- **Tabs** - вкладки
- **Accordion** - аккордеон
- **Alert** - предупреждения

**Полный список всех доступных компонентов:** См. файл `SIGMA_UI_COMPONENTS_LIST.md`

## Быстрый старт

### 1. Установите зависимости

```bash
cd frontend
npm install reka-ui clsx tailwind-merge class-variance-authority
```

**Примечание:** `class-variance-authority` используется для вариантов компонентов (variant, size и т.д.)

### 2. Инициализируйте Sigma UI

```bash
npx sigma-ui init
```

Скопируйте содержимое из `.sigma-ui.json.example` в созданный файл `.sigma-ui.json` и при необходимости отредактируйте пути.

### 3. Добавьте первый компонент

```bash
npx sigma-ui add
```

Выберите компонент из списка (например, `button`).

### 4. Используйте компонент

```vue
<template>
  <div class="space-x-4">
    <Button variant="default">По умолчанию</Button>
    <Button variant="outline">Контур</Button>
    <Button variant="destructive">Удалить</Button>
    <Button variant="ghost">Призрачный</Button>
    <Button size="sm">Маленький</Button>
    <Button size="lg">Большой</Button>
  </div>
</template>

<script setup lang="ts">
import { Button } from '@/components/ui/button'
</script>
```

**Пример компонента:** См. `src/components/ui/button/Button.example.vue` для примера реализации.

## Интеграция с существующим проектом

### Обновление существующих компонентов

Вы можете заменить существующие компоненты на Sigma UI компоненты:

1. Добавьте нужный компонент через `npx sigma-ui add`
2. Импортируйте его в вашем Vue файле
3. Замените старый компонент на новый
4. Настройте стили под ваш дизайн

### Пример замены кнопки в Users.vue

```vue
<!-- Было -->
<button class="bg-blue-600 hover:bg-blue-700...">
  Создать пользователя
</button>

<!-- Стало -->
<Button variant="default" size="md">
  Создать пользователя
</Button>
```

## Доступность (Accessibility)

Все компоненты Sigma UI построены на Reka-UI примитивах, которые обеспечивают:

- Поддержку клавиатурной навигации
- ARIA атрибуты
- Фокус-менеджмент
- Поддержку скринридеров

## Полезные ссылки

- [Официальный сайт](https://sigma-ui.dev)
- [GitHub репозиторий](https://github.com/sigma-hub/sigma-ui)
- [Документация Reka-UI](https://reka-ui.com)

## Структура файлов проекта

После установки компонентов структура будет следующей:

```text
frontend/
  src/
    components/
      ui/              # Компоненты Sigma UI
        button/
          Button.vue
          index.ts
        input/
          Input.vue
          index.ts
        ...
    lib/
      utils.ts         # Утилита cn() для классов
    ...
  .sigma-ui.json       # Конфигурация Sigma UI
```

## Интеграция с TypeScript

Все компоненты полностью типизированы. Убедитесь, что в `tsconfig.json` настроены алиасы:

```json
{
  "compilerOptions": {
    "paths": {
      "@/*": ["./src/*"]
    }
  }
}
```

## Часто задаваемые вопросы

**Q: Можно ли использовать компоненты без Tailwind?**  
A: Нет, Sigma UI требует Tailwind CSS для стилизации.

**Q: Как обновить компоненты?**  
A: Компоненты копируются в ваш проект, поэтому обновления нужно делать вручную или переустановить компонент через `npx sigma-ui add`.

**Q: Поддерживается ли Vue 2?**  
A: Нет, только Vue 3 и выше.

**Q: Можно ли использовать в Nuxt?**  
A: Да, Sigma UI поддерживает Nuxt, Vue, Laravel и Astro.

**Q: Что делать, если компонент не работает?**  
A: Убедитесь, что:

1. Установлены все зависимости (`reka-ui`, `clsx`, `tailwind-merge`)
2. Файл `src/lib/utils.ts` существует с функцией `cn()`
3. Пути в `.sigma-ui.json` соответствуют структуре проекта
4. Tailwind CSS правильно настроен в `tailwind.config.js`
