# 📌 Daily Discord Standup Reminder Bot

A GitHub Actions-powered Discord bot that reminds your team to join the daily standup meeting at **5:50 PM IST (Mon–Fri)**. It also includes an inspiring quote fetched from the ZenQuotes API.

---

## ✅ Features

* ⏰ **Scheduled reminder at 5:50 PM IST**
* 📆 **Skips Saturday and Sunday**
* 🧘 **Includes motivational quote**
* 🔐 **Uses GitHub secrets for security**

---

## 📁 Project Structure

```
.
├── bot.py                          # Python script to send the message
└── .github/
    └── workflows/
        └── standup-reminder.yml   # GitHub Actions workflow
```

---

## 🚀 Setup Instructions

### 1. **Create a Discord Bot**

* Visit: [Discord Developer Portal](https://discord.com/developers/applications)
* Create an application → Go to **Bot** tab → Click **"Reset Token"** and copy it
* Under OAuth2 → URL Generator, select `bot` + `Send Messages`, generate the invite URL, and add it to your server

### 2. **Enable Developer Mode in Discord**

* Go to **User Settings → Advanced → Enable Developer Mode**
* Right-click your desired channel and role → Copy IDs for `THREAD_ID` and `ROLE_ID`

### 3. **Add GitHub Secrets**

Go to your repo → **Settings → Secrets → Actions → New repository secret**:

* `DISCORD_TOKEN` = Bot token from Discord Developer Portal
* `THREAD_ID` = Channel ID where bot should post
* `ROLE_ID` = Role ID to mention (optional)

### 4. **Push the Code to GitHub**

Make sure both `bot.py` and `.github/workflows/standup-reminder.yml` are pushed.

### 5. **Run the Bot**

* Go to **Actions** tab in GitHub
* Manually trigger the workflow or wait for automatic daily trigger

---

## 🧪 Test Your Bot

* Trigger the workflow manually to confirm successful message delivery
* Check the thread in Discord for your bot's reminder message

---

## 📌 Customization

* Change reminder time: edit the `cron` line in `standup-reminder.yml`
* Use your own quotes: replace `get_quote()` function in `bot.py`
* Post to multiple channels: duplicate the `fetch_channel()` and `send()` logic

---

## 📞 Support

Need help or want more features? Ping your DevOps/Automation engineer or drop your queries in this project's issue tab.

---

Made with 💻 + ☁️ by your AI assistant ✨
