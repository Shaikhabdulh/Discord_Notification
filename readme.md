# 🤖 Discord Reminder Bot Setup with GitHub Actions

A GitHub Actions-powered Discord bot that reminds your team to join the daily standup meeting at **5:50 PM IST (Mon–Fri)**. It also includes an inspiring quote fetched from the ZenQuotes API.
This document walks you through everything you need to set up a Discord bot that sends daily reminder messages via GitHub Actions. It includes setup, file structure, deployment, and how to get the necessary Discord IDs.

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

---
## 🔧 Get Your Discord IDs (Enable Developer Mode)

### Step 2.1: Enable Developer Mode

1. Open the **Discord app**
2. Click **⚙️ User Settings** (bottom left)
3. Go to **Advanced** under "App Settings"
4. Turn **Developer Mode** → ON

### Step 2.2: Get `THREAD_ID`

1. Go to the **channel or thread** where your bot will post
2. Right-click the channel/thread name in the sidebar
3. Click **"Copy Channel ID"**
4. Save it as `THREAD_ID`

### Step 2.3: Get `ROLE_ID`

1. Click your **Server Name → Server Settings → Roles**
2. Right-click the desired role or click (⋯)
3. Select **"Copy Role ID"**
4. Save it as `ROLE_ID`
   
---

### 3. **Add GitHub Secrets**

Go to your repo → **Settings → Secrets → Actions → New repository secret**:

* `DISCORD_TOKEN` = Bot token from Discord Developer Portal
* `THREAD_ID` = Channel ID where bot should post
* `ROLE_ID` = Role ID to mention (optional)
## 📘 More Information 'ROLE_ID'

See [`ROLE_ID` = Role ID to mention (Why_it_is_optional)→](./ROLE_ID.md)

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
