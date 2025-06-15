# auto_news_genie/cron_setup.sh

# This script is used only for local/Linux server testing
# Render.com has built-in cron job support via Background Workers

# Add the following line to your crontab using `crontab -e`
# It runs the job every day at 6 AM

# ┌───────────── minute (0 - 59)
# │ ┌───────────── hour (0 - 23)
# │ │ ┌───────────── day of month (1 - 31)
# │ │ │ ┌───────────── month (1 - 12)
# │ │ │ │ ┌───────────── day of week (0 - 6) (Sunday to Saturday)
# │ │ │ │ │
# │ │ │ │ │
# │ │ │ │ │
# 0 6 * * * /usr/bin/python3 /path/to/auto_news_genie/daily_job.py >> /tmp/news_update.log 2>&1

# Replace /path/to/ with actual path of your project

# Use `crontab -l` to verify if it's scheduled
# Use `cat /tmp/news_update.log` to check run output
