#Telegram Notification Bot
#Send alerts và notifications về pipeline status
# 1. Import telegram bot library (python-telegram-bot)
# 2. Load TELEGRAM_BOT_TOKEN và TELEGRAM_CHAT_ID từ env
# 3. Implement send_message(message, parse_mode='Markdown')
# 4. Implement send_alert(alert_type, title, description, severity)
# 5. Format messages với emoji và markdown
# 6. Include link to logs/Grafana dashboard
# 7. Handle retry logic nếu send failed
# 8. Implement rate limiting để tránh spam
# 9. Support multiple chat IDs cho different alert levels
# 10. CLI interface: python telegram_bot.py --message "text"