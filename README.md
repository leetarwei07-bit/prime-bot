# PRIME Bot

Telegram бот для мини-приложения PRIME.

## Деплой на Railway

### 1. Залей на GitHub
```bash
git init
git add .
git commit -m "init"
git remote add origin https://github.com/ВАШ_АККАУНТ/prime-bot.git
git push -u origin main
```

### 2. Railway
1. railway.app → New Project → Deploy from GitHub
2. Выбери репозиторий
3. Variables → добавь:
   - `BOT_TOKEN` = твой токен от @BotFather
   - `WEBAPP_URL` = URL твоего мини-приложения (например https://prime.up.railway.app)
4. Deploy

### Переменные окружения
| Переменная | Описание |
|---|---|
| `BOT_TOKEN` | Токен бота от @BotFather |
| `WEBAPP_URL` | URL мини-приложения |

### Файлы
- `Bot.py` — основной код бота
- `image.jpg` — приветственное фото (замени на своё)
- `requirements.txt` — зависимости
- `Procfile` — команда запуска для Railway
